import numpy as np
import pytest
from StressedCube import *

# example stress tensor
tij = np.array(
    [
        [1, 2, 3],
        [2, 5, 6],
        [3, 6, 9]
    ]
)

# let's take n direction a canonical one
n = np.array([1, 0, 0])

# this function will test if given
# tensor succeed symmetry condition
def test_tensorSymmetry():
    assert np.allclose(tij, tij.T, rtol=1e-5) == True

# checking normalization of each row of constructed
# aij matrix, each row norm must be 1.0
def test_normalizedDirections():
    testCube = StressedCube(tij, n)
    normalizedPrincipalDirections = testCube.normalizePrincipalDirections()
    flag = True
    for dir in normalizedPrincipalDirections:
        if abs( 1.0 - np.linalg.norm(dir) ) >= 1e-5:
            flag = False; break  # whenever it encounters non-1.0 norm
    assert flag == True

# test to check if angle is less than 360 deg
def test_angle():
    testCube = StressedCube(tij, n)
    assert testCube.getNormalStressAngle(angle='deg') <= 360.0

# let's try if raises the exception when it finds non valid angle unit
def test_angleUnit():
    testCube = StressedCube(tij, n)
    error = True
    try:
        # non valid angle unit named 'celsius'
        testAngle = testCube.getNormalStressAngle(angle='celsius')
        error = False
    except:
        error = True
    assert error == True