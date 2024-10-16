# MathSEE

First steps for Heat Group:
- Lennart tries to connect SimuLink to UMBridge or create a Mockup in Python that can be connected to UMBridge
- The rest of the group writes Code to vary input parameter and generate qualitative output for sensitivity analysis

Input work ideas:
- ...

Output work ideas:
- Look for correlations between input variations and output (i.e., cor(T,i), for i = all R, all C variations)
- For correlating combinations, look into graphs
- evtl. GLM to detect most influencing parameters (exclude autocorrelated parameters > 0.45)

====================================================\\
First steps for Power Group:
- Maren translates all the constraints given in the paper into code (LateX, Python), optimization problem formulation of objective function and constraints
- Ecem puts the differential equations into py functions, sets up the umbridge server
- Simon gets a deeper understanding of the inputs and outputs of each step

Progress: 
- objective function is correct (checked with Niklas)
- constraints are translated into code (LateX, Python), except for the constraint about the first derivative of x_7-12, it stays unclear how this constraint will be added to the optimization problem
- coded constraints and differential equations are merged into one code, first simulation for x_1-6 is generated 
