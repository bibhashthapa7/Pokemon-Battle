import csv
from pokemon import Pokemon
import random 

class Pokedex:
    __slots__ = ["__pokemon_list"]

    def __init__(self): #constructor
        self.__pokemon_list = list()

    def load(self, filename = "data/pokemon.csv"):
        with open(filename) as csv_file: #opening the file 
            csv_reader = csv.reader(csv_file) #reading as csv file
            next(csv_reader)
            for record in csv_reader:
                self.__pokemon_list.append(Pokemon(record[0], record[1], record[2], record[3])) #adding the fields to the list

    def create_particles(self):
        party1 = set() #initializing an empty set
        party2 = set() #initializing an empty set

        random.shuffle(self.__pokemon_list) #shuffling the list 

        for i in range(6): #iterating 6 times
            random_index = random.randint(0, len(self.__pokemon_list)) #picking a random index
            party1.add(self.__pokemon_list[random_index]) #adding the pokemon from the list to the set
            self.__pokemon_list.pop(random_index) #removing the index so it does not repeat

            random_index = random.randint(0, len(self.__pokemon_list)) #picking a random index
            party2.add(self.__pokemon_list[random_index]) #adding the pokemon from the list to the set
            self.__pokemon_list.pop(random_index) #removing the index so it does not repeat


        return party1, party2
            


