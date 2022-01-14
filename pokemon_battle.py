from pokedex import Pokedex
from pokemon import Pokemon

def battle(party1, party2):
    round_number = 1 #starting round number as 1

    while len(party1) > 0 and len(party2) > 0: #checks if both parties have sufficient number of pokemons
        print("Round", round_number)
        print("Party 1: ", party1)
        print("Party 2: ", party2)

        pokemon1 = party1.pop() #selecting a pokemon from the party for the battle
        pokemon2 = party2.pop() #selecting a pokemon from the party for the battle

        battle_result = pokemon1.battle_result(pokemon2) #calling the battle_result method which returns who won, lost, or drew

        if battle_result == "Draw": #checks if result is draw
            print(pokemon1, "and", pokemon2, "battle to a DRAW")
            party1.add(pokemon1) #adds the pokemon back to party
            party2.add(pokemon2) #adds the pokemon back to party

        elif battle_result == "Win": #checks if pokemon1 won pokemon2
            print(pokemon1, "has WON the round over", pokemon2)
            party1.add(pokemon1) #adds pokemon1 to the party since it won
            pokemon2.lost_round(pokemon1.get_damage_points()) 
            if pokemon2.is_fainted() == True: #checks if pokemon2 has fainted and does not add back to party if true
                 print(pokemon2, "has fainted") 
            else:
                party2.add(pokemon2) #adds pokemon2 back to party if it did not faint

        else: #checks if pokemon2 won pokemon1
            print(pokemon2, "has WON the round over", pokemon1) 
            party2.add(pokemon2) #adds pokemon2 to the party since it won
            pokemon2.lost_round(pokemon1.get_damage_points())
            if pokemon1.is_fainted() == True: #checks if pokemon1 has fainted
                 print(pokemon1, "has fainted")
            else:
                party1.add(pokemon1) #adds pokemon1 back to party if it did not faint

        round_number += 1 #incrementing round number after battle ends
        input("Enter any key to continue...")

        if len(party1) == 0: #checks if all pokemons have fainted
            print("Winning Party: ", party2)
        elif len(party2) == 0: #checks if all pokemons have fainted
            print("Winning Party: ", party1)

if __name__ == "__main__":
    pokedex = Pokedex()
    pokedex.load("data/pokemon.csv")
    party1, party2 = pokedex.create_particles()
    battle(party1, party2)



        


