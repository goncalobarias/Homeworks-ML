import numpy as np, pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPRegressor
from sklearn.metrics import mean_squared_error

# Just like in the previous exercise
data = pd.read_csv("./data/winequality-red.csv", sep=";")
X, y = data.drop("quality", axis=1), data["quality"]
X_train, X_test, y_train, y_test = train_test_split(X, y,
                                    test_size=0.2, random_state=0)

n_iterations, rmse_scores = [20, 50, 100, 200], []
for n_iter in n_iterations:
    y_preds = []
    for rs in range(1, 11):
        # Train the MLP regressor with a specific number of iterations
        mlp = MLPRegressor(hidden_layer_sizes=(10, 10), activation="relu",
                           max_iter=n_iter, validation_fraction=0.2,
                           random_state=rs)
        mlp.fit(X_train, y_train)

        # Predict the target values on the test set
        y_preds.append(mlp.predict(X_test))

    # Calculate RMSE
    y_pred = np.mean(y_preds, axis=0)
    rmse_scores.append(mean_squared_error(y_test, y_pred, squared=False))

# Print the RMSE for the different numbers of iterations
for i, n_iter in enumerate(n_iterations):
    print(f"RMSE with {n_iter} iterations: {rmse_scores[i]}")
