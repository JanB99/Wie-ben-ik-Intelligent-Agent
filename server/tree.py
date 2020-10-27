from utils import count_classes, partition
from question import Question
import math
import random


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

    def toJson(self):

        return {
            'prob': self.prob,
            'question': self.question.__repr__(),
            'true_branch': self.true_branch.toJson(compact),
            'false_branch': self.false_branch.toJson(compact),
            'rows': self.rows
        }


class Leaf:
    def __init__(self, rows, headers):
        self.predictions = rows

    def print(self, spacing, boolean):
        print(spacing, str(boolean) + "-->", self.predictions)

    def toJson(self):
        return {
            'type': 'leaf',
            'prob': self.predictions
        }


class Tree:
    def __init__(self, rows, headers):
        self.headers = headers
        self.root = self.create_tree(rows)

    def create_tree(self, rows):

        gain, question = self.find_best_question(rows)
        if gain == 0:
            return Leaf(rows, self.headers)
        true_rows, false_rows = partition(rows, question)

        true_branch = self.create_tree(true_rows)
        false_branch = self.create_tree(false_rows)
        prob = 1/len(rows)
        return Node(question, true_branch, false_branch, prob, rows)

    def find_best_question(self, rows):
        best_question = None
        best_gain = 0
        current = self.gini(rows)

        num_features = len(rows[0])-1

        for col in range(num_features):

            values = {row[col] for row in rows}

            for value in values:

                question = Question(col, value, self.headers)

                true, false = partition(rows, question)

                # info_gain = self.information_gain_gini(current, true, false)
                info_gain = self.information_gain_entropy(true, false)

                if info_gain > best_gain:
                    best_gain = info_gain
                    best_question = question

        return best_gain, best_question

    def information_gain_entropy(self, left, right):
        p = len(left) / (len(left) + len(right))
        if p == 0:
            return - (1-p) * math.log2(1-p)
        elif (1-p) == 0:
            return - p * math.log2(p)
        else:
            return - p * math.log2(p) - (1-p) * math.log2(1-p)

    def information_gain_gini(self, current, left, right):
        p = len(left) / (len(left) + len(right))
        return current - p * gini(left) - (1-p) * gini(right)

    def gini(self, rows):
        counts = count_classes(rows, self.headers)
        impurity = 1
        for label in counts:
            prob = counts[label][1] / float(len(rows))
            impurity -= prob**2
        return impurity

    def print_tree(self):
        self.root.print("", "")
        print("\n")

    def toJson(self):
        return self.root.toJson(compact)

    def getQuestion(self):
        if isinstance(self.root, Node):
            return self.root.question.toJson()
        else:
            return self.root.toJson()

    # def guess(self, threshold):
    #     if isinstance(self.root, Node) and self.root.prob >= threshold:
    #         guess = random.choice(self.root.rows)
    #         nameIndex = headers.index('name')
    #         self.root.rows.remove(guess)
    #         return Question(nameIndex, guess[nameIndex]).toJson()
    #     else:
    #         return None
