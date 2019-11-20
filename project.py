import server
def menu():
    def menu1():
        n=int(input("Enter your choice : "))
        if n==1:
            veg()
        elif n==2 :
            nonveg()
        elif n==3 :
            drinks()
        elif n==4 :
            icecreams()
        else :
            print("Enter the correct choice ")
            menu1()
    print("1.Veg \n 2.Non-veg \n 3.Drinks \n 4.IceCreams ")
    menu1()
def veg():
    def menu2():
        y=int(input("Enter your choice : "))
        if y==1 :
            starters()
        elif y==2 :
            biryani() 
        elif y==3 :
            soups()
        elif y==0:
            menu()
        else :
            print("Enter correct choice ")
            menu2()
    print("****************************VEG_MENU********************************* \n 1.STARTERS \n 2.BIRYANI PACKS \n 3.SOUPS \n PRESS '*' TO GO BACK TO MAIN MENU ")
    menu2()
def nonveg():
    def menu3():
        n8=int(input("Enter your choice : "))
        if n8==1 :
            nonstarters()
        elif n8==2 :
            nonbiryani() 
        elif n8==3 :
            nonsoups()
        elif n8==0:
            menu()
        else :
            print("enter correct choice ")
            menu3()
    print("********************************NON-VEG_MENU************************** \n 1.STARTERS \n 2.BIRYANI PACKS \n 3.SOUPS \n PRESS '*' TO GO BACK TO MAIN MENU ")
    menu3()
def drinks():
    def checck():
        def last66():
            bg8=int(input(""))
            if bg8==1 :
                checck()
            elif bg8==0 :
                menu()
            elif bg8==5 :
                checko()
            else :
                print("Enter correct choice ")
                last66()
        dri={1:'coke',2:'thumbs.up',3:'maaza',4:'frooti',5:'mountain.dew',6:'mirinda',7:'sprite'}
        n71=int(input("Enter your choice : "))
        while(n71>0) :
            rem=n71%10
            if(rem>7):
                print(rem,"is not available ")
                n71=n71//10
            else:
                lis.append(dri[rem])
                n71=n71//10
        print("items added to cart ")
        print("want to add some more items ? \n if yes enter '1' \n press '0' to bo back to your menu \n press '5' for check out ")
        last66()
    print("************************************DRINKS************************************\n 1.coke(1)   35 \n 2.thumbs up(2)      40 \n 3.maaza(3)       35 \n 4.frooti(4)      40 \n 5.Mountain Dew(5)        45 \n 6.Mirinda(6)     40 \n 7.Sprite(7)      40")
    checck()
def icecreams():
    def checkk() :
        def last65():
            bg69=int(input(""))
            if bg69==1 :
                checkk()
            elif bg69==0 :
                menu()
            elif bg69==5 :
                checko()
            else :
                print("Enter correct choice ")
                last65()
        ice={1:'vanilla',2:'butter.scotch',3:'strawberry',4:'chocolate',5:'pista'}
        n70=int(input("Enter your choice : "))
        while(n70>0) :
            rem=n70%10
            if(rem>5):
                print(rem,"is not available ")
                n70=n70//10
            else:
                lis.append(ice[rem])
                n70=n70//10  
        print("items added to cart ")
        print("want to add some more items ? \n if yes enter '1' \n press '0' to bo back to your menu \n press '5' for check out ")
        last65()
    print("************************************ICE_CREAMS************************************\n 1.vanilla(8)       80 \n 2.butter scotch(9)       80 \n 3.strawberry(10)      80 \n 4.chocolate(11)       120 \n 5.pista(12)      200")
    checkk()
def starters() :
    def check() :
        def last6():
            bg=int(input(""))
            if bg==1 :
                check()
            elif bg==0 :
                menu()
            elif bg==5 :
                checko()
            else :
                print("Enter correct choice ")
                last6()
        veg={1:'aloo65',2:'veg.manchuria',3:'veg65',4:'gobi65',5:'veg.spring.rolls',6:'chilli.paneer.dry',7:'paneer65'}
        n7=int(input("Enter your choice : "))
        while(n7>0):
            rem=n7%10
            if(rem>7):
                print(rem,"is not available ")
                n7=n7//10
            else:
                lis.append(veg[rem])
                n7=n7//10
        print("items added to cart ")
        print("want to add some more items ? \n if yes enter '1' \n press '0' to bo back to your menu \n press '5' for check out ")
        last6()
    print("************************************STARTERS_VEG************************************\n 1.aloo65(35)   189 \n 2.veg.manchuria(36)  189 \n 3.veg.65(37)  189 \n 4.gobi65(38)  189 \n 5.veg.spring rolls(39)  189 \n 6.paneer65(40)  189 \n 7.chilli paneer dry(41)  189")
    check()
