def main():
    urls = read_urls_from_csv(CSV_FILE_PATH)
    df = capture_network_activity()

    scaler = MinMaxScaler(feature_range=(0, 1))
    df['request_count'] = scaler.fit_transform(df['request_count'].values.reshape(-1, 1))

    X, y = create_sequences(df)

    if X.shape[0] == 0:
        print("No sequences were created due to insufficient data.")
        return  

    print("X shape:", X.shape)
    print("y shape:", y.shape)

    if X.ndim == 2:
        X = X.reshape(X.shape[0], X.shape[1], 1)
        print("Reshaped X:", X.shape)

    if X.shape[0] > 0 and X.shape[1] == TIME_STEP:
        model = train_model(X, y)
    else:
        print("Skipping model training due to insufficient data.")
        return

    open_websites(model, df, scaler, urls)


if __name__ == "__main__":
    main()
