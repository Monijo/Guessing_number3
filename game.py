from flask import Flask, request

app = Flask(__name__)

HTML_Start = """
<!DOCTYPE html>
<html lang = "en">
<head>
    <meta charset="UTF-8">
    <title>Guess the number</title>
</head>
<body>
<h1> Imagin number between 0 and 1000 </h1>
<form action = "" method ="POST">
    <input type="submit" name="user_answer" value="too big">
    <input type="submit" name="user_answer" value="too small">
    <input type="submit" name="user_answer" value="you won">
    <input type ="hidden" name="min" value="{min}">
    <input type ="hidden" name="max" value="{max}">
    <input type = "hidden" name="guess" value="{guess}">
    
</form>
</body>
</html>
"""





if __name__ == "__main__":
    app.run(debug=True)