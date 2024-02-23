from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score


def evaluate_model(y_val, y_pred, set):
    # Calculate the mean squared error
    mse = mean_squared_error(y_val, y_pred)
    # Calculate the mean absolute error
    mae = mean_absolute_error(y_val, y_pred)
    # Calculate the R2 score
    r2 = r2_score(y_val, y_pred)
    print(f'Mean Squared Error on {set} Set: {mse}')
    print(f'Mean Absolute Error on {set} Set: {mae}')
    print(f'R2 Score on {set} set: {r2}')
    return mse, mae, r2
