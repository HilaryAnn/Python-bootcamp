#
# Find all Prime Numbers up to N.
#

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
    
      return False

# ---------------------------------
# start of body of program
# -------------------------------

# Input number of prime numbers to find
#
prime_numbers = int(input( "Find the first ? Prime Numbers: "))
print ("Number " + str(2) +" is prime" )
print ("Number " + str(3) +" is prime" )
prime_numbers=prime_numbers-2

j=4
i=1
while i <prime_numbers+1:
  result = FindPrime(j)
  if result == True:
    i=i+1
  j=j+1
  
  
  
  