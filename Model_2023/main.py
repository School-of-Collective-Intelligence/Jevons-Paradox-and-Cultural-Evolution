import argparse
from modules.scenarios import scenario

def main():
    parser = argparse.ArgumentParser(description='Run the scenario.')
    parser.add_argument('--m1', type=float, default=0, help='Mean efficiency for action 1')
    parser.add_argument('--m2', type=float, default=0, help='Mean efficiency for action 2')
    parser.add_argument('--m3', type=float, default=0, help='Mean efficiency for action 3')
    parser.add_argument('--m4', type=float, default=0, help='Mean efficiency for action 4')
    parser.add_argument('--eps', type=float, default=0, help='Epsilon value: probability to explore')
    parser.add_argument('--t', type=int, default=100, help='Number of time steps')
    parser.add_argument('--N', type=int, default=100, help='Number of agents')
    parser.add_argument('--bs', type=float, default=0, help='Baseline resources consumed')
    parser.add_argument('--r_t0', type=float, default=0, help='Initial existing resources')
    parser.add_argument('--rep_rate', type=float, default=0, help='Replenishment rate')
    parser.add_argument('--rebound', type=float, default=0, help='Direct rebound effect')
    parser.add_argument('--se_1', type=float, default=0, help='Indirect rebound effect 1')
    parser.add_argument('--se_2', type=float, default=0, help='Indirect rebound effect 2')

    args = parser.parse_args()

    result = scenario(args.m1, args.m2, args.m3, args.m4, args.eps, args.t, args.N, args.bs,
                      args.r_t0, args.rep_rate, args.rebound, args.se_1, args.se_2)

    # Process the result as needed
    print(result)

if __name__ == '__main__':
    main()
