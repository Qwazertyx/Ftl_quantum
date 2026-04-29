import os
from dotenv import load_dotenv
import matplotlib.pyplot as plt
from qiskit import QuantumCircuit, transpile
from qiskit.visualization import plot_histogram
from qiskit_aer import AerSimulator
from qiskit_ibm_runtime import QiskitRuntimeService, SamplerV2

load_dotenv()

# Get credentials from environment variables
token = os.getenv("IBM_QUANTUM_TOKEN")
instance = os.getenv("IBM_QUANTUM_INSTANCE")

if not token or token.startswith("<"):
    print("ERROR: IBM_QUANTUM_TOKEN not configured in .env file")
    print("Please add your 44-character token to the .env file")
    service = None
else:
    # Create service with credentials from .env
    service = QiskitRuntimeService(
      token=token, 
      instance=instance if instance and not instance.startswith("<") else None
      )


def build_entanglement_circuit() -> QuantumCircuit:
    """Build a 2-qubit circuit that prepares (|00> + |11>) / sqrt(2)."""
    circuit = QuantumCircuit(2, 2)
    circuit.h(0)
    circuit.cx(0, 1)
    circuit.measure([0, 1], [0, 1])
    return circuit

def run_on_ibm_hardware(circuit: QuantumCircuit, shots: int) -> dict:
    if service is None:
        raise RuntimeError("IBM Quantum service is not configured.")

    backend = service.least_busy(operational=True, simulator=False, min_num_qubits=2)

    if backend is None:
        raise RuntimeError("No operational IBM backend was available.")

    print(f"Using backend: {backend.name}")

    compiled = transpile(circuit, backend, optimization_level=1)
    sampler = SamplerV2(mode=backend)
    job = sampler.run([compiled], shots=shots)
    print(f"Submitted job: {job.job_id()}")
    print(f"Initial job status: {job.status()}")
    result = job.result()[0]

    if hasattr(result.data, "c"):
        return result.data.c.get_counts()

    if hasattr(result.data, "meas"):
        return result.data.meas.get_counts()

    raise RuntimeError("Sampler result did not include a classical register with counts.")


def run_on_local_simulator(circuit: QuantumCircuit, shots: int) -> dict:
    simulator = AerSimulator()
    compiled = transpile(circuit, simulator, optimization_level=1)
    job = simulator.run(compiled, shots=shots)
    result = job.result()
    return result.get_counts()


def run_exercise(shots: int = 500) -> None:
    circuit = build_entanglement_circuit()

    print("Circuit (text diagram):")
    print(circuit.draw("text"))

    counts = None
    title = ""
    try:
        counts = run_on_ibm_hardware(circuit, shots)
        title = f"Hardware Entanglement ({shots} shots)"
    except Exception as error:
        print(f"hardware unavailable: {error}")
        counts = run_on_local_simulator(circuit, shots)
        title = f"Local Simulator Entanglement ({shots} shots)"

    print(f"Counts for {shots} shots: {counts}")

    fig = plot_histogram(counts, title=title)
    fig.tight_layout()
    plt.show()


if __name__ == "__main__":
    run_exercise(500)