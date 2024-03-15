import pandas as pd
from sklearn.impute import KNNImputer


def interpolate_dataframe(df):
    new_data = pd.DataFrame()
    # Loop through each pair of 'u' and 'v'
    for col in df.columns:
        data = df[col].copy()
        # get all the rows with NaN values
        data = data.interpolate(method='polynomial', order=2)
        imputer_knn = KNNImputer(n_neighbors=2)
        data = data.values.reshape(-1, 1)
        data = imputer_knn.fit_transform(data)
        data = data.flatten()
        data = pd.DataFrame(data, columns=[col])
        # combine the original data with the interpolated data
        new_data = pd.concat([new_data, data], axis=1)

    return new_data
