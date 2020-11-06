from utils import count_classes, partition
from question import Question
from leaf import Leaf
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
            'true_branch': self.true_branch.toJson(),
            'false_branch': self.false_branch.toJson(),
            'rows': self.rows
        }


class Tree:
    def __init__(self, rows, headers, strategy="entropy log2"):
        self.headers = headers
        self.strategy = strategy
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

                if self.strategy == "gini index":
                    info_gain = self.information_gain_gini(current, true, false)
                elif self.strategy == "entropy log2":
                    info_gain = self.information_gain_entropy2(true, false)
                elif self.strategy == "entropy log10":
                    info_gain = self.information_gain_entropy10(true, false)
                elif self.strategy == "entropy logE":
                    info_gain = self.information_gain_entropy10(true, false)

                if info_gain >= best_gain:
                    best_gain = info_gain
                    best_question = question

        return best_gain, best_question

    def information_gain_entropyE(self, left, right):
        p = len(left) / (len(left) + len(right))
        if p == 0:
            return - (1-p) * math.log1p(1-p)
        elif (1-p) == 0:
            return - p * math.log1p(p)
        else:
            return - p * math.log1p(p) - (1-p) * math.log1p(1-p)

    def information_gain_entropy2(self, left, right):
        p = len(left) / (len(left) + len(right))
        if p == 0:
            return - (1-p) * math.log2(1-p)
        elif (1-p) == 0:
            return - p * math.log2(p)
        else:
            return - p * math.log2(p) - (1-p) * math.log2(1-p)

    def information_gain_entropy10(self, left, right):
        p = len(left) / (len(left) + len(right))
        if p == 0:
            return - (1-p) * math.log10(1-p)
        elif (1-p) == 0:
            return - p * math.log10(p)
        else:
            return - p * math.log10(p) - (1-p) * math.log10(1-p)

    def information_gain_gini(self, current, left, right):
        p = len(left) / (len(left) + len(right))
        return current - p * self.gini(left) - (1-p) * self.gini(right)

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
        return self.root.toJson()

    def getQuestion(self):
        if isinstance(self.root, Node):
            return self.root.question.toJson()
        else:
            return self.root.toJson()
