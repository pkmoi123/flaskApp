from flask import Flask, request
from markupsafe import escape
from urllib.parse import urlsplit, urlunsplit
from textwrap import dedent

app = Flask(__name__)

@app.route('/receive-flag', methods=['GET'])
def receive_flag():
    flag = request.args.get('flag')
    if flag:
        # Log the flag to a file
        with open('flag.txt', 'a') as f:
            f.write(flag + '\n')
        return 'Flag received successfully!'
    else:
        return 'No flag provided.'

@app.route("/")
def hello_world():
    app.logger.info('test')
    return "<p>Server is running</p>"

@app.route("/malfunction", methods=['GET'])
def malfunction():
    destination = request.args.get('link')
    if(not destination):
        return ''

    (scheme, host, path, query, fragment) = urlsplit(destination)
    result = urlunsplit(('', '', path, query, fragment))
    return "<p>%s</p>" % result    

if __name__ == '__main__':
    app.run(debug=True)
