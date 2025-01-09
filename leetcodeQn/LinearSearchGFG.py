def searchInSorted(arr, k):
        #Your code here
        case = False
        for num in arr:
            if (num == k):
                case = True
    
        return case
                
userInput = int(input("What number you want to search for ? "))
print(searchInSorted([1,2,3,4,5,6,7,8], userInput))