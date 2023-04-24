import sqlite3
import datetime

conn = sqlite3.connect('expenses.db')
cur = conn.cursor()

while True:
    print('Select an option:')
    print('1. Log a new expense')
    print('2. View expenses summary')
    
    choice = int(input())
    
    if choice == 1:
        date = input('Enter the data of expense (yyyy-mm-dd):')
        description = input('Enter the expense details:')
        
        cur.execute("SELECT DISTINCT category FROM expenses")
        
        categories= cur.fetchall()
        
        print('Select category by choosing the appropriate number: ')
        for idx, categories  in enumerate(categories):
            print(f'{idx+1}.{category[0]}')
        print(f'{len(categories) + 1 }. Create a new category ')
        
        category_choice = int(input())
        
        if category_choice == len(categories) + 1:
            category = input('Enter the name of new category: ')
        else:
            category = categories[category_choice - 1][0]
        price = input('Enter the cost of the expense: ')
        
        cur.execute("INSERT INTO expenses (Date, description, category, price) values(?,?,?,?)", (date,description,category,price))
        
        conn.commit()
    elif choice ==2:
        print('Select an option:')
        print('1: View all expenses')
        print('2. View monthly expenses by category')
        
        view_choice = int(input())
        
        if view_choice == 1:
            cur.execute("SELECT * FROM expenses")
            expenses = cur.fetchall()
            for expense in expenses:
                print(expense)
        elif view_choice == 2:
            month = input('Enter the month (MM): ')
            year = input('Enter the year (YYYY): ')
            cur.execute("SELECT category, SUM(price) FROM expenses WHERE strtime('%m',Date)= ? AND strtime('%Y',Date)= ? GROUP BY category",(month, year))
            
            expenses = cur.fetchall()
            for expense in expenses:
                print(f"Category: {expense[0]}, Total: {expense[1]}")
            
        else:
            exit()
    else:
        exit()
    repeat = input('Would you like to do something else (y/n)?\n')
    if repeat.lower != 'y':
        break
    
conn.close()
