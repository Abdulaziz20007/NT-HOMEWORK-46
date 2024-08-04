data = input("So'z kiriting: ")
replacers = {'a': 0, 'e': 1, 'i': 2, 'o': 2, 'u': 3}

# Reverse the string and convert it to a list of characters
word = list(data[::-1])

# Replace characters using the replacers dictionary
ls = []
for item in word:
    if item.lower() in replacers:
        ls.append(replacers[item.lower()])
    else:
        ls.append(item)

# Convert list of elements to a string
ls_to_str = ''.join([str(elem) for elem in ls])
ls_to_str += 'aca'

print(ls_to_str)
