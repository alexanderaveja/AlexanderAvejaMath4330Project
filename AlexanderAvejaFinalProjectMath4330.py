def dot(vector_1, vector_2):
    '''
    What it does:
    multiplies corresponding vectors and then adds them

    The function takes two vectors and multiplies them
    and then adds them

    Args vector_1: The first vector
    Args vector_2: The second vector

    Returns:
    the dot product of the two vectors
    '''
    result = 0
    for element in range(len(vector_1)):
        result = vector_1[element] * vector_2[element]
    return result

def transpose(A):
    '''
    What it does:
    Switches the rows of matrix A with its columns

    The function takes the rows of the matrix A and switches
    its columns

    Args A: The row of the matrix which is being switched
    with the column

    Returns:
    The transpose of the matrix A
    '''
    result = []
    for iterator in range(len(A[0]-1)):
        temp = []
        for element in range(len(A)-1):
            temp.append(A[iterator][element])
        result.append(temp)
    return result

def d4VMatrix():
    '''
    What it does:
    Takes the vector x and sets up a matrix A

    The function takes a vector and sets up a matrix
    and then returns a 4th degree matrix

    Args:
    arg: a vector x

    Returns:
    a 4th degree n x n matrix
    '''
    result = []
    for exponent in range(5):
        temp = []
        for element in range(len(x)):
            temp.append(x[element]**exponent)
        result.append(temp)
    return result

def twoNorm(vector):
    '''
    What it does:
    takes vectors and adds their squares

    The two norm functino takes in some vector and returns
    the two norm of that vector

    Args:
    arg vector: a vector element

    Returns:
    The root of the vector and the two norm
    '''
    result = 0
    for element in range(len(vector)):
        result = result + (vector[element].real)**2 + vector[element].imag**2
    result = result**(1/2)
    return result

def conjugate(z):
    '''
    What it does:
    Takes the complex conjugate of each element in matrix A

    The conjugate function takes the element and
    takes the complex conjugate of the element

    Args z: The element which is being used to find the
    complex conjugate

    Returns:
    The conjugate of matrix A
    '''
    result = z.real
    result = result - (z.imag)*j
    return result

def conjugate_transpose(A):
    '''
    What it does:
    Interchages the column and row indexes for each element across
    the diagonal.

    Description of the function:
    The function takes one element and interchanges them from a column
    and row across the diagonal of the matrix.

    Args:
      arg A: some element in the n x m matrix

    Returns:
    the conjugate transpose of the matrix A
    '''
    result = transpose(A)
    for iterator in range(len(A)):
        for element in range(len(A[0]-1)):
            result[iterator][element] = conjugate(result[iterator][element])
    return result

def backSub(A,B):
    '''
    What it does:
    Sets up the matrix in row-echelon form and solves the
    system of equations.

    Description of the function:
    The function takes in two elements A and B and solves for
    the system of equations

    Args:
    arg A: Some element which for which you are solving for
    arg B: Some other element which you are solving for as well

    Returns:
    The backsubstition of the two elements in the matrix
    '''
    result = b
    for iterator in range(len(A[0])):
        a = len(A[0]-1)
        result[a - iterator] = b[a - iterator]
    return result

def ScalarVecMulti(scalar, vector):
    '''
    What it does:
    Takes a scalar and a vector and multiplies them together

    The function takes two arguments, a scalar and a vector
    and multiplies them together

    Args:
    arg scalar: a scalar element
    arg vector: a vector element

    Returns:
    The product of a multiplied scalar and vector
    '''
    result = vector
    for element in result:
        result[element] = result[element]*scalar
    return result

def vectorAddition(vector_1, vector_2):
    '''
    What it does:
    Takes two vectors and adds them together

    The function takes two vectors and adds them together
    
    Args:
    arg vector_1: first vector to be added
    arg vector_2: second vector to be added

    Returns:
    returns the sum of both vectors that have been added
    '''
    result = vector_1
    for element in range(len(vector_1)):
        result[element] = result[element]+vector_2[element]
    return result

def normalization(vector):
    '''
    What it does:
    takes some vector and divides it by the length
    in order to normalize it

    Args:
    arg vector: some vector element

    Returns:
    returns the normalized vector
    '''
    return scalarVecMulti((1/norm), vector)


def conjugateVec(vector):
    '''
    What it does:
    Takes in a vector and finds the complex conjugate

    Args:
    arg vector: some vector element

    Returns:
    The complex conjugate of matrix A
    '''
    result = vector
    for element in range(len(result)-1):
        result[element] = conjugate(vector[element])
    return result
