import math
from math import sqrt
import numbers

def zeroes(height, width):
        """
        Creates a matrix of zeroes.
        """
        g = [[0.0 for _ in range(width)] for __ in range(height)]
        return Matrix(g)

def identity(n):
        """
        Creates a n x n identity matrix.
        """
        I = zeroes(n, n)
        for i in range(n):
            I.g[i][i] = 1.0
        return I

class Matrix(object):

    # Constructor
    def __init__(self, grid):
        self.g = grid
        self.h = len(grid)
        self.w = len(grid[0])

    #
    # Primary matrix math methods
    #############################
 
    def determinant(self):
        """
        Calculates the determinant of a 1x1 or 2x2 matrix.
        """
        if not self.is_square():
            raise(ValueError, "Cannot calculate determinant of non-square matrix.")
        if self.h > 2:
            raise(NotImplementedError, "Calculating determinant not implemented for matrices largerer than 2x2.")
        
        
        if self.h == 1 and self.w == 1:
            return self.g[0][0]
        else:
            return self.g[0][0]*self.g[1][1] - self.g[0][1]*self.g[1][0]
            
        

    def trace(self):
        """
        Calculates the trace of a matrix (sum of diagonal entries).
        """
        if not self.is_square():
            raise(ValueError, "Cannot calculate the trace of a non-square matrix.")
        return sum(self.g[i][i] for i in range(self.h))
        
    def inverse(self):
        """
        Calculates the inverse of a 1x1 or 2x2 Matrix.
        """
        if not self.is_square():
            raise(ValueError, "Non-square Matrix does not have an inverse.")
        if self.h > 2:
            raise(NotImplementedError, "inversion not implemented for matrices larger than 2x2.")

        if self.h == 1 and self.w == 1:
            a = self.g[0][0]
            if a == 0:
                raise(ValueError, "The matrix is singular and cannot be inverted")
            return Matrix([[1/a]])
        else:
            a, b = self.g[0]
            c, d = self.g[1]
            
            determinant = a * d - b * c
            if determinant == 0:
                raise(ValueError, "The matrix is singular and cannot be inverted")
            return Matrix([[d / determinant, -b / determinant],[-c / determinant, a / determinant]])

    def T(self):
        """
        Returns a transposed copy of this Matrix.
        """
        
        transposed = [[self.g[j][i] for j in range(self.h)] for i in range(self.w)]
        return Matrix(transposed)

    def is_square(self):
        return self.h == self.w

    #
    # Begin Operator Overloading
    ############################
    def __getitem__(self,idx):
        """
        Defines the behavior of using square brackets [] on instances
        of this class.

        Example:

        > my_matrix = Matrix([ [1, 2], [3, 4] ])
        > my_matrix[0]
          [1, 2]

        > my_matrix[0][0]
          1
        """
        return self.g[idx]

    def __repr__(self):
        """
        Defines the behavior of calling print on an instance of this class.
        """
        s = ""
        for row in self.g:
            s += " ".join(["{} ".format(x) for x in row])
            s += "\n"
        return s

    def __add__(self,other):
        """
        Defines the behavior of the + operator
        """
        if self.h != other.h or self.w != other.w:
            raise(ValueError, "Matrices can only be added if the dimensions are the same") 

        
        result = [[self.g[i][j] + other.g[i][j] for j in range(self.w)] for i in range(self.h)]
        return Matrix(result)
            

    def __neg__(self):
        """
        Defines the behavior of - operator (NOT subtraction)

        Example:

        > my_matrix = Matrix([ [1, 2], [3, 4] ])
        > negative  = -my_matrix
        > print(negative)
          -1.0  -2.0
          -3.0  -4.0
        """

        return Matrix([[-element for element in row] for row in self.g])

    def __sub__(self, other):
        """
        Defines the behavior of - operator (as subtraction)
        """

        if self.h != other.h or self.w != other.w:
            raise(ValueError, "Matrices can only be subtracted if the dimensions are the same") 
            
        result = [[self.g[i][j] - other.g[i][j] for j in range(self.w)] for i in range(self.h)]
        return Matrix(result)

    def __mul__(self, other):
        """
        Defines the behavior of * operator (matrix multiplication)
        """
        
        if self.w != other.h:
            raise(ValueError, "Number of columns in the first matrix must equal the number of rows in the second matrix")
            
        result = [[0] * other.w for _ in range(self.h)]
        
        for i in range(self.h):
            for j in range(other.w):
                for k in range(other.h):
                    result[i][j] += self.g[i][k] * other.g[k][j]
        return Matrix(result)

    def __rmul__(self, other):
        """
        Called when the thing on the left of the * is not a matrix.

        Example:

        > identity = Matrix([ [1,0], [0,1] ])
        > doubled  = 2 * identity
        > print(doubled)
          2.0  0.0
          0.0  2.0
        """
        if isinstance(other, numbers.Number):
            result = [[other * self.g[i][j] for j in range(self.w)] for i in range(self.h)]
            return Matrix(result)
            