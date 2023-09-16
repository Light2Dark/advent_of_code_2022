from typing import List

def read_file(path:str) -> List[str]:
    with open(path, "r") as f:
        lines = f.readlines()
        # lines consist of a list of strings, some strings have \n at the end and others are just \n
        
        # remove \n from the end of each string
        lines = [line.strip() for line in lines]
        return lines

lines = read_file("day7/input.txt")


class File():
    def __init__(self, name: str, size: int):
        self.name = name
        self.size = size
        
    def __repr__(self):
        return f"File {self.name} with size {self.size}"
    
    def get_size(self):
        return self.size
    

class Directory():    
    def __init__(self, name: str, parent_directory = None):
        self.name = name
        self.files = []
        self.parent_directory = parent_directory
        self.child_directories = []
        self.min_size = float('inf')
    
    def __repr__(self):
        return f"Directory {self.name}, parent {self.parent_directory}" 
    
    def add_file(self, file_name: str, file_size: int):
        new_file = File(file_name, file_size)
        self.files.append(new_file)
        return new_file
        
    def add_directory(self, directory_name: str):
        new_dir = Directory(directory_name, self)
        # print("new_dir", new_dir)
        self.child_directories.append(new_dir)
        return new_dir
    
    def get_directory(self, directory_name: str):
        for child_directory in self.child_directories:
            if child_directory.name == directory_name:
                return child_directory
        return None
    
    def print_tree(self, level=0):
        print('--' * level + ">" + self.name)
        for file in self.files:
            print(" " * level * 3, end="")
            print("-" + f"{file.name} {file.size}b")
        for child in self.child_directories:
            child.print_tree(level + 1)
    
    def get_size(self):
        file_sizes = [file.get_size() for file in self.files]
        directory_sizes = [child_directory.get_size() for child_directory in self.child_directories]
        
        return sum(file_sizes) + sum(directory_sizes)
    
    def num_directories_with_size(self, size: int) -> int:
        '''return the number of directories of size lower than or equal to size'''
        count = 0
        if self.get_size() <= size:
            count += 1
        for child_directory in self.child_directories:
            count += child_directory.num_directories_with_size(size)
        return count
    
    def sum_directories_with_size(self, size:int) -> int:
        '''return the sum of sizes of directories of size lower than or equal to size'''
        sum = 0
        if self.get_size() <= size:
            sum += self.get_size()
        for child_directory in self.child_directories:
            sum += child_directory.sum_directories_with_size(size)
        return sum

    def find_directory_closest_in_size(self, size: int) -> int:
        '''return the size of the smallest directory closest to size'''
        diff = self.get_size() - size 
        self.min_size = diff if diff > 0 and diff < self.min_size else self.min_size
        
        for child in self.child_directories:
            child.find_directory_closest_in_size(size)
            
    
root_directory = Directory("root")
current_directory = root_directory

lines = ['$ cd /', '$ ls', '233 glh.fcb', '10000 gb.sz', 'dir lap', 'dir lo', '$ cd lap', '$ ls', '100 xz.xpi', 'dir fishcake', 'dir lapdog', '$ cd fishcake', '10000 pls.app', '$ cd ..', '$ cd lapdog', '$ ls', '40000000 loki.zip', '$ cd ..', '$ cd ..', '$ cd lo']
    
for line in lines:
    messages = line.split(" ")
    if messages[0] == '$': # command, $ ls, $ cd x, $ cd .., $ cd /
        command = messages[1]
        if command == 'cd': # make directory
            if messages[2] == "/":
                current_directory = root_directory
            elif messages[2] == "..":
                current_directory = current_directory.parent_directory
            else:
                # print(messages, current_directory)
                current_directory = current_directory.get_directory(messages[2])
        elif command == 'ls':
            pass
    elif messages[0] == 'dir':
        current_directory.add_directory(messages[1])
    else:
        file_size = int(messages[0])
        file_name = messages[1]
        current_directory.add_file(file_name, file_size)

# print(root_directory.print_tree())

size = 100000
# print(f"Num of directories with size <= {size}: {root_directory.num_directories_with_size(size)}")
# print(f"Sum of directories with size <= {size}: {root_directory.sum_directories_with_size(size)}")

file_space_needed = 70000000 - root_directory.get_size()
if  file_space_needed < 30000000:
    file_space_needed = 30000000 - file_space_needed
    print(f"Not enough space, need to delete {file_space_needed} bytes")
    direc = root_directory.find_directory_closest_in_size(file_space_needed)
    print(root_directory.min_size)
    print(f"Deleting {direc} bytes")
else:
    print("Enough space")



def test():
    a = Directory("a")
    a.add_file(File("a1", 4))
    a.add_file(File("a2", 5))
    b = a.add_directory("b")
    b.add_file(File("b1", 3))

    print(a.get_size())
        
    print(b.parent_directory)