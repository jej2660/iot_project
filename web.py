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
    global alarm
    global th
    alarm = Alarm()
    alarm.setTime(settime)
    th = threading.Thread(target=alarm.run)
    try:
        th.start()
    except Exception:
        return "Already Operation"
    return "ok"
@app.route('/stop')
def stop():
    alarm.stopflag = True
    return "stop"
    
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)