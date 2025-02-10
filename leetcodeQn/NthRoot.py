def nthRoot(n,m):
        low, high = 1, m  

        while low <= high:
            mid = (low + high) // 2
            
            ans = 1
            for i in range(n):
                ans *= mid
                if ans > m:  
                    break

            if ans == m:
                return mid  
            elif ans > m:
                high = mid - 1
            else:
                low = mid + 1
        
        return -1

print(nthRoot(2,9))