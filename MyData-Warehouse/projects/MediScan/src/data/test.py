from load_data import load_all_data
from data_preprocessing import X_data_processing , y_data_processing
from encoding import y_scaler
from train_test_split import train_test_split_data
all = load_all_data()
df = all["main"]
x , cols = X_data_processing(df)
y = y_data_processing(df)
y_scaled = y_scaler(df["Disease"])
x_train , x_test , y_train , y_test = train_test_split_data(x, y_scaled , 0.8)
print(x_test , y_test)