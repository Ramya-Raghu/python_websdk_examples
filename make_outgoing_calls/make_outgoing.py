import plivo, plivoxml
from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/', methods=['GET','POST'])
def make_outgoing():

    username = "Your SIP Endpoint Username"
    password = "Your SIP Endpoint Password"
    # Render the html file
    return render_template('make_outgoing.html', username=username, password=password)

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
