#
#
# class for storing an order  details
#
#
import time

from AliExp_OrderListParser.AliItem import AliItem


class AliOrder:

    def __init__(self):
        self.itemList = []
        self.seller = "someones shop"
        self.orderNum = 666
        self.datetime = time.strptime('1979-05-16', "%Y-%m-%d")
        self.orderAmount = 0


    def setShipping(self):
        totalItemsCost = 0

        for item in self.itemList:
            totalItemsCost += item.itemPrice * item.numUnits

        if totalItemsCost == self.orderAmount:
            return
        else:
            totalShipping = self.orderAmount - totalItemsCost
            for item in self.itemList:
                myRatio = (item.itemPrice * item.numUnits) / totalItemsCost
                item.shippingCost = totalShipping * myRatio
                #print(item.description + str(item.shippingCost))