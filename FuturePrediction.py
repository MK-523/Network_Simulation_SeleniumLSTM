def predict_future_activity(model, last_visits):
    if last_visits.ndim == 1:
        last_visits = last_visits.reshape(1, TIME_STEP, 1)
    prediction = model.predict(last_visits, verbose=0)
    if prediction.ndim > 1:
        return prediction[0][0]
    else:
        return prediction
