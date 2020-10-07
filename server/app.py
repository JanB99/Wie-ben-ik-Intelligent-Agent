from flask import Flask, jsonify, request
from flask_cors import CORS
import main
import csv

app = Flask(__name__)
app.config["DEBUG"] = True
app.config["TEMPLATES_AUTO_RELOAD"] = True

CORS(app, resources={r'/*': {'origins': '*'}})

with open("dataset.csv", 'r', newline='') as file:
    reader = csv.reader(file)
    dataset = [row for (index, row) in enumerate(reader)]
    headers = dataset[0]
    del dataset[0]


tree = main.Tree(dataset)
ai = tree.root


@app.route('/', methods=['GET'])
def index():
    return jsonify(tree.toJson())

@app.route('/next', methods=['GET', 'POST'])
def ask():

    global ai

    answer = request.args.get('answer')

    if answer == '1':
        ai = ai.true_branch
        return ai.question.__repr__() if isinstance(ai, main.Node) else ai.probabilities
    elif answer == '0':
        ai = ai.false_branch
        return ai.question.__repr__() if isinstance(ai, main.Node) else ai.probabilities
    else:
        return answer


app.run()