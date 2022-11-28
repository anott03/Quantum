from qiskit import QuantumCircuit, QuantumRegister, \
        ClassicalRegister, Aer

# 3 qubits: origin, destination, auxilary
qr = QuantumRegister(3)
cr = ClassicalRegister(1)
qc = QuantumCircuit(qr, cr)

# in this case we are teleporting state `1`
# to the destination qubit
qc.x(0)

qc.h(1)  # 1 is now [1/sqrt(2), 1/sqrt(2)] (1/2 chance of measuring each state)
qc.cx(1, 2)  # 1 and 2 will now always measure the same state
qc.cx(0, 2)  # 0 and 2 will now always measure the same state
qc.h(0)  # 0 is now [1/sqrt(2), 1/sqrt(2)] (1/2 chance of measuring each state)
qc.cx(2, 1)  # flip 1 if 2 measures 1 - aka now 0 and 1 will measure the same?

# A CZ gate can be made using a CNOT gate (what qiskit does under the hood)
# qc.cz(0, 1)
qc.h(1)
qc.cx(0, 1)
qc.h(1)

qc.measure(1, 0)

sim = Aer.get_backend("aer_simulator")
job = sim.run(qc)
result = job.result()
print(result.get_counts())
