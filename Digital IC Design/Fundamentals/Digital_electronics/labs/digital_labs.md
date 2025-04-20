# lab 1 "Introduction to FPGA Design Flow"

## FPGA design flow
1. **Design Entry** : the desired circuit is specified either by means of a schematic diagram or by using a hardware description language (HDL), such as Verilog or VHDL 
2. **Synthesis** : the entered design is synthesized into a netlist that consists of the logic blocks provided in the FPGA chip.
3. **Functional Simulation** : the synthesized circuit is tested to verify its functional correctness; this kind of simulation does not consider any timing issues. 
4. **Placement and Routing (Fitting)** : the Fitter tool determines the placement of the logic blocks defined in the netlist into what is actual FPGA chip has, it also chooses routing wires in the chip to make the required connections between specific blocks. 
5. **Timing Analysis** : propagation delays along the various paths in the fitted circuit are analyzed to provide an indication of the expected performance of the circuit.
6. **Timing Simulation** : the fitted circuit is tested to verify both its functional correctness and timing. 
7. **Programming and Configuration** : the designed circuit is implemented in a physical FPGA chip by programming the configuration switches that configure the LEs (Logic Elements) and establish the required wiring connections.

## Creating new project in Quartus
1. File &rarr;   new project
2.  Next
3. **Enter project information** : name , location , then click next
>==Note== : Both the <u>project</u> and the <u>top level entity</u> **should have the same name**``
4. make sure to Choose Cyclone V as the target device family
- at this point we have created a project
- in order to implement a verilog code we need to create a **Verilog HDL file**
## Creating a Verilog file 
- creating verilog file on quartus text editor
1. File &rarr; New &rarr; "Verilog HDL File" &rarr; Ok
2. ctrl + s (Save as) &rarr; Choose the name for the verilog file (Do not forget the note)
3. Choose the vreilog file (.v extension)

## Adding files to the design 
- you can tell Quartus software which design files it should use as part of the current project
1. "Assignment" &rarr; "Settings" 
2. opening the settings window &rarr; in the left column &rarr; select "Files" 
3. then select Project
4. At the top in the middle there is a bottom that have '...' notations &rarr; click on it 
5. Browse the file destination U want to add 
6. Then add or remove files as U wish 

## Compiling the designed Circuit
- **Compiler** 
1. "Processing" &rarr; "Start Compilation" *OR* Click the blue triangle icon
2. As the compilation moves through various stages, its progress is reported in a window on the left side of the Quartus display.
3. Successful (or unsuccessful) compilation is indicated in a pop-up box. Acknowledge it by clicking OK

# lab 2 "Combinational Circuits"

## Objective Design, model, and simulate combinational circuits using behavioral, structural, and data flow description methodologies.


