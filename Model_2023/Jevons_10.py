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

    # Update of the action-value estimate (i.e. expected efficiency)
    def update(self, x):
        self.t += 1
        self.mean = (1 - 1.0 / self.t) * self.mean + 1.0 / self.t * x
        # self.mean = np.clip(self.mean, 0, None)
        return self.mean

# Agent behavior and consumption
def agent_type(m1, m2, m3, m4, eps, t, bs, rebound, se_1, se_2):
    actions = [Actions(m1), Actions(m2), Actions(m3), Actions(m4)]
    data = np.empty(t)
    data_2_dom_1 = np.empty(t)
    data_2_dom_2 = np.empty(t)
    data_2_dom_3 = np.empty(t)

    for i in range(t):
        if i <= 1:
            # efficiency at t0
            x = 0
            # resources consumed at t0
            resources_consumed_by_agent_dom_1 = bs
        else:
            # epsilon
            p = np.random.random()
            if p < eps:  # the larger epsilon is the more likely it is to explore new actions
                j = np.random.choice(4)
            else:  # exploit current knowledge
                j = np.argmax([a.mean for a in actions])
            x = actions[j].choose()  # choose action
            actions[j].update(x)  # update expected efficiency of actions

            # Resources consumed by agent in each resource domain:
            # We assume that each increase in efficiency by 1 unit of (x), there's the possibility of
            # substitution effect se (i.e. agents may start consuming resources in another resource domain)
        if x < 1:
                resources_consumed_by_agent_dom_1 = bs + (x * rebound) - (1 - rebound) * x
                resources_consumed_by_agent_dom_1 = np.clip(resources_consumed_by_agent_dom_1, 0, None)
                resources_consumed_by_agent_dom_2 = bs
                resources_consumed_by_agent_dom_2 = np.clip(resources_consumed_by_agent_dom_2, 0, None)
                resources_consumed_by_agent_dom_3 = bs
                resources_consumed_by_agent_dom_3 = np.clip(resources_consumed_by_agent_dom_3, 0, None)

        elif 1 < x <= 2:
                resources_consumed_by_agent_dom_1 = bs + (x * rebound * (1 - se_1)) - (1 - rebound) * x
                resources_consumed_by_agent_dom_1 = np.clip(resources_consumed_by_agent_dom_1, 0, None)
                resources_consumed_by_agent_dom_2 = bs + (x * rebound * (se_1)) - (1 - rebound) * x
                resources_consumed_by_agent_dom_2 = np.clip(resources_consumed_by_agent_dom_2, 0, None)
                resources_consumed_by_agent_dom_3 = bs
                resources_consumed_by_agent_dom_3 = np.clip(resources_consumed_by_agent_dom_3, 0, None)

        elif 2 < x <= 3:
                resources_consumed_by_agent_dom_1 = bs + (x * rebound * (1 - se_1)) - (1 - rebound) * x
                resources_consumed_by_agent_dom_1 = np.clip(resources_consumed_by_agent_dom_1, 0, None)
                resources_consumed_by_agent_dom_2 = bs + (x * rebound * (se_1) * (1 - se_2)) - (1 - rebound) * x
                resources_consumed_by_agent_dom_2 = np.clip(resources_consumed_by_agent_dom_2, 0, None)
                resources_consumed_by_agent_dom_3 = bs + (x * rebound * (se_1) * (se_2))
                resources_consumed_by_agent_dom_3 = np.clip(resources_consumed_by_agent_dom_3, 0, None)

        else:
                resources_consumed_by_agent_dom_1 = bs + (x * rebound * (1 - se_1)) - (1 - rebound) * x
                resources_consumed_by_agent_dom_1 = np.clip(resources_consumed_by_agent_dom_1, 0, None)
                resources_consumed_by_agent_dom_2 = bs + (x * rebound * (se_1) * (1 - se_2)) - (1 - rebound) * x
                resources_consumed_by_agent_dom_2 = np.clip(resources_consumed_by_agent_dom_2, 0, None)
                resources_consumed_by_agent_dom_3 = bs + (x * rebound * (se_1) * (se_2))
                resources_consumed_by_agent_dom_3 = np.clip(resources_consumed_by_agent_dom_3, 0, None)


        # data of given agent
        data[i] = x
        data_2_dom_1[i] = resources_consumed_by_agent_dom_1
        data_2_dom_2[i] = resources_consumed_by_agent_dom_2
        data_2_dom_3[i] = resources_consumed_by_agent_dom_3

    # Efficiency of the agent at each time step
    efficiency = np.cumsum(data) / (np.arange(t) + 1)
    efficiency = np.clip(efficiency, 0, None)
    # Consumption of the agent at each time step
    consumption_dom_1 = np.cumsum(data_2_dom_1) / (np.arange(t) + 1)
    consumption_dom_2 = np.cumsum(data_2_dom_2) / (np.arange(t) + 1)
    consumption_dom_3 = np.cumsum(data_2_dom_3) / (np.arange(t) + 1)
    # Total cumulative consumption of the agent at each time step
    cumulative_consumption_dom_1 = np.cumsum(data_2_dom_1)
    cumulative_consumption_dom_2 = np.cumsum(data_2_dom_2)
    cumulative_consumption_dom_3 = np.cumsum(data_2_dom_3)

    return efficiency, consumption_dom_1, cumulative_consumption_dom_1, consumption_dom_2, \
           cumulative_consumption_dom_2, consumption_dom_3, cumulative_consumption_dom_3

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
def existing_resources(total_consumption_pop, r_t0, rep_rate):
    existing_resources = [r_t0]
    prior = existing_resources[0]
    for n in total_consumption_pop:
        prior = (prior - n) * (1 + rep_rate)
        prior = np.clip(prior, 0, r_t0)
        existing_resources.append(prior)
    existing_resources = [max(min(y, r_t0), 0) for y in existing_resources]
    return existing_resources

