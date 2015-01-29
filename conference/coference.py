import plivo, plivoxml
from flask import Flask, request

app = Flask(__name__)

@app.route('/', methods=['GET','POST'])
def web_phone():
    try:    
        # Render the conference.html page
        return render_template('conference.html')
    except Exception as e:
        print '\n'.join(traceback.format_exc().splitlines())

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)