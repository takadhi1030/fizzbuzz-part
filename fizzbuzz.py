number = int(input("1つの自然数を入れてね: "))

if number % 3 == 0:
    output = "fizz"
else:
    output = str(number)

print(output)
