def game(player1,player2):
    winner={"rock":'siccer',"siccer":"paper","paper":"rock"}
    if  player1==player2:
        return "ничья"
    if winner [player1]==player2:
        return "игрок1 победитель"
    else:
        return "игрок2 победитель"
print(game('paper','rock'))

