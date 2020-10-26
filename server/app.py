from flask import Flask, jsonify, request, send_file
from flask_cors import CORS
from utils import load_dataset, partition
from tree import Tree
from question import Question
import random

#flask config
app = Flask(__name__)
app.config["DEBUG"] = True
app.config["TEMPLATES_AUTO_RELOAD"] = True
CORS(app, resources={r'/*': {'origins': '*'}})

tree = None
player_character = None
ai_character = None
# factor = 0.5
playerDataset, dataset, headers = load_dataset()

@app.route('/reset', methods=['GET'])
def reset():
    global playerDataset, dataset, headers 
    playerDataset, dataset, headers = load_dataset()
    player_character = None
    ai_character = None
    tree = None
    return 'reset succesful'

@app.route('/tree', methods=['GET'])
def index():
    arg = request.args.get('compact')
    if tree:     
        if arg == '1':
            return jsonify(tree.toJson(True))
        else:
            return jsonify(tree.toJson(False))
    else:
        return "No tree initialized"


@app.route('/getAllCharacters', methods=['GET'])
def get_all_characters():
    return jsonify(playerDataset)

@app.route('/character', methods=['GET'])
def character():
    global player_character, ai_character, tree

    arg = request.args.get('num')
    if arg:
        # if player_character == None:
        index = 0
        for (i, row) in enumerate(playerDataset):
            if row[-1] == arg:
                index = i
        player_character = playerDataset.pop(index)
        ai_character = playerDataset[random.randint(0, len(playerDataset)-1)]
        dataset.pop(playerDataset.index(ai_character))
        tree = Tree(dataset, headers)
        #     # ai_character = dataset.pop(random.randint(0, len(dataset)-1))
        #     # ai_character = dataset.pop(int(arg))
        # else:
            # playerDataset.append(player_character)
            # player_character = playerDataset.pop(int(arg))
            # dataset.append(ai_character)
            # ai_character = dataset.pop(random.randint(0, len(dataset)-1)
            # ai_character = dataset.pop(int(arg))
        # player_character = playerDataset[int(arg)]
        # ai_character = dataset[int(arg)]
    return jsonify(player_character, ai_character)

@app.route('/labels', methods=['GET'])
def get_labels():
    return jsonify(headers)

@app.route('/values', methods=['GET', 'POST'])
def get_values():
    label = request.args.get('label')
    if 'label' in request.args:
        return jsonify(list({x[headers.index(label)] for x in playerDataset}))
    else:
        return "Label not found"

@app.route('/question', methods=['GET'])
def post_question():

    global playerDataset

    label = request.args.get('label')
    value = request.args.get('value')

    true_branch, false_branch = partition(playerDataset, Question(headers.index(label), value, headers))
    
    if ai_character[headers.index(label)] == value:
        playerDataset = true_branch
    else:
        playerDataset = false_branch
    
    return jsonify(playerDataset) 


@app.route('/images', methods=['GET'])
def get_image():
    idChar = request.args.get('id')
    return send_file('images/Asset {}.png'.format(idChar), mimetype='image/png', as_attachment=True, cache_timeout=0)

@app.route('/aiquestion', methods=['GET'])
def get_AI_question():

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