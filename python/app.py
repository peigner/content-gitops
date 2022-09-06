from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Partyyyy to the Peeopleee  dam dam dam dam dam uz uz uz"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000)
