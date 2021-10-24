from flask import Flask

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









if __name__ == "__main__":
    app.run(degug=True)