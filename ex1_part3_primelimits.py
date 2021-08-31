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
    #print ("Number " + str(test_num) +" is not prime" )
    return False


#
# Function to make user enter a number
#
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






# ---------------------------------
# start of body of program
# -------------------------------
prime_lower = int(check_input( "Enter the lower limit for Prime Numbers "))
prime_upper = int(check_input( "Enter the upper limit for Prime Numbers "))
'''
print ("Number " + str(2) +" is prime" )
print ("Number " + str(3) +" is prime" )
prime_numbers=prime_numbers-2
'''
i=1
for i in range (prime_lower, prime_upper) :
  #print(" i ", i) 
  result = FindPrime(i)
  
  i=i+1
