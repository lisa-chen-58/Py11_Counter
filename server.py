from flask import Flask, render_template,redirect, request,session
app = Flask(__name__)
app.secret_key = 'keep it secret, keep it safe'

@app.route('/')
def index():
    if 'count' not in session:
        session["count"]=0
    else:
        session["count"] +=1
        print('hi')
    return render_template("index.html")

@app.route('/add_two')
def add_two():
    if "count" not in session:
        session["count"]=0
    else:
        session["count"] +=1 #adds one
        print('hello') 
    return redirect('/') #adds another one upon refresh

@app.route('/<int:num>')
def some_number(num):
    if 'count' not in session:
        session["count"]=0
    else:
        session["count"] += num
        print('hi')
    return render_template("index.html", num=num)

@app.route('/destroy_session')
def reset():
    session.clear()
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)