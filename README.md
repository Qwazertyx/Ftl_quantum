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
- Searching an unsorted database: classically $O(N)$, quantumly $O(\sqrt{N})$ (Grover's algorithm).
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

$$|\psi\rangle = \alpha\,|0\rangle + \beta\,|1\rangle$$

where $\alpha$ and $\beta$ are **complex amplitudes** (they can have an imaginary part) satisfying the **normalisation condition**:

$$|\alpha|^2 + |\beta|^2 = 1$$

Here $|\alpha|$ denotes the **modulus** (absolute value) of the complex number $\alpha$, not a quantum state. This condition ensures that probabilities always sum to 1.

The probability of measuring $|0\rangle$ is $|\alpha|^2$, and the probability of measuring $|1\rangle$ is $|\beta|^2$.

The most common 50/50 superposition state is:

$$|\psi\rangle = \frac{1}{\sqrt{2}}\,|0\rangle + \frac{1}{\sqrt{2}}\,|1\rangle$$

This gives a 50% chance of measuring 0 and 50% of measuring 1 — this is exactly what the Hadamard gate produces.

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

Running 500 shots on $\frac{1}{\sqrt{2}}(|0\rangle + |1\rangle)$ gives approximately 250 times "0" and 250 times "1".

The more shots you run, the more precise your estimate of the probabilities. A single shot tells you nothing about the superposition — it is only the statistical distribution over many shots that reveals it.

### 2.4 The Bloch Sphere

Any pure state of a qubit can be visualised as a **point on a unit sphere** — the Bloch sphere. Every qubit state can be written as:

$$|\psi\rangle = \cos\!\left(\frac{\theta}{2}\right)|0\rangle + e^{i\phi}\sin\!\left(\frac{\theta}{2}\right)|1\rangle$$

where $\theta \in [0, \pi]$ is the polar angle and $\phi \in [0, 2\pi)$ is the azimuthal angle.

- The **north pole** $(\theta = 0)$ represents $|0\rangle$
- The **south pole** $(\theta = \pi)$ represents $|1\rangle$
- The **equator** $(\theta = \pi/2)$ represents all 50/50 superpositions
- The **longitude** (angle $\phi$) encodes the complex phase

Quantum gates are **rotations** of this vector on the sphere:
- Pauli X: 180° rotation around the X axis
- Pauli Y: 180° rotation around the Y axis
- Pauli Z: 180° rotation around the Z axis
- Hadamard: 180° rotation around the diagonal X+Z axis

> **Why does the formula use $\theta/2$ instead of $\theta$?** This is a geometric subtlety: on the Bloch sphere, two opposite points represent orthogonal (completely distinct) quantum states. A full $360°$ rotation of the sphere only brings the qubit back to the same *physical* state up to a global phase — but it takes a $720°$ rotation to restore the state exactly. Dividing angles by 2 is the standard convention that keeps the parametrisation consistent.

<p align="center">
  <img src="srcs/imgs/real-Bloch-sphere-points.avif" alt="Bloch sphere with labelled axes and state vector" width="360"/>
  &nbsp;&nbsp;&nbsp;
  <img src="srcs/imgs/six-Bloch-sphere-points.avif" alt="Bloch sphere showing the six cardinal states" width="360"/>
</p>

---

## 3. Notations

### 3.1 Bra-Ket (Dirac) Notation

Bra-ket notation is the standard language of quantum mechanics. It allows quantum states and operations to be written in a compact, basis-independent way.

**Ket** $|\psi\rangle$ — represents a quantum state (column vector):

```math
|0\rangle = \begin{pmatrix} 1 \\ 0 \end{pmatrix}
\qquad
|1\rangle = \begin{pmatrix} 0 \\ 1 \end{pmatrix}
```

**Bra** $\langle\psi|$ — the conjugate transpose of the ket (row vector):

```math
\langle 0| = \begin{pmatrix} 1 & 0 \end{pmatrix}
\qquad
\langle 1| = \begin{pmatrix} 0 & 1 \end{pmatrix}
```

**Inner product** $\langle\phi|\psi\rangle$ — the overlap between two states. It measures how "similar" they are:

```math
\langle 0|0\rangle = 1 \qquad \langle 1|1\rangle = 1 \qquad \langle 0|1\rangle = 0 \qquad \langle 1|0\rangle = 0
```

The states $|0\rangle$ and $|1\rangle$ are **orthonormal**: they are perfectly distinct (zero overlap) and each has unit length.

**Common states and their vectors:**

| Notation | Description | Column vector |
|---|---|---|
| $\|0\rangle$ | Basis state "zero" | `[1, 0]` |
| $\|1\rangle$ | Basis state "one" | `[0, 1]` |
| $\|{+}\rangle = H\|0\rangle$ | $(+)$ superposition | `[1/√2, 1/√2]` |
| $\|{-}\rangle = H\|1\rangle$ | $(-)$ superposition | `[1/√2, -1/√2]` |

### 3.2 Vector and Matrix Representation

A qubit is a **vector in a 2-dimensional complex vector space** (Hilbert space). A single-qubit gate is a **unitary 2×2 matrix** $U$ satisfying $U^\dagger U = I$, where $U^\dagger$ is the conjugate transpose of $U$.

Applying a gate $U$ to a state $|\psi\rangle$ is a **matrix-vector multiplication**:

$$|\psi'\rangle = U|\psi\rangle$$

Example — the X gate applied to $|0\rangle$:

```math
X\,|0\rangle =
\begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}
\begin{pmatrix} 1 \\ 0 \end{pmatrix}
=
\begin{pmatrix} 0 \\ 1 \end{pmatrix}
= |1\rangle \quad \checkmark
```

The **unitarity** condition $U^\dagger U = I$ guarantees two fundamental things:
1. The normalisation is preserved — probabilities always sum to 1 after any gate.
2. The gate is **reversible** — given the output, you can always recover the input by applying $U^\dagger$.

### 3.3 Multi-Qubit Systems

To describe a system of $n$ qubits, the **tensor product** $\otimes$ is used to combine individual qubit spaces.

The state space of 2 qubits has dimension $2^2 = 4$, spanned by the four basis states:

```math
|00\rangle = \begin{pmatrix}1\\0\\0\\0\end{pmatrix}, \quad
|01\rangle = \begin{pmatrix}0\\1\\0\\0\end{pmatrix}, \quad
|10\rangle = \begin{pmatrix}0\\0\\1\\0\end{pmatrix}, \quad
|11\rangle = \begin{pmatrix}0\\0\\0\\1\end{pmatrix}
```

The notation $|ab\rangle$ means qubit 0 is in state $|b\rangle$ and qubit 1 is in state $|a\rangle$.

> **Qiskit convention:** qubit 0 is the **rightmost** bit. So $|01\rangle$ means qubit 1 = 0, qubit 0 = 1. This is the opposite of most textbooks and can be a source of confusion.

A system of $n$ qubits can be in superposition of **all $2^n$ basis states simultaneously**. This is the source of quantum computing's potential: $n = 50$ qubits span $2^{50} \approx 10^{15}$ states at once.

---

## 4. Quantum Gates

### 4.1 General Properties

All quantum gates satisfy two essential properties:

1. **Unitarity**: $U^\dagger U = I$ — the gate is reversible and preserves the normalisation of the state.
2. **Linearity**: $U\bigl(\alpha|0\rangle + \beta|1\rangle\bigr) = \alpha\,U|0\rangle + \beta\,U|1\rangle$

Unlike classical logic gates (AND, OR, NAND...), a quantum gate can **never lose information**. Knowing the output state is sufficient to recover the input state exactly, by applying $U^\dagger$.

### 4.2 Pauli Gates (X, Y, Z)

The three Pauli gates each correspond to a **180° rotation** around one of the three Cartesian axes of the Bloch sphere.

---

#### Pauli-X Gate (Quantum NOT)

The X gate is the quantum equivalent of the classical NOT gate. It flips $|0\rangle$ to $|1\rangle$ and vice versa.

```math
X = \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}
```

**Action on basis states:**

```math
X\,|0\rangle = |1\rangle \qquad X\,|1\rangle = |0\rangle
```

**Action on a general state:**

$$X\bigl(\alpha|0\rangle + \beta|1\rangle\bigr) = \alpha|1\rangle + \beta|0\rangle$$

The amplitudes are swapped, as expected for a NOT operation.

**Qiskit:** `circuit.x(qubit)`

<p align="center">
  <img src="srcs/imgs/pauli%20x%20gate%20bloch%20sphere.jpg" alt="Pauli-X gate — full Bloch sphere with rotation vectors" width="400"/>
  &nbsp;&nbsp;&nbsp;
  <img src="srcs/imgs/BlochSphere_X_01(pauli%20x%20gate%20sphere).png" alt="Pauli-X gate — rotation arc from |0⟩ to |1⟩" width="290"/>
</p>

---

#### Pauli-Y Gate

The Y gate combines a bit flip (like X) and a phase flip (like Z), with imaginary coefficients.

```math
Y = \begin{pmatrix} 0 & -i \\ i & 0 \end{pmatrix}
```

**Action on basis states:**

```math
Y\,|0\rangle = i\,|1\rangle \qquad Y\,|1\rangle = -i\,|0\rangle
```

The factor $i = \sqrt{-1}$ is an imaginary unit. It introduces a phase difference between the two terms — invisible to measurement directly, but it affects how the state behaves under subsequent gates.

**Qiskit:** `circuit.y(qubit)`

<p align="center">
  <img src="srcs/imgs/BlochSphere_Y_01%20(pauli%20y%20gate%20sphere).png" alt="Pauli-Y gate — 180° rotation around the Y axis" width="290"/>
</p>

---

#### Pauli-Z Gate (Phase Flip)

The Z gate leaves $|0\rangle$ unchanged but multiplies $|1\rangle$ by $-1$. It does **not** change the probability of measuring 0 or 1, but it changes the **phase** of the state, which affects interference with subsequent gates.

```math
Z = \begin{pmatrix} 1 & 0 \\ 0 & -1 \end{pmatrix}
```

**Action on basis states:**

```math
Z\,|0\rangle = |0\rangle \qquad Z\,|1\rangle = -|1\rangle
```

**Action on superposition states — where the effect is visible:**

$$Z\,|{+}\rangle = Z\cdot\frac{1}{\sqrt{2}}(|0\rangle + |1\rangle) = \frac{1}{\sqrt{2}}(|0\rangle - |1\rangle) = |{-}\rangle$$

$$Z\,|{-}\rangle = |{+}\rangle$$

> **Why does phase matter if it's invisible?** Measuring $|{+}\rangle$ and $|{-}\rangle$ both give 50/50 for 0 and 1 — they look identical. But if you apply a Hadamard gate afterwards, $H|{+}\rangle = |0\rangle$ and $H|{-}\rangle = |1\rangle$: the phase difference has been turned into a measurable difference. This is how quantum algorithms encode information in phases that only become visible at the right moment.

**Qiskit:** `circuit.z(qubit)`

<p align="center">
  <img src="srcs/imgs/pauli%20z%20gate%20sphere.png" alt="Pauli-Z gate — phase flip, 180° rotation around the Z axis" width="290"/>
</p>

---

### 4.3 Hadamard Gate (H)

The Hadamard gate is the **most fundamental gate** in quantum computing. It creates superposition from a basis state, and it is its own inverse.

```math
H = \frac{1}{\sqrt{2}}\begin{pmatrix} 1 & 1 \\ 1 & -1 \end{pmatrix}
```

**Action on basis states:**

$$H\,|0\rangle = \frac{1}{\sqrt{2}}\bigl(|0\rangle + |1\rangle\bigr) = |{+}\rangle$$

$$H\,|1\rangle = \frac{1}{\sqrt{2}}\bigl(|0\rangle - |1\rangle\bigr) = |{-}\rangle$$

**Key property — self-inverse:** $H^2 = I$

$$H\,|{+}\rangle = |0\rangle \qquad H\,|{-}\rangle = |1\rangle$$

This is interference at work. When you apply H to $|{+}\rangle = \frac{1}{\sqrt{2}}(|0\rangle + |1\rangle)$, both terms contribute to $|0\rangle$ with the same sign (constructive interference) and cancel each other for $|1\rangle$ (destructive interference). The result is the deterministic state $|0\rangle$.

This property is at the core of Deutsch-Jozsa: applying H twice undoes the superposition, *unless the oracle has modified the phases in between*, in which case the interference pattern changes and a different state emerges.

**Qiskit:** `circuit.h(qubit)`

<p align="center">
  <img src="srcs/imgs/BlochSphere_H_01%20(hadamard%20gate%20sphere).png" alt="Hadamard gate — rotation arc from |0⟩ to |+⟩ on the Bloch sphere" width="290"/>
</p>

---

### 4.4 Phase Gates (S, T)

Phase gates rotate the state around the Z axis by a fraction of 180°, without changing the measurement probabilities of $|0\rangle$ or $|1\rangle$ when measured in the standard basis.

#### S Gate ($\sqrt{Z}$)

```math
S = \begin{pmatrix} 1 & 0 \\ 0 & i \end{pmatrix}
```

Rotation of **90°** ($\pi/2$) around the Z axis.

Verification that $S^2 = Z$:

```math
S^2 = \begin{pmatrix} 1 & 0 \\ 0 & i \end{pmatrix}^2 = \begin{pmatrix} 1 & 0 \\ 0 & i^2 \end{pmatrix} = \begin{pmatrix} 1 & 0 \\ 0 & -1 \end{pmatrix} = Z \quad \checkmark
```

**Qiskit:** `circuit.s(qubit)`

#### T Gate ($\sqrt{S}$, or fourth root of Z)

```math
T = \begin{pmatrix} 1 & 0 \\ 0 & e^{i\pi/4} \end{pmatrix}
```

Rotation of **45°** ($\pi/4$) around the Z axis, where $e^{i\pi/4} = \frac{1+i}{\sqrt{2}}$.

$T^2 = S$, $\quad T^4 = Z$, $\quad T^8 = I$

**Qiskit:** `circuit.t(qubit)`

> **Universal gate set:** The combination $\{H,\ T,\ \text{CNOT}\}$ is sufficient to approximate any quantum computation to arbitrary precision. The T gate provides the "non-trivial" rotation that, combined with the others, generates the full space of possible operations.

---

### 4.5 CNOT Gate

The CNOT (Controlled-NOT) gate is a **two-qubit gate**. It introduces a conditional operation: the target qubit is flipped **only if** the control qubit is $|1\rangle$.

```math
\text{CNOT} = \begin{pmatrix} 1 & 0 & 0 & 0 \\ 0 & 1 & 0 & 0 \\ 0 & 0 & 0 & 1 \\ 0 & 0 & 1 & 0 \end{pmatrix}
```

(rows and columns ordered as $|00\rangle,\, |01\rangle,\, |10\rangle,\, |11\rangle$)

**Action on all basis states:**

| Input | Output | Explanation |
|---|---|---|
| $\|00\rangle$ | $\|00\rangle$ | control = 0 → nothing |
| $\|01\rangle$ | $\|01\rangle$ | control = 0 → nothing |
| $\|10\rangle$ | $\|11\rangle$ | control = 1 → flip target |
| $\|11\rangle$ | $\|10\rangle$ | control = 1 → flip target |

**Qiskit:** `circuit.cx(control, target)`

**Creating entanglement — step by step:**

$$|00\rangle \xrightarrow{H \otimes I} \frac{1}{\sqrt{2}}(|0\rangle + |1\rangle) \otimes |0\rangle = \frac{1}{\sqrt{2}}(|00\rangle + |10\rangle) \xrightarrow{\text{CNOT}} \frac{1}{\sqrt{2}}(|00\rangle + |11\rangle)$$

After the CNOT, the two qubits are **entangled**: the state $\frac{1}{\sqrt{2}}(|00\rangle + |11\rangle)$ cannot be written as a product of two individual qubit states.

<p align="center">
  <img src="srcs/imgs/ex01%20figure%20CNOT%20gate%20and%20Bell%20state%20creation.png" alt="H + CNOT circuit creating the Bell state" width="420"/>
</p>

---

### 4.6 Toffoli Gate (CCX)

The Toffoli gate is a **three-qubit gate** with two control qubits. The target is flipped if and only if **both** controls are $|1\rangle$.

$$\text{Toffoli}\,|110\rangle = |111\rangle \qquad \text{Toffoli}\,|111\rangle = |110\rangle$$

All other basis states are left unchanged.

**Qiskit:** `circuit.ccx(control1, control2, target)`

### 4.7 Multi-Controlled X Gate (MCX)

Generalisation of CNOT to **$n$ control qubits**: the target is flipped only if all $n$ controls are $|1\rangle$.

**Qiskit:** `circuit.mcx(control_list, target)`

This gate is used in Grover's oracle to identify a specific computational basis state among all $2^n$ possibilities.

---

## 5. Quantum Entanglement

Entanglement is perhaps the most counter-intuitive phenomenon in quantum mechanics. Two qubits are **entangled** when their combined state **cannot** be written as a product of two independent single-qubit states.

**Bell state** (one of the four maximally entangled 2-qubit states):

$$|\Phi^+\rangle = \frac{1}{\sqrt{2}}\bigl(|00\rangle + |11\rangle\bigr)$$

**Why this state cannot be factorised:** suppose it could be written as $(a|0\rangle + b|1\rangle)\otimes(c|0\rangle + d|1\rangle)$. Expanding:

$$= ac|00\rangle + ad|01\rangle + bc|10\rangle + bd|11\rangle$$

For this to equal $\frac{1}{\sqrt{2}}(|00\rangle + |11\rangle)$, we would need $ad = 0$ and $bc = 0$, while $ac = bd \neq 0$. But $ac \neq 0$ requires $a,c \neq 0$, and $bd \neq 0$ requires $b,d \neq 0$ — this contradicts $ad = 0$. **No solution exists**, so the state cannot be factorised.

**What entanglement means in practice:**
- Before measurement: neither qubit has a definite state on its own.
- Measuring qubit 0 and getting $|0\rangle$ → qubit 1 is instantly $|0\rangle$.
- Measuring qubit 0 and getting $|1\rangle$ → qubit 1 is instantly $|1\rangle$.
- This correlation exists regardless of the physical distance between the qubits.

> This is not faster-than-light communication: you cannot choose which outcome you get, so you cannot use this to transmit information. The correlation is real, but it only becomes apparent when you compare results — which requires a classical channel.

**How entanglement is created (ex01):**

$$|00\rangle \xrightarrow{H\text{ on q0}} \frac{1}{\sqrt{2}}(|0\rangle + |1\rangle) \otimes |0\rangle \xrightarrow{\text{CNOT}} \frac{1}{\sqrt{2}}(|00\rangle + |11\rangle)$$

**Observed results in the simulator:**
- Only `00` and `11` appear — each ~50% of shots.
- `01` and `10` **never** appear. This is the experimental signature of entanglement.

<p align="center">
  <img src="srcs/imgs/ex01%20entanglement%20histogram.png" alt="Entanglement histogram — only 00 and 11 appear, never 01 or 10" width="480"/>
</p>

---

## 6. Quantum Algorithms

### 6.1 Deutsch-Jozsa

#### Context and Motivation

The Deutsch-Jozsa problem is the **first algorithm proven to have quantum advantage** over any classical algorithm for the same task. It has no direct practical application, but it is historically and pedagogically important: it shows clearly *how* quantum superposition allows a global question to be answered in a single step.

**The problem:** we are given a black-box function $f : \{0,1\}^n \to \{0,1\}$ (called an oracle). We are told it is **guaranteed** to be one of two kinds:
- **Constant**: $f(x) = 0$ for all $x$, or $f(x) = 1$ for all $x$.
- **Balanced**: $f(x) = 0$ for exactly $2^{n-1}$ inputs, and $f(x) = 1$ for the other $2^{n-1}$ inputs.

**Question:** Is $f$ constant or balanced?

| Approach | Worst-case queries to $f$ |
|---|---|
| Classical (deterministic) | $2^{n-1} + 1$ |
| Quantum (Deutsch-Jozsa) | **1** |

For $n = 100$, a classical computer might need $2^{99} + 1 \approx 6 \times 10^{29}$ queries. The quantum algorithm always answers in exactly **one** query.

---

#### The Circuit

```
q0 :  ───── H ── [  Oracle  ] ── H ───  Measure
q1 :  ───── H ── [  Oracle  ] ── H ───  Measure
q2 :  ───── H ── [  Oracle  ] ── H ───  Measure
q3 :  ─ X ─ H ── [  Oracle  ] ─────── (not measured)
       Init  Superposition  Interference  Result
```

<p align="center">
  <img src="srcs/imgs/ex03%20deutsch%20jozsa%20circuit.png" alt="Deutsch-Jozsa circuit — 3 input qubits + 1 ancilla" width="750"/>
</p>

---

#### Detailed Steps

**Step 1 — Initialisation**

$$|0\rangle^{\otimes n}|0\rangle \xrightarrow{X \text{ on ancilla}} |0\rangle^{\otimes n}|1\rangle$$

The ancilla (auxiliary) qubit is flipped to $|1\rangle$ before anything else.

**Step 2 — Superposition (first H layer)**

$$|0\rangle^{\otimes n}|1\rangle \xrightarrow{H^{\otimes(n+1)}} \frac{1}{\sqrt{2^n}}\sum_{x=0}^{2^n - 1}|x\rangle \otimes \frac{|0\rangle - |1\rangle}{\sqrt{2}}$$

- The $n$ input qubits are now in a **uniform superposition** of all $2^n$ possible inputs simultaneously.
- The ancilla is in the state $\frac{1}{\sqrt{2}}(|0\rangle - |1\rangle)$, which is the key to the phase kickback trick below.

**Step 3 — Oracle (phase kickback)**

The oracle implements the map $|x\rangle|y\rangle \to |x\rangle|y \oplus f(x)\rangle$, where $\oplus$ is addition modulo 2 (XOR).

When the ancilla is in $\frac{1}{\sqrt{2}}(|0\rangle - |1\rangle)$, this map produces:

$$|x\rangle \cdot \frac{|0\rangle - |1\rangle}{\sqrt{2}} \;\longrightarrow\; (-1)^{f(x)}\,|x\rangle \cdot \frac{|0\rangle - |1\rangle}{\sqrt{2}}$$

The function value $f(x)$ is "kicked back" as a **phase** on the input register, and the ancilla is unchanged. After the oracle:

$$\frac{1}{\sqrt{2^n}}\sum_{x=0}^{2^n-1}(-1)^{f(x)}|x\rangle \otimes \frac{|0\rangle - |1\rangle}{\sqrt{2}}$$

- If $f$ is **constant**: all $(-1)^{f(x)}$ are equal (all $+1$ or all $-1$) → the phases are identical across all terms.
- If $f$ is **balanced**: exactly half the $(-1)^{f(x)}$ are $+1$ and half are $-1$ → the phases cancel pairwise.

**Step 4 — Interference (second H layer on input qubits)**

Applying $H^{\otimes n}$ again on the $n$ input qubits. The result, after some algebra, is:

$$H^{\otimes n}\,\frac{1}{\sqrt{2^n}}\sum_{x}(-1)^{f(x)}|x\rangle = \sum_{z}\left(\frac{1}{2^n}\sum_{x}(-1)^{f(x)+x\cdot z}\right)|z\rangle$$

The amplitude of the all-zeros state $|0\rangle^{\otimes n} = |00\ldots0\rangle$ is:

$$\frac{1}{2^n}\sum_{x=0}^{2^n-1}(-1)^{f(x)}$$

- $f$ **constant**: all $(-1)^{f(x)}$ equal → sum $= \pm 2^n$ → amplitude $= \pm 1$ → **probability 1** of measuring $|00\ldots0\rangle$.
- $f$ **balanced**: exactly half are $+1$, half are $-1$ → sum $= 0$ → amplitude $= 0$ → **probability 0** of measuring $|00\ldots0\rangle$.

**Step 5 — Measurement**

| Measurement result | Oracle type |
|---|---|
| All qubits $= 0$ (i.e. `000`) | **Constant** |
| Any qubit $= 1$ | **Balanced** |

<p align="center">
  <img src="srcs/imgs/ex03%20oracle%20constant.png" alt="Deutsch-Jozsa — constant oracle: 100% of shots measure 000" width="450"/>
  &nbsp;&nbsp;&nbsp;
  <img src="srcs/imgs/ex03%20oracle%20balanced.png" alt="Deutsch-Jozsa — balanced oracle: 100% of shots measure a non-zero state" width="450"/>
</p>

---

#### Oracles used in ex03

**Constant-0 oracle:** does nothing — $f(x) = 0$ for all $x$.

**Constant-1 oracle:** applies X unconditionally to the ancilla — $f(x) = 1$ for all $x$.

**Balanced oracle:** CNOT from each input qubit to the ancilla, implementing:

$$f(x) = x_0 \oplus x_1 \oplus x_2$$

This function equals 0 for exactly 4 of the 8 inputs, and 1 for the other 4 — balanced by construction.

---

### 6.2 Grover's Search Algorithm

#### The Search Problem

We have $N = 2^n$ unsorted items and want to find the one(s) satisfying some condition (marked by an oracle). No structure is assumed — this is unstructured search.

| Approach | Average number of oracle queries |
|---|---|
| Classical (random) | $N/2$ |
| Quantum (Grover) | $\approx \frac{\pi}{4}\sqrt{N}$ |

For $N = 10^6$: classical $= 500{,}000$ queries, Grover $\approx 785$ queries. The quantum speedup is **quadratic**: $O(\sqrt{N})$ vs $O(N)$.

> Note: this is a provably optimal quantum speedup for unstructured search. No quantum algorithm can do better than $O(\sqrt{N})$ for this problem.

---

#### Circuit Overview

```
q0 :  ─ H ─ [ Oracle ] ─ [ Diffuser ] ─ [ Oracle ] ─ [ Diffuser ] ─ ... ─  Measure
q1 :  ─ H ─ [ Oracle ] ─ [ Diffuser ] ─ [ Oracle ] ─ [ Diffuser ] ─ ... ─  Measure
q2 :  ─ H ─ [ Oracle ] ─ [ Diffuser ] ─ [ Oracle ] ─ [ Diffuser ] ─ ... ─  Measure

      Init  ◄──────────── Repeat k_opt times ──────────────►
```

<p align="center">
  <img src="srcs/imgs/ex04%20grover%20circuit.png" alt="Grover's algorithm circuit — 3 qubits" width="750"/>
</p>

---

#### The Three Parts of the Algorithm

**Part 1 — Initialisation: uniform superposition**

Apply $H^{\otimes n}$ to $|0\rangle^{\otimes n}$:

$$|s\rangle = H^{\otimes n}|0\rangle^{\otimes n} = \frac{1}{\sqrt{N}}\sum_{x=0}^{N-1}|x\rangle$$

Every basis state has equal amplitude $\frac{1}{\sqrt{N}}$ and equal probability $\frac{1}{N}$.

**Part 2 — The Oracle: phase marking**

The oracle flips the sign of the amplitude of the target state(s) without changing any other state:

$$\text{Oracle}\,|x\rangle = \begin{cases} -|x\rangle & \text{if } x \text{ is a solution} \\ \phantom{-}|x\rangle & \text{otherwise} \end{cases}$$

After the oracle, the target amplitude is $-\frac{1}{\sqrt{N}}$ while all others remain $+\frac{1}{\sqrt{N}}$. The probability distribution is **still uniform** — you cannot yet detect the target by measuring. The information is encoded in the sign of the amplitude (the phase), not in the probability.

**Part 3 — The Diffuser: amplification by reflection**

The diffuser is defined as:

$$D = 2|s\rangle\langle s| - I = H^{\otimes n}(2|0\rangle\langle 0| - I)H^{\otimes n}$$

It performs a **reflection about the mean amplitude**. Let $\mu$ be the average amplitude of all states after the oracle. Reflecting each amplitude $a_x$ around $\mu$ transforms it to $2\mu - a_x$.

After one Oracle + Diffuser iteration on a single target:

$$\text{Target amplitude:} \quad -\frac{1}{\sqrt{N}} \;\longrightarrow\; \frac{(N-2)}{\sqrt{N}\cdot N} \cdot 2 + \frac{1}{\sqrt{N}} \approx \frac{3}{\sqrt{N}} \quad \text{(grows)}$$

Each Grover iteration increases the target amplitude by approximately $\frac{2}{\sqrt{N}}$, while slightly decreasing all others.

**Circuit implementation of the Diffuser:**

$$H^{\otimes n} \;\longrightarrow\; X^{\otimes n} \;\longrightarrow\; \text{MCX} \;\longrightarrow\; X^{\otimes n} \;\longrightarrow\; H^{\otimes n}$$

---

#### Optimal Number of Iterations

After $k$ iterations, the probability of measuring the target is:

$$P(k) = \sin^2\!\bigl((2k+1)\,\theta\bigr) \qquad \text{where} \quad \theta = \arcsin\!\left(\sqrt{\frac{m}{N}}\right)$$

and $m$ is the number of target states. The optimal number of iterations is:

$$k_{\text{opt}} \approx \frac{\pi}{4}\sqrt{\frac{N}{m}}$$

**Example:** $n = 3$, $N = 8$, $m = 1$:

$$k_{\text{opt}} \approx \frac{\pi}{4}\sqrt{8} \approx 0.785 \times 2.828 \approx 2.22 \quad \Rightarrow \quad k = 2$$

At $k = 2$: $P = \sin^2(5\theta)$ where $\theta = \arcsin(1/\sqrt{8}) \approx 0.361$ rad, giving $P \approx \sin^2(1.807) \approx 0.972$, i.e. **~97%**. ✓

> **Critical point:** too few iterations means low probability (the amplitude hasn't grown enough). Too many means the probability starts dropping again (the amplitude overshoots the peak and starts decreasing). The formula gives the unique optimal stopping point. This is fundamentally different from classical search — you must know when to stop.

---

#### Edge Case: $n = 2$ qubits

For $n = 2$, $N = 4$, $m = 1$:

$$k_{\text{opt}} = \frac{\pi}{4}\sqrt{4} = \frac{\pi}{2} \approx 1.57 \quad \Rightarrow \quad \text{rounds to } k = 2$$

But the **exact** probability at $k = 1$ is:

$$\theta = \arcsin\!\left(\frac{1}{2}\right) = \frac{\pi}{6} \qquad P(1) = \sin^2\!\left(\frac{3\pi}{6}\right) = \sin^2\!\left(\frac{\pi}{2}\right) = 1 \quad \Rightarrow \quad \textbf{100\%}$$

One iteration would be **perfect**. But the formula rounds to 2 iterations, and:

$$P(2) = \sin^2\!\left(\frac{5\pi}{6}\right) = \sin^2\!\left(\pi - \frac{\pi}{6}\right) = \sin^2\!\left(\frac{\pi}{6}\right) = \frac{1}{4} = 25\%$$

With $k = 2$, the target gets only **25% probability** — no better than random. This is visible in the histogram below: the distribution is nearly uniform over all four states. The approximation $k_{\text{opt}} \approx \frac{\pi}{4}\sqrt{N}$ breaks down for small $N$.

---

#### Results

**$n = 3$ qubits, target `101`, 2 iterations:** the target dominates with ~97% of shots.

<p align="center">
  <img src="srcs/imgs/ex%2004%203qubit%2C%20single%20target%20101.png" alt="Grover result — target state 101 at ~95% of 1024 shots" width="500"/>
</p>

**$n = 2$ qubits, target `11`, 2 iterations (one too many):** nearly uniform — the algorithm overshot.

<p align="center">
  <img src="srcs/imgs/ex04%20grover%20circuit%202%20qubits.png" alt="Ex04 — Grover circuit for 2 qubits" width="720"/>
</p>

<p align="center">
  <img src="srcs/imgs/ex04%202%20qubits%20histogram.png" alt="Ex04 — 2-qubit Grover: near-uniform distribution due to iteration overshoot" width="480"/>
</p>

---

## 7. Exercises — Code Reference

### Ex00 — Superposition

**Goal:** Create the state $\frac{1}{\sqrt{2}}(|0\rangle + |1\rangle)$ with a single qubit.

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

**Goal:** Create the Bell state $\frac{1}{\sqrt{2}}(|00\rangle + |11\rangle)$.

```
Circuit:  q0 : ─ H ─●─ Measure
                     │
          q1 : ─────⊕─ Measure
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
- **Decoherence**: physical qubits gradually lose their quantum state due to interactions with the environment. The longer the circuit, the more decoherence accumulates.
- **Gate errors**: no physical gate is perfectly implemented — there is always a small probability of error per gate application.
- **Transpilation**: the ideal circuit must be adapted to the physical chip's connectivity (not all qubit pairs are directly connected). Extra SWAP gates are inserted, each adding more error.
- **Readout errors**: the measurement process itself can misclassify a qubit — reading $|1\rangle$ when the qubit was actually $|0\rangle$.

These errors are why the histogram from real hardware shows small but non-zero bars at `01` and `10`, which would be exactly zero in the ideal simulation.

Comparing the two histograms side by side makes the difference clear: the simulator gives a perfectly clean result (`00` and `11` only), while real hardware leaks a few percent into the forbidden states `01` and `10`.

**Run:** `python ex02.py`

<p align="center">
  <img src="srcs/imgs/ex01%20entanglement%20histogram.png" alt="Ex01 — ideal simulator: only 00 and 11" width="420"/>
  &nbsp;&nbsp;&nbsp;
  <img src="srcs/imgs/quantum_noise_ex02.png" alt="Ex02 — real IBM hardware: 01 and 10 appear due to quantum noise" width="420"/>
</p>
<p align="center"><em>Left: ideal Aer simulator (ex01) &nbsp;—&nbsp; Right: real IBM hardware (ex02)</em></p>

---

### Ex03 — Deutsch-Jozsa

**Goal:** Implement the Deutsch-Jozsa algorithm on 4 qubits (3 input + 1 ancilla) and determine — in a single circuit execution — whether a given oracle is constant or balanced.

**Run:** `python ex03.py`  *(automatically tests Constant-0, Constant-1, and Balanced oracles)*

---

#### What the circuit does, step by step

The circuit uses **4 qubits**: q0, q1, q2 are the input qubits, and q3 is the **ancilla** (an auxiliary qubit used as a tool — it is never measured).

**Step 1 — Prepare the ancilla:**  
Apply X to q3, putting it in $|1\rangle$. Then apply H to all 4 qubits.  
- The 3 input qubits enter a **uniform superposition** of all 8 possible inputs simultaneously.  
- The ancilla ends up in $\frac{1}{\sqrt{2}}(|0\rangle - |1\rangle)$ — the specific state required for phase kickback.

**Step 2 — Apply the oracle:**  
The oracle is a black box that computes $f(x)$. Because the ancilla is in $\frac{1}{\sqrt{2}}(|0\rangle - |1\rangle)$, the effect on the input register is:

$$|x\rangle \;\longrightarrow\; (-1)^{f(x)}\,|x\rangle$$

The value of $f(x)$ is encoded as a **phase** ($+1$ or $-1$) on each input state — not as a bit flip. This is called **phase kickback**.

- If $f$ is constant: all phases are identical → no relative difference between input states.
- If $f$ is balanced: half the phases are $+1$, half are $-1$ → the input states are split into two groups with opposite signs.

**Step 3 — Second H layer (interference):**  
Apply H again to the 3 input qubits. Due to quantum interference:
- If all phases were identical (constant $f$): all terms constructively interfere into $|000\rangle$ → **100% chance of measuring `000`**.
- If phases were split (balanced $f$): $|000\rangle$ is completely cancelled by destructive interference → **0% chance of measuring `000`**, guaranteed to measure something else.

**Decision rule:**

$$\text{Measure } |000\rangle \;\Longrightarrow\; f \text{ is CONSTANT} \qquad \text{Measure anything else} \;\Longrightarrow\; f \text{ is BALANCED}$$

This is deterministic — not probabilistic. The algorithm answers with **certainty** in one shot.

---

#### Why this is faster than any classical algorithm

A classical computer must call $f$ on actual inputs to learn about it. In the worst case, it needs to evaluate $f$ on $2^{n-1} + 1 = 5$ different inputs (for $n=3$) before it can be certain. It could be lucky and find two different outputs early, but it could also see the same output 4 times in a row — still unable to distinguish constant from balanced.

The quantum algorithm queries $f$ only **once**, but queries it on all $2^n$ inputs *simultaneously* through superposition. The oracle's effect is felt across the entire superposition in a single step. The second H layer then turns that global phase pattern into a single measurable outcome.

---

#### The three oracles tested

**Constant-0:** the oracle does nothing. Every input gets phase $+1$. The second H collapses everything to $|000\rangle$. → `000`

**Constant-1:** the oracle applies X to the ancilla unconditionally. Every input gets phase $-1$. All phases are still equal, so the second H still collapses to $|000\rangle$ (with a global $-1$ that is undetectable). → `000`

**Balanced:** each input qubit is CNOTed onto the ancilla, implementing $f(x) = x_0 \oplus x_1 \oplus x_2$. Exactly 4 of the 8 inputs get phase $+1$ and 4 get phase $-1$. The second H completely cancels $|000\rangle$. → `111` (in this specific oracle)

<p align="center">
  <img src="srcs/imgs/ex03%20deutsch%20jozsa%20circuit.png" alt="Ex03 — Deutsch-Jozsa circuit: X on ancilla, H on all, oracle, H on inputs, measure" width="720"/>
</p>

<p align="center">
  <img src="srcs/imgs/ex03%20oracle%20constant.png" alt="Constant oracle: 100% of shots give 000" width="320"/>
  &nbsp;&nbsp;&nbsp;
  <img src="srcs/imgs/ex03%20oracle%20balanced.png" alt="Balanced oracle: 100% of shots give 111" width="320"/>
</p>
<p align="center"><em>Left: constant oracle — all 1024 shots give <code>000</code> &nbsp;—&nbsp; Right: balanced oracle — all 1024 shots give <code>111</code></em></p>

**Key code:**
```python
def build_dj_circuit(oracle, n):
    circuit = QuantumCircuit(n + 1, n)
    circuit.x(n)           # flip ancilla to |1⟩
    circuit.h(range(n+1))  # superpose all qubits
    circuit.compose(oracle, inplace=True)
    circuit.h(range(n))    # interference on input qubits only
    circuit.measure(range(n), range(n))
    return circuit
```

---

### Ex04 — Grover's Algorithm

**Goal:** Find one or more target states among $2^n$ with $O(\sqrt{N})$ oracle queries instead of the classical $O(N)$.

**Run:** `python ex04.py`

---

#### What the circuit does, step by step

**Step 1 — Initialisation:**  
Apply H to all $n$ qubits. Every state $|x\rangle$ gets amplitude $\frac{1}{\sqrt{N}}$ — a perfectly uniform superposition. All states are equally likely.

**Step 2 — Oracle (phase marking):**  
The oracle flips the sign of the amplitude of any target state and leaves all others unchanged:

$$\text{Oracle}\,|x\rangle = \begin{cases} -|x\rangle & \text{if } x \text{ is a target} \\ \phantom{-}|x\rangle & \text{otherwise} \end{cases}$$

After the oracle, the probabilities of measuring each state are still all $\frac{1}{N}$ — the oracle changed only the **sign** of the target's amplitude, not its magnitude. The information is hidden in the phase. You cannot detect the target yet.

**Step 3 — Diffuser (amplification by reflection):**  
The diffuser reflects all amplitudes around their **mean value**. After the oracle, the target amplitude is the only negative one, so the mean is slightly below $\frac{1}{\sqrt{N}}$. Reflecting around this mean pushes the target well above average and slightly lowers all other states.

Each Oracle + Diffuser iteration increases the target amplitude by approximately $\frac{2}{\sqrt{N}}$. After $k_{\text{opt}}$ iterations, the target amplitude has grown large enough that measuring it is near-certain.

**Step 4 — Measure:**  
The target state now has overwhelmingly higher probability than all others. Measuring collapses the state to the target with high probability.

---

#### The optimal number of iterations

$$k_{\text{opt}} \approx \frac{\pi}{4}\sqrt{\frac{N}{m}}$$

where $N = 2^n$ is the total number of states and $m$ is the number of targets.

| Qubits $n$ | States $N$ | Targets $m$ | $k_{\text{opt}}$ | Classical average |
|:---:|:---:|:---:|:---:|:---:|
| 3 | 8 | 1 | 2 | 4 |
| 5 | 32 | 1 | 4 | 16 |
| 10 | 1 024 | 1 | 25 | 512 |
| 20 | 1 048 576 | 1 | 804 | 524 288 |

**Important:** the formula is an approximation. It works very well when $N \gg m$, but breaks down when $N/m$ is small (e.g. $N/m = 4$). In those cases, the rounded $k$ can be one step past the optimal, and the amplitude overshoots the peak — reducing the success probability back toward random. This is demonstrated in examples 2 and 3 below.

---

#### Example 1 — $n=3$ qubits, single target `101`

$k_{\text{opt}} = \text{round}\!\left(\frac{\pi}{4}\sqrt{8}\right) = \text{round}(2.22) = 2$

The target appears in ~95% of shots. The remaining ~5% are spread evenly across the other 7 states.

<p align="center">
  <img src="srcs/imgs/ex04 exemple 1 circuit.png" alt="Grover circuit — n=3, single target 101" width="620"/>
</p>
<p align="center">
  <img src="srcs/imgs/ex04 example 1 graph.png" alt="Grover histogram — n=3, target 101: ~95% of shots" width="380"/>
</p>

---

#### Example 2 — $n=3$ qubits, two targets `011` and `110`

With 2 targets, the formula gives:

$$k_{\text{opt}} = \text{round}\!\left(\frac{\pi}{4}\sqrt{\frac{8}{2}}\right) = \text{round}\!\left(\frac{\pi}{4} \cdot 2\right) = \text{round}(1.57) = 2$$

But the **exact** optimal is $k = 1$. At $k = 1$ with $m = 2$ targets:

$$\theta = \arcsin\!\sqrt{\frac{2}{8}} = \arcsin\!\left(\frac{1}{2}\right) = \frac{\pi}{6} \qquad P(1) = \sin^2\!\left(\frac{3\pi}{6}\right) = \sin^2\!\left(\frac{\pi}{2}\right) = 1 \quad (100\%)$$

With $k = 2$ however:

$$P(2) = \sin^2\!\left(\frac{5\pi}{6}\right) = \sin^2\!\left(\frac{\pi}{6}\right) = \frac{1}{4} = 25\% \text{ per target}$$

The algorithm overshot. The histogram is nearly uniform — the amplification went past the peak and came back down, making all states equally likely again. This is the same failure mode as Example 3 for the same mathematical reason: $N/m = 4$ in both cases.

<p align="center">
  <img src="srcs/imgs/ex04 example2 circuit.png" alt="Grover circuit — n=3, two targets 011 and 110" width="620"/>
</p>
<p align="center">
  <img src="srcs/imgs/ex04 example 2 graph.png" alt="Grover histogram — n=3, two targets: near-uniform, algorithm overshot" width="380"/>
</p>

---

#### Example 3 — $n=2$ qubits, single target `11`

With $N = 4$ and $m = 1$:

$$k_{\text{opt}} = \text{round}\!\left(\frac{\pi}{4}\sqrt{4}\right) = \text{round}\!\left(\frac{\pi}{2}\right) = \text{round}(1.57) = 2$$

But the exact optimal is again $k = 1$ (probability = 100%). With $k = 2$, the probability drops to 25% — no better than guessing at random among 4 states. The histogram is uniform.

This is an important result: **Grover's algorithm requires a large enough search space to work well.** The approximation $k_{\text{opt}} \approx \frac{\pi}{4}\sqrt{N/m}$ assumes $N \gg m$. When $N/m$ is small (here $N/m = 4$), the rounding error in $k$ is significant relative to the period of the probability oscillation.

<p align="center">
  <img src="srcs/imgs/ex04 example 3 circuit.png" alt="Grover circuit — n=2, single target 11" width="620"/>
</p>
<p align="center">
  <img src="srcs/imgs/ex04 example 3 graph.png" alt="Grover histogram — n=2, target 11: near-uniform, algorithm overshot" width="380"/>
</p>

**Key code:**
```python
run_exercise(n=3, targets=["101"], shots=1024)         # Example 1: single target, works perfectly
run_exercise(n=3, targets=["011", "110"], shots=1024)  # Example 2: two targets, k_opt rounding fails
run_exercise(n=2, targets=["11"], shots=1024)          # Example 3: too small N, k_opt rounding fails
```

```python
# Iterations computed automatically:
iterations = max(1, round((math.pi / 4) * math.sqrt(N / k)))
```

---

## 8. Glossary

| Term | Definition |
|---|---|
| **Qubit** | Quantum unit of information, capable of being in superposition of $\|0\rangle$ and $\|1\rangle$ |
| **Superposition** | State $\alpha\|0\rangle + \beta\|1\rangle$ where the qubit has no definite classical value before measurement |
| **Amplitude** | Complex coefficient $\alpha$ or $\beta$ of a basis state. The measurement probability equals its squared modulus $\|\alpha\|^2$ |
| **Phase** | The complex argument of an amplitude. Invisible to direct measurement, but shapes interference between states |
| **Normalisation** | The condition $\|\alpha\|^2 + \|\beta\|^2 = 1$ ensuring all probabilities sum to 1 |
| **Measurement** | Irreversible operation that collapses superposition to a single classical outcome |
| **Shot** | One execution of the circuit. Many shots are needed to reconstruct the probability distribution |
| **Entanglement** | Correlation between qubits such that their joint state cannot be written as a product of individual states |
| **Bell state** | One of the four maximally entangled 2-qubit states; e.g. $\frac{1}{\sqrt{2}}(\|00\rangle+\|11\rangle)$ |
| **Unitary gate** | Reversible quantum transformation $U$ satisfying $U^\dagger U = I$ |
| **Oracle** | Black-box circuit encoding a function $f$ into the quantum computation via phase manipulation |
| **Phase kickback** | Technique where an ancilla qubit in $\frac{1}{\sqrt{2}}(\|0\rangle-\|1\rangle)$ absorbs $(-1)^{f(x)}$ as a phase on the input register |
| **Diffuser** | Grover operator implementing reflection about the uniform superposition $\|s\rangle$; amplifies target amplitudes |
| **Decoherence** | Gradual loss of quantum superposition due to uncontrolled interactions with the environment |
| **Quantum noise** | Collective term for errors from decoherence, imperfect gates, and faulty measurements on real hardware |
| **Transpilation** | Process of rewriting an ideal circuit to comply with a backend's physical gate set and qubit connectivity |
| **Aer Simulator** | IBM/Qiskit software simulator that models a perfect (noiseless) quantum computer classically |
| **Bloch Sphere** | Geometric representation of a single qubit state as a point on a unit sphere in 3D space |
| **Tensor product $\otimes$** | Mathematical operation that combines the state spaces of individual qubits into a joint multi-qubit space |

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
