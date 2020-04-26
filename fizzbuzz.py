number = int(input("1つの自然数を入れてね: "))

if number % 15 == 0:
    output = "Fizz Buzz"
elif number % 5 == 0:
    output = "Buzz"
elif number % 3 == 0:
    output = "Fizz"
else:
    output = str(number)

print(output)
