#matrix multiplication using function
#Step1 Need to initialise c to zero.
#Step2 Need to consider two matrix A and B.
#Step3 Need to find the dot product of two lists.
def initialize_mat(dim):
  c = []
  for i in range(dim):
    c.append([])
  for  i in range(dim):
    for j in range(dim):
      c[i].append(0)
  return c

def dot_product(u,v):
  dim = len(u)
  ans = 0
  for i in range(dim):
    ans = ans + (u[i]*v[i])
  return ans

def row(m,i):
  dim = len(m)
  l = []
  for k in range(dim):
    l.append(m[i][k])
  return l

def column(m,j):
  dim = len(m)
  l =[]
  for k in range(dim):
    l.append(m[k][j])
  return l

def mat_mul(A,B):
  dim = len(A)
  c = initialize_mat(dim)
  for i in range(dim):
    for j in range(dim):
      c[i][j] = dot_product(row(A,i),column(B,j))
  return c

A = [[1,2,3],[4,5,6],[7,8,9]]
B = [[1,2,1],[3,1,7],[6,2,3]]
print(mat_mul(A,B))
