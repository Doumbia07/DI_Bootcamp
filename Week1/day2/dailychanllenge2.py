# Matrice donnée
matrix_strings = ["7ii", "Tsx", "h%?", "i #", "sM ", "$a ", "#t%", "^r!"]


max_len = max(len(row) for row in matrix_strings)


grid = []
for row in matrix_strings:

    grid.append(list(row.ljust(max_len)))


message_chars = []
for col in range(max_len):
    for row in range(len(grid)):
        char = grid[row][col]
        message_chars.append(char)


result = []
previous_was_letter = False

for char in message_chars:
    if char.isalpha():
        result.append(char)
        previous_was_letter = True
    else:

        if previous_was_letter:
            result.append(" ")
            previous_was_letter = False


decoded = "".join(result).strip()
print(decoded)
