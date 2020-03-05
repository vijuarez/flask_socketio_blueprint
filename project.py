from app import create_app, SCKT

DEBUG = True

app = create_app(debug=DEBUG)

if __name__ == '__main__':
    SCKT.run(app, debug=DEBUG)