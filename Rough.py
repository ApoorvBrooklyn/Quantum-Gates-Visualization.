from qiskit import QuantumCircuit
from qiskit.visualization import visualize_transition
circuit = QuantumCircuit(1,0)
circuit.x(0)

visualize_transition(circuit)
#circuit.barrier()
#print(circuit)