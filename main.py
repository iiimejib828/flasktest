from flask import Flask

import datetime

app = Flask(__name__)

@app.route("/")
def show_time():
    now = datetime.datetime.now().strftime("%Y.%m.%d %H:%M:%S")
    # HTML с мета-тегом для автоматического обновления
    return f"""
        <html>
        <head>
            <meta charset="UTF-8">
            <title>Московское время</title>
            <meta http-equiv="refresh" content="1">
        </head>
        <body>
            <h1>Московское время: {now}</h1>
        </body>
        </html>
    """

if __name__ == "__main__":
    app.run()
