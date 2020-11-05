from flask import Flask, request, render_template
import random

app = Flask(__name__)

def sort_letters(message):
    """A helper method to sort the characters of a string in alphabetical order
    and return the new string."""
    return ''.join(sorted(list(message)))


@app.route('/')
def homepage():
    """A homepage with handy links for your convenience."""
    return render_template('home.html')

@app.route('/froyo')
def choose_froyo():
    """Shows a form to collect the user's Fro-Yo order."""
    return render_template('froyo_form.html')

@app.route('/froyo_results')
def show_froyo_results():
    """Shows the user what they ordered from the previous page."""
    context = {
        'users_froyo_flavor' : request.args.get('flavor'),
        'users_froyo_toppings' : request.args.get('toppings')
    }

    return render_template('froyo_results.html', **context)

@app.route('/favorites')
def favorites():
    """Shows the user a form to choose their favorite color, animal, and city."""
    return """
    <form action="/favorites_results" method="GET">
       <lable for='color'>What is your favorite color?</lable> <br/>
        <input type="text" name="color"><br/>
        <lable for='animal'>What is your favorite animal?</lable> <br/>
        <input type="text" name="animal"><br/>
        <lable for='city'>What is your favorite city?</lable> <br/>
        <input type="text" name="city">
        <input type="submit" value="Submit!"><br/>
    </form>
    """

@app.route('/favorites_results')
def favorites_results():
    """Shows the user a nice message using their form results."""
    users_color = request.args.get('color')
    users_city = request.args.get('city')
    users_animal = request.args.get('animal')
    return f"""Wow, I didn't  know {users_color} {users_animal} lived in {users_city}!"""

@app.route('/secret_message')
def secret_message():
    """Shows the user a form to collect a secret message. Sends the result via
    the POST method to keep it a secret!"""
    return """
    <form action="/message_results" method="POST">
       <lable for='message'>Secret Message</lable> <br/>
        <input type="text" name="message">
        <input type="submit" value="Submit!"><br/>
    </form>
    """

@app.route('/message_results', methods=['POST'])
def message_results():
    """Shows the user their message, with the letters in sorted order."""
    message = request.form.get('message')
    return f"""
        <span>Here's your secret message!</span><br />
        {''.join(sorted(message))}
    """

@app.route('/calculator')
def calculator():
    """Shows the user a form to enter 2 numbers and an operation."""
    return render_template('calculator_form.html')

@app.route('/calculator_results')
def calculator_results():
    """Shows the user the result of their calculation."""
    operation = request.args.get('operation')
    operand1 = request.args.get('operand1')
    operand2 = request.args.get('operand2')
    
    if operation == "add":
        answer = f"{int(operand1) + int(operand2)}"
    elif operation == "subtract":
        answer = f"{int(operand1) - int(operand2)}"
    elif operation == "multiply":
        answer = f"{int(operand1) * int(operand2)}"
    elif operation == "divide":
        answer = f"{int(operand1) / int(operand2)}"

    context = {
        'operation' : operation,
        'operand1' : operand1,
        'operand2' : operand2,
        'answer' : answer
    }

    return render_template('calculator_results.html', **context)


# List of compliments to be used in the `compliments_results` route (feel free 
# to add your own!) 
# https://systemagicmotives.com/positive-adjectives.htm
list_of_compliments = [
    'awesome',
    'beatific',
    'blithesome',
    'conscientious',
    'coruscant',
    'erudite',
    'exquisite',
    'fabulous',
    'fantastic',
    'gorgeous',
    'indubitable',
    'ineffable',
    'magnificent',
    'outstanding',
    'propitioius',
    'remarkable',
    'spectacular',
    'splendiferous',
    'stupendous',
    'super',
    'upbeat',
    'wondrous',
    'zoetic'
]

@app.route('/compliments')
def compliments():
    """Shows the user a form to get compliments."""
    return render_template('compliments_form.html')

@app.route('/compliments_results')
def compliments_results():
    """Show the user some compliments."""
    name = request.args.get('users_name')
    compliments = request.args.get('wants_compliments')
    num = int(request.args.get('num_compliments'))
    
    listCompliments = []
    if compliments == 'yes':
        if num > 0:
            i = 0 
            listCompliments = random.sample(list_of_compliments, k=num)

    context = {
        'name' : name,
        'compliments' : compliments,
        'num' : num,
        'listCompliments' : listCompliments
    }

    return render_template('compliments_results.html', **context)


if __name__ == '__main__':
    app.run(debug=True)
