import qiskit
from qiskit import QuantumCircuit
import numpy as np
from qiskit.visualization import visualize_transition
import tkinter
from tkinter import LEFT, END, DISABLED

#define Window
root = tkinter.Tk()
root.title('Quantum Visualization')

#set icon
#root.iconbitmap(default='Image.ico')
root.geometry('399x427')
root.resizable(0,0) #blocking resizing

#define color and background
background = '#2c94c8'
buttons = '#543565'
special_buttons = '#bc3454'
button_font = ('Ariel', 18)
display_font = ('Ariel', 32)

# Initialize the Quantum Circuit
def initialize_circuit():
    global circuit 
    circuit = QuantumCircuit(1)

initialize_circuit()
theta = 0


#define function
def display_gate(gate_input):
    """ Adds the operation to the Display Bar when a Button is pressed
        Automatically disables buttons if the operations exceed 10
    """
    #insert the defined gate
    display.insert(END, gate_input)

    input_gates = display.get()
    num_gates_pressed = len(input_gates)
    list_input_gates= list(input_gates)
    search_word = ["R", "D"]
    count_double_valued_gates = [list_input_gates.count(i) for i in search_word]
    num_gates_pressed -= sum(count_double_valued_gates)
    if num_gates_pressed == 10:
        gates = [x_gate, y_gate, z_gate, Rx_gate, Ry_gate, Rz_gate, hadamard, s_gate, t_gate, sd_gate, td_gate]
        for gate in gates:
            gate.config(state = DISABLED)




#define about Button 
def about():
#    Displays the  info about Button 
    info = tkinter.Tk()
    info.title('About')
    info.geometry('650x470')
    info.resizable(0,0)

    text = tkinter.Text(info, height=20, width=20)
    #Create label
    label = tkinter.Label(info, text='About the Project')
    label.config(font=('Ariel', 14))

    text_to_display ="""
        About : This project was initial Created by Mr. Jay Shah
        Recreated by Apoorv S and Preeti Yadav for Experiancial Learning
        Info about individual Gates

        X = Flips the stateof QBit
        Y = Rotates the state vector about Y axis
        Z = Flips the phase by PI Radian
        RX = parameterised rotation about X Axis
        RY = parameterised rotation about Y Axis
        RZ = parameterised rotation about Z Axis
        S = Rotates the state vector about Z Axis by PI/2 Radians
        T = Rotates the state vector about Z Axis by PI/4 Radians
        Sd = Rotates the state vector aboout Z Axis by -PI/2 Radians
        Td = Rotates the state vector aboout Z Axis by -PI/4 Radians
        H = Creates the state of superposition

        In case of error the app automatically closes 
        This indicates that visualization is not possible
        Note: At a time only 10 operations can be performed
     """
    label.pack()
    text.pack(fill='both', expand=True)

    #INSERT THE TEXT
    text.insert( END, text_to_display)

    #RUN THE CODE
    info.mainloop()

def change_theta(num, window, circuit, key):
        global theta
        theta = num * np.pi
        if key == 'x':
             circuit.rx(theta, 0)
             theta = 0
        elif key == 'y':
             circuit.ry(theta, 0)
             theta = 0
        else : 
             circuit.rz(theta, 0)
             theta = 0
        window.destroy()

        
    
def user_input(circuit, key):
    get_input= tkinter.Tk()
    get_input.title('Get Theta ')
    get_input.geometry('360x160')
    get_input.resizable(0,0)

    val1=tkinter.Button(get_input, height = 2, width= 10, bg=buttons, font=('Ariel',10), text= 'PI/4',command= lambda: change_theta(0.25, get_input, circuit, key) )    
    val1.grid(row=0, column = 0)
    val2=tkinter.Button(get_input, height = 2, width= 10, bg=buttons, font=('Ariel',10), text= 'PI/2',command= lambda: change_theta(0.50, get_input, circuit, key) )    
    val2.grid(row=0, column = 1)
    val3=tkinter.Button(get_input, height = 2, width= 10, bg=buttons, font=('Ariel',10), text= 'PI',command= lambda: change_theta(1.0, get_input, circuit, key) )    
    val3.grid(row=0, column = 2)
    val4=tkinter.Button(get_input, height = 2, width= 10, bg=buttons, font=('Ariel',10), text= '2*PI',command= lambda: change_theta(2.0, get_input, circuit, key) )    
    val4.grid(row=0, column = 3,sticky= 'W')

    nval1=tkinter.Button(get_input, height = 2, width= 10, bg=buttons, font=('Ariel',10), text= '-PI/4',command= lambda: change_theta(-0.25, get_input, circuit, key) )    
    nval1.grid(row=1, column = 0)
    nval2=tkinter.Button(get_input, height = 2, width= 10, bg=buttons, font=('Ariel',10), text= '-PI/2',command= lambda: change_theta(-0.50, get_input, circuit, key) )    
    nval2.grid(row=1, column = 1)
    nval3=tkinter.Button(get_input, height = 2, width= 10, bg=buttons, font=('Ariel',10), text= '-PI',command= lambda: change_theta(-1.0, get_input, circuit, key) )    
    nval3.grid(row=1, column = 2)
    nval4=tkinter.Button(get_input, height = 2, width= 10, bg=buttons, font=('Ariel',10), text= '-2*PI',command= lambda: change_theta(-2.0, get_input, circuit, key) )    
    nval4.grid(row=1, column = 3,sticky= 'W')

    text_object= tkinter.Text(get_input, height= 20, width=20, bg='Light cyan')
    
