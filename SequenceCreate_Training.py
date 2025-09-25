def create_sequences(df, time_step=TIME_STEP):
    if len(df) < time_step:
        print(f"Not enough data to create sequences. Need at least {time_step} data points.")
        return np.array([]), np.array([])
    X, y = [], []
    for i in range(time_step, len(df)):
        X.append(df['request_count'].iloc[i-time_step:i].values)
        y.append(df['request_count'].iloc[i])
    return np.array(X), np.array(y)


def train_model(X, y):
    model = Sequential()
    model.add(LSTM(units=50, return_sequences=False, input_shape=(X.shape[1], 1)))
    model.add(Dense(units=1))
    model.compile(optimizer='adam', loss='mean_squared_error')
    model.fit(X, y, epochs=50, batch_size=32, verbose=0)
    return model
