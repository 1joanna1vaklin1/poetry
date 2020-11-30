#Three line poem creator
#By: Joanna B. Vaklin


import random
import csv
from pathlib import Path

def starters_creation():
    base_path = Path(__file__).parent
    starters = []
    file_path = (base_path / "../poetry/starters.txt").resolve() 
    with open(file_path) as my_file:
        for line in my_file:
            starters.append(line)
    return starters

def actions_creation():
    base_path = Path(__file__).parent
    file_path = (base_path / "../poetry/actions.txt").resolve()
    actions = []
    with open(file_path) as my_file:
        for line in my_file:
            actions.append(line)
    return actions

def endings_creation():
    base_path = Path(__file__).parent
    file_path = (base_path / "../poetry/endings.txt").resolve()
    endings = []
    with open(file_path) as my_file:
        for line in my_file:
            endings.append(line)
    return endings

def poetry():
    starters = starters_creation()
    actions = actions_creation()
    endings = endings_creation()

    start_num = random.randint(0, (len(starters)-2))
    act_num = random.randint(0, (len(actions)-2))
    end_num = random.randint(0, (len(endings)-2))

    poem = str(starters[start_num]) + str(actions[act_num]) + str(endings[end_num])
    print("____________________________")
    print(poem)
    print("____________________________")
    

if __name__ == "__main__":
    poetry()