# -*- coding: utf-8 -*-


#main
from book import book
def main(): 
    book = Book("TEST")
    book.insert_Buy(10,10.0)
    book.insert_Sell(120,12.0)
    book.insert_Buy(5, 10.0)
    book.insert_Buy(2,11.0)
    book.insert_Sell(1,10.0)
    book.insert_Sell(10,10.0)
    
if _name_ == "_main_":
    main()
    i=0
        for i in range(max(len(self.BuyOrders),len(self.SellOrders))):
            if self.BuyOrders != [] and self.SellOrders != []:
                BidAskSpread = self.BuyOrders[0].Prix - self.SellOrders[0].Prix
                while BidAskSpread > 0:
                    if self.BuyOrders[0].Prix == self.SellOrders[0].Prix:
                        TradePrix = self.SellOrders[0].Prix
                        if self.BuyOrders[0].NbAction == self.SellOrders[0].NbAction:
                            QuantityTraded = self.BuyOrders[0].NbAction
                            self.BuyOrders.pop(0)
                            self.SellOrders.pop(0)
                            print("Trade Executed : \n Sold",QuantityTraded, "@", TradePrix)
                        elif self.BuyOrders[0].NbAction < self.SellOrders[0].NbAction:
                            QuantityTraded = self.BuyOrders[0].NbAction
                            self.BuyOrders.pop(0)
                            self.SellOrders[0].NbAction = self.SellOrders[0].NbAction - QuantityTraded
                            print("Trade Executed : \n Sold",QuantityTraded, "@", TradePrix)
                        elif self.BuyOrders[0].NbAction > self.SellOrders[0].NbAction:
                            QuantityTraded = self.SellOrders[0].NbAction
                            self.SellOrders.pop(0)
                            self.BuyOrders[0].NbAction = self.BuyOrders[0].NbAction - QuantityTraded
                            print("Trade Executed : \n Sold",QuantityTraded, "@", TradePrix)
                    elif self.BuyOrders[0].Prix >= self.SellOrders[0].Prix:
                        QuantityTraded = max(self.BuyOrders[0].NbAction, self.SellOrders[0].NbAction)
                        for j in range(QuantityTraded):
                            self.BuyOrders[0].NbAction = self.BuyOrders[0].NbAction - QuantityTraded
                            if self.BuyOrders[0].NbAction == 0:
                                self.affichage()

