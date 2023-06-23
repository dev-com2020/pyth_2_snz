import json
import logging
import random
import sys
import time
from datetime import datetime
from typing import Iterator

from flask import Flask, render_template, request, Response, stream_with_context

logging.basicConfig(stream=sys.stdout, level=logging.INFO, format="%(asctime)s"
                                                                  "%(levelname)s"
                                                                  "%(message)s")
logger = logging.getLogger(__name__)
app = Flask(__name__)
random.seed()


@app.route('/')
def index() -> str:
    return render_template("index.html")


def generate_random_data() -> Iterator[str]:
    if request.headers.getlist("X-Forwarded-For"):
        client_ip = request.headers.getlist("X-Forwarded-For")[0]
    else:
        client_ip = request.remote_addr or ""
    try:
        logger.info("Client %s connected", client_ip)
        while True:
            json_data = json.dumps(
                {
                    "time": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                    "value": random.random() * 100,
                }
            )
            yield f"data:{json_data}\n\n"
            time.sleep(4)
    except GeneratorExit:
        logger.info("Client %a disconnected", client_ip)


@app.route('/chart-data')
def chart_data() -> Response:
    response = Response(stream_with_context(generate_random_data()), mimetype="text/event-stream")
    response.headers["Cache-Control"] = "no-cache"
    response.headers["X-Accel-Buffering"] = "no"
    return response

if __name__ == '__main__':
    app.run()
