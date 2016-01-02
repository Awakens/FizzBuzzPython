z = "Fizz";
for x in range (1, 101):
    if x % 3 == 0:
        z = "Fizz"
        if x % 5 == 0:
            z = "FizzBuzz"
    elif x % 5 == 0:
        z = "Buzz"
    else:
        z = x
    print(z)
