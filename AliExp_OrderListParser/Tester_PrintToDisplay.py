#
#   main parser:
#
#

from lxml import html



fileURL = '..\SavedFiles\Page10.html'



with open(fileURL,  encoding="utf8") as content_file:
    content = content_file.read()

tree = html.fromstring(content)

#tree = etree.parse(fileURL)

orders = tree.cssselect('tbody')
print("orders are: " )
print(orders)
print('\n')


for order in orders:

    ordernum = order.find_class('info-body')
    print(ordernum[0].text_content())   #ordernum
    print(ordernum[1].text_content())   # date time
    print(ordernum[2].text_content())   #Seller Name
    print(order.find_class('amount-num')[0].text_content().split()[1]) #total amount of order

    items = order.find_class('order-body')
    for item in items:
        print(item.find_class('product-title')[0].text_content())   # description
        itemPriceAndNumber = item.find_class('product-amount')[0].text_content().split()
        print(itemPriceAndNumber[1])    #unit price
        print(itemPriceAndNumber[2].split('X')[1])    #amount ordered


#print (content)






