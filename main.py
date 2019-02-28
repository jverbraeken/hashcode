import os

DIR_EXAMPLES = "examples"


def get_interest_factor(set1, set2):
    return min(set1 - set2, set2 - set1, set1.intersection(set2))


def parse_file():
    name = "a_example.txt"

    pictures = []

    file = open(os.path.join(DIR_EXAMPLES, name), 'r')
    lines = file.readlines()
    num = int(lines[0])
    for i in range(1, num):
        line = lines[i].replace("\n", "")
        terms = line.split(" ")
        orientation = terms[0]
        numTags = int(terms[1])
        tags = set()
        for j in range(numTags):
            tags.add(terms[2 + j])
        pictures.append((orientation, tags))


parse_file()
