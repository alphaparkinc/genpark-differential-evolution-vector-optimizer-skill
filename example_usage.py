from client import DifferentialEvolutionOptimizer

def main():
    de = DifferentialEvolutionOptimizer()
    res = de.optimize(lambda p: (p[0] - 1.2)**2 + (p[1] + 2.5)**2, dims=2)
    print("Differential Evolution Verification:")
    print(f"Optimal Cost: {res['best_cost']}")
    print(f"Optimal Vector: {res['best_vector']} (Target: [1.2, -2.5])")

if __name__ == "__main__":
    main()
