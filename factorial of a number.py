# Python 3 programa para encontrar  
# fatorial de dado número 
def factorial(n): 
      
    # única linha para encontrar fatorial 
    return 1 if (n==1 or n==0) else n * factorial(n - 1);  
  
# Driver Code 
num = 5; 
print("Factorial of",num,"is", 
factorial(num)) 
  
# Este código é contribuído por Dorgival Fernando 