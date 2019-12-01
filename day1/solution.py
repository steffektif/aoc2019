import os

def calculate_fuel(mass): 
    return int(mass / 3) - 2

script_dir = os.path.dirname(os.path.abspath(__file__)) #<-- absolute dir the script is in
rel_path = "input.txt"
abs_file_path = os.path.join(script_dir, rel_path)

file = open(abs_file_path, 'r')

list = []

for x in file: 
    fuel = calculate_fuel(int(x)) #initial fuel needed for module
    list.append(fuel)
    while fuel > 0:
        fuel = calculate_fuel(fuel)
        if(fuel > 0):
            list.append(fuel)

solution = sum(list)
print(solution)