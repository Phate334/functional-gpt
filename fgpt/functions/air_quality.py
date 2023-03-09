from random import choice


def get_air_quality(location: str = "Kaohsiung", **kwargs):
    """
    - Get air quality information by location default is kaohsiung.
    input> what is the air quality in Taipei?
    [{"intent":"air_quality", "args": {"location": "Taipei"}}]
    ===="""
    return {"location": location, "air_quality": choice(["good", "bad", "normal"])}
