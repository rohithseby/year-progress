from flask import Flask
import time, progress
from threading import Thread

app = Flask(__name__)


@app.route("/")
def main():
    return progress.main()


def run():
    app.run(host="0.0.0.0", port=8000)


def keep_alive():
    server = Thread(target=run)
    server.start()


keep_alive()

while True:
    main()
    time.sleep(5)
