arr = ['apple','banana','cherry','orange']

# for  element in arr :
#     element = "Eat " + element

# range(0, 4) => [0, 1, 2, 3]
# for index in range(0,7,2):
#     print(index)
#     print("Wake up")

for i in range(0,len(arr)):
    # if arr[i] == 'banana':
    #     continue #skip keyword
    arr[i] = "Eat " + arr[i]
    print(arr[i])
    if i >= 1:
        break #stop
print(arr)    

