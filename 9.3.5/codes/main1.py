import math
p = 0.10  
q = 1 - p  
n = 12     
k = 9      
probability = math.comb(n, k) * (p ** k) * (q ** (n - k))
print(f"The probability of finding exactly 9 defective articles in a sample of 12 is approximately: {probability:.10f}")
