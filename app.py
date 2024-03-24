from flask import Flask, request

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

def is_prime(n):
    """Check if a number is prime."""
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
@app.route('/dummy')
def dummy():
    for i in range(0,10000):
        print(i)

    return "dummy"
@app.route('/prime/<int:n>')
def prime(n):
    """Return a list of prime numbers up to n."""
    primes = [str(i) for i in range(2, n+1) if is_prime(i)]
    return "Primes up to " + str(n) + ": " + ", ".join(primes)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=80)
