# Digital hardware
- a design of hardware can be implemented into many chip 
## Type of chips
1. Standard chips
2. PLD programmable logic device
3. CDC custom designed chips

### Standard chips
### PLD
### CDC

# Modeling style
- in verilog every thing is living in module 
- implementing the design on FPGA requires HDL &rarr; Hardware Describing language 
- writing the implementation of a model on an FPGA kit
##### Verilog is divided into 2 modeling style
1. Structural representation
   - Describe the structure of a circuit , like how many AND Gates , OR Gates , ...etc
2. Behavioral representation
   - describe the function of the circuit 


##### Dataflow modeling
# Structural Modeling 
- describe the gate structure for the project 
- *syntax* : `gate_type name (output , input);`
```verilog 

// structural verilog syntax

module first (x1 , x2 , output_);


input x1 , x2 ;
output output_ ; 

and first_gate(output_ , x1 , x2);

endmodule 

/*
 - and        --> gate type
 - first_gate --> gate name
 - x1 , x2    --> inputs to gate
 - output_    --> output of the gate
*/
```

- note: order of gates is not necessary because the code run concurrently   

# Data Flow modeling
- write the equation of the circuit 
- instead of using <u>gate level primitives</u> we can use <u>verilog operators and bit length</u>
```verilog

module first (x1 , x2 , output_);


input x1 , x2 ;
output output_ ; 

assign output_ = x1 & x2 ; // we need to use assign in the dataflow  

```
- any change in the right hand side the **(f)** will change (Continuous model)

# Behavioral modeling
- describing the behavior of a circuit 
- using IF ELSE
- we also need to use **assign** or we use **always end** block
```verilog

module mux_2x1 (x1 , x2 , s , f);

input x1 , x2 , s;
output reg f; // we use reg to remember the previous value --> only in the behavioral 

always@(x1 , x2 , s) // the code will be executed if one of the inputs changed 

if (s)
begin
f = x2;
end

else 
begin
f = x1;
end
end

endmodule 


```

- **IF ELSE** : have *begin* and *end* 
- **always** : have *end*
- **module** : have *end* 