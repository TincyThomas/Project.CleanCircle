from flask import Flask 
import random
  

app = Flask(__name__) 
  
value=round(random.uniform(0, 100))
@app.route('/') 
def hello_world(): 
    return str(value) + " %" 
  
if __name__ == '__main__': 
  
  
    app.run(port = 5003)