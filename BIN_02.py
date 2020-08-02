from flask import Flask 
import random
import math
  

app = Flask(__name__) 
  
value=math.ceil(random.uniform(0, 100))
@app.route('/') 
def hello_world(): 
    return str(value) + " %" 
  
if __name__ == '__main__': 
  
  
    app.run(port = 5004)