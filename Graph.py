import matplotlib.pyplot as plt

# Data for the problem size, generate time, and sort time
problem_size = [1000, 100000, 1000000]
generate_time = [2.78, 289.60, 2647.32]
sort_time = [0.00, 0.29, 3.15]

# Plotting the data
plt.figure(figsize=(10, 6))
plt.plot(problem_size, generate_time, marker='o', label='Generate Time')
plt.plot(problem_size, sort_time, marker='o', label='Sort Time')

# Adding titles and labels
plt.title('Performance Comparison: Generate vs Sort')
plt.xlabel('Problem Size')
plt.ylabel('Time (s)')
plt.legend()
plt.xscale('log')
plt.yscale('log')

# Display the graph
plt.grid(True, which="both", ls="--")

# Save the graph to a file
plt.savefig('performance_comparison.png')

# Show the graph
plt.show()
