#python
from flask import Flask,redirect,url_for,request,render_template

button=Flask(__name__)
@button.route("/")
def main():
    return render_template('flask.html')

@button.route('/success/<name>')
def success(name):
    return 'welcome %s' %name

@button.route('/login',methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        
        user=request.form['nm']
        password=request.form['pass']
        
        return redirect(url_for('success',name = user))

    else:
        user=request.args.get('nm')
        user=request.args.get['pass']
        return redirect(url_for('success',name = user))

if __name__ == '__main__':
    button.run(debug  = True)



