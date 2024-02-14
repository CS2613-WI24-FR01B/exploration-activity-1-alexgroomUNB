import tkinter as tk
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

def wind_direction_to_degree(direction): 
    str_to_num = {'With': 0, 'With-Right': 45, 'Right': 90, 'Into-Right': 135, 'Into': 180, 'Into-Left': 225, 'Left': 270, 'With-Left': 315}
    return str_to_num.get(direction, 0)

def loft_to_name(loft): 
    num_to_str = {60 : '60 Degree', 54 : '54 Degree', 50 : '50 Degree', 46 : 'Pitching Wedge', 42 : '9 Iron', 38 : '8 Iron', 34 : '7 Iron', 30 : '6 Iron',
                  27 :'5 Iron', 21 : '3 Hybrid', 15 : '3 Wood', 10 : 'Driver'}
    return num_to_str.get(loft, 'Unknown')

clubs = []
yardages = [] 
wind_speeds = []
wind_directions = []

raw_string = R'YardageData.txt'
out_file = open(raw_string, 'r')

#Getting data from text file to train the model
line = out_file.readline()

while line:
    
    parts = line.split()
        
    if len(parts) == 4:
        clubs.append(parts[0])
        yardages.append(int(parts[1]))
        wind_speeds.append(int(parts[2]))
        wind_directions.append(wind_direction_to_degree(parts[3]))

    line = out_file.readline()

data = {'Yardage': yardages,'WindSpeed': wind_speeds,'WindDirection': wind_directions,'Club': clubs}

#Creating the data frame (essentially a data table) for proper input format for the model
data_frame = pd.DataFrame(data)

#These will be features that will be used in the tree to optimize club selection based on previous data
features = data_frame[['Yardage', 'WindSpeed', 'WindDirection']]

#This is the target that we want to predict
target = data_frame['Club']

train_features, test_features, train_target, test_target = train_test_split(features, target, test_size=0.2, random_state=42)

model = RandomForestClassifier(random_state = 42)
model.fit(train_features, train_target)

predict_target = model.predict(test_features)

accuracy = accuracy_score(test_target, predict_target)
print(f"Accuracy: {accuracy}")

def predict_club(yardage, wind, direction):
    new_shot = pd.DataFrame({'Yardage': [yardage], 'WindSpeed': [wind], 'WindDirection': [wind_direction_to_degree(direction)]})
    predicted_club = model.predict(new_shot)
    return predicted_club[0]

def button_clicked():
    
    yardage = yardage_entry.get()
    wind_speed = wind_speed_entry.get()
    wind_direction = wind_direction_entry.get()
    
    recommended_club = predict_club(yardage, wind_speed, wind_direction)
    club_name = loft_to_name(int(recommended_club))
    label_string = "Recommended Club: " + club_name
    result_label.config(text = label_string)

#Main GUI window
main = tk.Tk()
main.title("Golf Club Predictor")

#GUI Labels and Entries
yardage_label = tk.Label(main, text="Yardage:")
yardage_label.pack()
yardage_entry = tk.Entry(main)
yardage_entry.pack()

wind_speed_label = tk.Label(main, text="Wind Speed (mph):")
wind_speed_label.pack()
wind_speed_entry = tk.Entry(main)
wind_speed_entry.pack()

# Create and pack a label and entry widget for Wind Direction
wind_direction_label = tk.Label(main, text="Wind Direction")
wind_direction_label.pack()
wind_direction_entry = tk.Entry(main)
wind_direction_entry.pack()

# Create and pack the predict button
predict_button = tk.Button(main, text="Predict", command=button_clicked)
predict_button.pack()

# Create and pack a label for displaying the prediction result
result_label = tk.Label(main, text="")
result_label.pack()

# Start the GUI event loop
main.mainloop()

