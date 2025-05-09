
print("\nbreak:")
count = 0
while True:
    if count >= 5:
        print("count >= 5, break")
        break
    print(f"count: {count}")
    count += 1

print("\ncontinue:")
count = 0
while count < 5:
    count += 1
    if count == 3:
        continue
    print(f"count: {count}")
