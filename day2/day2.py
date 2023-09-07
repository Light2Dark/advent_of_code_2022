from typing import List

def read_file(path:str) -> List[str]:
    with open(path, "r") as f:
        lines = f.readlines()
        # lines consist of a list of strings, some strings have \n at the end and others are just \n
        
        # remove \n from the end of each string
        lines = [line.strip() for line in lines]
        return lines
    
def simple_calc(lines):
    score = 0
    for line in lines:
        arr = line.split(' ')
        opponent, me = arr[0], arr[1]
        
        if me == 'X':
            score += 1
            if opponent == 'A':
                score += 3 # draw
            elif opponent == 'C':
                score += 6 # win
        elif me == "Y":
            score += 2
            if opponent == 'A':
                score += 6
            elif opponent == 'B':
                score += 3
        elif me == "Z":
            score += 3
            if opponent == 'B':
                score += 6
            elif opponent == 'C':
                score += 3
    return score

def complex_calc(lines: List[str]):  
    mapping = {
        'A': 'rock',
        'B': 'paper',
        'C': 'scissors',
        'X': 'lose',
        'Y': 'draw',
        'Z': 'win'
    }
    
    score_mapping = {
        'lose': 0,
        'draw': 3,
        'win': 6,
        'rock': 1,
        'paper': 2,
        'scissors': 3
    }
    score = 0
    for line in lines:
        arr = line.split(' ')
        opponent, me = arr[0], arr[1]
        opponent, me = mapping[opponent], mapping[me]
        
        if opponent == 'rock':
            if me == 'lose':
                score += score_mapping['scissors'] + score_mapping['lose']
            elif me == 'win':
                score += score_mapping['paper'] + score_mapping['win']
            elif me == 'draw':
                score += score_mapping['rock'] + score_mapping['draw']
        elif opponent == 'paper':
            if me == 'lose':
                score += score_mapping['rock'] + score_mapping['lose']
            elif me == 'win':
                score += score_mapping['scissors'] + score_mapping['win']
            elif me == 'draw':
                score += score_mapping['paper'] + score_mapping['draw']
        elif opponent == 'scissors':
            if me == 'lose':
                score += score_mapping['paper'] + score_mapping['lose']
            elif me == 'win':
                score += score_mapping['rock'] + score_mapping['win']
            elif me == 'draw':
                score += score_mapping['scissors'] + score_mapping['draw']
                
    return score
        
    
if __name__ == "__main__":
    lines = read_file("advent/day2/input-2.txt")
    print(complex_calc(lines))