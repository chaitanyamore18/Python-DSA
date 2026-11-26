arr = [100,101,100,102,101,100]
freq  = [0] * 4     # to save space and not creating big array/hashmap
for i in arr:
    freq[i-100] += 1    # freq[0], freq[1] .... 

for i in range(len(freq)):
    print(f"{i+100} occurs {freq[i]} times")