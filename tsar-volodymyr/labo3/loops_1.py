
counter = 0
while counter < 5:
    print(counter)
    counter += 1
else:
    print(f"Counter value reached {counter}")

for num in range(1, 10):
    if num % 5 == 0:
        break
    print(num)
else:
    print("This message is not printed because the loop was terminated by 'break', not by failing the condition.")


