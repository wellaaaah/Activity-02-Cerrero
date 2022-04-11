import random

l = 90
a = 205
d = 188
p = 110

t= 1
w = 1
b = 1
c = 1
random = round(random.uniform(0.85,1.0),2)
s = 1.5
ty = 0.5
bn = 1
m = t*w*b*c*random*s*ty*bn*1

dmg = ((2*l)/5)+2
dmg = (dmg*p)*(a/d)
dmg = ((dmg/50)+2)*m

print(round(dmg))
print("random number = "+str(random))