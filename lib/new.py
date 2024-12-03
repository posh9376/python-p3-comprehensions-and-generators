new_list= [((n**2)-1) for n in range(1,11)]

print(new_list)

one_to_three = range(1,4)

square_lc = [(n**2) for n in one_to_three]
print(square_lc)

square_ge = (n**2 for n in one_to_three)

for n in square_ge:
    print(n)

print(square_ge)