# Project: The Jevons Paradox and Cultural Evolution: Investigating the dynamics of
# coupled and decoupled resource use and efficiency gains.
#
# Authors:
# J. Segovia-Martin & J. Winters

from Jevons_7 import scenario
import matplotlib.pyplot as plt
import string
import random
import argparse

# Parameters
parser = argparse.ArgumentParser(description='Jevons paradox model')
parser.add_argument('-r', '--rebound', type=float, help='Marginal rebound. Additional number of resource units consumed for every one unit increase inefficiency. It takes values from 0 to 1 in steps of 0.1.')
args = parser.parse_args()

a_effic = [0, 1, 2, 3]  # Efficiency of actions
t = 1000  # time steps
N = 10  # population size
eps = [0, 0.01, 0.05, 0.1, 0.5]  # epsilon refers to the probability of choosing to explore.
bs = 0.1  # Baseline consumption of each agent at each time step assuming efficiency 0 (in units of the resource).
r_t0 = len(''.join(random.choices(string.ascii_uppercase + string.digits, k=1000)))  # initial_resource_pool in units.
rep_rate = 0.01  # resource units replenished per unit of existing resources at each time step.


c_5 = scenario(a_effic[0], a_effic[1], a_effic[2], a_effic[3], eps[4], t, N, bs, r_t0,
               rep_rate,
               args.rebound)
c_1 = scenario(a_effic[0], a_effic[1], a_effic[2], a_effic[3], eps[3], t, N, bs, r_t0, rep_rate, args.rebound)
c_05 = scenario(a_effic[0], a_effic[1], a_effic[2], a_effic[3], eps[2], t, N, bs, r_t0, rep_rate, args.rebound)
c_01 = scenario(a_effic[0], a_effic[1], a_effic[2], a_effic[3], eps[1], t, N, bs, r_t0, rep_rate, args.rebound)
c_0 = scenario(a_effic[0], a_effic[1], a_effic[2], a_effic[3], eps[0], t, N, bs, r_t0, rep_rate, args.rebound)

# Plots

# Plot(i): Mean efficiency of the population at each time step
plt.plot(c_5[0], label='eps = 0.5')
plt.plot(c_1[0], label='eps = 0.1')
plt.plot(c_05[0], label='eps = 0.05')
plt.plot(c_01[0], label='eps = 0.01')
plt.plot(c_0[0], label='eps = 0')
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
plt.legend()
plt.xscale('log')
plt.ylabel('sustainability index')
plt.xlabel('log(time)')
plt.show()

