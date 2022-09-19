# Project: The Jevons Paradox and Cultural Evolution: Investigating the dynamics of
# coupled and decoupled resource use and efficiency gains.
#
# Authors:
# J. Segovia-Martin & J. Winters


from Jevons_3 import scenario
import matplotlib.pyplot as plt
import string
import random


# Parameters
#a_effic = [0, 1, 2, 3]  # Efficiency of actions
num_actions = 10 #Number of actions
payoff = 1.0 #Increments of payoffs. E.g., payoff=1.0 will take the number of actions and multiply their index by 1.0.
t = 7000  # time steps
N = 10  # population size
eps = [0, 0.01, 0.05, 0.1, 0.5, 1.0]  # epsilon refers to the probability of choosing to explore.
bs = 0.1  # Baseline consumption of each agent at each time step assuming efficiency 0 (in units of the resource).
r_t0 = len(''.join(random.choices(string.ascii_uppercase + string.digits, k=1000)))  # initial_resource_pool in units.
rep_rate = 0.01  # resource units replenished per unit of existing resources at each time step.
rebound = 0.2  # Marginal rebound. Additional number of resource units consumed for every one unit increase in
# efficiency. It takes values from 0 to 1 in steps of 0.1.


c_5 = scenario(num_actions, payoff, eps[4], t, N, bs, r_t0, rep_rate, rebound)
c_1 = scenario(num_actions, payoff, eps[3], t, N, bs, r_t0, rep_rate, rebound)
c_05 = scenario(num_actions, payoff, eps[2], t, N, bs, r_t0, rep_rate, rebound)
c_01 = scenario(num_actions, payoff, eps[1], t, N, bs, r_t0, rep_rate, rebound)
c_0 = scenario(num_actions, payoff, eps[0], t, N, bs, r_t0, rep_rate, rebound)
c_new = scenario(num_actions, payoff, eps[5], t, N, bs, r_t0, rep_rate, rebound)

# Plots

# Plot(i): Mean efficiency of the population at each time step
plt.plot(c_5[0], label='eps = 0.5')
plt.plot(c_1[0], label='eps = 0.1')
plt.plot(c_05[0], label='eps = 0.05')
plt.plot(c_01[0], label='eps = 0.01')
plt.plot(c_0[0], label='eps = 0')
plt.plot(c_new[0], label='eps = 1.0')
plt.legend()
plt.xscale('log')
plt.ylabel('pop. efficiency')
plt.xlabel('log(time)')
plt.show()

# Plot (ii): existing resources at each time step
plt.plot(c_5[1], label='eps = 0.5')
plt.plot(c_1[1], label='eps = 0.1')
plt.plot(c_05[1], label='eps = 0.05')
plt.plot(c_01[1], label='eps = 0.01')
plt.plot(c_0[1], label='eps = 0')
plt.plot(c_new[1], label='eps = 1.0')
plt.legend()
plt.xscale('log')
plt.ylabel('existing resources')
plt.xlabel('log(time)')
plt.show()

# Plot (iii): mean consumption of the population at each time step
plt.plot(c_5[2], label='eps = 0.5')
plt.plot(c_1[2], label='eps = 0.1')
plt.plot(c_05[2], label='eps = 0.05')
plt.plot(c_01[2], label='eps = 0.01')
plt.plot(c_0[2], label='eps = 0')
plt.plot(c_new[2], label='eps = 1.0')
plt.legend()
plt.xscale('log')
plt.ylabel('mean consumption')
plt.xlabel('log(time)')
plt.show()

# Plot (iv): Sustainability index: baseline needs at t0 met per each unit of resources consumed.
# When Sust. indx = 1, it means that for each unit of resources consumed, we maintain the needs of one individual.
# When Sust. indx < 1, it means that more resources are consumed than the population would need to cover their basic needs.
# When Sust. indx > 1, it means that less resources are consumed than the population would need to cover their basic
# needs.
plt.plot(bs/c_5[2], label='eps = 0.5')
plt.plot(bs/c_1[2], label='eps = 0.1')
plt.plot(bs/c_05[2], label='eps = 0.05')
plt.plot(bs/c_01[2], label='eps = 0.01')
plt.plot(bs/c_0[2], label='eps = 0')
plt.plot(bs/c_new[2], label='eps = 1.0')
plt.legend()
plt.xscale('log')
plt.ylabel('sustainability index')
plt.xlabel('log(time)')
plt.show()

