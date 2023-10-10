import os
from flask import Flask, request

# Create a new Flask app
app = Flask(__name__)

# == Your Routes Here ==

# == Example Code Below ==

# GET /emoji
# Returns a emojiy face
# Try it:
#   ; curl http://127.0.0.1:5001/emoji
@app.route('/emoji', methods=['GET'])
def get_emoji():
    return ":)"

# This imports some more example routes for you to see how they work
# You can delete these lines if you don't need them.
from example_routes import apply_example_routes
apply_example_routes(app)

# == End Example Code ==

@app.route('/hello', methods=['GET'])
def hello():
    name = request.args['name'] # The value is 'David'

    # Send back a friendly greeting with the name
    return f"Hello {name}!"

@app.route('/goodbye', methods=['POST'])
def goodbye():
    name = request.form['name'] # The value is 'Alice'

    # Send back a fond farewell with the name
    return f"Goodbye {name}!"

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form['name']
    message = request.form['message']
    
    return f"Thanks {name}, you sent this message: {message}"

@app.route('/wave', methods=['GET'])
def wave():
    name = request.args['name']
    
    return f"I am waving at {name}"

@app.route('/count_vowels', methods=['POST'])
def count_vowels():
    text = request.form['text']
    count = request.form['num']
    vowels = set("AEIOUaeiou")
    vowel_count = 0
    for char in text:
        if char in vowels:
            vowel_count += 1
    return f"There are {count} vowels in {text}"
    
    
@app.route('/sort-names', methods=['POST'])
def post_sort_names():
    names = request.form['names'].split(',')
    names = sorted(names)
    
    return ','.join(names)


@app.route('/names', methods=['GET'])
def names():
    given_list = 'Julia, Alice, Karim, '
    name = request.args['add'] # The value is 'Eddie'
    new_list = f"{given_list}{name}"
    # Send back a friendly greeting with the name
    return sorted(new_list)



    
    '''text = request.form['text']
    
    return f"There are 3 vowels in {text}"


@app.route('/count_vowels', methods=['POST'])
def count_vowels():
    text = request.form['text']
    count = request.form['num']
    vowels = set("AEIOUaeiou")
    vowel_count = 0
    for char in text:
        if char in vowels:
            vowel_count += 1
    return f"There are {count} vowels in {text}"'''
# These lines start the server if you run this file directly
# They also start the server configured to use the test database
# if started in test mode.
if __name__ == '__main__':
    app.run(debug=True, port=int(os.environ.get('PORT', 5001)))

