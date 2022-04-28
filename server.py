from flask import Flask, render_template,redirect, request,session
app = Flask(__name__)
app.secret_key = 'keep it secret, keep it safe'

@app.route('/')
def index():
    if 'count' not in session:
        session["count"]=0
    else:
        session["count"] +=1
    return render_template("index.html")

@app.route('/add_two')
def add_two():
    if "count" not in session:
        session["count"]=0
    else:
        session["count"] +=1
    return redirect('/')

# Supposed to allow user input for increment
# @app.route('/add_num', methods=['POST'])
# def add_num(num):
#     if "count" not in session:
#         session["count"]=0
#     else:
#         session["count"] += num
#     return redirect('/',num=num)

@app.route('/destroy_session')
def reset():
    session.clear()
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)