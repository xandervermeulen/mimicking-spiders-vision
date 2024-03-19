from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score

from utils.plot_maker_gaussian_process import plot_maker_3d


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


# %%
def predict_evaluate_plot(X_test_val_scaled, y_test_val, nn_model, scaler_y_test,
                          title='Trajectory of Ball in 3D Space'):
    y_test_predicted_scaled = nn_model.predict(X_test_val_scaled)
    y_test_pred = scaler_y_test.inverse_transform(y_test_predicted_scaled)
    mse, mae, r2 = evaluate_model(y_test_val, y_test_pred, 'Test Data')
    # change col 1 and 2 from place, so it corresponds to the unity 3d space
    y_test_pred = y_test_pred[:, [0, 2, 1]]
    y_test_val = y_test_val.to_numpy()[:, [0, 2, 1]]
    plot_maker_3d(y_test_val, y_test_pred, title)
    return y_test_pred, mse, mae, r2
