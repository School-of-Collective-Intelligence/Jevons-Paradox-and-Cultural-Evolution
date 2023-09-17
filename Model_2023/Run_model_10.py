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
a_effic = [0, 1, 2, 3]  # a_effic stands for efficiency rewards. We normalise this vector for the plots. WE assume an
# equivalence with the efficiency vector: Efficiency=a_effic/max(efficiency). That's it, we assume efficiencies from 0 to 1.
t = 10000  # time steps
N = 100  # population size
eps = [0, 0.01, 0.05, 0.1, 0.5]  # epsilon refers to the probability of choosing to explore.
bs = 0.1  # Baseline consumption of each agent at each time step assuming efficiency 0 (in units of the resource).
r_t0 = len(''.join(random.choices(string.ascii_uppercase + string.digits, k=10000)))  # initial_resource_pool in units.
rep_rate = 0.01  # resource units replenished per unit of existing resources at each time step.
rebound = 0.75  # Marginal rebound. Additional number of resource units consumed for every one unit increase in
# efficiency. It takes values from 0 to 1 in steps of 0.1.
se_1 = 0.75 # Substitution effect 1: share of resource consumption due to rebound effects in the primary domain (1)
# that are consumed in the subsequent domain (2) as a consequence of the substitution effect
se_2 = 0.75 # Substitution effect 2: share of resource consumption due to rebound effects in the secondary domain (2)
# that are consumed in the subsequent domain (3) as a consequence of the substitution effect


c_5 = scenario(a_effic[0], a_effic[1], a_effic[2], a_effic[3], eps[4], t, N, bs, r_t0, rep_rate, rebound, se_1, se_2)
c_1 = scenario(a_effic[0], a_effic[1], a_effic[2], a_effic[3], eps[3], t, N, bs, r_t0, rep_rate, rebound, se_1, se_2)
c_05 = scenario(a_effic[0], a_effic[1], a_effic[2], a_effic[3], eps[2], t, N, bs, r_t0, rep_rate, rebound, se_1, se_2)
c_01 = scenario(a_effic[0], a_effic[1], a_effic[2], a_effic[3], eps[1], t, N, bs, r_t0, rep_rate, rebound, se_1, se_2)
c_0 = scenario(a_effic[0], a_effic[1], a_effic[2], a_effic[3], eps[0], t, N, bs, r_t0, rep_rate, rebound, se_1, se_2)

# Plots
max_e=max(a_effic)
# Plot(i): Mean efficiency of the population at each time step
plt.plot(c_5[0]/max_e, label='eps = 0.5')
plt.plot(c_1[0]/max_e, label='eps = 0.1')
plt.plot(c_05[0]/max_e, label='eps = 0.05')
plt.plot(c_01[0]/max_e, label='eps = 0.01')
plt.plot(c_0[0]/max_e, label='eps = 0')
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
plt.plot((bs/c_5[2]) + rep_rate, label='eps = 0.5')
plt.plot((bs/c_1[2]) + rep_rate, label='eps = 0.1')
plt.plot((bs/c_05[2]) + rep_rate, label='eps = 0.05')
plt.plot((bs/c_01[2]) + rep_rate, label='eps = 0.01')
plt.plot((bs/c_0[2]) + rep_rate, label='eps = 0')
plt.legend()
plt.xscale('log')
plt.ylabel('sustainability index')
plt.xlabel('log(time)')
plt.show()


# Plot (v): Combined plot of the primary resource domain

fig, axs = plt.subplots(2, 2)
fig.suptitle('Rebound 0.75')
axs[0, 0].set_ylabel('pop. efficiency')
axs[0, 0].plot(c_5[0]/max_e, label='ε = 0.5')
axs[0, 0].plot(c_1[0]/max_e, label='ε = 0.1')
axs[0, 0].plot(c_05[0]/max_e, label='ε = 0.05')
axs[0, 0].plot(c_01[0]/max_e, label='ε = 0.01')
axs[0, 0].plot(c_0[0]/max_e, label='ε = 0')
axs[0, 0].set_title('Efficiency')
axs[0, 1].set_ylabel('existing resources (a.u.)')
axs[0, 1].plot(c_5[1], label='ε = 0.5')
axs[0, 1].plot(c_1[1], label='ε = 0.1')
axs[0, 1].plot(c_05[1], label='ε = 0.05')
axs[0, 1].plot(c_01[1], label='ε = 0.01')
axs[0, 1].plot(c_0[1], label='ε = 0')
#Annotation for rebound = 0.25
arrow_text_resources = "Efficiency gains offset\nthe rebound effect"
arrow_properties_resources = dict(facecolor='black', arrowstyle='->')
axs[0, 1].annotate(arrow_text_resources, xy=(0.5, 0.5), xytext=(0.5, 0.7),
                   xycoords='axes fraction', textcoords='axes fraction',
                   arrowprops=arrow_properties_resources, ha='center', va='center')
