
import os
import time
import random
from colorama import Fore, Back, Style
from copy import copy, deepcopy

'''
some kind of competition like this
x x x  y
 x x  y y
x x xy y y


'''


'''

    Oliver Shapez. A celular automata in the vein of Conways game of life

    Dedicated to John Conway.

    Copyright (C) 2021 Adam Oliver


    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.


    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the

    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <https://www.gnu.org/licenses/>.

'''

hei = 22
wid = 80


print('#')
print(Fore.RED + '%', end='') #
#print(Fore.LIGHTGREEN + '%') #
print(Fore.YELLOW + '*') #
print(Fore.GREEN + '&') #
print(Fore.BLUE + '$') #
#quit()

global grid
global grid
grid = [[0 for i in range(wid)] for j in range(hei)] # 80 20 
grid = [[0 for i in range(wid)] for j in range(hei)] # 80 20 

# set all grid[x][y] to 6

county = 0
count = 0
for i in grid:
  for j in i:
    grid[county][count] = '6'
    
    count += 1
  count = 0 
  county += 1
# done

# set a few example variables (to be removed)

grid[0][1] = '1'
grid[0][2] = '2'
grid[0][3] = '3'
grid[0][4] = '4'
grid[0][9] = '5'
grid[1][7] = '6'


# prints the grid
def print_grid():

  #grid = deepcopy(grid)

  count = 0
  for i in grid:
    for e in i:

      if(e=='1'):print(Fore.WHITE + '#', end='' ) # end='' removes newline
      if(e=='2'):print(Fore.RED + '%', end='' ) # 
      if(e=='3'):print(Fore.YELLOW + '*', end='' ) # 
      if(e=='4'):print(Fore.GREEN + '&', end='' ) # 
      if(e=='5'):print(Fore.BLUE + '$', end='' ) # 
      if(e=='6'):print(Fore.BLUE + ' ', end='' ) # 

      if(e=='7'):print(Fore.BLUE + 'i', end='' ) # 

      if(e=='10'):print(Fore.WHITE + 'a', end='' ) # 
      if(e=='11'):print(Fore.RED + 'b', end='' ) # 
      if(e=='12'):print(Fore.YELLOW + 'c', end='' ) # 
      if(e=='13'):print(Fore.GREEN + 'd', end='' ) # 

      if(e=='a'):print(Fore.WHITE + 'a', end='' ) # 
      
      count += 1
      if(count == wid): print(''); count = 0


# this just stops list index out of range error
def numberz_h(thenum):

  if(thenum >= wid):
    return wid - 1
  else:
    return thenum
    
def numberz(thenum):

  if(thenum >= hei):
    return hei - 1
  else:
    return thenum

# a quick fix 
def reset():  

  global grid

  count = 0
  for i in grid:
    county = 0
    for j in i:

      if( j == '10' ): # 
        grid[count][county] = '1' # up
      if( j == '11' ): # 
        grid[count][county] = '2' # up
      if( j == '12' ): # 
        grid[count][county] = '3' # up
      if( j == '13' ): # 
        grid[count][county] = '4' # up
        
      county += 1
      
    count += 1


def expand():
  
  global grid

  count = 0
  for i in grid:
    county = 0
    for j in i:

      if( j == '1' ): # 
        #print('# detected')
        #print('x and y of # is: ...' + str(county) + ' ' + str(count))
        grid[count-1][county] = '10' # left
        grid[ numberz(count+1) ][county] = '10' # right

        grid[ count-1 ][county-1] = '10' # up left
        grid[ numberz(count+1) ][ numberz_h(county+1) ] = '10' # down right
        

      if( j == '2' ): # 
        grid[count][county-1] = '11' # up
        grid[count][ numberz_h(county+1) ] = '11' # down
        grid[count-1][county] = '11' # left
        grid[ numberz(count+1) ][county] = '11' # right


      if( j == '3' ): # 
        grid[ count-1 ][county-1] = '12' # up left
        grid[ numberz(count+1) ][ numberz_h(county+1) ] = '12' # down right
        grid[ numberz(count+1) ][ county-1 ] = '12' # down left
        grid[ count-1 ][ numberz_h(county+1) ] = '12' # up right
                

      if( j == '4' ): # 
        grid[count][county-1] = '13' # up
        grid[count][ numberz_h(county+1) ] = '13' # down

        grid[ count-1 ][county-1] = '13' # up left
        grid[ numberz(count+1) ][ numberz_h(county+1) ] = '13' # down right
        

      county += 1
      
    count += 1

###
#
#


# just grid
def add_a_cell():

  print('')
  print('')
  
  # change range(1) to change number of new characters
  
  for i in range(5):
    # finds a random place in the grid, adds a cell
    #print(random.randint(1,6))
    x = random.randint(0,hei-1)
    y = random.randint(0,wid-1)

    if( grid[x][y] != 6 ):
      grid[x][y] = str(random.randint(1,5))

    

add_a_cell()

print_grid()

while True:
  expand()
  reset()

  time.sleep(.1)

  print_grid()

quit()





