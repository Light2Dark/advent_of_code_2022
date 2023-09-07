from typing import List

def read_file(path:str) -> List[str]:
    with open(path, "r") as f:
        lines = f.readlines()
        # lines consist of a list of strings, some strings have \n at the end and others are just \n
        
        # remove \n from the end of each string
        lines = [line.strip() for line in lines]
        return lines
    
def count_max_cals(lines: List[str]):
    max_calories = 0
    current_calorie_count = 0
    for line in lines:
        if line == '':
            if current_calorie_count > max_calories:
                max_calories = current_calorie_count
            current_calorie_count = 0
        else:
            current_calorie_count += int(line)
            
    print("Max calories: " + str(max_calories))
    
def top_three_cals(lines: List[str]):
    # find the top three calorie counts
    calorie_counts = []
    current_calorie_count = 0
    for line in lines:
        if line == '':
            calorie_counts.append(current_calorie_count)
            current_calorie_count = 0
        else:
            current_calorie_count += int(line)
            
    calorie_counts.sort(reverse=True)
    print("Top three calorie counts:", str(calorie_counts[0:3]))


if __name__ == "__main__":
    lines = read_file("advent/day1/input-1.txt")
    # count_max_cals(lines)
    top_three_cals(lines)
    print(71924+69893+68589)
    
        
    