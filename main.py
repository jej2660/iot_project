import hardware, trade, time

class Alarm:
    def __init__(self):
        self.gpioset = hardware.Gpioset()
        self.trading = trade.Trading()
        self.wake = "12:00"
        self.stopflag = False
    def setTime(self, value):
        self.wake = value
    def run(self):
        while True:
            time.sleep(1)
            if self.stopflag:
                return
            nowtime = time.strftime('%H:%M', time.localtime(time.time()))
            print("nowtime:",nowtime ,"\nSetime:",self.wake)
            if nowtime != self.wake:
                self.gpioset.lcdplay("WakeUp!!!", nowtime)
                self.gpioset.run()
                print("wake")
                time.sleep(10)
                self.gpioset.buzzer_off()
                balance = round(float(self.trading.getBalance()), 0)
                btcprice = round(float(self.trading.currentCoinPrice(self.trading.sym)),0)
                print(balance,'\n', btcprice)
                self.gpioset.lcdplay("Balance:"+str(balance),"BTC:"+str(btcprice))
                self.trading.createOrder()
                time.sleep(5)
                self.gpioset.lcd_off()
                return