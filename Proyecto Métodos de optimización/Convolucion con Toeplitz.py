import numpy as np
from scipy.linalg import toeplitz


def matrix_to_vector(input):
    """Sirve para trnasformar la imagen en vector b"""

    input_h, input_w = input.shape
    output_vector = np.zeros(input_h * input_w, dtype=input.dtype)
    # flip the input matrix up-down because last row should go first
    input = np.flipud(input)
    for i, row in enumerate(input):
        st = i * input_w
        nd = st + input_w
        output_vector[st:nd] = row
    return output_vector

def vector_to_matrix(input, output_shape):
    """Sirve para transformar el x encontrado en la imagen que buscamos"""

    output_h, output_w = output_shape
    output = np.zeros(output_shape, dtype=input.dtype)
    for i in range(output_h):
        st = i * output_w
        nd = st + output_w
        output[i, :] = input[st:nd]
    # flip the output matrix up-down to get correct result
    output = np.flipud(output)
    return output

def create_doubly_blocked(I, F, print_ir=False):
    """
    Crear la metriz de toeplitz y reemplazar la operacion de convolucion
    """

    # number of columns and rows of the input
    I_row_num, I_col_num = I.shape

    # number of columns and rows of the filter
    F_row_num, F_col_num = F.shape

    #  calculate the output dimensions
    output_row_num = I_row_num + F_row_num - 1
    output_col_num = I_col_num + F_col_num - 1


    # zero pad the filter
    F_zero_padded = np.pad(F, ((output_row_num - F_row_num, 0),
                               (0, output_col_num - F_col_num)),
                           'constant', constant_values=0)


    # use each row of the zero-padded F to creat a toeplitz matrix.
    #  Number of columns in this matrices are same as numbe of columns of input signal
    toeplitz_list = []
    for i in range(F_zero_padded.shape[0] - 1, -1,
                   -1):  # iterate from last row to the first row
        c = F_zero_padded[i, :]  # i th row of the F
        r = np.r_[c[0], np.zeros(
            I_col_num - 1)]  # first row for the toeplitz fuction should be defined otherwise
        # the result is wrong
        toeplitz_m = toeplitz(c, r)  # this function is in scipy.linalg library
        toeplitz_list.append(toeplitz_m)

        # doubly blocked toeplitz indices:
    #  this matrix defines which toeplitz matrix from toeplitz_list goes to which part of the doubly blocked
    c = range(1, F_zero_padded.shape[0] + 1)
    r = np.r_[c[0], np.zeros(I_row_num - 1, dtype=int)]
    doubly_indices = toeplitz(c, r)

    ## creat doubly blocked matrix with zero values
    toeplitz_shape = toeplitz_list[0].shape  # shape of one toeplitz matrix
    h = toeplitz_shape[0] * doubly_indices.shape[0]
    w = toeplitz_shape[1] * doubly_indices.shape[1]
    doubly_blocked_shape = [h, w]
    doubly_blocked = np.zeros(doubly_blocked_shape)

    # tile toeplitz matrices for each row in the doubly blocked matrix
    b_h, b_w = toeplitz_shape  # hight and withs of each block
    for i in range(doubly_indices.shape[0]):
        for j in range(doubly_indices.shape[1]):
            start_i = i * b_h
            start_j = j * b_w
            end_i = start_i + b_h
            end_j = start_j + b_w
            doubly_blocked[start_i: end_i, start_j:end_j] = toeplitz_list[
                doubly_indices[i, j] - 1]

    return  doubly_blocked


if __name__ == '__main__':
    I = np.array([[1,2,3],[4,5,6]])
    F = np.array([[10,20],[30,40]])

    m1, n1 = I.shape
    m2, n2 = F.shape

    print(create_doubly_blocked(I,F))

    print("\n")

    final = vector_to_matrix(np.matmul(create_doubly_blocked(I,F), matrix_to_vector(I)), ((n1-m2-1)**2, n1**2))
    print(final)
