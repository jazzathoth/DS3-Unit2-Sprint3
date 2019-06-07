#! /usr/bin/env python

import sqlite3
import datetime


def get2_nwinfo():
    conn = sqlite3.connect('northwind_small.sqlite3')
    curs = conn.cursor()

    curs.execute("SELECT ProductName, UnitPrice FROM Product ORDER BY UnitPrice DESC LIMIT 10 ;")
    print("10 most expensive Products: ")
    print(curs.fetchall())

    emp_dates = curs.execute("SELECT (HireDate - BirthDate) FROM Employee ;").fetchall()
    
    ages = []

    for emp in emp_dates:
        ages.append(emp[0])

    print("Mean Hire Age: ", (sum(ages)/len(ages)))

def get3_nwinfo():
    conn = sqlite3.connect('northwind_small.sqlite3')
    curs = conn.cursor()

    curs.execute('SELECT Product.UnitPrice, Supplier.CompanyName \
                FROM Product \
                LEFT JOIN Supplier \
                ON Product.SupplierID = Supplier.Id \
                ORDER BY UnitPrice DESC LIMIT 10;')
    
    
    print('10 most expensive with Supplier Name: ')
    print(curs.fetchall())

    curs.execute('SELECT Category.CategoryName, COUNT(CategoryID) FROM Product LEFT JOIN Category on Product.CategoryID = Category.Id GROUP BY CategoryID;')
    print('Number of Products in each Category:')
    print(curs.fetchall())

    pass
