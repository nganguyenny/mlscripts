from mltools.clean_text import clean_text

def test_clean_text():
    assert clean_text("Functions evaluating a Regressor and a Classifier. Functions implementing your favorite ARIMA") == "functions evaluating regressor classifier functions implementing favorite arima"
