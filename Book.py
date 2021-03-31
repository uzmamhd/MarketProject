# -*- coding: utf-8 -*-
"""
Created on Sat Mar 20 20:14:22 2021

@author: uzmam
"""

class Order: 
    def _init_(self, NbAction, Prix, OrdreType):
        self.NbAction = NbAction
        self.Prix = Prix
        self.OrdreType = OrdreType
        
class Book:
    def _init_(self, BookName):
        self.BookName = BookName 
        self.BuyOrders = []
        self.SellOrders = []
       
    def BookState_BuySide(self):
        NbAction=[]
        Prix=[]
        if self.BuyOrders == []:
            print("ORDER BOOK: BUY SIDE \n There are no olders in the book \n")
        else:
            for i in range(len(self.BuyOrders)):
            NbAction.append(self.BuyOrders[i].NbAction)
            Prix.append(self.BuyOrders[i].Prix)
            df=pd.DataFrame({"NbAction" : NbAction , "Prix" : Prix })
                print("Order Book: BUY SIDE" '\n' , df, '\n')
            
    def BookState_SellSide(self):
    NbAction=[]
    Prix=[]
        if self.SellOrders == []:
            print("ORDER BOOK : SELL SIDE \n There are no orders in the book \n")
        else:
            for i in range(len(self.SellOrders)):
            NbAction.append(self.SellOrders[i].NbAction)
            Prix.append(self.SellOrders[i].Prix)
            df=pd.dataframe("Nb Action" : Nb Action , "Prix" : Prix)
                print("Order Book : SELL SIDE" '\n' , df, '\n')
    
    def affichage(self):
        print("This is the log for the order book of",self.BookName, ':\n')
        self.BookState_BuySide()
        self.BookState_SellSide()
        

    def insert_Buy(self, NbAction, Prix):
        order = Order(NbAction, Prix, 'Buy')
        print ("Insert Buy Order",order.NbAction,"@", order.Prix, "in",self.BookName)        
        if self.BuyOrders == []:
            self.BuyOrders.append(order)
            print("First order in the book")
        else:
            for i in range(len(self.BuyOrders)):
                if self.BuyOrders[i].Prix < order.Prix:
                    self.BuyOrders.insert(i,order)
                    print( "Order added to the book")
                    break
                elif self.BuyOrders[i].Prix == order.Prix:
                    if len(self.BuyOrders)<=i+1:
                        self.BuyOrders.append(order)
                        print("Order added after a similar order")
                        break
                    elif self.BuyOrders[i+1].Prix < order.Prix:
                        self.BuyOrders.insert(i+1,order)
                        print("Order added after a similar order")
                        break
            if self.BuyOrders[-1].Prix > order.Prix:
                self.BuyOrders.append(order)
                print("Order added at the end of the queue")
        self.execution_trade()


    def insert_Sell(self, NbAction, Prix):
        order = Order(NbAction, Prix, 'Sell')
        print ("Insert Sell Order",order.NbAction,"@", order.Prix, "in",self.BookName)
        if self.SellOrders == []:
            self.SellOrders.append(order)
            print("First order in the book")
        else:
            for i in range(len(self.SellOrders)):
                if self.SellOrders[i].Prix > order.Prix:
                    self.SellOrders.insert(i,order)
                    print( "Order added to the book")
                    break
                elif self.SellOrders[i].Prix == order.Prix:
                    if len(self.SellOrders)<=i+1:
                        self.SellOrders.append(order)
                        print("Order added after a similar order")
                        break
                    elif self.SellOrders[i+1].Prix > order.Prix:
                        self.SellOrders.insert(i+1,order)
                        print("Order added after a similar order")
                        break
            if self.SellOrders[-1].Prix < order.Prix:
                self.SellOrders.append(order)
                print("Order added at the end of the queue")
        self.execution_trade()
              
        
    def execution_trade(self):
        while self.BuyOrders != [] and self.SellOrders != []:
            BidAskSpread = self.BuyOrders[0].Prix - self.SellOrders[0].Prix
            if BidAskSpread <0:
                break
            else:
                if self.BuyOrders[0].Prix >= self.SellOrders[0].Prix:
                    TradePrix = min(self.SellOrders[0].Prix, self.BuyOrders[0].Prix)
                    if self.BuyOrders[0].NbAction == self.SellOrders[0].NbAction:
                        QuantityTraded = self.BuyOrders[0].NbAction
                        self.BuyOrders.pop(0)
                        self.SellOrders.pop(0)
                        print("TRADE EXECUTED : \n Sold",QuantityTraded, "@", TradePrix)
                    elif self.BuyOrders[0].NbAction < self.SellOrders[0].NbAction:
                        QuantityTraded = self.BuyOrders[0].NbAction
                        self.BuyOrders.pop(0)
                        self.SellOrders[0].NbAction = self.SellOrders[0].NbAction - QuantityTraded
                        print("TRADE EXECUTED : \n Sold",QuantityTraded, "@", TradePrix)
                    elif self.BuyOrders[0].NbAction > self.SellOrders[0].NbAction:
                        QuantityTraded = self.SellOrders[0].NbAction
                        self.SellOrders.pop(0)
                        self.BuyOrders[0].NbAction = self.BuyOrders[0].NbAction - QuantityTraded
                        print("TRADE EXECUTED : \n Sold",QuantityTraded, "@", TradePrix)
        self.affichage()  
      


book = Book('TEST')
book.insert_Buy(10,10.0)
book.insert_Buy(1,10.0)
book.insert_Buy(160,15.0)
book.insert_Sell(120,12.0)
book.insert_Buy(5, 10.0)
book.insert_Buy(2,11.0)
book.insert_Sell(110,10.0)
book.insert_Sell(10,10.0)
