import random

print("Welcome to the Band Name Generator!\n")
bandName = input("What is the name of the city you grown up?\n")
petName = input("What was the name of your first pet?\n")
plantName = input("Give the name of a plant:\n")
drinkName = input("Give the name of a drink:\n")
planetName = input("Give the name of a planet:\nS'a")

inputs = [bandName, petName, plantName, drinkName, planetName]

selected_inputs = random.sample(inputs, 2)

band_name = " ".join(selected_inputs)

print(f"Your band name is {band_name}")