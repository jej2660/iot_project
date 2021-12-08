from re import A
from flask import Flask, escape, request,render_template
from main import Alarm
import threading
app = Flask(__name__)

settime = "12:00"
alarm = Alarm()
th = threading.Thread(target=alarm.run)
@app.route('/')
def hello():
    return render_template('index.html')
@app.route("/SetAlarm",methods=['GET'])
def setAlarm():
    global settime
    settime = request.args.get('settime')
    print(settime)
    return settime
@app.route('/start')
def start():
    alarm.setTime(settime)
    th.start()
    return "ok"
    
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)