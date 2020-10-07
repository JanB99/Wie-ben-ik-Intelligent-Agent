from flask import Flask, jsonify, request, send_file
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

playerCharacter = None
name = ''


@app.route('/', methods=['GET'])
def index():
    return jsonify(tree.toJson())

@app.route('/test', methods=['GET', 'POST'])
def test():
    global name
    if request.args.get('name'):
        name = request.args.get('name')

    return jsonify(name)

@app.route('/getAllCharacters', methods=['GET'])
def characters():
    return jsonify(dataset)

@app.route('/character', methods=['GET', 'POST'])
def setCharacter():
    global playerCharacter

    arg = request.args.get('num')
    if arg and int(arg) < len(dataset) and int(arg) >= 0:
        playerCharacter = dataset[int(arg)]
    
    return jsonify(playerCharacter)

@app.route('/labels', methods=['GET'])
def getLabels():
    return jsonify(headers)

@app.route('/values', methods=['GET', 'POST'])
def getValues():

    if 'label' in request.args:
        return jsonify(list({x[headers.index(request.args.get('label'))] for x in dataset}))

@app.route('/question', methods=['GET', 'POST'])
def postQuestion():
    pass

@app.route('/image', methods=['GET'])
def getImage():
    return send_file('tijger.jpg', mimetype='image/jpg')

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