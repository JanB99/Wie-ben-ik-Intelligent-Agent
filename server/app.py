from flask import Flask, jsonify, request, send_file
from flask_cors import CORS
import main
import csv, random, copy

app = Flask(__name__)
app.config["DEBUG"] = True
app.config["TEMPLATES_AUTO_RELOAD"] = True

CORS(app, resources={r'/*': {'origins': '*'}})

with open("dataset.csv", 'r', newline='') as file:
    reader = csv.reader(file)
    playerDataset = [row for (index, row) in enumerate(reader)]
    dataset = copy.deepcopy(playerDataset)
    headers = dataset[0]
    del dataset[0], playerDataset[0]

tree = None
playerCharacter = None
aiCharacter = None
factor = 0.5


@app.route('/tree', methods=['GET'])
def index():
    return jsonify(tree.toJson())

@app.route('/getAllCharacters', methods=['GET'])
def characters():
    return jsonify(playerDataset)

@app.route('/character', methods=['GET', 'POST'])
def setCharacter():
    global playerCharacter, aiCharacter, tree

    arg = request.args.get('num')
    if arg and int(arg) < len(dataset) and int(arg) >= 0:
        if playerCharacter == None:
            playerCharacter = playerDataset.pop(int(arg))
            aiCharacter = playerDataset[random.randint(0, len(playerDataset)-1)]
            dataset.pop(playerDataset.index(aiCharacter))
        #     # aiCharacter = dataset.pop(random.randint(0, len(dataset)-1))

        #     # aiCharacter = dataset.pop(int(arg))

        # else:
            # playerDataset.append(playerCharacter)
            # playerCharacter = playerDataset.pop(int(arg))
            
            # dataset.append(aiCharacter)
            # aiCharacter = dataset.pop(random.randint(0, len(dataset)-1))

            # aiCharacter = dataset.pop(int(arg))

        # playerCharacter = playerDataset[int(arg)]
        # aiCharacter = dataset[int(arg)]

        print(aiCharacter)
        tree = main.Tree(dataset)
    
    return jsonify(playerCharacter, aiCharacter)

@app.route('/labels', methods=['GET'])
def getLabels():
    return jsonify(headers)

@app.route('/values', methods=['GET', 'POST'])
def getValues():
    label = request.args.get('label')
    if 'label' in request.args:
        return jsonify(list({x[headers.index(label)] for x in playerDataset}))

@app.route('/question', methods=['GET'])
def postQuestion():

    global playerDataset

    label = request.args.get('label')
    value = request.args.get('value')

    true_branch, false_branch = main.partition(playerDataset, main.Question(headers.index(label), value))
    
    if aiCharacter[headers.index(label)] == value:
        playerDataset = true_branch
    else:
        playerDataset = false_branch
    
    return jsonify(playerDataset) 


@app.route('/images', methods=['GET'])
def getImage():
    idChar = request.args.get('id')
    return send_file('images/Asset {}.png'.format(idChar), mimetype='image/png', as_attachment=True, cache_timeout=0)

@app.route('/test', methods=['GET'])
def test():
    return send_file('images/Asset 10.png', mimetype='image/png')

@app.route('/aiquestion', methods=['GET'])
def getAiQuestion():

    global tree
    answer = request.args.get('answer')

    # guess = tree.guess(factor)
    # if guess:

    #     if answer == '0':
    #         tree = main.Tree(tree.root.rows)
    #         guess = tree.guess(factor)
    #         return jsonify(guess)
    #     elif answer == '1':
    #         return 'AI WINT :P'
    # else:
    if answer == '1':
        tree.root = tree.root.true_branch
    elif answer == '0':
        tree.root = tree.root.false_branch

    
    return jsonify(tree.getQuestion())

app.run()