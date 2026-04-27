from qiskit import QuantumCircuit, transpile
from qiskit.visualization import plot_histogram
from qiskit_aer import AerSimulator
import matplotlib.pyplot as plt


# ─────────────────────────────────────────────
# Oracle builders
# ─────────────────────────────────────────────

def build_constant_oracle(n: int, output: int = 0) -> QuantumCircuit:
    """
    Constant oracle: always returns 0 or always returns 1.
    If output == 1, flip the ancilla qubit unconditionally.
    If output == 0, do nothing (identity on the ancilla).
    """
    oracle = QuantumCircuit(n + 1, name=f"Constant-{output}")
    if output == 1:
        oracle.x(n)
    return oracle


def build_balanced_oracle(n: int) -> QuantumCircuit:
    """
    Balanced oracle: CNOT from each input qubit to the ancilla.
    This flips the ancilla for exactly half the possible inputs.
    """
    oracle = QuantumCircuit(n + 1, name="Balanced")
    for i in range(n):
        oracle.cx(i, n)
    return oracle


# ─────────────────────────────────────────────
# Deutsch-Jozsa circuit
# ─────────────────────────────────────────────

def build_dj_circuit(oracle: QuantumCircuit, n: int) -> QuantumCircuit:
    """
    Build the Deutsch-Jozsa circuit.

    Structure:
      1. Put ancilla in |1>, apply H to all qubits.
      2. Apply the oracle.
      3. Apply H again to the n input qubits.
      4. Measure input qubits only.

    If all measured bits are 0  → the oracle is CONSTANT.
    If any measured bit is 1   → the oracle is BALANCED.
    """
    circuit = QuantumCircuit(n + 1, n)

    # Step 1 – initialise ancilla to |1> then superpose everything
    circuit.x(n)
    circuit.barrier()
    circuit.h(range(n + 1))
    circuit.barrier()

    # Step 2 – oracle
    circuit.compose(oracle, inplace=True)
    circuit.barrier()

    # Step 3 – interference
    circuit.h(range(n))
    circuit.barrier()

    # Step 4 – measure only the input qubits
    circuit.measure(range(n), range(n))

    return circuit


# ─────────────────────────────────────────────
# Runner
# ─────────────────────────────────────────────

def interpret_result(counts: dict, n: int) -> str:
    """Return 'CONSTANT' or 'BALANCED' based on the dominant measurement."""
    all_zeros = "0" * n
    # If the all-zeros state dominates, the oracle is constant
    dominant = max(counts, key=counts.get)
    return "CONSTANT" if dominant == all_zeros else "BALANCED"


def run_exercise(shots: int = 1024) -> None:
    n = 3  # number of input qubits (4 qubits total with ancilla)

    oracles = {
        "Constant-0": build_constant_oracle(n, output=0),
        "Constant-1": build_constant_oracle(n, output=1),
        "Balanced":   build_balanced_oracle(n),
    }

    simulator = AerSimulator()

    for name, oracle in oracles.items():
        print(f"\n{'=' * 50}")
        print(f"Oracle: {name}")

        circuit = build_dj_circuit(oracle, n)

        print("\nCircuit (text diagram):")
        print(circuit.draw("text"))

        figure = circuit.draw(output="mpl")
        figure.tight_layout()
        plt.show()

        compiled = transpile(circuit, simulator)
        result = simulator.run(compiled, shots=shots).result()
        counts = result.get_counts()

        verdict = interpret_result(counts, n)
        print(f"Counts ({shots} shots): {counts}")
        print(f"→ Oracle is: {verdict}")

        fig = plot_histogram(
            counts,
            title=f"Deutsch-Jozsa | Oracle: {name} | Result: {verdict} ({shots} shots)",
        )
        fig.tight_layout()
        plt.show()


if __name__ == "__main__":
    run_exercise(1024)