test_dict = {'Codingal' : 2, 'is' : 3, 'best' : 2, '2':2, 'Coding' : 1}

print("The Original dictionary : " + str(test_dict))

k=3

res= 0
for key in test_dict:
    if test_dict[key] == k:
        res = res + 1

print("Frequencry of K is " +str(res))