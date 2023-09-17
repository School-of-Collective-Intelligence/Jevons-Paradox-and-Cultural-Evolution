import numpy as np
from .agent import agent_type
from .resources import existing_resources

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
    total_consumption_pop_dom_1 = np.add.reduce(
        r_dom_1)  # array containing the consumption of the population at each time step
    total_consumption_pop_dom_2 = np.add.reduce(r_dom_2)  # array containing the consumption of the population at
    # each time step
    total_consumption_pop_dom_3 = np.add.reduce(r_dom_3)  # array containing the consumption of the population at
    # each time step

    return mean_eff_pop, existing_resources(total_consumption_pop_dom_1, r_t0, rep_rate), \
           mean_consumption_pop_dom_1, existing_resources(total_consumption_pop_dom_2, r_t0, rep_rate), \
           mean_consumption_pop_dom_2, existing_resources(total_consumption_pop_dom_3, r_t0, rep_rate), \
           mean_consumption_pop_dom_3
