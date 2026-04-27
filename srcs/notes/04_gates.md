all gates briefely showed, with links to the full explainations that will be all along
(add all gates on the lists), add all missing details, matrix, circuit representation, and circle representation on the full explanations


pauli x-gate
-quantum not


hadamard h-gate
transforms a definitive state into a superposition

pauli z-gate
phase flip

CNOT gate
acts on 2 qubit
control qubit decides if the action happens, target qubit gets flipped (not operation) if the control is 1

quantum gates are unitary and reversible, if you know the output, you can reconstruct the input

------------

pauli gates
(x y z)
qubit -> verctor pointing to the surface of a sphere
pauli gates rotate this vector around the x y z axes

pauli x is quantum not
flips the state of a qubit
|0> becomes |1>
|1> becomes |0>
matrix represntation -> [01][10]


pauli-y -> bit flip and phase flip
matrix represntation -> [0-i][i0]
|0> becomes i|1>
|1> becomes -i|0>


pauli-z gate
phase flip
matrix represntation -> [10][0-1]
|0> becomes |0>
|1> becomes |0>
effect on superposition: + becomes -
it changes the quantum phase without changing the probability of measuring 0 or 1


-----------------


hadamard gate
most fundamental gate in quantum computing
creates superposition

matrix representation

HxH = Identity

--------------

phase gates
s t rotation

what is quantum phase

zgate explained already (180 degree rotation)

s gate
square root of Z
90degree rotation pi/2 around Z axis

T gate
square root of S
45degree rotatio pi/4

-----------------

cnot gate
circuit representation
matrix representation
create entanglement

bell state = hadamard gate + CNOT gate 
measuring one qubit tells us the state of the other


https://www.youtube.com/watch?v=0WZmkIyHOks&list=PLE3ovFxnzNpY3zGw8sHqRorxecoItAAq4&index=10