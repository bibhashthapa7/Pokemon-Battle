class Pokemon:
    __slots__ = ["__name", "__pokemon_type", "__health_points", "__damage_points"]

    def __init__(self, name, pokemon_type, health_points, damage_points): #constructor
        self.__name = name
        self.__pokemon_type = pokemon_type
        self.__health_points = int(health_points)
        self.__damage_points = int(damage_points)

    def get_damage_points(self):
        return self.__damage_points

    def lost_round(self, damage_points):
        (self.__health_points) -= int(damage_points)

    def is_fainted(self):
        if self.__health_points <= 0:
            return True
        else:
            return False

    def __str__(self):
        return self.__name

    def __repr__(self):
        return (self.__name + ":" + self.__pokemon_type + ":" + str(self.__health_points))

    def __hash__(self):
        return hash(self.__name)

    def battle_result(self, pokemon_opponent):
        if self.__pokemon_type == pokemon_opponent.__pokemon_type and self.__health_points == pokemon_opponent.__health_points:
            return "Draw"
        elif self.__pokemon_type == pokemon_opponent.__pokemon_type and self.__health_points != pokemon_opponent.__health_points:
            if self.__health_points > pokemon_opponent.__health_points:
                return "Win"
            else:
                return "Loss"
        
        if self.__pokemon_type == "Water" and pokemon_opponent.__pokemon_type == "Fire":
            return "Win"
        elif self.__pokemon_type == "Fire" and pokemon_opponent.__pokemon_type == "Grass":
            return "Win"
        elif self.__pokemon_type == "Grass" and pokemon_opponent.__pokemon_type == "Water":
            return "Win"
        else:
            return "Loss"


        