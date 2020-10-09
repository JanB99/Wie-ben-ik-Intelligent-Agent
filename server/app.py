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



# ai = tree.root
tree = None
playerCharacter = None

aiCharacter = None
name = ''


@app.route('/tree', methods=['GET'])
def index():
    return jsonify(tree.toJson())

# @app.route('/test', methods=['GET', 'POST'])
# def test():
#     global name
#     if request.args.get('name'):
#         name = request.args.get('name')

#     return jsonify(name)

@app.route('/getAllCharacters', methods=['GET'])
def characters():
    return jsonify(playerDataset)

@app.route('/character', methods=['GET', 'POST'])
def setCharacter():
    global playerCharacter, aiCharacter, tree

    arg = request.args.get('num')
    if arg and int(arg) < len(dataset) and int(arg) >= 0:
        # if playerCharacter == None:
        #     # playerCharacter = playerDataset.pop(int(arg))
        #     # aiCharacter = dataset.pop(random.randint(0, len(dataset)-1))

        #     # aiCharacter = dataset.pop(int(arg))

        # else:
            # playerDataset.append(playerCharacter)
            # playerCharacter = playerDataset.pop(int(arg))
            
            # dataset.append(aiCharacter)
            # aiCharacter = dataset.pop(random.randint(0, len(dataset)-1))

            # aiCharacter = dataset.pop(int(arg))

        playerCharacter = playerDataset[int(arg)]
        aiCharacter = dataset[int(arg)]

        print(aiCharacter)
        tree = main.Tree(dataset)
    
    return jsonify(playerCharacter)

@app.route('/labels', methods=['GET'])
def getLabels():
    return jsonify(headers)

@app.route('/values', methods=['GET', 'POST'])
def getValues():

    if 'label' in request.args:
        return jsonify(list({x[headers.index(request.args.get('label'))] for x in dataset}))

@app.route('/question', methods=['GET'])
def postQuestion():

    global playerDataset

    label = request.args.get('label')
    value = request.args.get('value')

    true_branch, _ = main.partition(playerDataset, main.Question(headers.index(label), value))
    
    if aiCharacter[headers.index(label)] == value:
        playerDataset = true_branch
    
    return jsonify(playerDataset) 


@app.route('/image', methods=['GET'])
def getImage():
    return send_file('tijger.jpg', mimetype='image/jpg')

# @app.route('/next', methods=['GET', 'POST'])
# def ask():

#     global ai

#     answer = request.args.get('answer')

#     if answer == '1':
#         ai = ai.true_branch
#         return ai.question.__repr__() if isinstance(ai, main.Node) else ai.probabilities
#     elif answer == '0':
#         ai = ai.false_branch
#         return ai.question.__repr__() if isinstance(ai, main.Node) else ai.probabilities
#     else:
#         return answer


app.run()