"""Differential Evolution (DE/rand/1/bin) Engine
100% Python Standard Library (random).
"""

import random

class DifferentialEvolutionOptimizer:
    """Continuous black-box stochastic optimizer."""
    def __init__(self, pop_size=20, f_mut=0.8, cr=0.7):
        self.pop_size = pop_size
        self.f_mut = f_mut
        self.cr = cr

    def optimize(self, cost_fn, bounds=(-5.0, 5.0), dims=2, max_iter=40):
        lb, ub = bounds
        pop = [[random.uniform(lb, ub) for _ in range(dims)] for _ in range(self.pop_size)]
        costs = [cost_fn(ind) for ind in pop]

        for _ in range(max_iter):
            for i in range(self.pop_size):
                candidates = [idx for idx in range(self.pop_size) if idx != i]
                r1, r2, r3 = random.sample(candidates, 3)

                mutant = []
                for d in range(dims):
                    v = pop[r1][d] + self.f_mut * (pop[r2][d] - pop[r3][d])
                    mutant.append(min(ub, max(lb, v)))

                trial = []
                rand_d = random.randint(0, dims - 1)
                for d in range(dims):
                    if random.random() < self.cr or d == rand_d:
                        trial.append(mutant[d])
                    else:
                        trial.append(pop[i][d])

                trial_cost = cost_fn(trial)
                if trial_cost < costs[i]:
                    pop[i] = trial
                    costs[i] = trial_cost

        best_idx = min(range(self.pop_size), key=lambda i: costs[i])
        return {
            "best_cost": round(costs[best_idx], 6),
            "best_vector": [round(x, 4) for x in pop[best_idx]]
        }
