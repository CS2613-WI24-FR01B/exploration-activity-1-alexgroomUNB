#@author Alex Groom 3401740
#Exploration Activity 1
#This program generates a data set in a text file for the machine learning model to use
import random

raw_string = R'YardageData.txt'
out_file = open(raw_string, "w")

def wind(direction, distance, speed): #add wind speed
    affected = distance*speed*0.01 #1% per one mile an hour of wind speed
    adjusted = 0
    if direction == "With":
        adjusted = distance + affected
    elif direction == "Into":
        adjusted = distance - affected
    elif direction == "With-Right" or direction == "With-Left":
        adjusted = distance + affected/(2**0.5) #45 degree angle so divide by root 2
    elif direction == "Into-Right" or direction == "Into-Left":
        adjusted = distance + affected/(2**0.5)
    else:
        adjusted = distance
    return adjusted

#Each nested list is in format: Club loft, minimum yardage, maximum yardage.
clubs = [[60, 0, 80], [54, 80, 110], [50, 110, 130], [46, 130, 145],
         [42, 145, 160], [38, 160, 175], [34, 175, 190], [30, 190, 205], 
         [27, 205, 220], [21, 220, 245], [15, 245, 270], [10, 270, 600]]

#"With" refers to wind coming from behind and helping the ball go further
wind_directions = ["With", "With-Right", "Right", "Into-Right", "Into", "Into-Left", "Left", "With-Left"]

def generate_yardages(num):
    counter = 0
    data = ""

    while counter < num:
        stock_yards = int(random.randrange(40, 300, 1))
        wind_speed = int(random.randrange(0, 40, 1))
        direction = random.choice(wind_directions)
        yards = int(wind(direction, stock_yards, wind_speed))
        i = 0
        for i in range(len(clubs)):
            if yards in range(clubs[i][1], clubs[i][2]):
                data += str(clubs[i][0]) + " " + str(yards) + " " + str(wind_speed) + " " + str(direction) + "\n"
                break
            i += 1
        counter = counter + 1

    return data
print("How large would you like the data set to be?")
data_size = int(input())

data = generate_yardages(data_size)

out_file.write(data)
print("Data has been sucessfully generated and added to YardageData.txt")

out_file.close()