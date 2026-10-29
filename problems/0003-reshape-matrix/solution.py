import numpy as np

def reshape_matrix(a: list[list[int|float]], new_shape: tuple[int, int]) -> list[list[int|float]]:
	#Write your code here and return a python list after reshaping by using numpy's tolist() method

	# looks like this motherfucker is only gonna be a 2d lsit maximum
	a_np = np.array(a)

	# check possibility
	if a_np.size != new_shape[0] * new_shape[1]:
		return []

	# bro am i supposed to be doing it with numpy functions?
	a_np.reshape(new_shape[0], new_shape[1])

	reshaped_matrix = a_np.tolist()
	return reshaped_matrix