# Project: The Jevons Paradox and Cultural Evolution: Investigating the dynamics of
# coupled and decoupled resource use and efficiency gains.
#
# Authors:
# J. Segovia-Martin & J. Winters


from Jevons_10 import scenario
import matplotlib.pyplot as plt
import string
import random

# Parameters
a_effic = [0, 1, 2, 3]  # Efficiency of actions
t = 10000  # time steps
N = 100  # population size
eps = [0, 0.01, 0.05, 0.1, 0.5]  # epsilon refers to the probability of choosing to explore.
bs = 0.1  # Baseline consumption of each agent at each time step assuming efficiency 0 (in units of the resource).
r_t0 = len(''.join(random.choices(string.ascii_uppercase + string.digits, k=10000)))  # initial_resource_pool in units.
rep_rate = 0.0001  # resource units replenished per unit of existing resources at each time step.
rebound = 0.25  # Marginal rebound. Additional number of resource units consumed for every one unit increase in
# efficiency. It takes values from 0 to 1 in steps of 0.1.


c_5 = scenario(a_effic[0], a_effic[1], a_effic[2], a_effic[3], eps[4], t, N, bs, r_t0, rep_rate, rebound)
c_1 = scenario(a_effic[0], a_effic[1], a_effic[2], a_effic[3], eps[3], t, N, bs, r_t0, rep_rate, rebound)
c_05 = scenario(a_effic[0], a_effic[1], a_effic[2], a_effic[3], eps[2], t, N, bs, r_t0, rep_rate, rebound)
c_01 = scenario(a_effic[0], a_effic[1], a_effic[2], a_effic[3], eps[1], t, N, bs, r_t0, rep_rate, rebound)
c_0 = scenario(a_effic[0], a_effic[1], a_effic[2], a_effic[3], eps[0], t, N, bs, r_t0, rep_rate, rebound)

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


# Plot (v): Combined plot of the primary resource domain

fig, axs = plt.subplots(2, 2)
fig.suptitle('Rebound .25')
axs[0, 0].set_ylabel('pop. efficiency')
axs[0, 0].plot(c_5[0], label='eps = 0.5')
axs[0, 0].plot(c_1[0], label='eps = 0.1')
axs[0, 0].plot(c_05[0], label='eps = 0.05')
axs[0, 0].plot(c_01[0], label='eps = 0.01')
axs[0, 0].plot(c_0[0], label='eps = 0')
axs[0, 0].set_title('Efficiency')
axs[0, 1].set_ylabel('existing resources')
axs[0, 1].plot(c_5[1], label='eps = 0.5')
axs[0, 1].plot(c_1[1], label='eps = 0.1')
axs[0, 1].plot(c_05[1], label='eps = 0.05')
axs[0, 1].plot(c_01[1], label='eps = 0.01')
axs[0, 1].plot(c_0[1], label='eps = 0')
axs[0, 1].set_title('Existing resources')

axs[1, 0].set_ylabel('mean consumption (in units)')
axs[1, 0].plot(c_5[2], label='eps = 0.5')
axs[1, 0].plot(c_1[2], label='eps = 0.1')
axs[1, 0].plot(c_05[2], label='eps = 0.05')
axs[1, 0].plot(c_01[2], label='eps = 0.01')
axs[1, 0].plot(c_0[2], label='eps = 0')
axs[1, 0].set_title('Consumption')
axs[1, 1].set_ylabel('Sustainability index')
axs[1, 1].plot(bs/c_5[2], label='eps = 0.5')
axs[1, 1].plot(bs/c_1[2], label='eps = 0.1')
axs[1, 1].plot(bs/c_05[2], label='eps = 0.05')
axs[1, 1].plot(bs/c_01[2], label='eps = 0.01')
axs[1, 1].plot(bs/c_0[2], label='eps = 0')
axs[1, 1].set_title('sustainability index')

for ax in axs.flat:
    ax.set_xscale('log')
    ax.set(xlabel='log(time)')

# Hide x labels and tick labels for top plots and y ticks for right plots.
# for ax in axs.flat:
#     ax.label_outer()

handles, labels = axs[0, 0].get_legend_handles_labels()
#fig.legend(handles, labels,  loc='lower center', ncol=1, bbox_to_anchor=(0.85, 0.25))
plt.show()
fig.set_size_inches(7, 7)
fig.subplots_adjust(bottom=0.1)
fig.tight_layout()
fig.savefig('Jevons_25.pdf', bbox_inches="tight")








# Plot (vi): Combined plot of existing resources over time in 3 consecutive resurce domains

fig, axs = plt.subplots(3, 3)
fig.suptitle('Indirect rebound effects')
axs[0, 0].set_ylabel('existing resources (in units)')
axs[0, 0].plot(c_5[1], label='eps = 0.5')
axs[0, 0].plot(c_1[1], label='eps = 0.1')
axs[0, 0].plot(c_05[1], label='eps = 0.05')
axs[0, 0].plot(c_01[1], label='eps = 0.01')
axs[0, 0].plot(c_0[1], label='eps = 0')
axs[0, 0].set_title('Resource domain 1')
axs[0, 1].plot(c_5[3], label='eps = 0.5')
axs[0, 1].plot(c_1[3], label='eps = 0.1')
axs[0, 1].plot(c_05[3], label='eps = 0.05')
axs[0, 1].plot(c_01[3], label='eps = 0.01')
axs[0, 1].plot(c_0[3], label='eps = 0')
axs[0, 1].set_title('Resource domain 2')
axs[0, 2].plot(c_5[5], label='eps = 0.5')
axs[0, 2].plot(c_1[5], label='eps = 0.1')
axs[0, 2].plot(c_05[5], label='eps = 0.05')
axs[0, 2].plot(c_01[5], label='eps = 0.01')
axs[0, 2].plot(c_0[5], label='eps = 0')
axs[0, 2].set_title('Resource domain 3')

