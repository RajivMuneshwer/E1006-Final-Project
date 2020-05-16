# -*- coding: utf-8 -*-
"""
Created on Tue Apr 21 14:57:17 2020

@author: etill
"""

#import statements
from flask import Flask, render_template
import random
import numpy as np
import pandas as pd
from urllib.request import urlopen
from bs4 import BeautifulSoup
import re



#Flask app variable
app = Flask(__name__)



#static route
@app.route("/")
def homePage():
    return render_template('index.html')

@app.route("/1006")
def Second_page():
    return render_template('secPage.html')

@app.route("/420")
def Third_page():
    return render_template('thirdPage.html')

@app.route("/123")
def Sudoku_page():
    size  = random.randint(3,10)
    
    array = np.zeros((size,size))
    
    finished_array = np.copy(array)
    
    sudoku(finished_array)
    
    num_given = int((40/100)*(size*size))
    
    x= 0
    y= 0
    
    for i in range(num_given):
        x = random.randrange(size)
        y = random.randrange(size)
        while array[x][y] != 0: #it picks random places to give the numbers 
                                    #but also goes again if there already is a number there
            x = random.randrange(size)
            y = random.randrange(size) 
        array[x][y] = finished_array[x][y]
    
    str_array = np.zeros((size,size), dtype = str)
    
    for i in range(size):
        for j in range(size):
            str_array[i][j] = str(array[i][j])
            if str_array[i][j] == '0':
                str_array[i][j] = ""
    
    df = pd.DataFrame(str_array) #converts the sudoku array in to a panda's dataframe 
    
    return df.to_html(col_space = 20, header = False, index = False, index_names = False, justify = 'center', show_dimensions = True)


'''
I cannot get this to work 


@app.route("/930")
def sudokuFinder():
    html = urlopen('https://nine.websudoku.com/?')
    bs = BeautifulSoup(html, 'html.parser')
    table = bs.find(name = "table", attrs = {"id":"puzzle_grid"}) 
    rows = table.find_all("tr")
    l = []
    for tr in rows:
        td = tr.find_all('td')
        row = [tr.text for tr in td]
        l.append(row)
        print (l)
    
    return pd.DataFrame(l, columns=["A", "B","C","D","E","F","G","H", "I"])

'''

    

def rncChecker (array, x, y):
    return [j for j in [i for i in range(1,len(array)+1) if i not in array[x]] if j not in array[:,y]]

def Solver(array, x, y, remNums, orgi_array): #sudoku solver/ generator
    if y >= (len(array[0])):
        y = 0
        x  = x+1
    if x > (len(array)):
        return True
    
    if 0 not in array and len(remNums) == 0:
        return True
    
    if orgi_array[x][y] == 0 and array[x][y] == 0:
        remNums = rncChecker(array,x,y)
    
    if orgi_array[x][y] != 0:
        if (Solver(array,x,y+1,remNums,orgi_array) == True):
            return True
        else:
            return False
    else:
        while len(remNums) > 0:
            array[x][y] =  remNums.pop(random.randrange(len(remNums)))
            if (Solver(array,x,y+1,remNums,orgi_array) == True):
                return True
        array[x][y] = 0
        return False

def sudoku(array):
    
    copy_array = (array>0) * (-1)
    
    Solver(array,0,0,rncChecker(array,0,0),copy_array)
        
    return array

    

#start the server
if __name__ == "__main__":
    app.run()