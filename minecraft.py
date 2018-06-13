from bottle import route, get
import bottle as b
from sys import argv


@route('/')
def index():
    return b.template('minecraft.html')


@get('/js/<filename:re:.*\.js>')
def javascript(filename):
    return b.static_file(filename, root='js')


@get('/css/<filename:re:.*\.css>')
def stylesheets(filename):
    return b.static_file(filename, root='css')


@get('/sounds/<filename:re:.*\.mp3>')
def sounds(filename):
    return b.static_file(filename, root='sounds')


def main():
    b.run(host='0.0.0.0', port=argv[1])


if __name__ == '__main__':
    main()