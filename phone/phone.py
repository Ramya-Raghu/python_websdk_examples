import plivo, plivoxml
from flask import Flask, request

app = Flask(__name__)

@app.route('/', methods=['GET','POST'])
def web_phone():
    try:    
        # Render the phone.html page
        return render_template('phone.html')
    except Exception as e:
        print '\n'.join(traceback.format_exc().splitlines())

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)