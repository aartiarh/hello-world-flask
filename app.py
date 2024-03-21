from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    docker_whale = """
Hello World

                                       ##         .
                                 ## ## ##        ==
                              ## ## ## ## ##    ===
                          /""""""""""""""""""\___/ ===
                     ~~~ {~~ ~~~~ ~~~ ~~~~ ~~~ ~ /  ===- ~~~
                          \______ o           __/
                            \    \         __/
                             \____\_______/
"""
    return '<pre>' + docker_whale + '</pre>'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=80)
