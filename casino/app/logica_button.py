
from tabuleiro import Game

button_state = "AUTO"
gire_pare = 'GIRE'

def toggle_button_logic():
    global button_state
    if button_state == "AUTO":
        button_state = "STOP"
    else:
        button_state = "AUTO"
        
    return button_state

def toggle_gire_logic():
    global gire_pare
    
    gire_pare = "GIRE"
        
    
        
    return gire_pare

def play_game():
    global gire_pare
    if gire_pare == "GIRE":
        new_game = Game()
        new_game.gira_roleta()
        verificacao_result = new_game.verifica()
        return new_game.slots, verificacao_result
    return [], []


def money():
    new_game = Game()  
    saldo = 500

    if new_game.gira_roleta():
        
        saldo - 10
        print(saldo)
            
        return saldo

    if new_game.verifica():
        saldo += 10
    
    else:
        new_game.gira_roleta()
            
        return saldo


           
               
            
    