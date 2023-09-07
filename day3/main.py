with open("advent/day3/input.txt", 'r') as f:
    lines = f.readlines()
    # remove \n from the end of each string
    lines = [line.strip() for line in lines]

def get_common_letters_split(lines):
    common_letters = []
    for line in lines:
        length = len(line)
        part1, part2 = line[0:length//2], line[length//2:length]
        
        for letter in part1:
            if letter in part2:
                common_letters.append(letter)
                break
                        
def calc_priority_score(common_letters):
    val = 0
    for letter in common_letters:
        if ord(letter) >= ord('a'):
            val += ord(letter) - 96 # small letters start from 1
        else:
            val += ord(letter) - 38 # capital letters start from 27
    return val


def get_common_letters_group(lines):
    common_letters = []
    for i in range(0, len(lines), 3):
        part1, part2, part3 = lines[i], lines[i+1], lines[i+2]
        for letter in part1:
            if letter in part2 and letter in part3:
                common_letters.append(letter)
                break
    return common_letters

def more_efficient(lines):
    common_letters = []
    while len(lines) > 0:
        part1, part2, part3 = set(lines.pop()), set(lines.pop()), set(lines.pop())
        overlap_char = part1.intersection(part2).intersection(part3).pop()
        common_letters.append(overlap_char)
    return common_letters

if __name__ == "__main__":
    letters = more_efficient(lines)
    score = calc_priority_score(letters)
    print(score)