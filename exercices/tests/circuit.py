from qiskit import QuantumCircuit
from qiskit.quantum_info import Statevector
from numpy import sqrt
import matplotlib.pyplot as plt

circuit = QuantumCircuit(1)

circuit.h(0)
circuit.t(0)
circuit.h(0)
circuit.s(0)
circuit.y(0)

figure = circuit.draw(output="mpl")
figure.tight_layout()
plt.show()

ket0 = Statevector([1, 0])
v = ket0.evolve(circuit)
figure = v.draw("latex")
plt.show()