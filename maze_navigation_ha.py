#
# Hilary - recursive program to find way through maze - 
#
#
# Function to display resulting matrix with the path through it, P=Path
# Future improvement - see how to plot it useing matplotlib? or something else?

def maze_so_far(mlength,mwidth):
  for mi in range (0,mlength):
    #print( mazearray[mi])
    for mj in range (0,mwidth):
      print (mazearray[mi][mj], end='')
      if mj == mwidth-1 :
        print (' ')
      
  return      
    

#
#Recursive Function to find path thru maze
#future improvement - use special character to see path more easily
#
def find_path(x, y, dim): 
#  1. 	if (x,y outside maze) return false 

  if x<=0 or x>=dim or y<=0 or y>=dim:
   
    #print("limit ", x, y)
    return False
#  2. 	if (x,y is goal) return true 
  if mazearray[x][y] == "G":
    
    return True
#  3. 	if (x,y not open) return false 
  if mazearray[x][y] == "1":
    return False
#  4. 	mark x,y as part of solution path 
  if mazearray[x][y] =="P":
     return False
  else:
    mazearray[x][y]="P"
    #print ("path ", x,y, dim)
#  5. 	if (FIND-PATH(North WESTof x,y) == true) return true
   
  if find_path(x,y-1,dim) ==True :
    #print("West")
    return True
#  6. 	if (FIND-PATH(EastSOUTH of x,y) == true) return true 
  if find_path(x+1, y, dim) ==True :
    #print("South")
    return True
#  7. 	if (FIND-PATH(SouthEAST of x,y) == true) return true 
  if find_path(x, y+1, dim) ==True :
    #print("East")
    return True
#  8. 	if (FIND-PATH(WestNORTH of x,y) == true) return true 
  if find_path(x-1, y, dim) ==True :
    #print("North")
    return True
#  9. 	unmark x,y as part of solution path 
  mazearray[x][y]="0"
  #print("unmark path ", x, y)
#  10. return false 
  return False


# ----------------------------------------
# Main program
# -----------------------------------------

# open the data file
f = open("maze.dat")    # open file in current directory

mazearray=[]

# found this code to bring the data into a 2D array
# try understand elt, strip, split better
#
for line in f:
  
  inner_list = [elt.strip() for elt in line.split(',')]
  mazearray.append(inner_list)
  
mdim =len(mazearray)-1
mlength = int(mazearray[mdim][0])  
mwidth = int(mazearray[mdim][1])

  
  
#print("dim  ",mdim, "length ", mlength, " width ",mwidth)

# Find starting point
findstart=False
for i in range (0,mlength):
  for j in range (0,mwidth):
    #print (i,j, mazearray[i][j])
      
    if mazearray[i][j] == 'S':
      #print( "TRUE")
      findstart=True
      # Have the starting point so break out of first loop
      break
  # break out of second loop - indent must be correct!!!!
  if findstart==True:
    break  

print ("Start is at coords", i,j)
result = False
# Call recursive function
result = find_path(i,j,mdim)

if result == True:
  print("There is a result")
  maze_so_far(mdim,mdim)
else:
  print("No result")







    
