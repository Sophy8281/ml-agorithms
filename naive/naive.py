"""
# SOPHIA WANJIKU NJOROGE
# MACHINE_LEARNING_ALGORITHMS
# NAIVE_BAYESIAN_ALGORITHM
"""


import csv

Play_Tennis_Yes = 0
Play_Tennis_No = 0
Sunny_Yes = 0
Sunny_No = 0
Rain_Yes = 0
Rain_No = 0
Overcast_Yes = 0
Overcast_No = 0
Hot_Yes = 0
Hot_No = 0
Cool_Yes = 0
Cool_No = 0
Mild_Yes = 0
Mild_No = 0
High_Yes = 0
High_No = 0
Normal_Yes = 0
Normal_No = 0
Strong_Yes = 0
Strong_No = 0
Weak_No = 0
Weak_Yes = 0
count = 0
with open('naive.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)
    if csv.Sniffer().has_header:
        next(csv_reader)
    for line in csv_reader:
        print(line)
        count += 1
        print(count)
        # Calculating the probability of Yes and No
        if line[5] == 'Yes':
            Play_Tennis_Yes += 1
            if line[1] == 'Sunny':
                Sunny_Yes += 1
            if line[1] == 'Overcast':
                Overcast_Yes += 1
            if line[1] == 'Rain':
                Rain_Yes += 1
            if line[2] == 'Hot':
                Hot_Yes += 1
            if line[2] == 'Mild':
                Mild_Yes += 1
            if line[2] == 'Cool':
                Cool_Yes += 1
            if line[3] == 'High':
                High_Yes += 1
            if line[3] == 'Normal':
                Normal_Yes += 1
            if line[4] == 'Strong':
                Strong_Yes += 1
            if line[4] == 'Weak':
                Weak_Yes += 1
        elif line[5] == 'No':
            Play_Tennis_No += 1
            if line[1] == 'Sunny':
                Sunny_No += 1
            if line[1] == 'Overcast':
                Overcast_No += 1
            if line[1] == 'Rain':
                Rain_No += 1
            if line[2] == 'Hot':
                Hot_No += 1
            if line[2] == 'Mild':
                Mild_No += 1
            if line[2] == 'Cool':
                Cool_No += 1
            if line[3] == 'High':
                High_No += 1
            if line[3] == 'Normal':
                Normal_No += 1
            if line[4] == 'Strong':
                Strong_No += 1
            if line[4] == 'Weak':
                Weak_No += 1
        else:
            print("Error")
print("***************NAIVE BAYESIAN ALGORITHM*******************")
print(f"The probability of Yes is {Play_Tennis_Yes}/{count}\n")
print(f"The probability of No is {Play_Tennis_No}/{count}\n")

print("Enter Your Recorded Weather\n")
print("Select Outlook: 1.Sunny 2.Overcast 3.Rain")
Input_Outlook = input()
print("Select Temperature: 1.Hot 2.Cool 3.Mild")
Input_Temperature = input()
print("Select Humidity: 1.High 2.Normal")
Input_Humidity = input()
print("Select Wind: 1.Strong 2.Weak")
Input_Wind = input()

# Calculating Probability using MAP
MAP_Yes = ((Sunny_Yes / Play_Tennis_Yes) * (Cool_Yes / Play_Tennis_Yes) * (High_Yes / Play_Tennis_Yes) * (
            Strong_Yes / Play_Tennis_Yes)) * (Play_Tennis_Yes / count)
MAP_No = ((Sunny_No / Play_Tennis_No) * (Cool_No / Play_Tennis_No) * (High_No / Play_Tennis_No) * (
            Strong_No / Play_Tennis_No)) * (Play_Tennis_No / count)
print("This is the MAP Probability of Playing:", [MAP_Yes])
print("This is the MAP Probability of Not_Playing", [MAP_No])

# Calculating Probability using ML
ML_Yes = ((Sunny_Yes / Play_Tennis_Yes) * (Cool_Yes / Play_Tennis_Yes) * (High_Yes / Play_Tennis_Yes) * (
            Strong_Yes / Play_Tennis_Yes))
ML_No = ((Sunny_No / Play_Tennis_No) * (Cool_No / Play_Tennis_No) * (High_No / Play_Tennis_No) * (
            Strong_No / Play_Tennis_No))
print("\nThis is the ML Probability of Playing:", [ML_Yes])
print("This is the ML Probability of Not_Playing", [ML_No])