# Running scenarios
def scenario(m1, m2, m3, m4, eps, t, N, bs, r_t0, rep_rate, rebound, se_1, se_2):
    a = []  # array containing the vectors containing the efficiency of each agent in the population at each time step
    r_dom_1 = []  # array containing the vectors containing the resource consumption of each agent in the population
    # at each time step in resource domain 1
    rt_dom_1 = []  # array containing the vectors containing the cumulative resource consumption of each agent in the
    # population at each time step in resource domain 1
    r_dom_2 = []  # array containing the vectors containing the resource consumption of each agent in the population
    # at each time step in resource domain 2
    rt_dom_2 = []  # array containing the vectors containing the cumulative resource consumption of each agent in the
    # population at each time step in resource domain 2
    r_dom_3 = []  # array containing the vectors containing the resource consumption of each agent in the population
    # at each time step in resource domain 3
    rt_dom_3 = []  # array containing the vectors containing the cumulative resource consumption of each agent in the
    # population at each time step in resource domain 3

    for agent in range(N):
        agent = agent_type(m1, m2, m3, m4, eps, t, bs, rebound, se_1, se_2)
        a.append(agent[0])
        r_dom_1.append(agent[1])
        rt_dom_1.append(agent[2])
        r_dom_2.append(agent[3])
        rt_dom_2.append(agent[4])
        r_dom_3.append(agent[5])
        rt_dom_3.append(agent[6])
    mean_eff_pop = np.mean(a, 0)  # array containing mean efficiency of the population at each time step
    mean_consumption_pop_dom_1 = np.round(np.mean(r_dom_1, 0), 10)  # array containing mean resource consumption of the
    # population at each time step in resource domain 1
    mean_consumption_pop_dom_2 = np.round(np.mean(r_dom_2, 0), 10)  # array containing mean resource consumption of the
    # population at each time step in resource domain 2
    mean_consumption_pop_dom_3 = np.round(np.mean(r_dom_3, 0), 10)  # array containing mean resource consumption of the
    # population at each time step in resource domain 3
    total_consumption_pop_dom_1 = np.add.reduce(r_dom_1)  # array containing the consumption of the population at each time step
    total_consumption_pop_dom_2 = np.add.reduce(r_dom_2)  # array containing the consumption of the population at
    # each time step
    total_consumption_pop_dom_3 = np.add.reduce(r_dom_3)  # array containing the consumption of the population at
    # each time step

    return mean_eff_pop, existing_resources(total_consumption_pop_dom_1, r_t0, rep_rate), mean_consumption_pop_dom_1,\
           existing_resources(total_consumption_pop_dom_2, r_t0, rep_rate), mean_consumption_pop_dom_2, \
           existing_resources(total_consumption_pop_dom_3, r_t0, rep_rate), mean_consumption_pop_dom_3

# if __name__ == '__main__':
# main()
