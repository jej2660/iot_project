from binance.client import Client
import math,random,time

class Trading:
    def __init__(self):
        self.future_url = "https://testnet.binancefuture.com/fapi"
        self.api_key = "ba02149b5604c873fbf402169af58da894a74b56867f37e1b6f9e225cc952752"
        self.secret_key = "719507ff0249617491c4af68aea292e760c4987af76a0d94b0039e1af08547e1"
        self.client = Client(self.api_key, self.secret_key, testnet=True)
        self.sym ="BTCUSDT"
        self.side = ['BUY','SELL']

    def getBalance(self):
        return self.client.futures_account_balance()[1]['balance']
    def currentCoinPrice(self, symbol):
        return self.client.get_avg_price(symbol=symbol)['price']
    def preciseQuantity(self, quantity):
        print(quantity)
        quantity = float(round(quantity, 2)) * 10
        print(quantity)
        return quantity

    def closeOrder(self):
        orderdata = self.client.futures_get_all_orders(symbol=self.sym)
        for id in orderdata:
            self.client.futures_cancel_order(orderid=id['orderid'])

    def createOrder(self):
        money = self.getBalance()
        price = self.currentCoinPrice(self.sym)
        pos_side = self.side[random.randint(0,1)]
        quantity = (float(money) * (random.randint(0, 30) * 0.01)) / float(price)
        print("before",quantity)
        quantity = self.preciseQuantity(quantity)
        print("send",quantity)
        self.client.futures_create_order(symbol=self.sym, side=pos_side, type='MARKET', quantity=float(quantity))