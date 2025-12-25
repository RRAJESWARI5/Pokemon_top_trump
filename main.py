import requests
import random
from tabulate import tabulate

def pick_pokemon():
    masterlist=list(range(1,151))
    poke_id=random.choice(masterlist)
    url = 'https://pokeapi.co/api/v2/pokemon/{}'.format(poke_id)
    response=requests.get(url)
    poke = response.json()
    p_dict = {
        "name": poke["name"],
        "height": poke["height"],
        "weight": poke["weight"]
        }
    return p_dict

print("The Game is on...")

def comp_stat():
    global player
    player1 = pick_pokemon()
    player2 = pick_pokemon()

    print( "Both the players have been successfully assigned Pokemons randomly" )
    if turn=="Player1":
        print( "Player1 poke is {} with height {} and weight {}".format( player1["name"], player1["height"],
                                                                        player1["weight"] ) )
    else:
        print( "Player2 poke is {} with height {} and weight {}".format( player2["name"], player2["height"],
                                                                     player2["weight"] ) )

    p1stat = input("{}, which stat do you want to compare: height or weight ?".format( turn ) )
    while p1stat not in player1:
       p1stat=input("{}, Please type height, weight as valid stats".format(turn))

    if p1stat in player1:
        A="Player1"
        B="Player2"
        if player1[p1stat]>player2[p1stat]:
            print("{} wins this round".format(A))
            player="A"

        elif player1[p1stat] < player2[p1stat]:
            print( "{} wins this round".format( B ))
            player = "B"

        elif player1[p1stat]==player2[p1stat]:
            print( "This round was a draw. Please play again to score" )
            comp_stat()

        if turn=="Player1":
            print("Player2 poke was {} with height {} and weight {}".format( player2["name"], player2["height"],
                                                                     player2["weight"] ) )
        else:
            print("Player1 poke was {} with height {} and weight {}".format( player1["name"], player1["height"],
                                                                      player1["weight"] ) )
        return player


pointsA=0
pointsB=0
rounds=1
maxrounds=20

while rounds<=maxrounds+1:

    if rounds == 1:
        turn="Player1"
        print( "Round{}, {}'s turn".format( rounds, turn ) )

    points= comp_stat()
    if points=="A":
        pointsA=pointsA+1
    elif points=="B":
        pointsB=pointsB+1
    print("points Player1={}".format(pointsA))
    print( "points Player2={}".format(pointsB))
    rounds=rounds+1
#    print(rounds)

    if turn == "Player1":
        turn = "Player2"
        print( "Round{}, {}'s turn".format( rounds, turn ) )
    elif turn== "Player2":
        turn = "Player1"
        print("Round{}, {}'s turn".format(rounds,turn))
#       print(rounds)

    if rounds == maxrounds - 9:
        Contd = input( "10 rounds are complete.Do you wish to continue the game?. Please type yes or no=" )
        if Contd == "yes":
            maxrounds = maxrounds + 10
            continue
        elif Contd == "no":
            print( "Thank you for playing \n" )
            break

score={"Rounds":rounds,"Player1":pointsA,"Player2":pointsB}

Winner=max(score["Player1"],score["Player2"])

for name, points in score.items():
    if points == Winner:
        win=name

        print("The winner of the Game is {} \n"
              "The Final Scores are:".format(win))

score1=[score]
rows = []
headers=("Rounds","Player1\n points","Player2 \n points")
for x in score1:
    rows.append(x.values())
table = tabulate(rows,headers,tablefmt="grid" )
print(table)