def nonstarters() :
    def check1():
        def last5():
            bg1=int(input(""))
            if bg1==1 :
                check1()
            elif bg1==0 :
                menu()
            elif bg1==5 :
                checko()
            else :
                print("enter correct choice ")
                last5()
        nonveg={1:'chicken65',2:'chicken.manchuria',3:'egg65',4:'chilli.chicken',5:'chicken.spring.rolls',6:'chillifish',7:'chilli.chicken.dry'}
        n11=int(input("Enter ypur choice : "))
        while(n11>0) :
            rem=n11%10
            if(rem>7):
                print(rem,"is not available ")
                n11=n11//10
            else:
                lis.append(nonveg[rem])
                n11=n11//10
        print("items added to cart ")
        print("want to add some more items ? \n if yes enter '1' \n press '0' to bo back to your menu \n press '5' for check out ")     
        last5()
    print("**********************************STARTERS_NON-VEG***********************************\n 1.chicken65(28)   189 \n 2.chicken.manchuria(29)  189 \n 3.egg65(30)  189 \n 4.chilli chicken(31)  189 \n 5.chicken.spring rolls(32)  189 \n 6.chillifish(33)  189 \n 7.chilli chicken dry(34)  189")
    check1()
def biryani() :
    def check2():
        def last4():
            bg2=int(input(""))
            if bg2==1 :
                check2()
            elif bg2==0 :
                menu()
            elif bg2==5 :
                checko()
            else :
                print("enter correct choice ")
                last4()
        veg1={1:'veg.fried.rice',2:'corn.fried.rice',3:'plain.rice',4:'paneer.biryani'}
        n2=int(input("Enter ypur choice : "))
        while(n2>0) :
            rem=n2%10
            if(rem>4):
                print(rem,"is not available ")
                n2=n2//10
            else:
                lis.append(veg1[rem])
                n2=n2//10
        print("items added to cart ")
        print("want to add some more items ? \n if yes enter '1' \n press '0' to bo back to your menu \n press '5' for check out ")
        last4()
    print("****************************************BIRYANI_VEG***************************************\n 1.veg.fried rice(24)       140 \n 2.corn fried rice(25)        140 \n 3.plain rice(26)     100 \n 4.paneer biryani(27)     200")  
    check2()
def nonbiryani() :
    def chech3():
        def last1():
            bg3=int(input(""))
            if bg3==1 :
                chech3()
            elif bg3==0 :
                menu()
            elif bg3==5 :
                checko()
            else :
                print("enter correct choice ")
                last1()
        nonveg1={1:'chicken.biryani',2:'mutton.biryani',3:'egg.fried.rice',4:'fish.fried.rice'}
        n22=int(input("Enter ypur choice : "))
        while(n22>0) :
            rem=n22%10
            if(rem>4):
                print(rem,"is not available ")
                n22=n22//10
            else:
                lis.append(nonveg1[rem])
                n22=n22//10
        print("items added to cart ")
        print("want to add some more items ? \n if yes enter '1' \n press '0' to bo back to your menu \n press '5' for check out ")
        last1()
    print("**************************************BIRYANI_NON_VEG********************************************\n 1.chicken biryani(21)      140 \n 2.mutton biryani(22)       140 \n 3.egg fried rice(50)    100 \n 4.fish fried rice(23)     200")
    chech3()
def soups() :
    def check4():
        def last():
            bg4=int(input(""))
            if bg4==1 :
                check4()
            elif bg4==0 :
                menu()
            elif bg4==5 :
                checko()
            else :
                print("enter correct choice ")
                last()
        veg2={1:'veg.mancho.soup',2:'clear.soup',3:'sweet.corn.soup',4:'mushroom.soup'}
        n0=int(input("Enter your choice : "))
        while(n0>0):
            rem=n0%10
            if(rem>7):
                print(rem,"is not available ")
                n0=n0//10
            else:
                lis.append(veg2[rem])
                n0=n0//10
        print("items added to cart ")
        print("want to add some more items ? \n if yes enter '1' \n press '0' to bo back to your menu \n press '5' for check out ")
        last()
    print("*****************************************SOUPS_VEG********************************************\n 1.veg mancho soup(19)     80 \n 2.clear soup(45)      100\n 3.veg.sweet corn soup(20)     80\n 4.mushroom soup(21)        89")
    check4()
