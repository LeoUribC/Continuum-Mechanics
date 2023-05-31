**Problem 3.28**
================

At point :math:`P` in acontinuum body, the stress tensor components are
given in MPa with respect to the axes :math:`Px_1x_2x_3` by the matrix

.. math::

    [t_{ij}] =
   \begin{bmatrix}
       1 & -3 & \sqrt2 \\
       -3 & 1 & -\sqrt2 \\
       \sqrt2 & -\sqrt2 & 4
   \end{bmatrix}

| Determine
| (a) the principal stress values
  :math:`\sigma_{I}`,\ :math:`\sigma_{II}` and :math:`\sigma_{III}`
  together with the corresponding principal directions
| (b) The stress invariants :math:`I_T`, :math:`II_T` and :math:`III_T`
| (c) The maximum shear stress value and the normal to the plane on wich
  it acts
| (d) the principal deviator stress values
| (e) the stress vector on the octahedral plane together with it’s
  normal and shear components
| (f) the stress matrix for axes rotated 60° counterclockwise with
  respect to the axis :math:`PQ`, which makes equal angles relative to
  the coordinate axes :math:`Px_1x_2x_3`

Solving
=======

(a) Principal stress values and principal stress directiones

.. code:: python

    import numpy as np
    t = np.array([[1,-3,np.sqrt(2)],
                  [-3,1,-np.sqrt(2)],
                  [np.sqrt(2),-np.sqrt(2),4]])

.. code:: python

    values, directions = np.linalg.eig(t)
    
    print("Principal stress values")
    print(values)
    print("\n")
    print("Principal stress directions")
    print(directions)
    


.. parsed-literal::

    Principal stress values
    [ 6. -2.  2.]
    
    
    Principal stress directions
    [[-5.00000000e-01  7.07106781e-01 -5.00000000e-01]
     [ 5.00000000e-01  7.07106781e-01  5.00000000e-01]
     [-7.07106781e-01  1.92232847e-16  7.07106781e-01]]
    

(b) the stress invariants

.. code:: python

    IT = np.trace(t)
    IT




.. parsed-literal::

    6.0



.. code:: python

    IIT = (1/2)*((np.trace(t))**2 - np.trace(t**2))
    IIT




.. parsed-literal::

    9.0



.. code:: python

    IIIT = np.linalg.det(t)
    IIIT




.. parsed-literal::

    -24.000000000000014



(c) The maximum shear stress value and the normal to the plane on wich
    it acts

.. math::  \sigma_{max} = \max \left( \left| \frac{\sigma_1}{2} \right|, \left| \frac{\sigma_2}{2} \right|, \left| \frac{\sigma_3}{2} \right|, \left| \frac{\sigma_1 - \sigma_2}{2} \right|, \left| \frac{\sigma_1 - \sigma_3}{2} \right|, \left| \frac{\sigma31 - \sigma_2}{2} \right| \right) 

.. code:: python

    sigma1,sigma2,sigma3 = np.linalg.eig(t)[0][0],np.linalg.eig(t)[0][1],np.linalg.eig(t)[0][2]
    
    sigmas = [abs(sigma1/2), abs(sigma2/2), abs(sigma3/2), abs(sigma1 - sigma2)/2, abs(sigma1 -sigma3)/2, abs(sigma2-sigma3)/2]

.. code:: python

    max(sigmas)




.. parsed-literal::

    3.999999999999999



(d) The principal deviator stress values

We know that

.. math:: \sigma_M = \frac{t_{ij}}{3} = \frac{T_{kk}}{2} = \frac{4}{2}

We define deviatoric stress to be

.. math:: S = T - \frac{T_{kk}}{2} I

Then

.. math::

    [t_{ij}] =
   \begin{bmatrix}
       1 & -3 & \sqrt2 \\
       -3 & 1 & -\sqrt2 \\
       \sqrt2 & -\sqrt2 & 4
   \end{bmatrix} -
   \begin{bmatrix}
       4/2 & 0 & 0 \\
       0 & 4/2 & 0 \\
       0 & 0 & 4/2
   \end{bmatrix}

.. code:: python

    T_kk = np.array([[4/2,0,0],
                     [0,4/2,0],
                     [0,0,4/2]])
    T_kk




.. parsed-literal::

    array([[2., 0., 0.],
           [0., 2., 0.],
           [0., 0., 2.]])



.. code:: python

    s = t - T_kk
    print(s)


.. parsed-literal::

    [[-1.         -3.          1.41421356]
     [-3.         -1.         -1.41421356]
     [ 1.41421356 -1.41421356  2.        ]]
    

.. code:: python

    np.linalg.eig(s)[0]




.. parsed-literal::

    array([ 4.00000000e+00, -4.00000000e+00, -1.25961676e-16])



