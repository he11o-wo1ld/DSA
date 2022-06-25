def minimumNumbers(num, k):
	for i in range(2, num):
	    if (num % i) == 0:
	    	return -1
	    
	    s = num - k
	    


num = 37
k = 2
print(minimumNumbers(num, k))

# def prime(x, y):
# 	prime_list = []
# 	for i in range(x, y):
# 	    if i == 0 or i == 1:
# 	        continue
# 	    else:
# 	        for j in range(2, int(i/2)+1):
# 	            if i % j == 0:
# 	                break
# 	        else:
# 	            prime_list.append(i)
# 	return prime_list
# print(prime(1, 100))