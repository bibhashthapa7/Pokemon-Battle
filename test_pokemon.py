from pokemon import Pokemon

def test_pokemon_str():
    exp = "Venusaur"
    res = Pokemon("Venusaur", "Green", 30, 12)

    assert exp == res.__str__()

def test_pokemon_repr():
    exp = "Venusaur:Green:30"
    res = Pokemon("Venusaur", "Green", 30, 12)

    assert exp == res.__repr__()
# python3 -m pytest test_pokemon.py