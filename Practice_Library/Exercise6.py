dic = {}

s='abcdefgabc'

for s in s:
    dic[s]=dic.get(s,0)+1
print('\n'.join(['%s,%s' % (k, v) for k, v in dic.items()]))