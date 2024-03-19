import pandas as pd


def prepare_and_scale_test_data(X_test_val, y_test_val, scaler_x_test, amount_of_cams):
    combined_test = pd.concat([X_test_val, y_test_val], axis=1)
    combined_test.dropna(inplace=True)
    X_val = combined_test.iloc[:, :amount_of_cams * 2]
    y_val = combined_test.iloc[:, amount_of_cams * 2:]
    X_scaled_test = scaler_x_test.transform(X_val)
    return X_scaled_test, y_val
