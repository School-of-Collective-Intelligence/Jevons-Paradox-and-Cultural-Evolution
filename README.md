# Jevons-Paradox-and-Cultural-Evolution
Exploration-exploitation model for the investigation of the coupling and decoupling processes between efficiency gains and resource consumption.

The file named Jevons_2.py contain the core classes and functions needed to run the model.

The file named Run_Jevons_2.py is the main script that imports the above mentioned file to run the simulation. In these scripts you can manipulate:

To run simulations, make sure the two files are in the same directory. Open the ```Run_Jevons_2.py``` file and declare the variables. To start with, we recommend you manipulate the values of the rebound variable, which can take values from 0 to 1.
```
# Parameters
a_effic = [0, 1, 2, 3]  # Efficiency of actions
t = 1000  # time steps
N = 10  # population size
eps = [0, 0.01, 0.05, 0.1, 0.5]  # epsilon refers to the probability of choosing to explore.
bs = 0.1  # Baseline consumption of each agent at each time step assuming efficiency 0 (in units of the resource).
r_t0 = len(''.join(random.choices(string.ascii_uppercase + string.digits, k=1000)))  # initial_resource_pool in units.
rep_rate = 0.01  # resource units replenished per unit of existing resources at each time step.
rebound = 0.2  # Marginal rebound. Additional number of resource units consumed for every one unit increase in
# efficiency. It takes values from 0 to 1 in steps of 0.1.
```

![image](https://user-images.githubusercontent.com/22002158/183128009-e776a519-3cba-480e-9d2d-878ab02e429e.png)
