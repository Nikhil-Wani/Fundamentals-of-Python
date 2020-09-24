#py
import pyodbc as db
from flask import Flask,redirect,url_for,request,render_template

con=db.connect('DRIVER={SQL SERVER};'
               'SERVER=ACE11;'
               'DATABASE=signin;'
               'uid=sa;pwd=Apt@1234')

signin=Flask(__name__)
@signin.route("/")
def main():
    return render_template('signin.html')

@signin.route('/success/<name>')
def success(name):
    return 'Your sign_in %s' %name

@signin.route('/fail')
def fail():
    return 'Invalid!! Already exist Email id or Password'

@signin.route('/login',methods=['POST', 'GET'])
def sign():
    if request.method == 'POST':

        first_name=request.form['fn']
        last_name=request.form['ln']
        email=request.form['em']
        pwd=request.form['pass']
        phone=request.form['ph']

        cur=con.cursor()   
        cur.execute('SELECT * FROM signininfo WHERE Email_Id=?', email)
        n=cur.fetchone()
        cur.execute('SELECT * FROM signininfo WHERE pass=?', pwd)
        m=cur.fetchone()

        if(n==m==None):
            cur=con.cursor()   
            cur.execute('INSERT INTO signininfo values(?,?,?,?,?)',first_name,last_name,email,pwd,phone)
            con.commit()
            return redirect(url_for('success',name = first_name))
        else:
            return redirect(url_for('fail'))

    else:

        user=request.args.get('nm')
        pwd=request.args.get['pass']
        return redirect(url_for('success',name = first_name))


if __name__ == '__main__':
    signin.run(debug  = True)