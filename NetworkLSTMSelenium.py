def open_websites(model, df, scaler, urls):
    last_visits = df['request_count'].iloc[-TIME_STEP:].values

    if last_visits.shape[0] != TIME_STEP:
        print("Not enough data points for prediction")
        return

    prediction = predict_future_activity(model, last_visits)
    print(f"Prediction: {prediction}")
    predicted_count = int(round(prediction))

    sorted_urls = sorted(urls, key=lambda x: prediction, reverse=True)

    for i in range(predicted_count):
        if i < len(sorted_urls):
            print(f"Opening: {sorted_urls[i]}")
            driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
            driver.get(sorted_urls[i])
            time.sleep(2)
            driver.quit()
