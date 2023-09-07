from typing import List

def read_file(path:str) -> List[str]:
    with open(path, "r") as f:
        lines = f.readlines()
        # lines consist of a list of strings, some strings have \n at the end and others are just \n
        
        # remove \n from the end of each string
        lines = [line.strip() for line in lines]
        return lines
    
def process_elf(line):
    splits = line.split("-")
    first_section, second_section = int(splits[0]), int(splits[1])
    
    elf_array = []
    for i in range(first_section, second_section+1):
        elf_array.append(i)
        
    return elf_array  

def is_range_a_in_range_b(range_a, range_b):
    # range_a / b = '1-3'
    start_a, end_a = map(lambda x: int(x), range_a.split("-"))
    start_b, end_b = map(lambda x: int(x), range_b.split("-"))
    return start_a >= start_b and end_a <= end_b

def is_range_a_overlapping_range_b(range_a, range_b):
    # range_a / b = '1-3'
    start_a, end_a = map(lambda x: int(x), range_a.split("-"))
    start_b, end_b = map(lambda x: int(x), range_b.split("-"))
    return start_a <= end_b and end_a >= start_b
    
if __name__ == "__main__":
    lines = read_file("advent/day4/input.txt")
    pairs = 0
    
    for line in lines:
        splits = line.split(",")
        first_elf, second_elf = splits[0], splits[1]
        
        # if is_range_a_in_range_b(first_elf, second_elf) or is_range_a_in_range_b(second_elf, first_elf):
        #     pairs += 1
        
        if is_range_a_overlapping_range_b(first_elf, second_elf) or is_range_a_overlapping_range_b(second_elf, first_elf):
            pairs += 1
            
    print("Pairs: ", pairs)