from flask import request, Flask, jsonify, render_template, redirect
app = Flask(__name__)

@app.route('/')
def main_route():
    return redirect('/get_my_ip'), 308

@app.route("/get_my_ip", methods=["GET"])
def get_my_ip():
    return jsonify({"ip" : request.remote_addr}), 200

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80, debug=True)