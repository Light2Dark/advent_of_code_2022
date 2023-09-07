from typing import List

def read_file(path:str) -> List[str]:
    with open(path, "r") as f:
        lines = f.readlines()
        # lines consist of a list of strings, some strings have \n at the end and others are just \n
        
        # remove \n from the end of each string
        lines = [line.strip() for line in lines]
        return lines

lines = read_file("advent/day7/input.txt")


class File():
    def __init__(self, name: str, size: int):
        self.name = name
        self.size = size
        
    def __repr__(self):
        return f"File {self.name} with size {self.size}"
    
    def get_size(self):
        return self.size
    

class Directory():    
    def __init__(self, name: str):
        self.name = name
        self.files = []
        self.directories = []
    
    def __repr__(self):
        return f"Directory {self.name}" 
    
    def add_file(self, file: File):
        self.files.append(file)
        
    def add_directory(self, directory):
        self.directories.append(directory)
    
    def get_size(self):
        file_sizes = [file.get_size() for file in self.files]
        directory_sizes = [directory.get_size() for directory in self.directories]
        
        return sum(file_sizes) + sum(directory_sizes)


class FileSystem():
    
    
for line in lines:
    messages = line.split(" ")
    if messages[0] == '$': # command, $ ls, $ cd x, $ cd ..
        if messages[1] == 'cd': # make directory
            
            new_dir = Directory(messages[2])
    