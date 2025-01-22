import numpy as np

a = np.array([3,8,5])
b = np.array([9,4,2])
c = np.array([7,1,4])

print(a)
print(b)
print(c)

ab = np.concatenate((a,b))
bc = np.concatenate((b,c))
ac = np.concatenate((a,c))
abc = np.concatenate((a,b,c))

print(ab)
print(bc)
print(ac)

print(abc)

print(np.sort(abc))
print(np.where(abc == 4))

print("Adding Arrays", np.add(a,b))
print("Subtracting Arrays", np.subtract(b,a))
print("Multiplying Arrays", np.multiply(a,b))
print("Dividing Arrays", np.divide(a,b))