from typing import List

def read_file(path:str) -> List[str]:
    with open(path, "r") as f:
        lines = f.readlines()
        # lines consist of a list of strings, some strings have \n at the end and others are just \n
        
        # remove \n from the end of each string
        lines = [line.strip() for line in lines]
        return lines

lines = read_file("day8/input.txt")

# fill whole array first
# loop through array to check visibility of trees
whole_array = []

for line in lines:
    new_arr = []
    for char in line:
        new_arr.append(int(char))
    whole_array.append(new_arr)


def check_if_value_higher_than_list(value:int, list_to_check:List[int]) -> bool:
    for item in list_to_check:
        if value > item:
            return True
    return False

def save_output(path:str, output:str) -> None:
    with open(path, "w") as f:
        f.write(str(output))

visible_trees = 0
first_row, first_col = 0,0
last_col, last_row = len(whole_array[0]) - 1, len(whole_array) - 1

for row_index, row in enumerate(whole_array):
    if row_index == first_row or row_index == last_row:
        continue
    for col_index, col in enumerate(row):
        if col_index == first_col or col_index == last_col:
            continue
        left_of_values = whole_array[row_index][0:col_index]
        right_of_values = whole_array[row_index][col_index + 1:]
        above_values = [whole_array[i][col_index] for i in range(0, row_index)]
        below_values = [whole_array[i][col_index] for i in range(row_index + 1, len(whole_array))]
        
        if col > max(left_of_values) or col > max(right_of_values) or col > max(above_values) or col > max(below_values):
            visible_trees += 1

edge_trees = len(whole_array) * 2 + (len(whole_array[0]) - 2) * 2
print(f"Visible trees: {visible_trees + edge_trees}")



        
# PART 2        
def score_side(array):
    scenic_scores = []
    
    for row_index, row in enumerate(array):
        if row_index == first_row or row_index == last_row:
            continue
        for col_index, col in enumerate(row):
            if col_index == first_col or col_index == last_col:
                continue
            
            left_count, right_count, above_count, below_count = 0,0,0,0
            for i in range(col_index-1, -1, -1): # for left
                left_count += 1
                if array[row_index][i] < col:
                    continue
                break
            for i in range(col_index+1, len(array[0])): # for right
                right_count += 1
                if array[row_index][i] < col:
                    continue
                break
            for i in range(row_index-1, -1, -1): # for above
                above_count += 1
                if array[i][col_index] < col:
                    continue
                break
            for i in range(row_index+1, len(array)): # for below
                below_count += 1
                if array[i][col_index] < col:
                    continue
                break
            score = left_count * right_count * above_count * below_count
            # print(f"Value {col} has score {score}")
            scenic_scores.append(score)
    return scenic_scores


arr = [[1,2,3,4], [4,5,6,7], [7,8,9,10], [11,12,13,14]]
print(max(score_side(whole_array)))