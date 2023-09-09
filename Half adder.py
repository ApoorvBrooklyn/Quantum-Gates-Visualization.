from qiskit import Aer, IBMQ, QuantumCircuit, execute
from qiskit.providers.aer.noise import NoiseModel
import matplotlib.pyplot as plt
#%matplotlib inline
from qiskit.visualization import plot_histogram

qc = QuantumCircuit(2)
qc.cx(0,1)
qc.draw(output='mpl')

qc = QuantumCircuit(4,2)
# encode inputs in qubits 0 and 1
qc.x(0) #flips 1st qubit to 1
qc.x(1) #flips 2nd qubit to 1 since we want to perform the addition 1+1

# use cnots to write the XOR of the inputs on qubit 2
qc.cx(0,2)
qc.cx(1,2)

# extract outputs
qc.measure(2,0) # extract XOR value
qc.measure(3,1)

qc.draw(output='mpl')

qc = QuantumCircuit(4,2)
# encode inputs in qubits 0 and 1
qc.x(0) 
qc.x(1)
# use cnots to write the XOR of the inputs on qubit 2
qc.cx(0,2)
qc.cx(1,2)
# use ccx to write the AND of the inputs on qubit 3
qc.ccx(0,1,3)
# extract outputs
qc.measure(2,0) # extract XOR value
qc.measure(3,1) # extract AND value

qc.draw(output='mpl')

counts = execute(qc,Aer.get_backend('qasm_simulator')).result().get_counts()
plot_histogram(counts)