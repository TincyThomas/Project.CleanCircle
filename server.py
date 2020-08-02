from flask import Flask
import requests as req

list1=[] 
list2=['BIN_01','BIN_02', 'BIN_03', 'BIN_04']
data={}

app = Flask(__name__)
 
@app.route('/')
def hello_world():
    BIN_01=req.get('http://127.0.0.1:5001/')
    BIN_02=req.get('http://127.0.0.1:5004/')
    BIN_03=req.get('http://127.0.0.1:5002/')
    BIN_04=req.get('http://127.0.0.1:5003/')
    list1.append(int(str(BIN_01.text).split('%')[0]))
    list1.append(int(str(BIN_02.text).split('%')[0]))
    list1.append(int(str(BIN_03.text).split('%')[0]))
    list1.append(int(str(BIN_04.text).split('%')[0]))
    for i,j in zip(list1,list2):
        if i>80:
            data[j]="__BIN IS FULL!__"
        else:

            data[j]="__No need to empty.__"
    
    

    return str(data)
 
if __name__ == '__main__':
 
 
    app.run(debug=True)