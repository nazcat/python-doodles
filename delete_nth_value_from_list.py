#### Write code that uses slicing to get rid of the the second 8 so that here are only two 8’s in the list bound to the variable nums.
#### nums = [4, 2, 8, 23.4, 8, 9, 545, 9, 1, 234.001, 5, 49, 8, 9 , 34, 52, 1, -2, 9.1, 4]

# shorter method
nums = [4, 2, 8, 23.4, 8, 9, 545, 9, 1, 234.001, 5, 49, 8, 9 , 34, 52, 1, -2, 9.1, 4]

idx = [ i for i in range(len(nums)) if nums[i]==8 ]
del nums[idx[1]]

print( nums )

#longer method
def RemoveIthWord(lst, value, N):
    newList = []
    count = 0
  
    # iterate the elements
    for i in lst:
        if(i == value):
            count = count + 1
            if(count != N):
                newList.append(i)
        else:
            newList.append(i)
              
    lst = newList
      
    if count == 0:
        print("Item not found")
    else:
        print("Updated list is: ", lst)    
      
    return newList
  
# Driver code
nums = [4, 2, 8, 23.4, 8, 9, 545, 9, 1, 234.001, 5, 49, 8, 9 , 34, 52, 1, -2, 9.1, 4]
value = 8
N = 2
  
RemoveIthWord(nums, value, N)
