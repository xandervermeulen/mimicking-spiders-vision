from matplotlib import pyplot as plt


def gaussian_process_plot(actual_values, predicted_values, uncertainties, confidence_interval=1.96, xlim=None,
                          ylim=None):
    # Create subplots
    num_points = len(actual_values)
    figsize = (15, 5)
    _, axs = plt.subplots(1, figsize=figsize)
    # Plot the covariance as a shaded area over the entire graph
    x_vals = range(num_points)
    axs.fill_between(x_vals, predicted_values - confidence_interval * uncertainties,
                     predicted_values + confidence_interval * uncertainties, color='red', alpha=0.2,
                     label=f'Covariance ({(confidence_interval - 1) * 100}%)')
    # Scatter plot for actual and predicted values
    axs.plot(x_vals, actual_values, color='blue', label='Actual', alpha=0.7)
    axs.plot(x_vals, predicted_values, color='green', label='Predicted', alpha=0.7)

    # Set axis limits
    if xlim:
        axs.set_xlim(xlim)
    if ylim:
        axs.set_ylim(ylim)

    axs.set_xlabel('x')
    axs.set_ylabel('y')
    axs.set_xlim(0, num_points)
    axs.set_title('Gaussian Process Regression')
    axs.legend()

    plt.show()


def plot_maker_3d(y_test, y_pred, title, amount_to_show=10):
    fig = plt.figure()
    ax = plt.axes(projection='3d')
    # Scatter plot for true values
    ax.scatter3D(y_test[:amount_to_show, 0], y_test[:amount_to_show, 1],
                 y_test[:amount_to_show, 2], color='blue', label='True values')

    # Connect the points with lines according to time
    ax.plot(y_test[:amount_to_show, 0], y_test[:amount_to_show, 1],
            y_test[:amount_to_show, 2], color='blue', linestyle='-', linewidth=1)

    ax.scatter3D(y_pred[:amount_to_show, 0], y_pred[:amount_to_show, 1],
                 y_pred[:amount_to_show, 2], color='red', label='Predicted values')

    # Connect the points with lines according to time
    ax.plot(y_pred[:amount_to_show, 0], y_pred[:amount_to_show, 1],
            y_pred[:amount_to_show, 2], color='red', linestyle='-', linewidth=1)
    ax.set_xlim(0)
    ax.set_ylim(0)
    ax.set_zlim(0)
    # Customize labels and legend
    ax.set_xlabel('X axis')
    ax.set_ylabel('Y axis')
    ax.set_zlabel('Z axis')
    ax.set_title(title)
    ax.legend()

    # Show the plot
    plt.show()
