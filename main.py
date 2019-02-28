import os

DIR_EXAMPLES = "examples"

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
        tags = []
        for j in range(numTags):
            tags.append(terms[2+j])
        pictures.append((orientation, tags))

parse_file()