from main import get_weather

def test_get_weather():
    assert get_weather(21) == "Está frio"
    assert get_weather(30) == "Está quente"
    