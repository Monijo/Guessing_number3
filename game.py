from flask import Flask, request

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def guessing_number():
    if request.method == 'GET':
        "Let's play!Imagine  number in the range 0-1000 and I will guess your number in max 10 attempts!"
        form = '''
            <form action='' method = 'POST'>
                <h2> "Let's play!Imagine  number in the range 0-1000 and I will guess your number in max 10 attempts!"</h2>

               <input type="submit" value="Start">
                   </form>
                   '''
        return form

if __name__ == "__main__":
    app.run(debug = True)





