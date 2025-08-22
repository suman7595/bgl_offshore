l=[1,1,1,2,2,2,3,3,3,4,4,5]
uniq=set(l)
print(list(uniq))
u=[]
for i in l:
      if i not in u:
             u.append(i)
print(u)             