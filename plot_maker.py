from matplotlib import pyplot as plt


def create_plot_of_trajectory(mean_x, mean_y, lim):
    # Plot the trajectory
    plt.scatter(mean_x, mean_y, marker='o', linestyle='-', color='red')
    plt.xlabel('X Coordinate')
    plt.ylabel('Y Coordinate')
    plt.title('Trajectory of Detected Red Ball')

    # Invert the y-axis if needed
    plt.xlim(0, lim)
    plt.ylim(0, lim)
    plt.grid(True)
    plt.show()


def create_plot_of_one_frame(x_coordinates, y_coordinates, lim):
    return []