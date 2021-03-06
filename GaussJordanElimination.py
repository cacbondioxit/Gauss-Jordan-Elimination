# Gauss-Jordan Elimination #GaussJordanElimination.py

import numpy as np
import copy

class GaussJordanElimination:
    def __init__(self, A, b): 
        self.A = A
        self.b = b

    def show(self): # show the augmented matrix
        for i in range(len(A)):
            print(A[i], b[i])
        print()

    # Elimentary Row Operation (swap, multiplication, Addition) 
    def swap(self, row1, row2): 
        if row1==row2:
            return
        tmp = copy.deepcopy(A[row1])
        A[row1] = A[row2]
        A[row2] = tmp
    
        tmp = copy.deepcopy(b[row1])
        b[row1] = b[row2]
        b[row2] = tmp

        print("R"+str(row1+1)+"<->"+"R"+str(row2+1))

    def mul(self, row, k):
        if k==1:
            return

        A[row] = k*A[row]
        b[row] = k*b[row]

        if k!=1:
            print("R"+str(row+1)+"*("+str(k)+")")

    def add(self, row1, row2, k):
        if k==0:
            return

        A[row1] += k*A[row2]
        b[row1] += k*b[row2]

        if k==1:
            print("R"+str(row1+1)+"+R"+str(row2+1))
        else:
            print("R"+str(row1+1)+"+("+str(k)+")*R"+str(row2+1))

    def pivot(self, col): # Find pivot in the col-th column. if doesn't exist, make the pivot by dividing(ERO).
        for row in range(col, len(A[0])):
            if A[row][col] == 1:
                if row==col:
                    continue
                self.swap(row, col)
                self.show()
                return
        if A[col][col]!=0 and A[col][col]!=1:
            self.mul(col, 1/A[col][col])
            self.show()
            return
        
    def calculate(self):
        self.show()
        for col in range(len(A[0])):
            self.pivot(col)
            for row in range(len(A)):
                if row==col:
                    continue
                else:
                    if A[row][col]!=0:
                        self.add(row, col, -A[row][col]) # for making RREF of the matrix A.
                        self.show()

A = np.array([[1,-1,1,2,3],[2,-2,3,-6,-1],[1,4,-1,1,2],[0,1.5,2,1,-1],[-1,0,1,3,4]])
b = np.array([[1],[3],[-.5],[0],[10]])

Cal = GaussJordanElimination(A, b)
Cal.calculate()