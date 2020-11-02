import csv
import copy
import random
from leaf import Leaf


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
            charId = row[headers.index("id")]
            counts[label] = [charId, 0]
        counts[label][1] += 1
    return counts


def partition(rows, question):
    true_rows, false_rows = [], []
    for row in rows:
        if question.match(row):
            true_rows.append(row)
        else:
            false_rows.append(row)
    return true_rows, false_rows


def simulate_games(n, Tree, strategy_ai1, strategy_ai2):

    results = {
        "AI 1": {
            "total wins": 0,
            "strategy": strategy_ai1
        },
        "AI 2": {
            "total wins": 0,
            "strategy": strategy_ai2
        },
        "average turns": 0,
        "num Games": n
    }

    for i in range(n):
        ai1_dataset, ai2_dataset, headers = load_dataset()

        rand_index1 = random.randint(0, len(ai1_dataset)-1)
        ai1 = ai1_dataset.pop(rand_index1)
        rand_index2 = random.randint(0, len(ai1_dataset)-1)
        ai2 = ai1_dataset[rand_index2]
        del ai2_dataset[rand_index2]

        ai1_tree = Tree(ai1_dataset, headers, strategy=strategy_ai1)
        ai2_tree = Tree(ai2_dataset, headers, strategy=strategy_ai2)

        character, turns, winner = sim(ai1_tree.root, ai1, ai2_tree.root, ai2, random.randint(0, 1))
        results[winner]["total wins"] += 1
        results["average turns"] += turns
    
    results["average turns"] /= n
    results["AI 1"]["ratio"] = results["AI 1"]["total wins"] / n
    results["AI 2"]["ratio"] = results["AI 2"]["total wins"] / n
    return results


def sim(ai1_root, ai1, ai2_root, ai2, turn):

    if turn % 2 == 0:
        if isinstance(ai1_root, Leaf):
            return ai1_root.predictions, turn, "AI 1"

        if (ai1_root.question.match(ai2)):
            result = sim(ai1_root.true_branch, ai1, ai2_root, ai2, turn + 1)
        else:
            result = sim(ai1_root.false_branch, ai1, ai2_root, ai2, turn + 1)
    else:
        if isinstance(ai2_root, Leaf):
            return ai2_root.predictions, turn, "AI 2"

        if (ai2_root.question.match(ai1)):
            result = sim(ai1_root, ai1, ai2_root.true_branch, ai2, turn + 1)
        else:
            result = sim(ai1_root, ai1, ai2_root.false_branch, ai2, turn + 1)

    return result

def ask(root):

    if isinstance(root, Leaf):
        print("\n", root.predictions)
        return

    print(root.question)

    answer = bool(int(input("input (True, 1 or False, 0): ")))

    if answer:
        ask(root.true_branch)
    else:
        ask(root.false_branch)