# Annotation for rebound = 0.75
# arrow_text_resources = "Higher efficiency\nleads to faster\n depletion"
# arrow_properties_resources = dict(facecolor='black', arrowstyle='->')
# axs[0, 1].annotate(arrow_text_resources, xy=(0.5, 0.5), xytext=(0.5, 0.7),
#                    xycoords='axes fraction', textcoords='axes fraction',
#                    arrowprops=arrow_properties_resources, ha='right', va='center')
# Annotation for rebound = 1
# arrow_text_top_right = "Negative resource\nsavings for all\npossible strategies"
# arrow_properties_top_right = dict(facecolor='black', arrowstyle='->')
# axs[0, 1].annotate(arrow_text_top_right, xy=(0.55, 0.5), xytext=(0.5, 0.85),
#                    xycoords='axes fraction', textcoords='axes fraction',
#                    arrowprops=arrow_properties_top_right, ha='left', va='center')
axs[0, 1].set_title('Existing resources (PE)')
axs[1, 0].set_ylabel('mean consumption (a.u.)')
axs[1, 0].plot(c_5[2], label='ε = 0.5')
axs[1, 0].plot(c_1[2], label='ε = 0.1')
axs[1, 0].plot(c_05[2], label='ε = 0.05')
axs[1, 0].plot(c_01[2], label='ε = 0.01')
axs[1, 0].plot(c_0[2], label='ε = 0')
#Annotation for rebound = 0.5
# arrow_text_resources = "Resource savings are equal\nto the expected savings"
# arrow_properties_resources = dict(facecolor='black', arrowstyle='->')
# axs[1, 0].annotate(arrow_text_resources, xy=(0.5, 0.5), xytext=(0.5, 0.7),
#                    xycoords='axes fraction', textcoords='axes fraction',
#                    arrowprops=arrow_properties_resources, ha='center', va='center')
# Annotation for rebound = 0.75
# arrow_text = "Optimal efficiency\nstrategies lead to\nmore consumption"
# arrow_properties = dict(facecolor='black', arrowstyle='->')
# axs[1, 0].annotate(arrow_text, xy=(0.95, 0.95), xytext=(0.02, 0.95),
#                    xycoords='axes fraction', textcoords='axes fraction',
#                    arrowprops=arrow_properties, ha='left', va='top')
axs[1, 0].set_title('Consumption')
axs[1, 1].set_ylabel('sustainability index')
axs[1, 1].plot((bs/c_5[2]) + rep_rate, label='ε = 0.5')
axs[1, 1].plot((bs/c_1[2]) + rep_rate, label='ε = 0.1')
axs[1, 1].plot((bs/c_05[2]) + rep_rate, label='ε = 0.05')
axs[1, 1].plot((bs/c_01[2]) + rep_rate, label='ε = 0.01')
axs[1, 1].plot((bs/c_0[2]) + rep_rate, label='ε = 0')
axs[1, 1].set_title('Sustainability index')

for ax in axs.flat:
    ax.set_xscale('log')
    ax.set(xlabel='log(time)')

# Hide x labels and tick labels for top plots and y ticks for right plots.
# for ax in axs.flat:
#     ax.label_outer()

handles, labels = axs[0, 0].get_legend_handles_labels()
fig.legend(handles, labels,  loc='lower center', ncol=1, bbox_to_anchor=(0.85, 0.25))
plt.show()
fig.set_size_inches(7, 7)
fig.subplots_adjust(bottom=0.1)
fig.tight_layout()
fig.savefig('Jevons_xx.pdf', bbox_inches="tight")



# Plot (vi): Combined plot of existing resources over time in 3 consecutive resurce domains

