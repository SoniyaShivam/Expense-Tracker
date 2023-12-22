import os
import csv
import datetime
import matplotlib.pyplot as plt


def add_money():
    deposit=int(input("enter the amount to deposit :"))
    global income
    income+=deposit



def enter_data():
    if not os.path.exists("data.csv"):
        with open("data.csv",'w',newline="") as file :
            writer =csv.writer(file)
            writer.writerow(['date','lable','expense'])


    if os.path.exists('data.csv'):
        read_file_list=list(csv.reader(open("data.csv",'r')))
        if len(read_file_list)==0:
            with open('data.csv','a',newline="")as file:
                writer=csv.writer(file)
                writer.writerow(['date','lable','expense'])

    date=int(input("enter the date :"))
    lable=input("lable your expense:")
    expense = int(input("expenditure :"))

    with open(data.csv,'a',newline="")as file:
        writer=csv.writer(file)
        writer.writerow([date,lable,expense])


def choices():
    print("0: add money to account ")
    print("1: enter the data ")
    print("2: insights of data ")
    print("3: graphical view of data")
    print("4: range graphical view ")

    try:
        choice=int(input())
    except:
        print("!Enter a valid value..")

    return choice

def data_insights():
    try:

        with open('data.csv','r') as file:
            read =csv.reader(file)
            read_list=list(read)
            print(read_list)
            total_expense=0

            if (income<=0):
                print("! you don't have any income yet . add some money first")
                return

            for each in read_list[1:]:
                total_expense+=int(each[2])

            balance=income-total_expense
            print("account balance :",balance)
            print("total expenditure this month :",total_expense)
            pecent=(total_expense/income*100)
            print("expenditure is {:.4f}% of income in {} days of this month .\n".format(percent,len(read_list)-1))

    except Exception as e :
        print("it looks like you don't have enough data yet ",e)



def data_visualization():
    try:
        with open('data.csv','r') as file :
            dates=[]
            expense=[]
            read=csv.reader(file)
            file_list=list(read)
            for each in file_list[1:]:
                dates.append(int(each[0]))
                expense.append(int(each[2]))

            today =datetime.date.today()

            plt.plot(dates,expense,lable='per month')
            plt.title("--my expenditure--")
            plt.xlable(f"date{today.month} {today.year}")
            plt.ylable("expense")
            plt.xticks(dates)
            plt.legend()
            plt.show()

    except Exception :
        print("it looks like you don't have enough data")


def limited_visualization(start_date,stop_date):
    try:
        with open('data.csv','r') as file:
            dates=[]
            expense=[]
            read=csv.reader(file)
            file_list(read)
            #print(len(file_list))
            if stop_date>(len(file_list)-1):
                print("!!stop date out of range ")

                for each in file_list[start_date:stop_date+1]:
                    dates.append(int(each[0]))
                    expense.append(int(each[2]))
                total_expenses=sum(list(map(int,expense)))
                total_expense/income*100
                print(f"total expenditure inthis period is {total_expense} which is {percent:.4f}% of the monthly income")
                today=datetime.date.today()
                plt.plot(dates,expense,lable='per day range')
                plt.title("range of the days expenditure")
                plt.xlable(f"date{today.month} {today.year}")
                plt.ylable("expense")
                plt.legend()
                plt.show()


    except Exception:
        print("it looks like you don't have enough data")


if __name__=="__main__":
    income=0

    print("select the choice::")
    running=True
    while running :
        choice= choices()
        if choice==0:
            add_money()
        elif choice ==1:
            enter_data()
        elif choice==2:
            data_insights()
        elif choice==3:
            data_visualization()
        elif choice==4:
            print("specify")
            start=int(input("start date :"))
            stop=int(input("stop date:"))
            limited_visualization(start,stop)
        else:
            print("!invalid choice")

        ask=input("do you want to continue :(y/n)")
        if ask=='n' or ask=='N':
            running = False

from tkinter import*
window=Tk()
window.title("EXPENSE TRACKER ")
label=Label(window,text='HELLO')
label.pack()
window.mainloop()
