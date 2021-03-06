# ----------------------------------------------------------
# Author: Joaquin Cuomo
# Date: October 2021
# Project: Chat API
# Brief: Project to test skill working with Python & REST APIs
# ----------------------------------------------------------

# API entry point
# Creates the database with all the tables if they haven't been created.

from chatapi import app, db

if __name__ == '__main__':
    print('init chatapi')
    app.run(host="0.0.0.0", port=8080, debug=False)
    db.create_all()