axs[1, 0].set_ylabel('mean consumption (in units)')
axs[1, 0].plot(c_5[2], label='eps = 0.5')
axs[1, 0].plot(c_1[2], label='eps = 0.1')
axs[1, 0].plot(c_05[2], label='eps = 0.05')
axs[1, 0].plot(c_01[2], label='eps = 0.01')
axs[1, 0].plot(c_0[2], label='eps = 0')
axs[1, 0].set_title('Resource domain 1')
axs[1, 1].plot(c_5[4], label='eps = 0.5')
axs[1, 1].plot(c_1[4], label='eps = 0.1')
axs[1, 1].plot(c_05[4], label='eps = 0.05')
axs[1, 1].plot(c_01[4], label='eps = 0.01')
axs[1, 1].plot(c_0[4], label='eps = 0')
axs[1, 1].set_title('Resource domain 2')
axs[1, 2].plot(c_5[6], label='eps = 0.5')
axs[1, 2].plot(c_1[6], label='eps = 0.1')
axs[1, 2].plot(c_05[6], label='eps = 0.05')
axs[1, 2].plot(c_01[6], label='eps = 0.01')
axs[1, 2].plot(c_0[6], label='eps = 0')
axs[1, 2].set_title('Resource domain 3')

axs[2, 0].set_ylabel('sustainability index')
axs[2, 0].plot(bs/c_5[2], label='eps = 0.5')
axs[2, 0].plot(bs/c_1[2], label='eps = 0.1')
axs[2, 0].plot(bs/c_05[2], label='eps = 0.05')
axs[2, 0].plot(bs/c_01[2], label='eps = 0.01')
axs[2, 0].plot(bs/c_0[2], label='eps = 0')
axs[2, 0].set_title('Resource domain 1')
axs[2, 1].plot(bs/c_5[4], label='eps = 0.5')
axs[2, 1].plot(bs/c_1[4], label='eps = 0.1')
axs[2, 1].plot(bs/c_05[4], label='eps = 0.05')
axs[2, 1].plot(bs/c_01[4], label='eps = 0.01')
axs[2, 1].plot(bs/c_0[4], label='eps = 0')
axs[2, 1].set_title('Resource domain 2')
axs[2, 2].plot(bs/c_5[6], label='eps = 0.5')
axs[2, 2].plot(bs/c_1[6], label='eps = 0.1')
axs[2, 2].plot(bs/c_05[6], label='eps = 0.05')
axs[2, 2].plot(bs/c_01[6], label='eps = 0.01')
axs[2, 2].plot(bs/c_0[6], label='eps = 0')
axs[2, 2].set_title('Resource domain 3')


for ax in axs.flat:
    ax.set_xscale('log')
    ax.set(xlabel='log(time)')

# Hide x labels and tick labels for top plots and y ticks for right plots.
# for ax in axs.flat:
#     ax.label_outer()

handles, labels = axs[0, 0].get_legend_handles_labels()
fig.legend(handles, labels,  loc='lower center', ncol=1, bbox_to_anchor=(0.9, 0.15))
plt.show()
fig.set_size_inches(10, 10)
fig.subplots_adjust(bottom=0.1)
fig.tight_layout()
fig.savefig('Jevons_se_10000.pdf', bbox_inches="tight")




#
# fig, (ax1, ax2, ax3) = plt.subplots(3)
# fig.suptitle('Simulation 1')
# ax1.plot(c_5[1], label='eps = 0.5')
# ax1.plot(c_1[1], label='eps = 0.1')
# ax1.plot(c_05[1], label='eps = 0.05')
# ax1.plot(c_01[1], label='eps = 0.01')
# ax1.plot(c_0[1], label='eps = 0')
# ax1.set_xscale('log')
# ax1.set_xlabel('')
# ax1.set_ylabel('existing resources (in units)')
# ax1.set_title("Resource domain 1")
#
# ax2.plot(c_5[3], label='eps = 0.5')
# ax2.plot(c_1[3], label='eps = 0.1')
# ax2.plot(c_05[3], label='eps = 0.05')
# ax2.plot(c_01[3], label='eps = 0.01')
# ax2.plot(c_0[3], label='eps = 0')
# ax2.set_xscale('log')
# ax2.set_xlabel('log(time)')
# ax2.set_ylabel('existing resources (in units)')
# ax2.set_title("Resource domain 2")
#
# ax3.plot(c_5[5], label='eps = 0.5')
# ax3.plot(c_1[5], label='eps = 0.1')
# ax3.plot(c_05[5], label='eps = 0.05')
# ax3.plot(c_01[5], label='eps = 0.01')
# ax3.plot(c_0[5], label='eps = 0')
# ax3.set_xscale('log')
# ax3.set_xlabel('log(time)')
# ax3.set_ylabel('existing resources (in units)')
# ax3.set_title("Resource domain 3")
#
# handles, labels = ax2.get_legend_handles_labels()
# fig.legend(handles, labels,  loc='lower center', ncol=2, bbox_to_anchor=(0.36, 0.1))
# plt.show()
# fig.set_size_inches(10, 10)
# fig.subplots_adjust(bottom=0.1)
# fig.tight_layout()
# fig.savefig('Jevons_1.png', bbox_inches="tight")