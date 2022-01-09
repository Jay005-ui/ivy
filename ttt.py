from flask import Flask,jsonify,request

app = Flask(__name__)
Position=['','','','','','','','','']

@app.route("/",methods=['POST'])
def game():
    request_data=request.get_json()
    player1_name=request_data['player1']
    player2_name=request_data['player2']
    return jsonify ({'player1':player1_name,'player2':player2_name})


@app.route("/tic",methods=['POST'])
def check_game():
    def win():
        player1='X'
        player2='O'
        if Position[0]==Position[1]==Position[2]==player1 or Position[0]==Position[1]==Position[2]==player2:
            return True
        elif Position[3]==Position[4]==Position[5]==player1 or Position[3]==Position[4]==Position[5]==player2:
            return True
        elif Position[6]==Position[7]==Position[8]==player1 or Position[6]==Position[7]==Position[8]==player2:  
            return True
        elif Position[0]==Position[3]==Position[6]==player1 or Position[0]==Position[3]==Position[6]==player2:
            return True
        elif Position[1]==Position[4]==Position[7]==player1 or Position[1]==Position[4]==Position[7]==player2:
            return True
        elif Position[2]==Position[5]==Position[8]==player1 or Position[2]==Position[5]==Position[8]==player2:
            return True
        elif Position[0]==Position[4]==Position[8]==player1 or Position[0]==Position[4]==Position[8]==player2:
            return True
        elif Position[2]==Position[4]==Position[6]==player1 or Position[2]==Position[4]==Position[6]==player2:
            return True
        else:
            return False

    def insert():
        x=int(input("Enter the Position: "))
        if Position[x]!='':
            print("Already Occupied. Choose some other position")
            insert()
        else:
            return x
    result=""
    for i in range(8):
        x=insert()
        Position[x]='X'
        if win():
            result="P1 wins"
            break
        else:
            x=insert()
            Position[x]='O'
            if win():
                result="P2 wins"
                break
    print(result)
    print("Game done")
    return result

    
    
if __name__=="__main__":
    app.run()

