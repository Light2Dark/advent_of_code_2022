from typing import List

def read_file(path:str) -> List[str]:
    with open(path, "r") as f:
        lines = f.readlines()
        # lines consist of a list of strings, some strings have \n at the end and others are just \n
        
        # remove \n from the end of each string
        lines = [line.strip() for line in lines]
        return lines

lines = read_file("advent/day6/input.txt")


def get_marker_arr(text:str) -> str:
    marker_arr = []
    for index, letter in enumerate(text):
        if len(marker_arr) == 14:
            print(''.join(marker_arr))
            return index
        try:
            matching_index = marker_arr.index(letter) # returns index of first matching letter
            marker_arr = marker_arr[matching_index+1:] # remove all letters before the matching letter
        except:
            pass
        marker_arr.append(letter)
    return index

# print(get_marker_arr(lines[0]))

for i in range(len(lines[0])):
    if len(set(lines[0][i:i+4])) == 4:
        print(i+4)
        break
