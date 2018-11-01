import matplotlib.pyplot as plt


## Create data

constructive_heuristic = [100, 10, 200]
hill_climbing = [80, 30, 200]
multi_start_hill_climbing = [90, 20, 200]
awesome_algorithm = [70, 25, 200]

## combine these different collections into a list
algorithms_to_plot = [constructive_heuristic, hill_climbing, multi_start_hill_climbing, awesome_algorithm]

# Create a figure instance
fig = plt.figure(1, figsize=(9, 6))

# Create an axes instance
ax = fig.add_subplot(111)

# Create the boxplot
bp = ax.boxplot(algorithms_to_plot)

# Save the figure
fig.savefig('fig1.png', bbox_inches='tight')
plt.show()
