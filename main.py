import hardware, trade, time

class Alarm:
    def __init__(self):
        self.gpioset = hardware.Gpioset()
        self.trading = trade.Trading()
        self.wake = "12:00"
    def setTime(self, value):
        self.wake = value
    def run(self):
        while True:
            time.sleep(5)
            nowtime = time.strftime('%H:%M', time.localtime(time.time()))
            if nowtime == self.wake:
                self.gpioset.run()
                self.gpioset.lcdplay("WakeUp!!!", "!!!")
                time.sleep(30)
                self.gpioset.lcdplay(str(self.trading.getBalance()),str(self.trading.currentCoinPrice()))
                return

