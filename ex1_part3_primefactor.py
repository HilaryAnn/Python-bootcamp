#
# Function to calculate the prime factorization of a number entered by the user
# future improvment - calculate the primes then use them to work out the
#    factorisation
# put loop around the sections doing the division191
#

# Checking input
def check_input(message):
  while True:
    try:
        # Note: Python 2.x users should use raw_input, the equivalent of 3.x's input
        output_var = float(input(message))
    except ValueError:
        print("Sorry, I didn't understand that. Press CTRL Z to exit")
        #better try again... Return to the start of the loop
        continue
    else:
        #age was successfully parsed!
        #we're ready to exit the loop.
        break 
  return output_var

#
# function to check if a number is a prime
#
def FindPrime (test_num):
  isPrime = True
  sqroot_num=int(test_num**0.5)+1
  #clearprint("square root",sqroot_num)
  for ii in range (2,sqroot_num):
    result = test_num%ii
    #print(" ii ",ii,"result ", result)
    if result== 0 :
      isPrime=False 
      break
    else:
      isPrime = True

  if isPrime:
    print ("Number " + str(test_num) +" is prime" )
    return True
  else:
    #print ("Number " + str(test_num) +" is not prime" )
    return False




# ---------------------------------
# start of body of program
# -------------------------------
prime_factor = int(check_input( "Enter the number to be factorised: "))
result=prime_factor

tfactor=[]

# Check division by prime number 2
#
modres=0
while result >=2 and modres == 0:
  modres=result%2
  if modres == 0:
    tfactor.append(2)
    result = result/2
  #print( "result", result)


# Check division by prime number 3
#
modres=0
while result >=3 and modres == 0:
  modres=result%3
  if modres == 0:
    tfactor.append(3)
    result = result/3
  #print( "result", result)

# Check division by prime number 5
#
modres=0
while result >=5 and modres == 0:
  modres=result%5
  if modres == 0:
    tfactor.append(5)
    result = result/5
  #print( "result", result)


# Check division by prime number 7
#
modres=0
while result >=7 and modres == 0:
  modres=result%7
  if modres == 0:
    tfactor.append(7)
    result = result/7
  #print( "result", result)

if modres>0 :
    tfactor.append(int(result))


#
# Print out the results
#
flen=len(tfactor)
#
print ("length ", flen)
print("Number to factorise : ", prime_factor, " = ",end='')
for i in range (0,flen):
  print(tfactor[i], end='')
  if i<flen-1:
    print(' * ', end='')
  else:
    print(' ')
  

