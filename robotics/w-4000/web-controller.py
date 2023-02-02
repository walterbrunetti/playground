from flask import Flask, render_template, jsonify
from gpio import initialize, move_forward, stop, move_left, move_right, move_backward, exit_program


app = Flask(__name__)


@app.route('/')
def home():
    initialize()
    return render_template('index.html', status="Status: ready")


@app.route('/go-forward',methods = ['GET', ])
def go_forward():
    move_forward()
    return jsonify({"success": True})


@app.route('/go-stop',methods = ['GET', ])
def stop():
    stop()
    return jsonify({"success": True})


@app.route('/go-right',methods = ['GET', ])
def go_right():
    move_right()
    return jsonify({"success": True})


@app.route('/go-left',methods = ['GET', ])
def go_left():
    move_left()
    return jsonify({"success": True})


@app.route('/go-backward',methods = ['GET', ])
def go_backward():
    move_backward()
    return jsonify({"success": True})


@app.route('/go-exit',methods = ['GET', ])
def exit_program():
    exit_program()
    return jsonify({"success": True})




if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
