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
            time.sleep(1)
            nowtime = time.strftime('%H:%M', time.localtime(time.time()))
            if nowtime == self.wake:
                self.gpioset.lcdplay("WakeUp!!!", nowtime)
                self.gpioset.run()
                print("wake")
                time.sleep(10)
                self.gpioset.buzzer_off()
                self.gpioset.lcdplay(str(self.trading.getBalance()),str(self.trading.currentCoinPrice(self.trading.sym)))
                self.trading.createOrder()
                time.sleep(10)
                return