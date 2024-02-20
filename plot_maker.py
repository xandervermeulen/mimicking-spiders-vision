from matplotlib import pyplot as plt


def gaussian_process_plot(actual_values, predicted_values, uncertainties, confidence_interval=1.96, xlim=None,
                          ylim=None):
    # Create subplots
    num_points = len(actual_values)
    figsize = (num_points/10, 5)
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
