from datetime import datetime


name=input("enter your name")

lists='''
Rice   Rs 20/kg
Sugar  Rs 30/kg
Salt   Rs 20/kg
Oil    Rs 30/liter
Maggi  Rs 50/kg
'''

price=0
pricelist=[]
totalprice=0
Finalfinalprice=0
ilist=[]
qlist=[]
plist=[]

items={'Rice':1000,
'Sugar':200,'Salt':23,
'Oil':300,'Maggi':40}

option=int(input("for list of items press 1"))
if option==1:
    print(lists)
for i in range(len(items)):
    inp1=int(input("if you to buy press 1 or 2 for exit:"))
    if inp1==2:
        break
    if inp1==1:
        items=input("enter your items:")
        quantity=int(input('enter your quantity:'))
        if item in items.keys():
            price=quantity*(item[items])
            pricelist.append((item,quantity,items,price))
            totalprice+=price
            ilist.append(item)
            qlist.append(quantity)
            plist.append(price)
            gst=(totlaprice*5)/100
            finalamount=gst+totalprice
        else:
            print("sorry you entered item is not available")
    else:
        print("you entered wrong number")

    inp=input("can i bill the items yes or no:")
    if inp=='yes':
        pass
        if finalamount!=0:
            print(25*"=","Meghana supermarket",25*"=")
            print(28*" ","wanaparthy")
            print("Name:",name,30*" ","Date:",datetime.now())
            print(75*"-")
            print("sno",8*" ",'items',8*" ",'Quantity',3*" ",'price')
           
           
            for i in range(len(pricelist)):
                print(i,8*' ',8*' ',ilist[i],3*' ',qlist[i],plist[i])
                
            print(75*"-")
            print(50*" ",'TotalAmount:','Rs',totalprice)
            print("gst amount",50*" ",'Rs',gst)
            print(75*"-")
            print(50*" ",'finalAmount:','Rs',finalamount)
            print(75*"-")
            print(50*" ","Thanks for visiting")
            print(7*"-")

    
                  


