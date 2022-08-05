# Jevons-Paradox-and-Cultural-Evolution

Exploration-exploitation model for the investigation of the coupling and decoupling processes between efficiency gains and resource consumption.

The file named Jevons_2.py contain the core classes and functions needed to run the model.

The file named Run_Jevons_2.py is the main script that imports the above mentioned file to run the simulation.

Please note that given the collaborative nature of this project, this version of the model has many comments in the scripts. The purpose is to make it as easy as possible to understand the algorithms we are building from scratch.

## Running simulations

To run simulations, make sure the two files are in the same directory. Open the ```Run_Jevons_2.py``` file in your IDE and declare the variables. To start with, we recommend you to keep the default values and manipulate only the values of the ```rebound``` variable, which can take values from 0 to 1.

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
## Plots

By running the simulations you can obtain charts of population efficiency, existing resources, mean consumption and sustainability index. They look like this:

![image](https://user-images.githubusercontent.com/22002158/183128009-e776a519-3cba-480e-9d2d-878ab02e429e.png)

## Preliminary results

Simulations using the default values and manipulating the rebound value:

Simulations for ```rebound < 0.5```.
There is no resource depletion. Efficiency gains offset the rebound effect.
As efficiency increases, average consumption goes down and sustainability index grows over time.

Simulations for ```rebound = 0.5```.
No resource depletion. Neutral model. Constant mean consumption (assuming constant population).
Sustainability index = 1.

Scenarios for ```rebound = 0.6```.
Most of the time, no resource depletion within the time scales tested.
Consumption goes up. Sustainability index decreases over time.

Scenarios for ```rebound = 0.7, 0.8, 0.9```.
Resource depletion when ```eps = 0.05, eps = 0.1, eps = 0.5 and 0.01```.
No resource depletion when eps = 0.
The higher the efficiency, the faster the resource depletion.
Consumption goes up. Sustainability index decreases over time.

Scenarios for ```rebound = 1```.
Resource depletion when ```eps = 0.05, eps = 0.1, eps = 0.5 and 0.01```.
No resource depletion when ```eps = 0```.
The higher the efficiency, the faster the probability of resource depletion.
Consumption goes up. Sustainability index decreases over time.

The simulations illustrate that in scenarios where there is absolute decoupling between resource consumption and efficiency gains, there is no resource depletion. However, in scenarios where efficiency gains are not able to compensate for the rebound effect, resources are depleted.

In short, the concern is not that consumption (and by extension pollution) within a given resource domain cannot be decoupled from efficiency, but that in absolute terms the decoupling is fast enough to compensate for the rebound effect. In scenarios with a rebound effect of less than 0.5 we observe that this objective is met: there may be an initial increase in consumption, but as the population increases its efficiency, consumption is reduced and allows resources not to be depleted.

## Some limitations

1. The code uses np.random.random(); that's deprecated in favour of the new generators. In future versions we can use
default_rng.

2. The algorithm I use is quite slow in Python. Mainly because there is some recurrence in
the update function. There are several options.
Use scipy.signal.lfilter to try to speed up the simulations.
Change language.
Use the university clusters.
In any case, I have found that the results are the same keeping the N/r_t0 ratio, so it may not be so terrible.
With a bit of time you can simulate larger populations.

3. Constant population.

4. There is only a single domain of natural resources. More could be implemented, which would allow agents to
transition from consumption of one domain to another, so that the pools of some resources are replenished.

5. The distributions of efficiency and resources are probably too simplistic at this stage of development. Although the model illustrates the Jevons paradox quite well.
