## Rotate 2D Matrix  

> Given an n x n 2D matrix, rotate it 90 degrees clockwise.

- Prototype: *def rotate_2d_matrix(matrix):  

- Do not return anything. The matrix must be edited in-place.
- You can assume the matrix will have 2 dimensions and will not be empty.  *

## Solution    
```   
def rotate_2d_matrix(matrix):  
	matrix[:] = [list(row[::-1]) for row in zip(*matrix)]  

	```

* matrix[:]: the original matrix
* zip(): reverses each row individually
* [list(row[::-1]) for row in zip(*matrix)] : list comprehension to construct \ a new list of lists with reversed rows

