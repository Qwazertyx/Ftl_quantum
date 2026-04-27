import math
from qiskit import QuantumCircuit, transpile
from qiskit.visualization import plot_histogram
from qiskit_aer import AerSimulator
import matplotlib.pyplot as plt


# ─────────────────────────────────────────────
# Oracle
# ─────────────────────────────────────────────

def build_oracle(n: int, targets: list[str]) -> QuantumCircuit:
    """
    Phase oracle: applies a -1 phase to each target state.

    For each target bitstring (e.g. "101"):
      1. Flip qubits that are '0' in the target (X gates).
      2. Apply a multi-controlled Z (via H + MCX + H on the last qubit).
      3. Flip back the same qubits.

    The qubit order follows Qiskit's convention: targets[i][0] is qubit 0 (LSB).
    """
    oracle = QuantumCircuit(n, name="Oracle")

    for target in targets:
        # Pad / slice to exactly n bits (LSB first)
        bits = target.zfill(n)[::-1]  # reverse so index 0 = qubit 0

        # Flip 0-qubits
        for i, bit in enumerate(bits):
            if bit == "0":
                oracle.x(i)

        # Multi-controlled Z on the full register
        oracle.h(n - 1)
        oracle.mcx(list(range(n - 1)), n - 1)
        oracle.h(n - 1)

        # Unflip
        for i, bit in enumerate(bits):
            if bit == "0":
                oracle.x(i)

        oracle.barrier()

    return oracle


# ─────────────────────────────────────────────
# Diffuser  (Grover operator)
# ─────────────────────────────────────────────

def build_diffuser(n: int) -> QuantumCircuit:
    """
    Grover diffuser: reflection about the uniform superposition |s>.

    D = H^⊗n · (2|0><0| - I) · H^⊗n

    Implementation:
      H on all → X on all → multi-controlled Z → X on all → H on all
    """
    diffuser = QuantumCircuit(n, name="Diffuser")

    diffuser.h(range(n))
    diffuser.x(range(n))

    diffuser.h(n - 1)
    diffuser.mcx(list(range(n - 1)), n - 1)
    diffuser.h(n - 1)

    diffuser.x(range(n))
    diffuser.h(range(n))

    return diffuser


# ─────────────────────────────────────────────
# Full Grover circuit
# ─────────────────────────────────────────────

def build_grover_circuit(n: int, targets: list[str]) -> QuantumCircuit:
    """
    Build the full Grover search circuit for n qubits.

    Optimal number of iterations ≈ (π/4) * sqrt(N / k)
    where N = 2^n and k = number of target states.

    Structure per iteration:
      Oracle → Diffuser
    """
    if n < 2:
        raise ValueError("Grover's algorithm requires at least 2 qubits.")

    N = 2 ** n
    k = len(targets)
    iterations = max(1, round((math.pi / 4) * math.sqrt(N / k)))

    circuit = QuantumCircuit(n, n)

    # ── Initialisation: uniform superposition
    circuit.h(range(n))
    circuit.barrier()

    oracle   = build_oracle(n, targets)
    diffuser = build_diffuser(n)

    # ── Grover iterations
    for _ in range(iterations):
        circuit.compose(oracle,   inplace=True)
        circuit.compose(diffuser, inplace=True)
        circuit.barrier()

    # ── Measurement
    circuit.measure(range(n), range(n))

    print(f"n={n} qubits | N={N} states | {k} target(s) | {iterations} iteration(s)")
    return circuit


# ─────────────────────────────────────────────
# Runner
# ─────────────────────────────────────────────

def run_exercise(n: int = 3, targets: list[str] | None = None, shots: int = 1024) -> None:
    """
    Run Grover's algorithm.

    Args:
        n       : number of qubits (minimum 2)
        targets : list of bitstrings to search for (e.g. ["101", "011"])
                  defaults to a single target: the all-ones state
        shots   : number of simulation shots
    """
    if targets is None:
        targets = ["1" * n]  # default: search for |111...1>

    circuit = build_grover_circuit(n, targets)

    print("\nCircuit (text diagram):")
    print(circuit.draw("text"))

    figure = circuit.draw(output="mpl")
    figure.tight_layout()
    plt.show()

    simulator = AerSimulator()
    compiled = transpile(circuit, simulator)
    result = simulator.run(compiled, shots=shots).result()
    counts = result.get_counts()

    print(f"\nTarget(s): {targets}")
    print(f"Counts ({shots} shots): {counts}")

    # Show measured probabilities for targets
    for t in targets:
        key = t.zfill(n)
        prob = counts.get(key, 0) / shots * 100
        print(f"  |{key}> measured {counts.get(key, 0)} times ({prob:.1f}%)")

    fig = plot_histogram(
        counts,
        title=f"Grover | n={n} qubits | target(s)={targets} ({shots} shots)",
    )
    fig.tight_layout()
    plt.show()


if __name__ == "__main__":
    # ── Example 1: 3 qubits, single target "101"
    run_exercise(n=3, targets=["101"], shots=1024)

    # ── Example 2: 3 qubits, two targets
    run_exercise(n=3, targets=["011", "110"], shots=1024)

    # ── Example 3: 2 qubits minimum
    run_exercise(n=2, targets=["11"], shots=1024)