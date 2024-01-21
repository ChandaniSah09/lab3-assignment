# 5) WAP that input cost price(cp) and selling price(sp) and determine whether there is profit or loss.

cp=float(input("enter the cost price :"))
sp=float(input("enter the selling price :"))
if sp>cp:
    print("there is profit by",sp-cp)
else:
    print ("there is loss by",cp-sp) 