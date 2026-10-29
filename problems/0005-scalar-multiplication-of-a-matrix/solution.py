import numpy as np

def scalar_multiply(matrix: list[list[int|float]], scalar: int|float) -> list[list[int|float]]:
	# why in the hell is numpy allowed here man

	mat = np.array(matrix)
	return mat * scalar