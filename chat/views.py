from flask import render_template, request, jsonify
from chat import app, db
from chat.models import Message 

@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'GET':
        #TODO Check to see if loading page or getting messages
        return render_template('index.html')

    if request.method == 'POST':
        # Grab fields from form
        user = request.form['username']
        message = request.form['message']
        

        #TODO sanitize input
        #If blank message or username, return error
        if user == "":
            return render_template('index.html', error="Error: You put in a blank username!")

        if message == "":
            return render_template('index.html', error="Error: You put in a blank message!")

        #Check length of message and username
        if len(user) > 15:
           return render_template('index.html',
                    error="Error: Username exceeds 15 characters")

        if len(message) > 500:
            return render_template('index.html',
                    error="Error: Message exceeds 500 characters")

        # Create and add database record of message
        msg = Message(message=message, user=user)
        db.session.add(msg)
        db.session.commit()

        # Return successful POST request to homepage
        return render_template('index.html', message="Success! You added a message to the database")

    # If bad request, render error page
    return render_template('error.html', error='ERROR: Bad request!')

@app.route('/messages', methods=['GET'])
def messages():
    if(request.method == 'GET'):
        #Queries database for most recent 30 messages:
        messages = Message.query.limit(30).all()

        #Builds JSON format list for front end
        message_list = {}
        for i in range(0, len(messages)):
            message_list[i] = { messages[i].username: messages[i].message }

        return flask.jsonify(**message_list)
    else:
        return render_template('index.html', error='ERROR: Bad request!')
