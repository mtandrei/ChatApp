from flask import render_template, request
from url import app, db
from url.models import Message 

@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'GET':
        #TODO Grab messages from DB query and return them to front end
        return render_template('index.html')

    if request.method == 'POST':
        # Grab fields from form
        user = request.form['username']
        message = request.form['message']

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
    return render_template('error.html')
