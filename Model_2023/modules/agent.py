import numpy as np
from .actions import Actions

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
