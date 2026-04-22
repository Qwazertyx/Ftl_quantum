from qiskit import QuantumCircuit, transpile
from qiskit.visualization import plot_histogram
from qiskit_aer import AerSimulator
import matplotlib.pyplot as plt


def build_entanglement_circuit() -> QuantumCircuit:
    """Build a 2-qubit circuit that prepares (|00> + |11>) / sqrt(2)."""
    circuit = QuantumCircuit(2, 2)
    circuit.h(0)
    circuit.cx(0, 1)
    circuit.measure([0, 1], [0, 1])
    return circuit

def run_exercise(shots: int) -> None:
    circuit = build_entanglement_circuit()

    print("Circuit (text diagram):")
    print(circuit.draw("text"))

    #figure = circuit.draw(output="mpl")
    #figure.tight_layout()
    #plt.show()

    simulator = AerSimulator()
    compiled = transpile(circuit, simulator)
    result = simulator.run(compiled, shots=shots).result()
    counts = result.get_counts()

    print(f"Counts for {shots} shots: {counts}")

    fig = plot_histogram(counts, title=f"Entanglement ({shots} shots)")
    fig.tight_layout()
    plt.show()


if __name__ == "__main__":
    run_exercise(500)
