# Comparison-and-Development-of-an-Algorithm-for-Ring-Topology-Optimization

# Ring Topology Optimization Using Heuristic Algorithms

This repository contains the Python implementation of a heuristic algorithm aimed at optimizing ring topologies in network design, specifically targeting the minimization of cost and computation time for networks modeled after the Travelling Salesman Problem (TSP). Our algorithm offers a promising approach for network design optimization, showing notable efficiency and effectiveness in comparison with traditional methods such as Brute Force and Ant Colony Optimization (ACO).

## Abstract

Ring topology is a cornerstone of network design, especially in optical networks, due to its robustness and efficient data transmission capabilities. Optimizing ring topology involves solving a variant of the TSP, focusing on cost minimization and computational efficiency. Our proposed heuristic algorithm demonstrates a substantial reduction in deviation from Brute Force results and outperforms ACO in terms of computational speed, making it a viable solution for real-time applications in telecommunications networks.

## Key Features

- **Optimization of Ring Topology**: Efficiently connects all nodes in a ring with minimal cost.
- **Comparison with Existing Algorithms**: Benchmarks against Brute Force and ACO.
- **Enhanced Computational Efficiency**: Faster computation times suitable for larger networks.

## Installation

To run the simulation, ensure that you have Python 3.x installed. Clone this repository and install the required packages:

```bash
git clone https://github.com/your-github-username/ring-topology-optimization.git
cd ring-topology-optimization
pip install -r requirements.txt
```

## Usage

To execute the program, run the following command in the terminal:

```bash
python topology_optimizer.py
```

Replace `topology_optimizer.py` with the path to your script if different.

## Simulation Results

The algorithm was tested on networks with up to 15 nodes, and the results have been promising:

- **Cost Efficiency**: Only 7.49% deviation from Brute Force and 2.11% from ACO.
- **Computation Time**: Significant reduction in time compared to existing methods.

Results and comparison graphs are available in the `results` folder.

## Contributing

Contributions are welcome! Please read `CONTRIBUTING.md` for details on our code of conduct, and the process for submitting pull requests to us.

## Authors

- **Kushkumar Hetalbhai Patel** - *Initial work* - [KushkumarHP](https://github.com/KushkumarHP)

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE) file for details.

## Acknowledgments

- Thanks to Carleton University for providing the environment to conduct this research.
- Gratitude to our professor for their invaluable guidance and support.
