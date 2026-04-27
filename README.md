# Quantum Computing — Course & Reference

> Study guide for the **ftl_quantum** project — 42 Lyon  
> This document covers the theoretical foundations and algorithms implemented in the exercises.

---

## Table of Contents

1. [Introduction to Quantum Computing](#1-introduction-to-quantum-computing)
2. [The Qubit](#2-the-qubit)
   - [Bit vs Qubit](#21-bit-vs-qubit)
   - [Superposition](#22-superposition)
   - [Measurement and State Collapse](#23-measurement-and-state-collapse)
   - [The Bloch Sphere](#24-the-bloch-sphere)
3. [Notations](#3-notations)
   - [Bra-Ket Notation](#31-bra-ket-dirac-notation)
   - [Vector and Matrix Representation](#32-vector-and-matrix-representation)
   - [Multi-Qubit Systems](#33-multi-qubit-systems)
4. [Quantum Gates](#4-quantum-gates)
   - [General Properties](#41-general-properties)
   - [Pauli Gates (X, Y, Z)](#42-pauli-gates-x-y-z)
   - [Hadamard Gate (H)](#43-hadamard-gate-h)
   - [Phase Gates (S, T)](#44-phase-gates-s-t)
   - [CNOT Gate](#45-cnot-gate)
   - [Toffoli Gate (CCX)](#46-toffoli-gate-ccx)
   - [Multi-Controlled X Gate (MCX)](#47-multi-controlled-x-gate-mcx)
5. [Quantum Entanglement](#5-quantum-entanglement)
6. [Quantum Algorithms](#6-quantum-algorithms)
   - [Deutsch-Jozsa](#61-deutsch-jozsa)
   - [Grover's Search Algorithm](#62-grovers-search-algorithm)
7. [Exercises — Code Reference](#7-exercises--code-reference)
   - [Ex00 — Superposition](#ex00--superposition)
   - [Ex01 — Entanglement](#ex01--entanglement)
   - [Ex02 — Quantum Noise (IBM)](#ex02--quantum-noise-ibm)
   - [Ex03 — Deutsch-Jozsa](#ex03--deutsch-jozsa)
   - [Ex04 — Grover's Algorithm](#ex04--grovers-algorithm)
8. [Glossary](#8-glossary)
9. [References](#9-references)

---

## 1. Introduction to Quantum Computing

Classical computing is built on **bits**: switches that are either 0 or 1. All digital information is encoded as sequences of these two states.

Quantum computing uses a different unit of information: the **qubit**. A qubit can also be 0 or 1, but before being measured, it can exist in a **combination of both** — this is called *superposition*. Additionally, two qubits can be **entangled**, meaning they are correlated in a way that no classical physics can reproduce.

These are not just curiosities. These properties allow certain quantum algorithms to solve problems that classical computers cannot handle in a reasonable amount of time.

**A few concrete examples:**
- Factoring large numbers: classically exponential, quantumly polynomial (Shor's algorithm).
- Searching an unsorted database: classically O(N), quantumly O(sqrt(N)) (Grover's algorithm).
- Simulating molecules and materials for chemistry or pharmacology.

> **Important:** quantum computers do not replace classical computers. They are useful for a specific family of problems where the mathematical structure allows superposition and entanglement to be exploited.

---

## 2. The Qubit

### 2.1 Bit vs Qubit

| Property | Classical Bit | Qubit |
|---|---|---|
| Possible states | 0 or 1 | 0, 1, or superposition |
| Before measurement | Deterministic | Probabilistic |
| After measurement | Unchanged | Irreversible collapse |
| Correlation | Independent | Can be entangled |

A classical bit is like a light switch: either off (0) or on (1). A qubit, before measurement, is like a coin spinning in the air — it is neither heads nor tails, it is *both at the same time*, with associated probabilities.

### 2.2 Superposition

Superposition is the state a qubit is in **before** any measurement. It is not ignorance — the qubit truly does not have a defined value yet. It is a physical state in its own right.

Mathematically, a qubit in superposition is written:

```
|psi> = alpha|0> + beta|1>
```

where alpha and beta are **complex amplitudes** satisfying:

```
|alpha|^2 + |beta|^2 = 1
```

The probability of getting 0 upon measurement is **|alpha|^2**, and the probability of getting 1 is **|beta|^2**.

The most common 50/50 superposition state is:

```
|psi> = (1/sqrt(2))|0> + (1/sqrt(2))|1>
```

This gives 50% chance of measuring 0 and 50% of measuring 1 — this is exactly what the Hadamard gate produces.

<p align="center">
  <img src="srcs/imgs/Superposition%20probatility%20bars%20(ex00).png" alt="Superposition — equal probability of measuring 0 or 1 over 500 shots" width="480"/>
</p>

### 2.3 Measurement and State Collapse

Measurement is an **active and irreversible process**. When a qubit in superposition is measured, its state collapses to one of the classical values (0 or 1) according to the probabilities dictated by its amplitudes.

Analogy: imagine a vending machine whose contents you don't know. Before pressing a button, it could dispense anything (superposition). The moment you press (measurement), it dispenses one item and can never dispense the others. The act of choosing forced the system to define itself.

**Practical consequences:**
- You cannot "read" a quantum state directly without destroying it.
- To know the probabilities, you must repeat the experiment many times.
- Each repetition is called a **shot**.

```
500 shots on (|0> + |1>) / sqrt(2)  →  ~250 times "0",  ~250 times "1"
```

### 2.4 The Bloch Sphere

Any pure state of a qubit can be visualised as a **point on a unit sphere** — the Bloch sphere.

```
|psi> = cos(theta/2)|0> + e^(i*phi) sin(theta/2)|1>
```

- The **north pole** represents |0⟩
- The **south pole** represents |1⟩
- The **equator** represents all 50/50 superpositions
- The **longitude** (angle phi) encodes the complex phase

Quantum gates are **rotations** of this vector on the sphere:
- Pauli X: 180° rotation around the X axis
- Pauli Y: 180° rotation around the Y axis
- Pauli Z: 180° rotation around the Z axis
- Hadamard: 180° rotation around the diagonal X+Z axis

<p align="center">
  <img src="srcs/imgs/real-Bloch-sphere-points.avif" alt="Bloch sphere with labelled axes and state vector" width="370"/>
  &nbsp;&nbsp;&nbsp;
  <img src="srcs/imgs/six-Bloch-sphere-points.avif" alt="Bloch sphere showing the six cardinal states" width="370"/>
</p>

---

## 3. Notations

### 3.1 Bra-Ket (Dirac) Notation

Bra-ket notation is the standard language of quantum mechanics. It allows states and inner products to be written compactly.

**Ket** `|psi>` — represents a quantum state (column vector):
```
|0> = [1]    |1> = [0]
      [0]          [1]
```

**Bra** `<psi|` — represents the conjugate transpose of the ket (row vector):
```
<0| = [1, 0]    <1| = [0, 1]
```

**Inner product** `<phi|psi>` — probability amplitude of finding |psi⟩ in state |phi⟩:
```
<0|0> = 1    <1|1> = 1    <0|1> = 0    <1|0> = 0
```

The states |0⟩ and |1⟩ are **orthonormal**: perpendicular and of unit norm.

**Common states:**

| Notation | Description | Vector |
|---|---|---|
| `\|0⟩` | Base state "zero" | [1, 0]^T |
| `\|1⟩` | Base state "one" | [0, 1]^T |
| `\|+⟩` | (+) superposition = H\|0⟩ | [1/sqrt(2), 1/sqrt(2)]^T |
| `\|−⟩` | (−) superposition = H\|1⟩ | [1/sqrt(2), −1/sqrt(2)]^T |

### 3.2 Vector and Matrix Representation

A qubit is a **vector in a 2-dimensional Hilbert space**. A single-qubit quantum gate is a **unitary 2×2 matrix** (such that U†U = I).

Applying a gate U to a state |psi⟩ is a **matrix multiplication**:

```
|psi'> = U|psi>
```

Example — gate X applied to |0⟩:
```
X|0> = [0 1] x [1] = [0] = |1>
       [1 0]   [0]   [1]
```

The **unitarity** condition (U†U = I) guarantees:
1. The norm is preserved (probabilities always sum to 1).
2. The operation is **reversible** — the input can always be reconstructed from the output.

### 3.3 Multi-Qubit Systems

To describe a system of n qubits, the **tensor product** ⊗ is used.

The state space of 2 qubits has dimension 4:

```
Basis: |00>, |01>, |10>, |11>

|00> = |0> x |0> = [1, 0, 0, 0]^T
|01> = |0> x |1> = [0, 1, 0, 0]^T
|10> = |1> x |0> = [0, 0, 1, 0]^T
|11> = |1> x |1> = [0, 0, 0, 1]^T
```

> **Qiskit convention:** the lowest-index qubit (qubit 0) corresponds to the rightmost bit in the notation. So `|01⟩` means qubit 1 = 0, qubit 0 = 1.

A system of n qubits can exist in superposition of **2^n states simultaneously**. This is the source of quantum computing's exponential power: 50 qubits represent 2^50 ≈ 10^15 states at once.

---

## 4. Quantum Gates

### 4.1 General Properties

All quantum gates satisfy two essential properties:

1. **Unitarity**: `U†U = I` — the gate is reversible and preserves probabilities.
2. **Linearity**: `U(alpha|0> + beta|1>) = alpha*U|0> + beta*U|1>`

Unlike classical logic gates (NAND, OR...), a quantum gate can **never lose information**. Knowing the output is sufficient to recover the input.

### 4.2 Pauli Gates (X, Y, Z)

The three Pauli gates correspond to **180° rotations** around the three axes of the Bloch sphere.

---

#### Pauli-X Gate (Quantum NOT)

The X gate is the quantum equivalent of NOT. It swaps |0⟩ and |1⟩.

**Matrix:**
```
X = [0  1]
    [1  0]
```

**Action:**
```
X|0> = |1>
X|1> = |0>
```

**Qiskit:** `circuit.x(qubit)`

<p align="center">
  <img src="srcs/imgs/pauli%20x%20gate%20bloch%20sphere.jpg" alt="Pauli-X gate — full Bloch sphere with rotation vectors" width="420"/>
  &nbsp;&nbsp;&nbsp;
  <img src="srcs/imgs/BlochSphere_X_01(pauli%20x%20gate%20sphere).png" alt="Pauli-X gate — rotation arc from |0⟩ to |1⟩ on the Bloch sphere" width="300"/>
</p>

---

#### Pauli-Y Gate

The Y gate combines a bit flip and a phase flip, with an imaginary factor.

**Matrix:**
```
Y = [0   -i]
    [i    0]
```

**Action:**
```
Y|0> =  i|1>
Y|1> = -i|0>
```

**Qiskit:** `circuit.y(qubit)`

<p align="center">
  <img src="srcs/imgs/BlochSphere_Y_01%20(pauli%20y%20gate%20sphere).png" alt="Pauli-Y gate — 180° rotation around the Y axis on the Bloch sphere" width="300"/>
</p>

---

#### Pauli-Z Gate (Phase Flip)

The Z gate does not change measurement probabilities, but it inverts the **phase** of |1⟩. This is only visible when the qubit is in superposition.

**Matrix:**
```
Z = [1   0]
    [0  -1]
```

**Action:**
```
Z|0> =  |0>
Z|1> = -|1>
Z|+> =  |->    (flips the superposition sign)
Z|-> =  |+>
```

**Qiskit:** `circuit.z(qubit)`

> Phase is invisible to direct measurement, but essential for interference in all quantum algorithms.

<p align="center">
  <img src="srcs/imgs/pauli%20z%20gate%20sphere.png" alt="Pauli-Z gate — phase flip, rotation around the Z axis" width="300"/>
</p>

---

### 4.3 Hadamard Gate (H)

The Hadamard gate is the **most fundamental gate** in quantum computing. It creates superposition from a basis state.

**Matrix:**
```
H = (1/sqrt(2)) x [1   1]
                  [1  -1]
```

**Action:**
```
H|0> = (1/sqrt(2))(|0> + |1>) = |+>    → (+) superposition
H|1> = (1/sqrt(2))(|0> - |1>) = |->    → (−) superposition
```

**Key property:** `H x H = I` (its own inverse)

```
H|+> = |0>    → back to classical state through constructive interference
H|-> = |1>
```

This property is at the core of Deutsch-Jozsa: applying H twice undoes the superposition, unless the oracle has modified the phase in between.

**Qiskit:** `circuit.h(qubit)`

<p align="center">
  <img src="srcs/imgs/BlochSphere_H_01%20(hadamard%20gate%20sphere).png" alt="Hadamard gate — rotation arc from |0⟩ to |+⟩ on the Bloch sphere" width="300"/>
</p>

---

### 4.4 Phase Gates (S, T)

Phase gates add a partial rotation around the Z axis without changing measurement probabilities.

#### S Gate (sqrt(Z))

**Matrix:**
```
S = [1   0]
    [0   i]
```

**90° rotation** (pi/2) around the Z axis. `S^2 = Z`.

**Qiskit:** `circuit.s(qubit)`

#### T Gate (fourth-root of Z)

**Matrix:**
```
T = [1            0        ]
    [0   e^(i*pi/4)        ]
```

**45° rotation** (pi/4) around the Z axis. `T^2 = S`, `T^4 = Z`.

**Qiskit:** `circuit.t(qubit)`

> Together with H and CNOT, the T gate forms a universal gate set for quantum computation.

---

### 4.5 CNOT Gate

The CNOT (Controlled-NOT) gate acts on **two qubits**:
- The **control qubit**: if it is |1⟩, the operation is applied.
- The **target qubit**: receives a NOT if the control is |1⟩.

**Matrix (basis |00⟩, |01⟩, |10⟩, |11⟩):**
```
CNOT = [1  0  0  0]
       [0  1  0  0]
       [0  0  0  1]
       [0  0  1  0]
```

**Action:**
```
CNOT|00> = |00>    (control=0 → nothing)
CNOT|01> = |01>    (control=0 → nothing)
CNOT|10> = |11>    (control=1 → flip target)
CNOT|11> = |10>    (control=1 → flip target)
```

**Qiskit:** `circuit.cx(control, target)`

**Creating entanglement step by step:**
```
Start      : |00>
After H    : (1/sqrt(2))(|00> + |10>)    ← qubit 0 in superposition
After CNOT : (1/sqrt(2))(|00> + |11>)    ← Bell state — entangled!
```

<p align="center">
  <img src="srcs/imgs/ex01%20figure%20CNOT%20gate%20and%20Bell%20state%20creation.png" alt="H + CNOT circuit creating the Bell state" width="420"/>
</p>

---

### 4.6 Toffoli Gate (CCX)

The Toffoli gate is a CNOT with **two control qubits**: the target qubit is flipped if and only if both controls are |1⟩.

```
Toffoli|110> = |111>
Toffoli|111> = |110>
All other states → unchanged
```

**Qiskit:** `circuit.ccx(control1, control2, target)`

### 4.7 Multi-Controlled X Gate (MCX)

Generalisation of CNOT to **n control qubits**: the target qubit is flipped only if all controls are |1⟩.

**Qiskit:** `circuit.mcx(control_list, target)`

Used in Grover's oracle to identify a specific state among 2^n.

---

## 5. Quantum Entanglement

Entanglement is perhaps the most counter-intuitive phenomenon in quantum mechanics. Two qubits are **entangled** when their global state **cannot** be written as the product of two individual states.

**Bell state (maximally entangled state):**
```
|Phi+> = (1/sqrt(2))(|00> + |11>)
```

This state is **impossible to factorise**:
```
(1/sqrt(2))(|00> + |11>) != (a|0> + b|1>) x (c|0> + d|1>)  for any a, b, c, d
```

**What this means concretely:**
- Before measurement: the two qubits have no individually defined state.
- Measuring qubit 0 and getting 0 → qubit 1 will be 0.
- Measuring qubit 0 and getting 1 → qubit 1 will be 1.
- This correlation is instantaneous, regardless of distance.

> This is not that the qubits "communicate": information does not travel. It is that their shared state was non-local from the beginning.

**How entanglement is created (ex01):**
```
Step 1: circuit.h(0)    → qubit 0 in superposition: (|0>+|1>)/sqrt(2)
Step 2: circuit.cx(0,1) → CNOT copies the uncertainty into qubit 1

Result: (1/sqrt(2))(|00> + |11>)
```

**Observed results:**
- Only `00` and `11` appear.
- `01` and `10` never appear.
- Proportions ~50/50.

<p align="center">
  <img src="srcs/imgs/ex01%20entanglement%20histogram.png" alt="Entanglement histogram — only 00 and 11 appear, never 01 or 10" width="480"/>
</p>

---

## 6. Quantum Algorithms

### 6.1 Deutsch-Jozsa

#### Context and motivation

The Deutsch-Jozsa problem is the **first algorithm to prove quantum advantage**. It has no direct practical application, but it perfectly illustrates how superposition allows a global property to be determined in a single query where a classical computer would need many.

**The problem:** We are given a black-box function f : {0,1}^n → {0,1}. This function is guaranteed to be either:
- **Constant**: always returns 0, or always returns 1.
- **Balanced**: returns 0 for exactly half of all inputs, 1 for the other half.

**Question:** Is the function constant or balanced?

**Classical cost:** In the worst case, f must be evaluated on **2^(n-1) + 1 inputs** (half + 1) to be certain.

**Quantum cost: a single evaluation of the oracle**, regardless of input size.

---

#### The Deutsch-Jozsa Circuit

```
Input qubits  : q0, q1, q2  (n=3)
Ancilla qubit : q3

q0 : ─── H ─── [Oracle] ─── H ─── Measure
q1 : ─── H ─── [Oracle] ─── H ─── Measure
q2 : ─── H ─── [Oracle] ─── H ─── Measure
q3 : ─ X ─ H ─ [Oracle] ───────── (not measured)
```

<p align="center">
  <img src="srcs/imgs/ex03%20deutsch%20jozsa%20circuit.png" alt="Deutsch-Jozsa circuit — 3 input qubits + 1 ancilla" width="750"/>
</p>

---

#### Detailed Steps

**1. Initialisation**
```
|psi_0> = |0>|0>|0>|0>
Apply X on ancilla q3  →  |0>|0>|0>|1>
```

**2. Superposition**
```
Apply H on all qubits:
input qubits → uniform superposition of all 2^n inputs
ancilla      → (|0> - |1>) / sqrt(2)   ← phase kickback setup
```

**3. Quantum Oracle (black box)**

The oracle performs the transformation `|x>|y> → |x>|y XOR f(x)>`.

Thanks to the ancilla being in `(|0>-|1>)/sqrt(2)`, this is equivalent to a **phase kickback**:
```
|x> → (-1)^f(x) |x>
```

The oracle encodes f(x) **into the phase**, not into an output qubit.

- f **constant**: all phases are +1 (or all −1) → no relative difference.
- f **balanced**: half the phases are +1, half are −1 → destructive interference.

**4. Second application of H (interference)**
```
Apply H on the n input qubits only
```

Quantum interference amplifies |00...0⟩ if f is constant, and cancels it if f is balanced.

**5. Measurement**

| Oracle | Expected result | Interpretation |
|---|---|---|
| Constant | `000` (all bits zero) | Constructive interference on |0⟩ |
| Balanced | Anything other than `000` | Destructive interference on |0⟩ |

<p align="center">
  <img src="srcs/imgs/ex03%20oracle%20constant.png" alt="Deutsch-Jozsa — constant oracle: 100% of shots give 000" width="460"/>
  &nbsp;&nbsp;&nbsp;
  <img src="srcs/imgs/ex03%20oracle%20balanced.png" alt="Deutsch-Jozsa — balanced oracle: 100% of shots give a non-zero state" width="460"/>
</p>

---

#### Oracles used in ex03

**Constant-0 oracle:** Does nothing. f(x) = 0 for all x.

**Constant-1 oracle:** Applies X on the ancilla unconditionally. f(x) = 1 for all x.

**Balanced oracle:** CNOT from each input qubit to the ancilla.
```
f(x) = x_0 XOR x_1 XOR x_2
```
This flips the ancilla for exactly half of all inputs.

---

### 6.2 Grover's Search Algorithm

#### The Search Problem

We have **N = 2^n unsorted items** and want to find one or more items satisfying a given condition (the oracle).

- **Classical:** O(N) on average — half the items must be checked on average.
- **Quantum (Grover):** O(sqrt(N)) — a quadratic speedup.

For N = 1,000,000: classical = 500,000 checks on average, Grover = ~785.

---

#### Circuit Overview

```
q0 : ─ H ─ [Oracle] ─ [Diffuser] ─ ... ─ Measure
q1 : ─ H ─ [Oracle] ─ [Diffuser] ─ ... ─ Measure
q2 : ─ H ─ [Oracle] ─ [Diffuser] ─ ... ─ Measure

      Init  ◄─── Repeat ~(pi/4)*sqrt(N/k) times ───►
```

<p align="center">
  <img src="srcs/imgs/ex04%20grover%20circuit.png" alt="Grover's algorithm circuit — 3 qubits, init + Oracle+Diffuser iterations + measure" width="750"/>
</p>

---

#### The Three Parts of the Algorithm

**1. Initialisation: uniform superposition**

Apply H on all qubits to create an equal superposition of all 2^n states:

```
|s> = H^(xn)|0...0> = (1/sqrt(N)) * sum of all |x>   for x in {0, ..., N-1}
```

Each state has amplitude 1/sqrt(N) and therefore probability 1/N.

**2. The Oracle: phase marking**

The oracle inverts the phase of the target state(s):

```
Oracle|x> = -|x>   if x is a solution
Oracle|x> =  |x>   otherwise
```

After the oracle, only the target amplitude is negative. Measuring now would still give 1/N for each state — the information is in the phase, not yet visible in probabilities.

**3. The Diffuser: amplification by reflection**

The diffuser applies a **reflection around the mean amplitude**:

```
D = 2|s><s| - I = H^(xn) * (2|0><0| - I) * H^(xn)
```

**Geometric intuition:** The mean of all amplitudes is slightly below 1/sqrt(N) because one state is negative. Reflecting each amplitude around this mean pushes the target well above 1/sqrt(N) and all other states slightly below.

```
Before oracle  : all amplitudes at +1/sqrt(N)
After oracle   : target at -1/sqrt(N), others at +1/sqrt(N)
After diffuser : target much higher, others slightly lower
```

**Implementation:**
```
H on all → X on all → H on last qubit → MCX → H on last qubit → X on all → H on all
```

---

#### Optimal Number of Iterations

After k iterations of Oracle + Diffuser, the probability of measuring the target state is:

```
P(k) = sin^2((2k+1)*theta)    where sin(theta) = sqrt(m/N), m = number of targets
```

The optimal number of iterations is:

```
k_opt ≈ (pi/4) * sqrt(N/m)
```

For n=3, N=8, one target: `k_opt ≈ (pi/4) * sqrt(8) ≈ 2`

> **Note on small n:** The formula is an approximation. For very small registers (e.g. n=2, N=4), the rounding can land on the wrong number of iterations and the probability actually drops back. This is visible in the n=2 histogram in the exercises section — the distribution is nearly uniform because one extra iteration overshoots the peak.

---

#### Expected Results

For n=3 qubits, target "101", 2 iterations: state |101⟩ should appear in **~97%** of measurements.

<p align="center">
  <img src="srcs/imgs/ex%2004%203qubit%2C%20single%20target%20101.png" alt="Grover result — target state 101 dominates at ~95% of 1024 shots" width="500"/>
</p>

---

## 7. Exercises — Code Reference

### Ex00 — Superposition

**Goal:** Create the state `(|0⟩ + |1⟩) / sqrt(2)` with a single qubit.

```
Circuit:  q0 : ─ H ─ Measure
```

**Key code:**
```python
circuit = QuantumCircuit(1, 1)
circuit.h(0)
circuit.measure(0, 0)
```

**Expected result:** ~50% `0`, ~50% `1` over 500 shots.

**Run:** `python ex00.py`

<p align="center">
  <img src="srcs/imgs/Superposition%20probatility%20bars%20(ex00).png" alt="Ex00 — superposition histogram: ~50% 0, ~50% 1 over 500 shots" width="480"/>
</p>

---

### Ex01 — Entanglement

**Goal:** Create the Bell state `(|00⟩ + |11⟩) / sqrt(2)`.

```
Circuit:  q0 : ─ H ─●─ Measure
                     │
          q1 : ─────X─ Measure
```

**Key code:**
```python
circuit = QuantumCircuit(2, 2)
circuit.h(0)
circuit.cx(0, 1)
circuit.measure([0, 1], [0, 1])
```

**Expected result:** Only `00` and `11`, never `01` or `10`.

**Run:** `python ex01.py`

<p align="center">
  <img src="srcs/imgs/ex01%20figure%20CNOT%20gate%20and%20Bell%20state%20creation.png" alt="Ex01 — H + CNOT circuit" width="380"/>
  &nbsp;&nbsp;&nbsp;
  <img src="srcs/imgs/ex01%20entanglement%20histogram.png" alt="Ex01 — only 00 and 11 appear" width="420"/>
</p>

---

### Ex02 — Quantum Noise (IBM)

**Goal:** Run the same circuit as ex01 on a real IBM quantum computer and observe the differences caused by hardware noise.

**Expected result:** States `01` and `10` appear (a few percent) even though the circuit is identical to ex01.

**Why the difference?**
- Physical qubits have limited **coherence times** — they lose their quantum state over time.
- **Gate errors** — no physical gate is perfectly implemented.
- **Transpilation** adapts the circuit to the backend's physical topology (extra SWAP gates add more noise).
- **Readout errors** — measuring a qubit can give the wrong answer.

**Run:** `python ex02.py`

---

### Ex03 — Deutsch-Jozsa

**Goal:** Implement the algorithm on 4 qubits (3 input + 1 ancilla) and identify whether the oracle is constant or balanced in a single run.

**Key code:**
```python
def build_dj_circuit(oracle, n):
    circuit = QuantumCircuit(n + 1, n)
    circuit.x(n)           # ancilla → |1>
    circuit.h(range(n+1))  # global superposition
    circuit.compose(oracle, inplace=True)
    circuit.h(range(n))    # interference
    circuit.measure(range(n), range(n))
    return circuit
```

**Decision rule:**
```
All measured bits = 0  →  CONSTANT oracle
Any measured bit  = 1  →  BALANCED oracle
```

**Run:** `python ex03.py`

> Automatically tests 3 oracles: Constant-0, Constant-1, Balanced.

<p align="center">
  <img src="srcs/imgs/ex03%20deutsch%20jozsa%20circuit.png" alt="Ex03 — Deutsch-Jozsa circuit with 3 input qubits and 1 ancilla" width="720"/>
</p>

<p align="center">
  <img src="srcs/imgs/ex03%20oracle%20constant.png" alt="Ex03 — constant oracle: all shots give 000" width="420"/>
  &nbsp;&nbsp;&nbsp;
  <img src="srcs/imgs/ex03%20oracle%20balanced.png" alt="Ex03 — balanced oracle: all shots give 111" width="420"/>
</p>

---

### Ex04 — Grover's Algorithm

**Goal:** Find one or more target states among 2^n with O(sqrt(N)) complexity.

**Key code:**
```python
run_exercise(n=3, targets=["101"], shots=1024)         # single target
run_exercise(n=3, targets=["011", "110"], shots=1024)  # two targets
run_exercise(n=2, targets=["11"], shots=1024)          # minimum 2 qubits
```

The number of iterations is computed automatically:
```python
iterations = max(1, round((math.pi / 4) * math.sqrt(N / k)))
```

**Complexity comparison:**

| Qubits (n) | States (N) | Classical avg | Grover |
|---|---|---|---|
| 3 | 8 | 4 | 2 |
| 5 | 32 | 16 | 4 |
| 10 | 1 024 | 512 | 25 |
| 20 | 1 048 576 | 524 288 | 804 |

**Run:** `python ex04.py`

**3-qubit result (n=3, target="101"):**

<p align="center">
  <img src="srcs/imgs/ex04%20grover%20circuit.png" alt="Ex04 — Grover circuit for 3 qubits" width="720"/>
</p>

<p align="center">
  <img src="srcs/imgs/ex%2004%203qubit%2C%20single%20target%20101.png" alt="Ex04 — Grover histogram: 101 dominates at ~95% of shots" width="480"/>
</p>

**2-qubit edge case (n=2, target="11"):**

With n=2 and N=4, the exact optimal number of iterations is 1, but the rounding in the formula yields 2. The second iteration overshoots the amplitude peak and the distribution collapses back to near-uniform. This demonstrates that the approximation breaks down for very small registers.

<p align="center">
  <img src="srcs/imgs/ex04%20grover%20circuit%202%20qubits.png" alt="Ex04 — Grover circuit for 2 qubits" width="720"/>
</p>

<p align="center">
  <img src="srcs/imgs/ex04%202%20qubits%20histogram.png" alt="Ex04 — 2-qubit Grover: uniform distribution due to iteration overshoot" width="480"/>
</p>

---

## 8. Glossary

| Term | Definition |
|---|---|
| **Qubit** | Quantum unit of information, capable of being in superposition of \|0⟩ and \|1⟩ |
| **Superposition** | State in which a qubit is simultaneously 0 and 1 with associated complex amplitudes |
| **Measurement** | Irreversible operation that collapses superposition to a classical state |
| **Shot** | One execution of the circuit. Many shots are accumulated to reconstruct probabilities |
| **Entanglement** | Non-local correlation between qubits: the global state cannot be factorised into individual states |
| **Bell state** | Maximally entangled 2-qubit state: `(|00⟩+|11⟩)/sqrt(2)` |
| **Amplitude** | Complex number associated with each basis state. Probability = squared norm of amplitude |
| **Phase** | Complex argument of an amplitude. Invisible to direct measurement, crucial for interference |
| **Unitary gate** | Reversible quantum transformation that preserves the norm of the state |
| **Oracle** | Black box encoding a function f into the quantum circuit via phase manipulation |
| **Phase kickback** | Technique to encode f(x) into the phase via an ancilla qubit prepared in `(|0⟩-|1⟩)/sqrt(2)` |
| **Diffuser** | Grover operator that amplifies target amplitudes by reflecting around the mean |
| **Decoherence** | Loss of a qubit's quantum superposition due to interaction with the environment |
| **Quantum noise** | Errors due to hardware imperfections, decoherence, and parasitic interactions |
| **Transpilation** | Adaptation of an ideal circuit to the topology and constraints of a real IBM backend |
| **Aer Simulator** | Ideal (noiseless) quantum circuit simulator provided by IBM/Qiskit |
| **Bloch Sphere** | Geometric representation of a single qubit state as a point on a unit sphere |
| **Tensor product ⊗** | Mathematical operation for combining state spaces of multiple qubits |

---

## 9. References

**Official documentation**
- [IBM Quantum — Hello World](https://quantum.cloud.ibm.com/docs/en/guides/hello-world)
- [IBM Quantum Learning — Basics of Quantum Information](https://quantum.cloud.ibm.com/learning/en/courses/basics-of-quantum-information/single-systems/introduction)
- [Qiskit Documentation](https://docs.quantum.ibm.com/)

**Video resources**
- [Introduction to Quantum Computing (playlist)](https://www.youtube.com/watch?v=9PQIKPHgzo4&list=PLE3ovFxnzNpY3zGw8sHqRorxecoItAAq4)
- [Qubits in detail](https://www.youtube.com/watch?v=bLW4wraE77I&list=PLE3ovFxnzNpY3zGw8sHqRorxecoItAAq4&index=4)
- [Quantum gates](https://www.youtube.com/watch?v=0WZmkIyHOks&list=PLE3ovFxnzNpY3zGw8sHqRorxecoItAAq4&index=10)
- [Quantum algorithms](https://www.youtube.com/watch?v=5_Di12FXRsM&list=PLE3ovFxnzNpY3zGw8sHqRorxecoItAAq4&index=18)

**Books**
- *L'Univers à portée de main* — Christophe Galfard
- *A Brief History of Time* — Stephen Hawking
- *Quantum Computation and Quantum Information* — Nielsen & Chuang (complete academic reference)