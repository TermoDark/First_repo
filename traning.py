first = int(input("Enter the first integer: "))
second = int(input("Enter the second integer: "))
# gcd = 
def hcf(first, econd):

      if first > second:
              gcd = first
      else:
              gcd = second

      for i in range(1,gcd + 1):
              if((first % i == 0) and (second % i == 0)):
                      hcf = i

      return hcf

# while 


print("The H.C.F. of", first,"and", second,"is", hcf(first, second))