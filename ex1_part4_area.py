# -*- coding: utf-8 -*-
"""
Created on Wed Sep  1 17:23:02 2021

@author: Hilary
"""

# Exerise 1 Part 4 Finding Area under a curve#

# - start simple using formula y=0.5(x*x)
# - to run smaller increments and an amount on to the array incr_amt
#
# future improvment - print area to 3 decimal places

lower_lim = -4
upper_lim = 4
incr_amt=[1.0,0.5,0.25,0.1,0.05,0.01,0.005, 0.001,0.0005, 0.0001]

j=0
jmax=len(incr_amt)
print( j)
while j < jmax:
    incr=incr_amt[j]
    area=0
    i=lower_lim
    max_lim=upper_lim+incr
    
    while i<max_lim:
        width=incr
        height=0.5*((i)*(i))
        #print(i,"width ", width, " height ",height)
        area=area+(width*height)
        #print("area",area)
       
        i=i+incr
    print("final area ",area, " with ", incr ," increments") 
    j=j+1    




