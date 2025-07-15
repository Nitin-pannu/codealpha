import csv

stock_prices={
    "AAPL":180, 
    "TSLA":250, 
    "SMSNG":110,
    "GGL":195,
    "SNSX":120  
}

portfolio={}
print("Enter \'ok\' to stop\n")
while 1:
    stck_nam=input("Enter stock name:").upper()
    if(stck_nam=='OK'):
        break
    elif stck_nam not in stock_prices:
        print("Stock not found in the list :",stck_nam)
        continue
    else:
        try:
            qty=int(input("Enter quantity of stock:"))
            if qty<0:
                raise ValueError
            portfolio[stck_nam]=portfolio.get(stck_nam,0) + qty
        except ValueError:
            print("Quantity can not be less than 0")

ttl=0
print("\n --Your stock summary--")
print("|----------------------|")
for stk,qty in portfolio.items():
    price=stock_prices[stk]
    ttl+=(price*qty)
    print(f"| {stk}: {price} X {qty} = {price*qty}  |")
print(f"Total investment: {ttl}\n")

choice=input("Do you want to save these detail(yes/no):").upper()
if choice=="YES":
    typ=input("Enter the file type(txt/csv):").strip().lower()
    if typ=="txt":
        with open("abc.txt","w") as f:
            for stk,qty in portfolio.items():
                  price=stock_prices[stk]
                  f.write(f"{stk}: {price} X {qty} = {price*qty}  \n")
            f.write(f"\nTotal investment: {ttl}")
        print("Data has been saved to abc.txt")
    
    elif typ=="csv":
        with open("abc.csv","w",newline='') as f:
            obj=csv.writer(f)
            obj.writerow(["Stock","Price","Quantity","Total price"])
            for stk,qty in portfolio.items():
                obj.writerow([stk,stock_prices[stk],qty,stock_prices[stk]*qty])
            obj.writerow(["Total","","",ttl])
        print("Saved to abc.csv")

    else:
        print("Invalid file type.Unable to save")
