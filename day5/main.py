from typing import List

def read_file(path:str) -> List[str]:
    with open(path, "r") as f:
        lines = f.readlines()
        # lines consist of a list of strings, some strings have \n at the end and others are just \n
        
        # remove \n from the end of each string
        lines = [line.strip() for line in lines]
        return lines
    
def one_crane_move(stacks: List[str], procedures: List[str]):
    for procedure in procedures:
        procedure = procedure.split(' ')
        
        num_items_to_move = int(procedure[1])
        stack_to_move_from = int(procedure[3]) - 1
        stack_to_move_to = int(procedure[5]) - 1
        
        for _ in range(num_items_to_move):
            stacks[stack_to_move_to].append(stacks[stack_to_move_from].pop())
            
    top_of_stack = [stack[-1] for stack in stacks]
    return ''.join(top_of_stack)

def crane_move_multiple_crates(stacks: List[str], procedures: List[str]):
    for procedure in procedures:
        procedure = procedure.split(' ')
        
        num_items_to_move = int(procedure[1])
        stack_to_move_from_index = int(procedure[3]) - 1
        stack_to_move_to_index = int(procedure[5]) - 1
        
        temp_arr = [stacks[stack_to_move_from_index].pop() for _ in range(num_items_to_move)]
        temp_arr = reversed(temp_arr)
        
        for _ in range(num_items_to_move):
            stacks[stack_to_move_to_index].append(next(temp_arr))
            
    top_of_stack = [stack[-1] for stack in stacks]
    return ''.join(top_of_stack)
        
        
    
if __name__ == "__main__":
    lines = read_file("advent/day5/input.txt")

    empty_line = lines.index('')
    board = lines[0:empty_line]
    procedures = lines[empty_line+1:]

    num_stacks = int(board[-1].split(' ')[-1])
    stacks = [[] for _ in range(num_stacks)]
    
    items = reversed(board[0:-1])
    
    d = 4
    a = 1
   
    for item in items:
        for index in range(a, 1 + (num_stacks) * d, d): # a+(n-1)d is the last term in sequence. ### could have used range(1,-1,4)
            try:
                value_to_append = item[index]
            except:
                continue
            
            stack_to_append_to = index // 4
            if value_to_append.strip() == '':
                continue
            
            stacks[stack_to_append_to].append(value_to_append)
            
    print(crane_move_multiple_crates(stacks, procedures))
     
     
     
    def test():
        arr = [1,2,3,4]
        arr2 = [2,3,4,5]
        
        temp = arr[-2:]
        print(temp)