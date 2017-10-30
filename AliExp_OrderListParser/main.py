#
#   main parser:
#
#
import csv
import datetime

from DateTime import DateTime
from lxml import html

from AliExp_OrderListParser.AliItem import aliTimeToTime, AliItem
from AliExp_OrderListParser.AliOrder import AliOrder


fileURLs = ['..\SavedFiles\Page1.html',
            '..\SavedFiles\Page2.html',
            '..\SavedFiles\Page3.html',
            '..\SavedFiles\Page4.html',
            '..\SavedFiles\Page5.html',
            '..\SavedFiles\Page6.html',
            '..\SavedFiles\Page7.html',
            '..\SavedFiles\Page8.html',
            '..\SavedFiles\Page9.html',
            '..\SavedFiles\Page10.html']

ordersList = []

# create the objects and fill them with data
for fileURL in fileURLs:

    try:
        with open(fileURL,  encoding="utf8") as content_file:
            content = content_file.read()

        tree = html.fromstring(content)



        orders = tree.cssselect('tbody')
        for order in orders:

            myOrder = AliOrder()
            orderNum = order.find_class('info-body')

            myOrder.orderNum = orderNum[0].text_content()   #ordernum
            myOrder.datetime = aliTimeToTime( orderNum[1].text_content() )   # date time
            myOrder.seller = orderNum[2].text_content()   #Seller Name
            myOrder.orderAmount = float(order.find_class('amount-num')[0].text_content().split()[1]) #total amount of order

            items = order.find_class('order-body')
            for item in items:
                thisItem = AliItem()
                thisItem.seller = myOrder.seller
                thisItem.ordernum = myOrder.orderNum
                thisItem.datetime = myOrder.datetime
                thisItem.description = item.find_class('product-title')[0].text_content().strip().replace(",", " ")   # description
                itemPriceAndNumber = item.find_class('product-amount')[0].text_content().split()
                thisItem.itemPrice = float(itemPriceAndNumber[1])    #unit price
                thisItem.numUnits = int(itemPriceAndNumber[2].split('X')[1])    #amount ordered
                myOrder.itemList.append(thisItem)


            myOrder.setShipping()
            ordersList.append(myOrder)
    except:
        print("error! " + fileURL + " does not exist")





if len(ordersList) > 0:
    #filename = str('{0:%Y-%m-%d %H:%M:%S}'.format(datetime.now() + ".csv")
    with open('..\Output\csvfile.csv' , 'w',newline='') as csvfile:
        csvwriter = csv.writer(csvfile, delimiter = ',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

        for order in ordersList:
            for item in order.itemList:
                csvwriter.writerow(item.getAllItems())



