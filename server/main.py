import csv
import math
import random

class Question:
    def __init__(self, col, value):
        self.column = col
        self.value = value

    def match(self, example):
        value = example[self.column]
        if self.is_int():
            return value >= self.value
        else:
            return value == self.value

    def match_value(self, value):
        if self.is_int():
            return float(value) >= self.value
        else:
            return value == self.value

    def is_int(self):
        return isinstance(self.value, int) or isinstance(self.value, float)

    def __repr__(self):
        return "is {} {} {}?".format(headers[self.column], ">=" if self.is_int() else "==", self.value)

    def toJson(self):
        return {
            "question": self.__repr__(),
            "label": headers[self.column],
            "value": self.value
        }


def partition(rows, question):
    true_rows, false_rows = [], []
    for row in rows:
        if question.match(row):
            true_rows.append(row)
        else:
            false_rows.append(row)

    return true_rows, false_rows


def count_classes(rows):
    counts = {}
    for row in rows:
        label = row[headers.index("name")]
        if label not in counts:
            counts[label] = 0
        counts[label] += 1
    return counts


def gini(rows):
    counts = count_classes(rows)
    impurity = 1
    for label in counts:
        prob = counts[label] / float(len(rows))
        impurity -= prob**2
    return impurity


def information_gain(current, left, right):
    # de mate aan chaos/onzekerheid meten. normaal gesproken word deze gemeten met de log ipv de gini
    # gini is ook een methode om disorder te meten

    p = len(left) / (len(left) + len(right))
    # return current - p * gini(left) - (1-p) * gini(right)

    # ff mee stoeien
    if p == 0:
        return - (1-p) * math.log2(1-p)
    elif (1-p) == 0:
        return - p * math.log2(p)
    else:
        return - p * math.log2(p) - (1-p) * math.log2(1-p)


def find_best_question(rows):
    best_question = None
    best_gain = 0
    current = gini(rows)

    num_features = len(rows[0])-2

    for col in range(num_features):

        values = {row[col] for row in rows}

        for value in values:

            question = Question(col, value)

            true, false = partition(rows, question)

            info_gain = information_gain(current, true, false)

            if info_gain > best_gain:
                best_gain = info_gain
                best_question = question

    # print(best_gain, best_question)
    return best_gain, best_question


class Node:
    def __init__(self, question, true_branch, false_branch, prob, rows):
        self.question = question
        self.true_branch = true_branch
        self.false_branch = false_branch
        self.prob = prob
        self.rows = rows

    def print(self, spacing, boolean):
        print(spacing, ">", self.question)
        self.true_branch.print(spacing+"  ", True)
        self.false_branch.print(spacing+"  ", False)
    
    def toJson(self, compact):
        if compact: 
            return {
                'true_branch': self.true_branch.toJson(compact),
                'false_branch': self.false_branch.toJson(compact),
            }
        else: 
            return {
                'prob': self.prob,
                'question': self.question.__repr__(),
                'true_branch': self.true_branch.toJson(compact),
                'false_branch': self.false_branch.toJson(compact),
                'rows': self.rows
            }


class Leaf:
    def __init__(self, rows):
        self.predictions = count_classes(rows)
        total_counts = sum(self.predictions.values())
        self.probabilities = {
            key: value / total_counts for (key, value) in self.predictions.items()}

    def print(self, spacing, boolean):
        print(spacing, str(boolean) + "-->", self.probabilities)
    
    def toJson(self, compact):
        return {
            'type': 'leaf', 
            'prob': self.probabilities
        }


class Tree:
    def __init__(self, rows):
        self.root = self.create_tree(rows)

    def create_tree(self, rows):

        gain, question = find_best_question(rows)
        if gain == 0:
            return Leaf(rows)
        true_rows, false_rows = partition(rows, question)

        true_branch = self.create_tree(true_rows)
        false_branch = self.create_tree(false_rows)
        prob = 1/len(rows)
        return Node(question, true_branch, false_branch, prob, rows)

    def print_tree(self):
        self.root.print("", "")
        print("\n")

    def predict(self, row, node):

        if isinstance(node, Leaf):
            print(node.probabilities)
            return

        if node.question.match(row):
            self.predict(row, node.true_branch)
        else:
            self.predict(row, node.false_branch)

    def toJson(self, compact):
        return self.root.toJson(compact) 
    
    def getQuestion(self):
        if isinstance(self.root, Node):
            return self.root.question.toJson()
        else:
            return self.root.toJson()

    def guess(self, threshold):
        if isinstance(self.root, Node) and self.root.prob >= threshold:
            guess = random.choice(self.root.rows)
            nameIndex = headers.index('name')
            self.root.rows.remove(guess)
            return Question(nameIndex, guess[nameIndex]).toJson()
        else:
            return None


with open("dataset.csv", 'r', newline='') as file:
    reader = csv.reader(file)
    dataset = [row for (index, row) in enumerate(reader)]
    headers = dataset[0][0:-1]
    del dataset[0]

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


# def ask(root):

#     if isinstance(root, Leaf):
#         print("\n", root.probabilities)
#         return

#     print(root.question)

#     answer = bool(int(input("input (True, 1 or False, 0): ")))

#     if answer:
#         ask(root.true_branch)
#     else:
#         ask(root.false_branch)


# ask(tree.root)
