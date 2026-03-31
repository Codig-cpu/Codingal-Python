list1=[1,2,3]
list2 =[4,5,6,7,]
result = map(lambda x, y: x + y, list1, list2)
print("Addition of two lists")
print(list(result))

nums = [1,2,3,4,5]
def sq(n):
    return n*n
square = list(map(sq, nums))
print("Sqaure of numbers in a list")
print(square)
