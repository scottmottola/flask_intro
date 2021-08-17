"""Greeting Flask app."""

from random import choice

from flask import Flask, request

# "__name__" is a special Python variable for the name of the current module
# Flask wants to know this to know what any imported things are relative to.
app = Flask(__name__)

AWESOMENESS = [
    'awesome', 'terrific', 'fantastic', 'neato', 'fantabulous', 'wowza',
    'oh-so-not-meh', 'brilliant', 'ducky', 'coolio', 'incredible',
    'wonderful', 'smashing', 'lovely']

DISS = [
  'stupid', 'weak', 'squishy'
]


@app.route('/')
def start_here():
    """Home page."""

    return """
    <!doctype html>
    <html>
      <a href="/hello">Hi! This is the home page.</a>
    </html>
    """


@app.route('/hello')
def say_hello():
    """Say hello and prompt for user's name."""
    clist = ""
    for comp in AWESOMENESS:
      clist += f"<option value={comp}>{comp}</option>"

    return f"""
    <!doctype html>
    <html>
      <head>
        <title>Hi There!</title>
      </head>
      <body>
        <h1>Hi There!</h1>
        <form action="/greet">
          What's your name? <input type="text" name="person">

          <select name="compliment" id="compliment" action="/">
            {clist}
          </select>

          <input type="submit" value="Submit">
        </form>
        <h2>Want a Diss?</h2>
        <div>
          <form action="/diss">
            What's your name? <input type="text" name="person">

            <select name="compliment" id="compliment" action="/">
              {clist}
            </select>

            <input type="submit" value="Submit">
          </form>
        </div>
      </body>
    </html>
    """


@app.route('/greet')
def greet_person():
    """Get user by name."""

    player = request.args.get("person")

    compliment = choice(AWESOMENESS)
    compliment += " and "
    compliment += request.args.get("compliment")
    compliment += " and not "
    compliment += choice(DISS)

    return f"""
    <!doctype html>
    <html>
      <head>
        <title>A Compliment</title>
      </head>
      <body>
        Hi, {player}! I think you're {compliment}!
      </body>
    </html>
    """
    

@app.route('/diss')
def diss_person():
    """Get user by name."""

    player = request.args.get("person")

    compliment = choice(DISS)
    compliment += " and not "
    compliment += request.args.get("compliment")

    return f"""
    <!doctype html>
    <html>
      <head>
        <title>A Compliment</title>
      </head>
      <body>
        Hi, {player}! I think you're {compliment}!
      </body>
    </html>
    """


if __name__ == '__main__':
    # debug=True gives us error messages in the browser and also "reloads"
    # our web app if we change the code.
    app.run(debug=True, host="0.0.0.0")
