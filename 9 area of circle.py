pi = 3.14
r=float(input("enter radius"))
area = pi*r**2
print(area)

from numpy import array

from scipy.linalg import svd

#define a matrix

A = array([[1, 2], [3, 4], [5, 6]])

print("A = ",A)

print("Shape of array A: ",A.shape)

print("")

U, pp. VT svd(A)# SVD

print("U = ",U)

print("Shape of matrix U: ", U.shape)

print("")

print("Sigma(diagonal matrix), s = ",s)

print("Shape of matrix sigma: ",s.shape)

print("")
