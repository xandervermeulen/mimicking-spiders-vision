import plotly.graph_objects as go
from plotly.subplots import make_subplots
import plotly.io as pio


def show_animation(y_test, y_pred,x_range, y_range, z_range):
    # Create a 3D scatter plot figure
    fig = make_subplots(rows=1, cols=1, specs=[[{'type': 'scatter3d'}]])

    # Add scatter plot for true values
    fig.add_trace(go.Scatter3d(
        x=y_test[:, 0],
        y=y_test[:, 1],
        z=y_test[:, 2],
        mode='markers',
        marker=dict(
            size=5,
            color='blue',
            opacity=0.5
        ),
        name='True values'
    ))

    # Add scatter plot for predicted values (initially empty)
    fig.add_trace(go.Scatter3d(
        x=[],
        y=[],
        z=[],
        mode='markers',
        marker=dict(
            size=5,
            color='red',
            opacity=0.5
        ),
        name='Predicted values'
    ))

    # Add scatter plot for connecting lines (initially empty)
    fig.add_trace(go.Scatter3d(
        x=[],
        y=[],
        z=[],
        mode='lines',
        line=dict(
            color='red',
            width=2
        ),
        name='Predicted trajectory'
    ))

    # Add scatter plot for true trajectory (initially empty)
    fig.add_trace(go.Scatter3d(
        x=[],
        y=[],
        z=[],
        mode='lines',
        line=dict(
            color='blue',
            width=2
        ),
        name='True trajectory'
    ))
    xaxis_range = x_range
    yaxis_range = y_range
    zaxis_range = z_range
    # Update layout
    fig.update_layout(
        scene=dict(
            xaxis=dict(showbackground=False, showgrid=True, showline=True, linecolor='black', linewidth=2),
            yaxis=dict(showbackground=False, showgrid=True, showline=True, linecolor='black', linewidth=2),
            zaxis=dict(showbackground=False, showgrid=True, showline=True, linecolor='black', linewidth=2),
            xaxis_title='X axis',
            yaxis_title='Y axis',
            zaxis_title='Z axis',
            # set the x-axis from 0 to 20

            xaxis_range=xaxis_range,
            yaxis_range=yaxis_range,
            zaxis_range=zaxis_range,
            # set the y-axis from 0 to 20
            aspectratio=dict(x=1, y=1, z=1),
            aspectmode='manual'
        ),
        title='True vs Predicted Values'
    )

    # Define the number of frames (each frame shows one point)
    num_frames = len(y_test)

    # Define animation frames
    frames = [go.Frame(
        data=[go.Scatter3d(
            x=y_test[:i + 1, 0],
            y=y_test[:i + 1, 1],
            z=y_test[:i + 1, 2],
            mode='markers',
            marker=dict(
                size=5,
                color='blue',
                opacity=0.5
            ),
            name='True values'
        ),
            go.Scatter3d(
                x=y_pred[:i + 1, 0],
                y=y_pred[:i + 1, 1],
                z=y_pred[:i + 1, 2],
                mode='markers',
                marker=dict(
                    size=5,
                    color='red',
                    opacity=0.5
                ),
                name='Predicted values'
            ),
            go.Scatter3d(
                x=y_pred[:i + 1, 0],
                y=y_pred[:i + 1, 1],
                z=y_pred[:i + 1, 2],
                mode='lines',
                line=dict(
                    color='red',
                    width=4
                ),
                name='Predicted trajectory'
            ),
            go.Scatter3d(
                x=y_test[:i + 1, 0],
                y=y_test[:i + 1, 1],
                z=y_test[:i + 1, 2],
                mode='lines',
                line=dict(
                    color='blue',
                    width=10
                ),
                name='True trajectory'
            )],
        name=f'frame_{i}'
    ) for i in range(num_frames)]

    # Add frames to animation
    fig.frames = frames

    # Create the animation
    animation = go.layout.Updatemenu(
        type='buttons',
        showactive=False,
        buttons=[dict(
            label='Play',
            method='animate',
            args=[None, dict(
                frame=dict(duration=40, redraw=True),
                fromcurrent=True,
                mode='immediate'
            )]
        )]
    )

    # Add animation to the layout
    fig.update_layout(updatemenus=[animation])

    # Show the plot
    fig.show()
    return fig


def save_animation(y_test, y_pred, output_location, x_range, y_range, z_range):
    fig = show_animation(y_test, y_pred, x_range, y_range, z_range)
    pio.write_html(fig, output_location)