#define layout
# Define frames
display_frame= tkinter.LabelFrame(root)
button_frame= tkinter.LabelFrame(root, bg='Black')
display_frame.pack()
button_frame.pack(fill='both', expand= True)

#define display frame layout
display = tkinter.Entry(display_frame, width= 120, font= display_font, bg=background, borderwidth=10, justify='left')
display.pack(padx=3, pady=4)


#Define 1st Row Button
x_gate = tkinter.Button(button_frame, font = button_font, bg= buttons, text= 'X', command= lambda: [display_gate('X'), circuit.x(0)])
y_gate = tkinter.Button(button_frame, font = button_font, bg= buttons, text= 'Y',command= lambda: [display_gate('Y'), circuit.y(0)])
z_gate = tkinter.Button(button_frame, font = button_font, bg= buttons, text= 'Z',command= lambda: [display_gate('Z'), circuit.z(0)])

x_gate.grid(row=0, column=0, ipadx=45, pady=1)
y_gate.grid(row=0, column=1, ipadx=45, pady=1)
z_gate.grid(row=0, column=2, ipadx=53, pady=1, sticky='E') # Sticks the buttons to east

#Define 2nd Row
Rx_gate = tkinter.Button(button_frame, font = button_font, bg= buttons, text= 'Rx', command= lambda: user_input(circuit, 'x'))
Ry_gate = tkinter.Button(button_frame, font = button_font, bg= buttons, text= 'Ry', command= lambda: user_input(circuit, 'y'))
Rz_gate = tkinter.Button(button_frame, font = button_font, bg= buttons, text= 'Rz', command= lambda: user_input(circuit, 'z'))
Rx_gate.grid(row=1, column=0, columnspan=1, sticky='WE', pady=1)
Ry_gate.grid(row=1, column=1, columnspan=1, sticky='WE', pady=1)
Rz_gate.grid(row=1, column=2, columnspan=1, sticky='WE', pady=1)

#define 3rd row of buttons
s_gate = tkinter.Button(button_frame, font = button_font, bg= buttons, text= 'S', command= lambda: [display_gate('S'), circuit.s(0)])
sd_gate = tkinter.Button(button_frame, font = button_font, bg= buttons, text= 'SD',command= lambda: [display_gate('Sd'), circuit.sdg(0)])
hadamard = tkinter.Button(button_frame, font = button_font, bg= buttons, text= 'H',command= lambda: [display_gate('H'), circuit.h(0)])
sd_gate.grid(row=2, column=1, sticky='WE', pady=1)
s_gate.grid(row=2, column=0, sticky='WE', pady=1)
hadamard.grid(row=2, column=2, rowspan=2,  sticky='WENS', pady=1)

#defining fifth Column
t_gate = tkinter.Button(button_frame, font = button_font, bg= buttons, text= 'T', command= lambda: [display_gate('T'), circuit.t()])
td_gate = tkinter.Button(button_frame, font = button_font, bg= buttons, text= 'TD',command= lambda: [display_gate('Td'), circuit.tdg()])
t_gate.grid(row=3, column=0, sticky='WE', pady=1)
td_gate.grid(row=3, column=1, sticky='WE', pady=1)

#DEFINE Quit and visualize buttons
quit = tkinter.Button(button_frame, font = button_font, bg= buttons, text= 'Quit', command=root.destroy)
visualize = tkinter.Button(button_frame, font = button_font, bg= buttons, text= 'Visualize')
quit.grid(row=4, column=0, columnspan= 2, sticky='WE',ipadx=5,  pady=1)
visualize.grid(row=4, column=2, columnspan=1, sticky='WE', ipadx = 8, pady=1)

#Define Clear Button
clear_button = tkinter.Button(button_frame, font = button_font, bg= buttons, text= 'Clear')
clear_button.grid(row=5, column=0, columnspan= 3, sticky='WE',ipadx=5,  pady=1)


#Define About 
about_button = tkinter.Button(button_frame, font = button_font, bg= buttons, text= 'About', command=about)
about_button.grid(row=6, column=0, columnspan= 3, sticky='WE',ipadx=5,  pady=1)


#Run the main loop
root.mainloop()