def nonsoups() :
    def check5() :
        def last2():
            bg5=int(input(""))
            if bg5==1 :
                check5()
            elif bg5==0 :
                menu()
            elif bg5==5 :
                checko()
            else :
                print("enter correct choice ")
                last2()
        nonveg2={1:'chi.mancho.soup',2:'chi.clear.soup',3:'chi.sweet.corn.soup',4:'chi.lemon.soup'}
        n00=int(input("Enter your choice : "))
        while(n00>0) :
            rem=n00%10
            if(rem>4):
                print(rem,"is not available ")
                n00=n00//10
            else:
                lis.append(nonveg2[rem])
                n00=n00//10 
        print("items added to cart ")
        print("want to add some more items ? \n if yes enter '1' \n press '0' to bo back to your menu \n press '5' for check out")
        last2()
    print("***************************************SOUPS_NON_VEG****************************************\n 1.chi.mancho soup(13)     80 \n 2.chi.clear soup(14)      100\n 3.chi.sweet corn soup(15)     80\n 4.chi.lemon soup(44)        89")
    check5()
def checko() :
    def bill() :
        def remov():
            result2={1:'coke',2:'thumbs.up',3:'maaza',4:'frooti',5:'mountain.dew',6:'mirinda',7:'sprite',8:'vanilla',9:'butter.scotch',10:'strawberry',11:'chocolate',12:'pista',13:'chi.mancho.soup',14:'chi.clear.soup',15:'chi.sweet.corn.soup',15:'chi.lemon.soup',44:'veg.mancho.soup',19:'clear.soup',45:'veg.sweet.corn.soup',20:'mushroom.soup',21:'chicken.biryani',22:'mutton.biryani',50:'egg.fried.rice',23:'fish.fried.rice',24:'veg.fried.rice',25:'corn.fried.rice',26:'plain.rice',27:'paneer.biryani',28:'chicken65',29:'chicken.manchuria',30:'egg65',31:'chilli.chicken',32:'chicken.spring.rolls',33:'chillifish',34:'chilli.chicken.dry',35:'aloo65',36:'veg.manchuria',37:'veg65',38:'gobi65',39:'veg.spring.rolls',40:'paneer65',41:'chilli.paneer.dry'}
            for i in lis :
                print(i)
	    
            l=input("enter comma seperated values to remove : ")
            lis.remove(result2[l])
        h=int(input(""))
        if h==4 :
            print("Sending order.... please wait")
        elif h==2 :
            remov()   
            checko()
        else :
            print("enter correct choice ")
            bill()
    cost=0
    result1={'coke':35,'thumbs.up':35,'maaza':40,'frooti':45,'mountain.dew':50,'mirinda':35,'sprite':40,'vanilla':80,'butter.scotch':80,'strawberry':80,'chocolate':120,'pista':200,'chi.mancho.soup':80,'chi.clear.soup':100,'chi.sweet.corn.soup':80,'chi.lemon.soup':89,'veg.mancho.soup':80,'clear.soup':100,'sweet.corn.soup':80,'mushroom.soup':89,'chicken.biryani':140,'mutton.biryani':140,'egg.fried.rice':100,'fish.fried.rice':200,'veg.fried.rice':140,'corn.fried.rice':140,'plain.rice':100,'paneer.biryani':200,'chicken65':189,'chicken.manchuria':189,'egg65':189,'chilli.chicken':189,'chicken.spring.rolls':189,'chillifish':189,'chilli.chicken.dry':189,'aloo65':189,'veg.manchuria':189,'veg65':189,'gobi65':189,'veg.spring.rolls':189,'paneer65':189,'chilli.paneer.dry':189}
    for i in lis :
        print("cost of ",i,"is ",result1[i])
        cost+=result1[i]
    print(cost)
    print("to confirm press '4' else to remove items press '2' ")
    bill()
        
lis=[]
menu()
name=input("Enter your name : ")
fp=open('order.txt','w')
for i in lis:
    fp.write(i+","+name+"\n")
fp.close()
server.send('order.txt')

