#
#
# class for storing an order items details
#
#


import DateTime
import time

class AliItem:


    def __init__(self):
        self.description = "none"
        self.seller = "None"
        self.ordernum = 0
        self.datetime = time.strptime('1979-05-16',"%Y-%m-%d")
        self.itemPrice = 0
        self.numUnits = 0
        self.shippingCost = 0



    def ItemAsLineOfCSV(self):
        array = (self.description, self.seller, self.ordernum, self.datetime.date(), self.datetime.time, self.itemPrice, self.numUnits, self.shippingCost)

    def getAllItems(self):
        array = []
        array.append(self.description)
        array.append(self.seller)
        array.append(self.ordernum)
        array.append(str(self.datetime.tm_year) + '-' + str(self.datetime.tm_mon) + '-' + str(self.datetime.tm_mday) )
        array.append(str(self.datetime.tm_hour) + ":" + str(self.datetime.tm_min) )
        array.append(str(self.itemPrice))
        array.append(str(self.numUnits))
        array.append(str(self.shippingCost))
        return array


        #12:36 Dec. 12 2012
def aliTimeToTime(aliTime):
    return time.strptime(aliTime,"%H:%M %b. %d %Y")

#testing...

if __name__ == "__main__":

    #aliTime = "12:36 Dec. 12 2012"
    #print(time.strptime(aliTime,"%H:%M %b. %d %Y"))

    item = AliItem()
    item.description = "crazy shit"
    item.seller = "someones shop"
    item.ordernum = 666
    item.datetime = aliTimeToTime("12:36 Dec. 12 2012")
    item.itemPrice = 667
    item.numUnits = 2
    item.shippingCost = 5


