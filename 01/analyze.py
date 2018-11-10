import json
import csv

def load_csv(filename):
    rows = []
    #...
    # ...
    return rows
    
def load_json(filename):
    rows = []
    #...
    return rows

def analyze_sales_by_month():
    """выводит сумму проданных товаров по месяцам за весь период, """
    #....
    for sale in sales:
        print(sale['year'], sale['month'], sale['summa'])
    
def best_3_persons():
    """выводит 3 имени лучших покупателя и сумму их покупок, от большего к меньшему"""
    #....
    for p in persons:
        print(p['persona'], p['summ_price'])    
        
def worst_3_products():
    """выводит 3 худших по продажам товаровб от меньшего к большему"""
    #....
    for p in persons:
        print(p['persona'], p['summ_price'])  

persons = load_csv('persons.csv')
products = load_csv('products.csv')
sales = load_csv('sales.csv')

analyze_sales_by_month()
best_3_persons()
worst_3_products()

persons = load_json('persons.json')
products = load_json('products.json')
sales = load_json('sales.json')

analyze_sales_by_month()
best_3_persons()
worst_3_products()
