import csv, copy

def load_dataset():
    dataset1, dataset2, headers = [], [], []
    with open("dataset.csv", 'r', newline='') as file:
        reader = csv.reader(file)
        dataset1 = [row for (index, row) in enumerate(reader)]
        dataset2 = copy.deepcopy(dataset1)
        headers = dataset2[0]
        del dataset1[0], dataset2[0]
    return dataset1, dataset2, headers

def count_classes(rows, headers):
    counts = {}
    for row in rows:
        label = row[headers.index("name")]
        if label not in counts:
            counts[label] = 0
        counts[label] += 1
    return counts

def partition(rows, question):
    true_rows, false_rows = [], []
    for row in rows:
        if question.match(row):
            true_rows.append(row)
        else:
            false_rows.append(row)
    return true_rows, false_rows

# with open("dataset.csv", 'r', newline='') as file:
#     reader = csv.reader(file)
#     dataset = [row for (index, row) in enumerate(reader)]
#     headers = dataset[0][0:-1]
#     del dataset[0]

# headers = ["haircolor", "job", "gender", "age", "label"]
#
# dataset = [
#     ["black", "musician", "male", 50, "Micheal Jackson"],
#     ["grey", "scientist", "male", 76, "Albert Einstein"],
#     ["n/a", "comedian", "male", 53, "Joe Rogan"],
#     ["blonde", "musician", "female", 43, "Shakira"],
#     ["blonde", "musician", "female", 50, "Gwen Stefani"],
#     ["black", "coder", "male", 21, "Jan Baljan"],
#     ["black", "fighter", "male", 35, "Nate Diaz"],
#     ["black", "fighter", "male", 35, "Jorge Masvidal"],
#     ["grey", "comedian", "male", 60, "Joey Diaz"],
#     ["black", "scientist", "male", 36, "Lex Fridman"],
#     ["black", "musician", "female", 39, "Beyonce"],
#     ["brown", "musician", "female", 18, "Billie Eilish"],
#     ["blonde", "bodybuilder", "male", 23, "Stan Deckers"],
# ]
#
# headers = ["color", "diameter", "label"]
#
# dataset = [
#     ['Green', 3, 'Apple'],
#     ['Yellow', 3, 'Apple'],
#     ['Red', 1, 'Grape'],
#     ['Yellow', 3, 'Lemon'],
# ]

# tree = Tree(dataset)

# tree.print_tree()

# tree.predict(test[0], tree.root)


def ask(root):

    if isinstance(root, Leaf):
        print("\n", root.probabilities)
        return

    print(root.question)

    answer = bool(int(input("input (True, 1 or False, 0): ")))

    if answer:
        ask(root.true_branch)
    else:
        ask(root.false_branch)

# ask(tree.root)
