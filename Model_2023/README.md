# Efficiency traps beyond the climate crisis: exploration–exploitation tradeoffs and rebound effects.

Python scripts to run the model, as described in:

Segovia-Martin J, Creutzig F, Winters J. 2023 Efficiency traps beyond the climate crisis: exploration–exploitation tradeoffs and rebound effects. Phil. Trans. R. Soc. B 
378: 20220405.
https://doi.org/10.1098/rstb.2022.0405

Reinforcement learning model for the investigation of the coupling and decoupling processes between efficiency gains and resource consumption.

The file named Jevons_10.py contain the core classes and functions needed to run the model.

The file named Run_model_10.py is the main script that imports the above mentioned file to run the simulation.

## Running simulations

### From IDE

To run simulations, make sure the two files (Jevons_10.py and Run_model_10.py) are in the same directory. Open the ```Run_Jevons_10.py``` file in your IDE and declare the variables. Here is an example:

```
# Parameters
a_effic = [0, 1, 2, 3]  # a_effic stands for efficiency rewards. We normalise this vector for the plots. WE assume an
# equivalence with the efficiency vector: Efficiency=a_effic/max(efficiency). That's it, we assume efficiencies from 0 to 1.
t = 10000  # time steps
N = 100  # population size
eps = [0, 0.01, 0.05, 0.1, 0.5]  # epsilon refers to the probability of choosing to explore.
bs = 0.1  # Baseline consumption of each agent at each time step assuming efficiency 0 (in units of the resource).
r_t0 = len(''.join(random.choices(string.ascii_uppercase + string.digits, k=10000)))  # initial_resource_pool in units.
rep_rate = 0.01  # resource units replenished per unit of existing resources at each time step.
rebound = 0.75  # Marginal direct rebound. Additional number of resource units consumed for every one unit increase in
# efficiency. It takes values from 0 to 1 in steps of 0.1.
se_1 = 0.75 # Indirect rebound effect 1: share of resource consumption due to rebound effects in the primary domain (1)
# that are consumed in the subsequent domain (2) as a consequence of the substitution effect
se_2 = 0.75 # Indirect rebound effect 2: share of resource consumption due to rebound effects in the secondary domain (2)
# that are consumed in the subsequent domain (3) as a consequence of the substitution effect
