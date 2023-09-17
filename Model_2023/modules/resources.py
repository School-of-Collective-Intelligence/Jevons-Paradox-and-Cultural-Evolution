import numpy as np

def existing_resources(total_consumption_pop, r_t0, rep_rate):
    existing_resources = [r_t0]
    prior = existing_resources[0]
    for n in total_consumption_pop:
        prior = (prior - n) * (1 + rep_rate)
        prior = np.clip(prior, 0, r_t0)
        existing_resources.append(prior)
    existing_resources = [max(min(y, r_t0), 0) for y in existing_resources]
    return existing_resources

