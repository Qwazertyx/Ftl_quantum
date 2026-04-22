import os
from dotenv import load_dotenv
from qiskit import QuantumCircuit
from qiskit.quantum_info import SparsePauliOp
from qiskit.transpiler import generate_preset_pass_manager
from qiskit_ibm_runtime import QiskitRuntimeService
from qiskit_aer import AerSimulator
from matplotlib import pyplot as plt

# Load environment variables from .env file
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



# Create a new circuit with two qubits
qc = QuantumCircuit(2)
# Add a Hadamard gate to qubit 0
qc.h(0)
# Perform a controlled-X gate on qubit 1, controlled by qubit 0
qc.cx(0, 1)
# Display the circuit
figure = qc.draw("mpl")
figure.tight_layout()
plt.show()


# Set up six different observables.
observables_labels = ["IZ", "IX", "ZI", "XI", "ZZ", "XX"]
observables = [SparsePauliOp(label) for label in observables_labels]

# Get the least busy backend using the service created above
backend = service.least_busy(simulator=False, operational=True)
# Convert to an ISA circuit and layout-mapped observables.
pm = generate_preset_pass_manager(backend=backend, optimization_level=1)
isa_circuit = pm.run(qc)

# Display the ISA circuit
figure2 = isa_circuit.draw("mpl", idle_wires=False)
figure2.tight_layout()
plt.show()