num = int(input("Enter a Number here :"))
counter = 1
while (counter <= 10):
    if (counter % 2 == 0):
        counter +=1
        continue
        
    print(f"{counter} * {num} = {counter*num}")
    counter +=1 