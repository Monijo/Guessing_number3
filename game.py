from flask import Flask, request

app = Flask(__name__)

Start_HTML = """
<!DOCTYPE html>
<html lang = "en">
<head>
    <meta charset = "UTF-8">
    <title> Guess the number</title>
</head>
<body>
<h1> Imagin number between 0 and 1000 </h1>
<form action="" method="POST">
    <input type="hidden" name="min" value="{}"></input>
    <input type="hidden" name="max" value="{}"></input>
    <input type="submit" value="START">
</form>
</body>
</html>
"""

Game_HTML = """
<!DOCTYPE html>
<html lang ="en">
<head>
    <meta charset="UTF-8">
    <title>Guess the number</title>
</head>
<body>
<h1> It is number {guess}</h1>
<form action="" method ="POST">
    <input type="submit" name="user_answer" value="too big">
    <input type="submit" name="user_answer" value="too small">
    <input type="submit" name="user_answer" value="You won!">
    <input type="hidden" name="min value= "{min}">
    <input type="hidden" name="min value= "{max}">
    <input type = "hidden" name="guess" value="{guess}"
</form>
</body>
</html>
"""

Win_HTML = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset= "UTF-8">
    <title>Guess the number</title>
</head>
<body>
    <h1> I guess your number {number}! I win!</h1>
</body>
</html>
"""

@app.route("/" method = ["GET", "POST"])
def guess_the_number():
    if request.method == "GET":
        return Start_HTML.format(0,1000)
    else:
        min_number = int(request.form.get("min"))
        max_number = int(request.form.get("max"))
        user_answer = request.form.get("user_answer")
        guess = int(request.form.get("guess", 500))

        if user_answer == "too big":
            max_number = guess
        elif user_answer == "too small":
            min_number = guess
        elif user_answer == "you won":
            return Win_HTML.format(guess=guess)
        guess = (max_number - min_number) //2 +min_number

        return Game_HTML.format(guess=guess, min = min_number, max= max_number)







if __name__ == "__main__":
    app.run(degug=True)