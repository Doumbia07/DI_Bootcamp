#Challenge 1:

number = int(input("Enter a number: "))
length = int(input("Enter the length: "))
multiples = []
for i in range(length):
    multiples.append(number * (i+1))
print(multiples)

#Challenge 2:
word = input("Enter a word: ")
result = ""
for ch in word:
    if ch != result[-1:]:  
        result += ch
print(result)