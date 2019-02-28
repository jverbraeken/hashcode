import itertools
import os

DIR_EXAMPLES = "examples"


def get_interest_factor(set1, set2):
    return min(len(set1 - set2), len(set2 - set1), len(set1.intersection(set2)))


def recursive(pairwise_if, my_list, is_first_vertical_one, just_had_two_vertical_ones):
    num = len(pairwise_if)
    skipped_elements = set(range(num)) - set(my_list)
    if is_first_vertical_one:
        skipped_elements = list(filter(lambda element: pictures[element][0], skipped_elements))
    if len(skipped_elements) == 0:
        return 0, my_list
    best = 0, None
    for i in skipped_elements:
        new_list = my_list.copy()
        new_list.append(i)
        if is_first_vertical_one:
            new_count = get_interest_factor(pictures[my_list[-2]][1], pictures[my_list[-1]][1].union(pictures[i][1]))
            tmp = recursive(pairwise_if, new_list, False, True)
            best = max(best[0], tmp[0]) + new_count, tmp[1]
        else:
            if just_had_two_vertical_ones:
                tmp = recursive(pairwise_if, new_list, pictures[i][0], False)
                best = max(best[0], tmp[0] + get_interest_factor(pictures[my_list[-2]][1].union(pictures[my_list[-1]][1]),
                                                              pictures[i][1])), tmp[1]
            else:
                if pictures[i][0]:
                    tmp = recursive(pairwise_if, new_list, True, False)
                    best = max(best[0], tmp[0]), tmp[1]
                else:
                    tmp = recursive(pairwise_if, new_list, True, False)
                    best = max(best[0], tmp[0] + pairwise_if[my_list[-1]][i]), tmp[1]
    return best


name = "a_example.txt"
pictures = []
file = open(os.path.join(DIR_EXAMPLES, name), 'r')
lines = file.readlines()
num = int(lines[0])
for i in range(1, num + 1):
    line = lines[i].replace("\n", "")
    terms = line.split(" ")
    orientation = terms[0] == "V"
    numTags = int(terms[1])
    tags = set()
    for j in range(numTags):
        tags.add(terms[2 + j])
    pictures.append((orientation, tags))
num_pictures = len(pictures)
pairwise_if = [[0 for x in range(num_pictures)] for y in range(num_pictures)]
for i in range(2, num_pictures):
    permutations = list(itertools.combinations(range(num_pictures), i))
    print(permutations)
    for j in permutations:
        interest_factor = get_interest_factor(pictures[j[0]][1], pictures[j[1]][1])
        pairwise_if[j[0]][j[1]] = interest_factor
        pairwise_if[j[1]][j[0]] = interest_factor

permutations = list(itertools.combinations(range(num_pictures), 2))
for i in range(len(permutations)):
    permutations.append((permutations[i][1], permutations[i][0]))

best_permutation = None
best = 0
for permutation in permutations:
    if pictures[list(permutation)[0]][0] and not pictures[list(permutation)[1]][0]:
        continue
    if pictures[list(permutation)[1]][0]:
        if pictures[list(permutation)[0]][0]:
            tmp = recursive(pairwise_if, list(permutation), False, True)
            if tmp[0] > best:
                best = tmp[0]
                best_permutation = tmp[1]
        else:
            tmp = recursive(pairwise_if, list(permutation), True, False)
            if tmp[0] + pairwise_if[list(permutation)[0]][list(permutation)[1]] > best:
                best = tmp[0]
                best_permutation = tmp[1]
    else:
        tmp = recursive(pairwise_if, list(permutation), False, False)
        if tmp[0] + pairwise_if[list(permutation)[0]][list(permutation)[1]] > best:
            best = tmp[0]
            best_permutation = tmp[1]
print(best)
print(best_permutation)
with open("1.txt", "w") as file:
    length = 0
    for i in range(len(best_permutation)):
        if pictures[i][0]:
            length += 0.5
        else:
            length += 1
    file.write(str(int(length)) + "\n")
    skip_iteration = False
    for i in range(len(best_permutation)):
        if skip_iteration:
            skip_iteration = False
            continue
        if pictures[best_permutation[i]][0]:
            file.write(str(best_permutation[i]) + " " + str(best_permutation[i+1]) + "\n")
            skip_iteration = True
        else:
            file.write(str(best_permutation[i]) + "\n")
