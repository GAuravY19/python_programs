from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/even_or_odd/<int:n>')
def even_or_odd(n):
    if n%2 == 0:
        result = {
            "Even" : True,
            "Odd" : False,
            "Number" : n
        }
        
    else:
        result = {
            "Even" : False,
            "Odd" : True,
            "Number" : n
        }
        
    return result

if __name__ == "__main__":
    app.run(debug=True)