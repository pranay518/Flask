from flask import Flask, redirect,url_for


app = Flask(__name__)


@app.route('/')
def welcome():
    return 'welcome to learn Flask'


@app.route('/success/<int:score>')
def success(score):
    return 'The person has passed and marks is'+ ' ' + str(score)

@app.route('/fail/<int:score>')
def fail(score):
    return 'The person has failed and marks is'+ ' ' + str(score)

##result checker
@app.route('/results/<int:marks>')
def results(marks):
    result=""
    if marks<50:
        result='fail'
    else:
        result='success'
    return redirect(url_for(result,score=marks))  # The score parameter is passed as a keyword argument to url_for(), which corresponds to the dynamic parameter <int:score> in the 'success' and 'fail' routes.

if __name__=='__main__' :
    app.run(debug=True)

