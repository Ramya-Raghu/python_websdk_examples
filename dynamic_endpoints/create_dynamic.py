import plivo, plivoxml
from flask import Flask, request


app = Flask(__name__)

# Creae an Endpoint
@app.route('/', methods=['GET','POST'])
def phone():
    try:
        auth_id = "Your AUTH_ID"
        auth_token = "Your AUTH_TOKEN"

        p = plivo.RestAPI(auth_id, auth_token)
        # Generate a random username
        username = ''.join([random.choice('abcdefghijklmnopqrstuvwxyz') for i in xrange(6)])
        # Generate a random password
        password = ''.join([random.choice('abcdefghijklmnopqrstuvwxyz') for i in xrange(6)])

        # Print the generated username and password
        print "Usernme ; %s " % (username)
        print "Password ; %s " % (password)

        # Create an Endpoint
        params = {
            'username': username, # The username for the endpoint to be created
            'password': password, # The password for your endpoint username
            'alias' : username # Alias for the endpoint
        }

        response = p.create_endpoint(params)
        # Print the response
        print str(response)

        # Fetch the username of the created Endpoint
        uname = response[1]['username']
        pwd = params['password']
        # Fetch the Endpoint ID
        endpoint_id = response[1]['endpoint_id']

        # Print the Endpoint details
        print "Usernme ; %s " % (uname)
        print "Password ; %s " % (pwd)
        print "Endpint ID ; %s " % (endpoint_id)

        # Render the phone.html page
        return render_template('phone.html', uname=uname, pwd=pwd, end_id=endpoint_id)
    except Exception as e:
        print '\n'.join(traceback.format_exc().splitlines())

# Delete an Endpoint
@app.route("/delete_endpoint/<endpoint_id>/", methods=['GET','POST'])
def delete_endpoint(endpoint_id):
    try:
        print endpoint_id
        auth_id = "Your AUTH_ID"
        auth_token = "Your AUTH_TOKEN"

        p = plivo.RestAPI(auth_id, auth_token)
        params = {
            'endpoint_id' : endpoint_id # ID of the endpoint that as to be deleted
        }

        # Delete the created Enpoint
        response = p.delete_endpoint(params)

        # Print the response
        print str(response)
        # Return the response
        return str(response)
    except Exception as e:
        print '\n'.join(traceback.format_exc().splitlines())

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)