import matplotlib.pyplot as plt

from random_walk import RandomWalk 


# Keep making new walks, as long as the program is active.
while True:
	# Make a random walk
	rw = RandomWalk()
	rw.fill_walk()

	# Plot the points
	point_numbers = list(range(rw.num_points))
	plt.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Blues,
		edgecolors='none', s=15)

	#Empasize the first and last points
	plt.scatter(0, 0, c='green', edgecolors='none', s=100)
	plt.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='none', s=100)

	plt.show()

	keep_running = input("Make another walk? (y/n): ")
	if keep_running == 'n':
		break