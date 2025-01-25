from collections import namedtuple

Data_transformed = namedtuple("Data", ["X", "y"])
Data_splitted = namedtuple("Data", ["X_train", "X_test", "y_train", "y_test"])
Grid_result = namedtuple("Grid_result", ["instance", "r2_test", "rmse_test"])
