import random

#generate numbers
numbers = random.sample(range(100,1000), 100)

#print number
print("All numbers in the List:")
print(numbers)

#print separated odd and even
print("Odd Numbers in the List:")
print([number for number in numbers if number%2 == 1])
print("Even Numbers in the List:")
print([number for number in numbers if number%2 == 0])

#print numbers divisible by 9
print("Numbers in the List that are divisible by 9:")
print([number for number in numbers if number%9 == 0])

#print prime numbers in the list
print("Prime numbers in the list:")
for num in numbers:
  isPrime = True
  for ref in range (2,8):
    if ref == num or ref == 4 or ref == 6: #the reference should not be equal to the number
      break
    if num%ref == 0: # this means the number is not prime
      isPrime = False
      break
  if isPrime == True:
    print(num, end=" ")
  
#print numbers with 9 in it(Example. 29,19,96)
print([number for number in (numbers) if 9 in num])