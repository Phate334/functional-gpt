from random import choice


def get_weather(location: str = "Kaohsiung"):
    """
    - Get weather information by location default is kaohsiung.
    input> what is the weather in Taipei?
    [{"intent":"weather", "args": {"location": "Taipei"}]
    ===="""
    return {"location": location, "weather": choice(["sunny", "rainy", "cloudy"])}
