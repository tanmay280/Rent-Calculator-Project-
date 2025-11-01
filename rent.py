#inputs we need from user
#Total rent
#Total food ordered 
#Electricity units spend
#Charge per unit
#Number of persons living in room
##Output
#Total amount you have to pay is


rent=int(input("Enter your /roomhostel/flat rent="))
food=int(input("Enter amount of food ordered="))
electricty=int(input("enetr electricity units spend="))
charge=int(input("Enetr Charge per unit in your area="))
persons=int(input("Enter Number of Persons living in Flat/Room/Hostel"))

total_bill=electricty*charge

output=(food+rent+total_bill)//persons

print("Each persons will pay =",output)
