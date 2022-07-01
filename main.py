import csv
import random
from turtle import back

#Importar raças
race_list = []
with open('C:\\Users\\tarik\\Documents\\VS Code Python\\D&D Character Creator\\Race.csv') as race_file:
    data = csv.reader(race_file)
    for character in data:
        race_list.append(character[0])

#Importar classes e subclasses
class_dict = {}
with open('C:\\Users\\tarik\\Documents\\VS Code Python\\D&D Character Creator\\Classes e Subclasses.csv') as class_file:
    data = csv.reader(class_file)
    for character in data:
        temp_list = []
        counter = 1
        for counter in range(1,len(character),1):
            temp_list.append(character[counter])
        temp_key = {character[0]:temp_list}
        class_dict.update(temp_key)
class_list = list(class_dict)

# #Importar backgrounds
background_list = []
with open('C:\\Users\\tarik\\Documents\\VS Code Python\\D&D Character Creator\\Backgrounds.csv') as background_file:
    data = csv.DictReader(background_file,delimiter=';')
    for character in data:
        background_list.append(character)

#Randomizar raça
slot = random.randint(0,len(race_list))-1
final_race = race_list[slot]

#Randomizar classe
slot = random.randint(0,len(class_list))-1
final_class = class_list[slot]

#Randomizar subclasse
subclass_list = class_dict.get(final_class)
slot = random.randint(0,len(subclass_list))-1
final_subclass = subclass_list[slot]

#Randomizar Background, Personality, Ideal, Bond, Flaw e Extra
slot = random.randint(0,len(background_list))-1
background_dict = background_list[slot]
final_background=background_dict.get('Background')
# Personality
temp_list = background_dict.get('Personality')
temp_list = temp_list.split('|')
personality = temp_list[random.randint(0,len(temp_list))-1]
# Ideal
temp_list = background_dict.get('Ideal')
temp_list = temp_list.split('|')
ideal = temp_list[random.randint(0,len(temp_list))-1]
# Flaw
temp_list = background_dict.get('Flaw')
temp_list = temp_list.split('|')
flaw = temp_list[random.randint(0,len(temp_list))-1]
# Extra
temp_list = background_dict.get('Extra')
temp_list = temp_list.split('|')
extra = temp_list[random.randint(0,len(temp_list))-1]
# Description
description = background_dict.get('Description')

#Texto 
print('Welcome to the D&D Character Creator!')
print('Race:',final_race)
print('Class:',final_class)
print('Subclass:',final_subclass)
print('Background:',final_background)
print('Personality:',personality)
print('Ideals:',ideal)
print('Flaws:',flaw)
print('Description:',description,extra)

wait = input("Press Enter to exit.")