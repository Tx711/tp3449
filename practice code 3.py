max = int(input("Enter a number: "))

odd_numbers = []

for i in range(1,max):
    if i % 2 == 1:
        odd_numbers.append(i)

print("Odd Numbers: ", odd_numbers)