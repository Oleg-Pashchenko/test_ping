import flask

app = flask.Flask(__name__)


@app.route('/ping')
def main():
    return flask.jsonify('ok')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8765)