fig, axs = plt.subplots(3, 3)
fig.suptitle('Indirect rebound effects')
axs[0, 0].set_ylabel('existing resources (a.u.)')
axs[0, 0].plot(c_5[1], label='ε = 0.5')
axs[0, 0].plot(c_1[1], label='ε = 0.1')
axs[0, 0].plot(c_05[1], label='ε = 0.05')
axs[0, 0].plot(c_01[1], label='ε = 0.01')
axs[0, 0].plot(c_0[1], label='ε = 0')
axs[0, 0].set_title('Resource domain 1')
axs[0, 1].plot(c_5[3], label='ε = 0.5')
axs[0, 1].plot(c_1[3], label='ε = 0.1')
axs[0, 1].plot(c_05[3], label='ε = 0.05')
axs[0, 1].plot(c_01[3], label='ε = 0.01')
axs[0, 1].plot(c_0[3], label='ε = 0')
axs[0, 1].set_title('Resource domain 2')
axs[0, 2].plot(c_5[5], label='ε = 0.5')
axs[0, 2].plot(c_1[5], label='ε = 0.1')
axs[0, 2].plot(c_05[5], label='ε = 0.05')
axs[0, 2].plot(c_01[5], label='ε = 0.01')
axs[0, 2].plot(c_0[5], label='ε = 0')
axs[0, 2].set_title('Resource domain 3')

axs[1, 0].set_ylabel('mean consumption (a.u.)')
axs[1, 0].plot(c_5[2], label='ε = 0.5')
axs[1, 0].plot(c_1[2], label='ε = 0.1')
axs[1, 0].plot(c_05[2], label='ε = 0.05')
axs[1, 0].plot(c_01[2], label='ε = 0.01')
axs[1, 0].plot(c_0[2], label='ε = 0')
axs[1, 0].set_title('Resource domain 1')
axs[1, 1].plot(c_5[4], label='ε = 0.5')
axs[1, 1].plot(c_1[4], label='ε = 0.1')
axs[1, 1].plot(c_05[4], label='ε = 0.05')
axs[1, 1].plot(c_01[4], label='ε = 0.01')
axs[1, 1].plot(c_0[4], label='ε = 0')
axs[1, 1].set_title('Resource domain 2')
axs[1, 2].plot(c_5[6], label='ε = 0.5')
axs[1, 2].plot(c_1[6], label='ε = 0.1')
axs[1, 2].plot(c_05[6], label='ε = 0.05')
axs[1, 2].plot(c_01[6], label='ε = 0.01')
axs[1, 2].plot(c_0[6], label='ε = 0')
axs[1, 2].set_title('Resource domain 3')

axs[2, 0].set_ylabel('sustainability index')
axs[2, 0].plot((bs/c_5[2]) + rep_rate, label='ε = 0.5')
axs[2, 0].plot((bs/c_1[2])+ rep_rate, label='ε = 0.1')
axs[2, 0].plot((bs/c_05[2]) + rep_rate, label='ε = 0.05')
axs[2, 0].plot((bs/c_01[2]) + rep_rate, label='ε = 0.01')
axs[2, 0].plot((bs/c_0[2]) + rep_rate, label='ε = 0')
axs[2, 0].set_title('Resource domain 1')
axs[2, 1].plot((bs/c_5[4]) + rep_rate, label='ε = 0.5')
axs[2, 1].plot((bs/c_1[4]) + rep_rate, label='ε = 0.1')
axs[2, 1].plot((bs/c_05[4]) + rep_rate, label='ε = 0.05')
axs[2, 1].plot((bs/c_01[4]) + rep_rate, label='ε = 0.01')
axs[2, 1].plot((bs/c_0[4]) + rep_rate, label='ε = 0')
axs[2, 1].set_title('Resource domain 2')
axs[2, 2].plot((bs/c_5[6]) + rep_rate, label='ε = 0.5')
axs[2, 2].plot((bs/c_1[6]) + rep_rate, label='ε = 0.1')
axs[2, 2].plot((bs/c_05[6]) + rep_rate, label='ε = 0.05')
axs[2, 2].plot((bs/c_01[6]) + rep_rate, label='ε = 0.01')
axs[2, 2].plot((bs/c_0[6]) + rep_rate, label='ε = 0')
axs[2, 2].set_title('Resource domain 3')


for ax in axs.flat:
    ax.set_xscale('log')
    ax.set(xlabel='log(time)')

handles, labels = axs[0, 0].get_legend_handles_labels()
fig.legend(handles, labels,  loc='lower center', ncol=1, bbox_to_anchor=(0.9, 0.15))
plt.show()
fig.set_size_inches(10, 10)
fig.subplots_adjust(bottom=0.1)
fig.tight_layout()
fig.savefig('Jevons_indirct_10.pdf', bbox_inches="tight")




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