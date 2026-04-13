print("FIZZ BUZZ")
number = int(input("type a number btween 1 and 1000"))

if number < 100:
    print('Number too short, ill use 100')
    number = 100
else:
    print("System ready to start counting")

#divisivel por 3 mostra fizz

#divisivel por 5 mostra buzz

#divisivel por ambos mostra fizz buzz
for i in range(number):
    if (i+1) %3 == 0 and (i+1) %5 == 0:
        print(f"FIZZBUZZ")
    elif (i+1) %3 == 0:
        print(f"FIZZ")
    elif (i+1) %5 == 0:
        print(f"BUZZ")
    else:
        print (i+1)