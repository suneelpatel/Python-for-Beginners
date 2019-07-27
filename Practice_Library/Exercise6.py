# What is the output of the following code? 
# nums = set([1,1,2,3,3,3,4,4]) 
# print(len(nums))
# Hint: Set consists unique element.

dic = {}

s='abcdefgabc'

for s in s:
    dic[s]=dic.get(s,0)+1
print('\n'.join(['%s,%s' % (k, v) for k, v in dic.items()]))
