num = int(input("Enter your number: "))

par = 0
impar = 0

while(num > 0):
  if num % 2 == 0:
    par = par + 1
  else:
    impar = impar + 1
  num = num // 10

print("Numeros par: ",par)
