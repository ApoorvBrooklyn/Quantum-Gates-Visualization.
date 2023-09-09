from qiskit import *
import matplotlib.pyplot as plt
#%matplotlib inline
from qiskit.visualization import plot_histogram
#In quantum computing, the CNOT gate(or controlled-NOT gate) acts in a similar way to the XOR gate. 
# In qiskit the gate is represented by qx.

qc = QuantumCircuit(4,2)
# encode inputs in qubits 0 and 1
qc.x(1) 
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
print(qc)