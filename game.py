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
    <input type ="hidden" name="min" value="{}">
    <input type ="hidden" name="max" value="{}">
    input type="submit" value = "OK">
</form>
</body>
</html>
"""





if __name__ == "__main__":
    app.run(debug=True)