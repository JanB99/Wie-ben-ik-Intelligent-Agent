from flask import Flask, jsonify, request, send_file
from flask_cors import CORS
import main
import csv, random, copy

app = Flask(__name__)
app.config["DEBUG"] = True
app.config["TEMPLATES_AUTO_RELOAD"] = True

CORS(app, resources={r'/*': {'origins': '*'}})

def loadDataset():
    dataset1, dataset2, headers = [], [], []
    with open("dataset.csv", 'r', newline='') as file:
        reader = csv.reader(file)
        dataset1 = [row for (index, row) in enumerate(reader)]
        dataset2 = copy.deepcopy(dataset1)
        headers = dataset2[0]
        del dataset1[0], dataset2[0]
    return dataset1, dataset2, headers

tree = None
playerCharacter = None
aiCharacter = None
factor = 0.5
playerDataset, dataset, headers = loadDataset()

@app.route('/reset', methods=['GET'])
def reset():
    global playerDataset, dataset, headers 
    playerDataset, dataset, headers = loadDataset()
    playerCharacter = None
    aiCharacter = None
    tree = None
    return 'reset succesful'

@app.route('/tree', methods=['GET'])
def index():
    arg = request.args.get('compact')
    if arg == '1':
        return jsonify(tree.toJson(True))
    else:
        return jsonify(tree.toJson(False))


@app.route('/getAllCharacters', methods=['GET'])
def characters():
    return jsonify(playerDataset)

@app.route('/character', methods=['GET', 'POST'])
def setCharacter():
    global playerCharacter, aiCharacter, tree

    arg = request.args.get('num')
    if arg:
        # if playerCharacter == None:
        index = 0
        for (i, row) in enumerate(playerDataset):
            if row[-1] == arg:
                index = i
        playerCharacter = playerDataset.pop(index)
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