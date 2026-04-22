# Quantum Computing - Basic Notes

## Setup & Configuration

### Environment Variables
Credentials are stored in a `.env` file to keep your API token secure.

1. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Configure your API token:**
   - Edit the `.env` file in this directory
   - Replace `<your-44-character-API-key>` with your actual IBM Quantum token
   - Get your token from https://quantum.ibm.com/
   - The `.env` file is **never committed** to Git (protected by `.gitignore`)

3. **Run exercises:**
   ```bash
   python exercices/ex00.py
   python exercices/ex01.py
   python exercices/tests/RealIBMexercice.py
   ```

---

## What quantum computing is
Quantum computing is a different way to process information. Classical computers use bits, and a bit is either 0 or 1. Quantum computers use qubits, which can behave like 0, like 1, or like a mix of both before measurement.

## Bit vs qubit
- A bit has one state at a time: 0 or 1.
- A qubit can be in a superposition: a combination of 0 and 1.
- When you measure a qubit, you do not keep the superposition. You get one classical result.

## Superposition
A superposition means the qubit is not forced to be only 0 or only 1 before measurement.
A common example is:

(|0> + |1>) / sqrt(2)

This means both outcomes are equally likely when measured.

## Measurement and shots
Measurement converts a quantum state into a classical result.
A simulation or a real quantum device is usually run many times. Each run is called a shot.
The histogram shows how often each result appears.

## Entanglement
Entanglement is when two qubits are linked so that you cannot describe them independently anymore.
If one qubit is measured, the result of the other is strongly correlated with it.

A classic entangled state is:

(|00> + |11>) / sqrt(2)

This means:
- you only see 00 or 11,
- you do not see 01 or 10 in an ideal case,
- the two qubits behave like one shared system.

## What creates entanglement
A common way to create entanglement is:
1. Put the first qubit in superposition with a Hadamard gate.
2. Use a CNOT gate to copy that uncertainty into the second qubit.

That is why the first qubit is no longer independent from the second one.

## Why this matters
Quantum effects can be useful because they let us shape probabilities and correlations in ways that classical bits cannot do directly. This is the basis for many quantum algorithms.

## Keywords
- Superposition = several possibilities before measurement.
- Measurement = one classical answer.
- Entanglement = linked qubits with correlated outcomes.
- Histogram = what you observe after repeating the experiment many times.

## References
- https://quantum.cloud.ibm.com/docs/en/guides/hello-world
- https://quantum.cloud.ibm.com/learning/en/courses/basics-of-quantum-information/single-systems/introduction
