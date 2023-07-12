# msg = 'welcome to flask'
# print(msg)
# print('1st flask app')


### WSGI application is standard that is used to create communication b/w web application & web server
from flask import Flask
app=Flask(__name__)

### decorator route to root directory
@app.route('/')
def welcome():
    return "welcome to flask. this is my first application"

@app.route('/members')
def members():
    return "welcome to flask - members"
    

if __name__ =='__main__':
    app.run(debug=True)


    