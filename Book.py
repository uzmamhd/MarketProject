# -*- coding: utf-8 -*-
"""
Created on Sat Mar 20 20:14:22 2021

@author: uzmam
"""

class Order: 
    def __init__(self, NbAction, Prix, OrdreType): #ajouter l id 
        self.NbAction = NbAction
        self.Prix = Prix
        self.OrdreType = OrdreType
        
class Book:
    def __init__(self, BookName):
        self.BookName = BookName 
        self.BuyOrders = []
        self.SellOrders = []
       
    def BookState_BuySide(self):
        print("Order book : Buy Side")
        if self.BuyOrders == []:
            print("There are no orders in the book \n")
        else:
            for i in range(len(self.BuyOrders)):
                print(self.BuyOrders[i].NbAction,"@",self.BuyOrders[i].Prix )
            
    def BookState_SellSide(self):
        print("Order book : Sell Side")
        if self.SellOrders == []:
            print("There are no orders in the book \n")
        else:
            for i in range(len(self.SellOrders)):
                print(self.SellOrders[i].NbAction,"@", self.SellOrders[i].Prix)