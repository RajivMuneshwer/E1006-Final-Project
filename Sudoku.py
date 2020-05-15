"""
Created on Mon Apr 20 22:47:26 2020

@author: rajivmuneshwer
"""
import numpy as np
import random


def rncChecker (array, x, y): #checks the numbers that are not in the row and column
                                # for a given x and y position in the array
    
    return [j for j in [i for i in range(1,len(array)+1) if i not in array[x]] if j not in array[:,y]]

def Solver(array, x, y, remNums, orgi_array): #this can solve or generate a sudoku puzzle
    
    '''   
    this is my first attempt at making the algorithm
    I wasn't a big cheat and looked at a guide online
    
    
    #checks if y and x are out of bounds
    
    if y >= (len(array[0])):
        y = 0
        x  = x+1
    if x > (len(array)):
        return True
    
    print('{},{}'.format(x,y))
    
    
    #checks whether the remNums is empty but there are still zeros in the array
    if 0 not in array and len(remNums) == 0:
        print('True')
        return True
    
    
    #if the position was originally full then it is passed 
    if orgi_array[x][y] == -1:
        print('here1')
        print('{},{}'.format(x,y))
    #this checks if the orginal array had it as empty but this one didn't
        #that means that this was visited before so it must be checked by the same remaining numbers
        
    if orgi_array[x][y] == 0 and array[x][y]!= 0:
        if len(remNums) == 0:
            array[x][y] = 0
            return False
        array[x][y] = remNums.pop(random.randrange(len(remNums)))
        print('here2')
        print('{},{}'.format(x,y))
    #this checks if the original array had an empty place as well as this array has an empty spot  
    if orgi_array[x][y] == 0 and array[x][y]== 0:
        remNums = rncChecker(array,x,y)
        #checks whether the current position is that one that solves the array
        if len(remNums) == 0 and  0 in array:
            return False
        array[x][y] = remNums.pop(random.randrange(len(remNums)))
        print('here3')
        print('{},{}'.format(x,y))

    
    if (Solver(array,x,y+1,remNums, orgi_array) == True):
        print('here4')
        print('{},{}'.format(x,y))
        return True
    
    
    
    
    (x,y) = WalkBac(x,y,orgi_array)
    
    print('here5')
    print(remNums)
    Solver(array,x,y,remNums,orgi_array)
    
    '''
    #checks whether it is out of bounds for the y coordinate so goes to the next row if true
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
    


def Sudoku(array): #starts the puzzle
    
    copy_array = (array>0) * (-1)
    
    Solver(array,0,0,rncChecker(array,0,0),copy_array)
        
    return array
    
    
    
def Sudoku_tester(): 
    a = np.array(([1,0,3],[0,1,0],[0,0,1]))
    
    b = np.array(([0,4,0,1],[0,0,0,0],[2,0,0,0],[0,1,0,0]))

    b_2 = np.array(([0,0,0,3],[0,1,0,4],[4,2,3,1],[1,3,4,2]))
    
    b_3 = np.array(([0,0,0,9,0,0,0,0,0],[0,3,0,0,6,0,1,0,0],[7,0,6,5,8,0,9,0,0],[0,0,0,1,0,8,7,0,4],[1,0,0,0,5,0,0,0,9],[9,0,5,3,0,4,0,0,0],[0,0,1,0,4,5,8,0,3],[0,0,4,0,3,0,0,6,0],[0,0,0,0,0,9,0,0,0]))

def main(): #acutally generates the sudoku game for the user to play
    
    again = 'y'
    
    while again == 'y':
        size = 0
        while (size < 3) or (size > 9):
            size = int(input("Enter the size of the puzzle that you wish to create (3) to (9): "))
    
        difficulty = 0
        
        # I wasn't getting input for strings to work so numbers it is
        while (difficulty < 1) or (difficulty > 3):
            difficulty = int(input('what difficulty would you like: easy(1), medium(2) or hard(3)?'))
    
        #num_given is the number of places on the finished puzzle that are given
        num_given = 0
        
        if difficulty == 1:
            num_given = int((70/100)*(size*size))
    
        if difficulty == 2:
        
            num_given = int((45/100)*(size*size))
    
        if difficulty == 3:
        
            num_given = int((25/100)* (size*size))
    
        array = np.zeros((size, size))
        
        finish_a = np.zeros((size, size))
    
        finish_a = Sudoku(finish_a)
        
        print(num_given)
        
        x= 0
        y= 0
    
        for i in range(num_given):
            x = random.randrange(size)
            y = random.randrange(size)
            while array[x][y] != 0: #it picks random places to give the numbers 
                                    #but also goes again if there already is a number there
                x = random.randrange(size)
                y = random.randrange(size) 
            array[x][y] = finish_a[x][y]
    
        start_array = np.copy(array)
    
    
        print('\nRemember,\n the x coordinate is for the row\n and y coordinate is for the column')
        print(array)
        
        while not  np.array_equal(array, finish_a):
            
            
            
            print('\n')
        
            print('\n')
            a =0
            b = 0
            while (a < 1 or a > (size)) or (b < 1 or b > (size)):
                 a = int(input('from 1 to {} enter coordinates (x): '.format(size)))
                 b = int(input('from 1 to {} enter coordinates (y): '.format(size)))
                 if start_array[a-1][b-1] != 0:
                     a = 0
                     b = 0
                     print('You cannot pick that spot')
                     continue
            
        
            inp = 0
            while int(inp) < 1 or int(inp) > size:
                inp = int(input('what would you like to put there?: '))
                if not isinstance(inp,int):
                    inp = 0
                    continue
            array[a-1][b-1] = int(inp)
            print(array)
            print(start_array)
            cont = -1 
            while cont < 0 or cont > 3:
                cont  = int(input('To continue enter (0)\nTo restart the puzzle just enter (2)\n if you want to quit enter (3)\n'))
                if cont == 1:
                    cont = -1
            
            if cont == 2:
                print(start_array)
                array = np.copy(start_array)
                print(array)
                continue
            if cont == 3:
                break 
    
        if np.array_equal(array, finish_a):
            print('\nCongratulations on finishing that boring puzzle')
        else:
            print('Aww to bad that suck and give up: ')
            print(finish_a)
            print('\nThis was the solution')
    
        again = input("\nPlay again? (y/n) ")

        

if __name__ == "__main__":
    main()
    
        
        
    
    
    
    
    
   
    
    
    
    
                
        
            
        
        
    

