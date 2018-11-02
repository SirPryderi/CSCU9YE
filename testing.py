from utils.draw_utils import benchmark_boxplot, benchmark_barchart_error

# Create data
constructive_heuristic = [100, 10, 200]
hill_climbing = [80, 30, 200]
multi_start_hill_climbing = [90, 20, 200]
awesome_algorithm = [70, 25, 200]

# combine these different collections into a list
algorithms_to_plot = [constructive_heuristic, hill_climbing, multi_start_hill_climbing, awesome_algorithm]

benchmark_boxplot(algorithms_to_plot)
