##jinja2 template engine

'''
{%...%} conditions , for loop
{{   }} expressions for print output
{#...#} This is for comments
'''

from flask import Flask, redirect,url_for,render_template,request
app = Flask(__name__)


@app.route('/')
def welcome():
    return render_template('index.html')

@app.route('/success/<int:score>')
def success(score):
      res=""
      if score>=50:
        res = "PASS"
      else:
        res= "FAIL"
      exp = {'score': score,'res':res}
      return render_template('jinja2_result.html',result=exp)

@app.route('/fail/<int:score>')
def fail(score):
    return 'The person has failed and marks is' + str(score)

##result checker
@app.route('/results/<int:marks>')
def results(marks):
    result=""
    if marks<50:
        result='fail'
    else:
        result='success'
    return redirect(url_for(result,score=marks))

@app.route('/submit',methods=['GET','POST'])
def submit():
    total_score = 0
    if request.method=='POST':
        science = float(request.form['science'])
        maths = float(request.form['maths'])
        c = float(request.form['c'])
        datascience = float(request.form['datascience'])
        total_score = (science+maths+c+datascience)/4
    return redirect(url_for('success',score=total_score))



if __name__=='__main__' :
    app.run(debug=True)


