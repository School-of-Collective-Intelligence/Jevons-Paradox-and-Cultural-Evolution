# Project: The Jevons Paradox and Cultural Evolution: Investigating the dynamics of
# coupled and decoupled resource use and efficiency gains.
#
# Authors:
# J. Segovia-Martin & J. Winters
#
# Keywords:
# cultural evolution, climate change, computational modelling, environmental economics, ecology
#
# Exploration-exploitation model for the investigation of the coupling and decoupling
# processes between efficiency gains and resource consumption.
#
# We consider a population of agents where agents decide whether to explore or exploit a natural resource.
# Agents become more efficient over time depending on their strategy. Over time, agents consume resources from
# a resource pool. Scenarios with different rebound effects are considered.
#
# We assume that each action has a separate distribution of efficiency and there is at least one action that
# generates maximum efficiency. The probability distribution of efficiency is unknown to the agent. Hence, the goal
# of the agent is to identify which action to choose to get the maximum efficiency after a number of time steps.
#
# Efficiency in this model is operationalised as a reward (we assume that agents want to be
# efficient). The value of each agent's action is calculated as an expected efficiency of that
# action for a set of possible actions: efficiency estimate = sum of efficiency observed for action x before time
# t / number of times action x was taken before time t.
#
# The epsilon here refers to the probability of choosing to explore.
#
# Resources consumed by each agent at each time step are computed as follows:
# resources_consumed_by_agent = bs + (x * rebound) - (1 - rebound) * x
# where bs stands for the baseline agent consumption, x stands for the observed efficiency, rebound stands for the
# marginal rebound effect, (x * rebound) stands for the units of resource consumed due to efficiency gains
# and (1 - rebound) * x stands for the units of resource saved due to efficiency gains. The rebound effect values
# vary between 0 and 1. When the rebound effect is less than 0.5, this means that the efficiency gain outweighs
# the rebound effect. When the rebound effect is greater than 0.5, efficiency gains cannot compensate
# for the rebound effect. When the rebound effect is 0.5, we have a neutral model.
#
# Existing resources at each time t are computed as (x-y)+(x-y)*rep_rate
# where x stands for the amount of resources at time t-1, y stands for the resources consumed by the
# population at time t, and rep_rate stands for the natural replenishment rate.


# Import required libraries
import numpy as np


# Define Action class
class Actions:
    def __init__(self, m):
        self.m = m
        self.mean = 0
        self.t = 0

# Choose a random action
    def choose(self):
        return np.random.randn() + self.m

# Update expected efficiency based on observed efficiency
    def update(self, x):
        self.t += 1
        self.mean = (1 - 1.0 / self.t) * self.mean + 1.0 / self.t * x
        #self.mean = np.clip(self.mean, 0, None)
        return self.mean

# Agent behavior and consumption
def agent_type(num_actions, payoff, eps, t, bs, rebound):
    actions = [Actions(m*payoff) for m in range(0,num_actions)]
    #actions = [Actions(m1), Actions(m2), Actions(m3), Actions(m4)]
    data = np.empty(t)
    data_2 = np.empty(t)

    for i in range(t):
            if i <= 1:
                # efficiency at t0
                x = 0
                # resources consumed at t0
                resources_consumed_by_agent = bs
            else:
                # epsilon
                p = np.random.random()
                if p < eps:  # the larger epsilon is the more likely it is to explore new actions
                    j = np.random.choice(num_actions)
                else:  # exploit current knowledge
                    j = np.argmax([a.mean for a in actions])
                x = actions[j].choose()  # choose action
                actions[j].update(x)  # update efficiency of actions
                # Resources consumed by agent
                resources_consumed_by_agent = bs + (x * rebound) - (1 - rebound) * x
                resources_consumed_by_agent = np.clip(resources_consumed_by_agent, 0, None)

            # data of given agent
            data[i] = x
            data_2[i] = resources_consumed_by_agent


    # Efficiency of the agent at each time step
    efficiency = np.cumsum(data) / (np.arange(t) + 1)
    efficiency = np.clip(efficiency, 0, None)
    # Consumption of the agent at each time step
    consumption = np.cumsum(data_2) / (np.arange(t) + 1)
    # Total cumulative consumption of the agent at each time step
    cumulative_consumption = np.cumsum(data_2)

    return efficiency, consumption, cumulative_consumption


# Running scenarios
def scenario(num_actions, payoff, eps, t, N, bs, r_t0, rep_rate, rebound):
    a = []  # array containing the vectors containing the efficiency of each agent in the population at each time step
    r = []  # array containing the vectors containing the resource consumpion of each agent in the population
    # at each time step
    rt = []  # array containing the vectors containing the cumulative resource consumpion of each agent in the
    # population at each time step

    for agent in range(N):
        agent = agent_type(num_actions, payoff, eps, t, bs, rebound)
        a.append(agent[0])
        r.append(agent[1])
        rt.append(agent[2])
    mean_eff_pop = np.mean(a, 0)  # array containing mean efficiency of the population at each time step
    mean_consumption_pop = np.round(np.mean(r, 0),10)  # array containing mean resource consumpion of the population at
    # each time
    # step
    total_consumption_pop = np.add.reduce(r)  # array containing the consumption of the population at each time step
    # total_consumption_pop =  np.add.reduce(rt)  # array containing the total consumption accumulated by the
    # population at each time step

    # Computing existing resources at each time step:
    # Logic
    # step 1: subtract from the previous value x (previous existing resources) another value y (total consumption of
    # the population)
    # step 2: multiply the result by rep_rate
    # step 3: add the two previous ones
    # Or in a single step:
    # In a single step:
    # Compute (x-y)*rep_rate. Since step 1 gives you (x-y), step 2 gives you (x-y)*rep_rate and step 3 gives you
    # (x-y)+(x-y)*rep_rate, which can be grouped as (x-y)(1+rep_rate).
    # We keep the existing resources with the limits max=r_t0 and min 0.
    existing_resources = [r_t0]
    prior = existing_resources[0]
    for n in total_consumption_pop:
        prior = (prior - n) * (1 + rep_rate)
        prior = np.clip(prior, 0, r_t0)
        existing_resources.append(prior)
    existing_resources = [max(min(y, r_t0), 0) for y in existing_resources]


    return mean_eff_pop, existing_resources, mean_consumption_pop

#if __name__ == '__main__':
    #main()
