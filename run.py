from chatapi import app, db

if __name__ == '__main__':
    print('oop')
    app.run(host="localhost", port=8080, debug=False)
    #db.create_all()