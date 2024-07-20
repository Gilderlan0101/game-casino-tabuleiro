from flask import Flask, render_template, jsonify
from tabuleiro import Game
from logica_button import money, play_game

app = Flask(__name__)

button_state = "AUTO"
saldo = 1000

def toggle_button_logic():
    global button_state
    if button_state == "AUTO":
        button_state = "STOP"
    else:
        button_state = "AUTO"
    return button_state

@app.route('/sem_saldo')
def sem_saldo():
    return render_template( result=[], verific=[])

def play_game():
    new_game = Game()
    new_game.gira_roleta()
    verificacao_result = new_game.verifica()
    slots = [[slot.display for slot in row] for row in new_game.slots]
    verificacao_data = [{"display": item.display, "value": item.value} for item in verificacao_result]
    return slots, verificacao_data

@app.route('/')
def index():
    new_game = Game()
    new_game.gira_roleta()
    verificacao = new_game.verifica()
    saldo = money()

   
    
    return render_template('tabuleiro.html', result=new_game.slots, verific=verificacao, saldo=saldo)

@app.route('/toggle-button', methods=['POST'])
def toggle_button():
    button_state = toggle_button_logic()
    return jsonify(button_state=button_state)

@app.route('/play_game', methods=['POST'])
def play_game_route():
    slots, verificacao_data = play_game()
    
    return jsonify(slots=slots, verificacao=verificacao_data)

@app.route('/play_game_auto', methods=['POST'])
def play_game_auto_route():
    global button_state
    if button_state == "AUTO":
        slots, verificacao_data = play_game()
        return jsonify(slots=slots, verificacao=verificacao_data)
    else:
        return jsonify(slots=[], verificacao=[])
    
if __name__ == '__main__':
    app.run(debug=True)
