from flask import Flask
from markupsafe import escape

app = Flask(__name__)

@app.route("/")
def hello_world():
    return """<p>hello, junha</p>"""

@app.route("/<name>")
def hello(name):
    num1 = int(name[0])
    op = name[1]
    num2 = int(name[2])
    print(num1, num2)

    if op == "+":
        result = num1 + num2
    elif op == "-":
        result = num1 - num2
    elif op == "X": 
        result = num1 * num2
    else:
        result = num1 / num2
        

    return f"Result : {escape(result)}!"        
if __name__ == '__main__':
    app.run()