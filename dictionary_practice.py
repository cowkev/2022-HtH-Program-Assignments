Acceptance = {"Irvine" : "29.9 percent", "Los Angeles" : "14.3 percent", "San Diego" : "36.6 percent" }
one = "Irvine"
#print ("UCI acceeptance is: " + str(Acceptance.get ("Irvine")))
#print ("UCLA acceptance is: " + str(Acceptance.get ("Los Angeles")))
#print ("UCSD acceptance is: " + str(Acceptance.get ("San Diego")))

perentage_irvine = Acceptance["Irvine"]
print(perentage_irvine)

Sneakers= {"Jordan 13": 1, "Yeezy": 8, "Foamposite": 10, "Air Max": 5, "SB Dunk": 20}
Jordan_Stock = Sneakers["Jordan 13"]
print(Jordan_Stock)

Sneakers["SB Dunk"] -= 2
print("\nCustomer came to purchase 2 pairs of SB Dunks")
print(Sneakers["SB Dunk"])

Sneakers["Yeezy"] -=1
print("\nCustomer returned a pair of Yeezys")
print(Sneakers["Yeezy"])

Sneakers["Air Max"] +=7
Sneakers["Foamposite"] +=7
Sneakers["Jordan 13"] +=7
Sneakers["SB Dunk"] +=7
Sneakers["Yeezy"] +=7
print("\nNew shipment. All stock increased by 7")
print(Sneakers)

Sneakers["Air Max"] -=3
Sneakers["Foamposite"] -=3
Sneakers["Jordan 13"] -=3
Sneakers["SB Dunk"] -=3
Sneakers["Yeezy"] -=3
print("\nStore Sale, all stock decreased by 3")
print(Sneakers)

Sneakers.update({"NMD": 6})
Sneakers.update({"Vans": 12})
Sneakers.update({"Uggs": 4})
print("\nAdding shoes with update( ) method")
print(Sneakers)

del Sneakers["Uggs"]
del Sneakers["NMD"]
print("\nDeleted NMD and Uggs")
print(Sneakers)