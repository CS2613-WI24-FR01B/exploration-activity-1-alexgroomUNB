[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-24ddc0f5d75046c5622901739e7c5dd533143b0c8e959d652212380cedb1ea36.svg)](https://classroom.github.com/a/FJiO-WNb)
# EA1

1. What package/library does the sample program demonstrate?
   
   This program uses various functionalities of sklearn to select a golf club based on previous data. The user will input the yardage, wind speed, and wind direction; based on a text file of previous data that includes a club, yardage wind speed, and wind direction of previous shots from this player the program uses sklearn's RandomForestClassifier to select a club for the new shot.

2. How does someone run your program?

   For test purposes, there is a data generation file that will create sample data for the program to learn from. In a real-world use case, all the data would be user input from previous rounds of golf.
   For accurate results at least 200 shots should be in the database. The program is ran through a Python GUI library called tkinter that allows users to enter yardage, wind, and direction into text fields
   then press a button for a club recommendation (as a label).
   
3. What purpose does your program serve?

   This program is intended to act as an AI golf caddy. Many golfers have a difficult time judging yardage and taking into account the wind. With a database of all this golfer's previous shots, this program will in theory make the most accurate choice that the golfer could make.

4. What would be some sample input/output?
   
   Input:
   
      Yardage - 200
   
      Wind Speed (mph) - 3

      Wind Direction - Left
   
   Output:
   
      Club Recommendation: 5 Iron

   ![image](https://github.com/CS2613-WI24-FR01B/exploration-activity-1-alexgroomUNB/assets/151641485/230d2cb5-092a-497b-bef6-d8824c4ce589)
