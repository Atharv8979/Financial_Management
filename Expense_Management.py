import csv
with open ("finance.csv", "w", newline='') as f:
    writer=csv.writer(f)
    writer.writerow(["Date","Type","Category","Amount"])
    def add_record():
        date=input("Enter date (DD-MM-YYYY): ")
        Type=input("Enter type(income/expense): ")
        category=input("Enter category: ")
        amount=int(input("Enter amount: "))

        with open("finance.csv", "a", newline='') as f:
            writer=csv.writer(f)
            writer.writerow([date,Type,category,amount])
            print("Record added successfully...")
            
    def view_record():
        with open("finance.csv", "r") as f:
            reader=csv.reader(f)
            for  row in reader:
                print(row)

    def report():
        income=0
        expense=0
        with open("finance.csv", "r") as f:
            reader=csv.reader(f)
            next(reader)
            for row in reader:
                amount=int(row[3])
                Type=row[1].lower()
                if Type=="income":
                    income+=amount
                elif Type=="expense":
                    expense+=amount
        balance= income-expense
        print("......REPORT......")
        print("Total income: ", income)
        print("Total expense: ", expense)
        print("Balance: ", balance)

while True:
    print("\n 1. Add record \n 2. View records \n 3. Report \n 4. Exit")
    ch=int(input("Enter choice: "))
    if ch==1:
        add_record()
    elif ch==2:
        view_record()
    elif ch==3:
        report()
    elif ch==4:
        break
    else:
        print("invalid choice...")
