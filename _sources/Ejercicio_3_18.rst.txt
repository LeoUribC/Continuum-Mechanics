**Exercise 3.18**
=================

The stress tensor at :math:`P` is given with respect to
:math:`Ox_1x_2x_3` in matrix form with units of MPa by

.. math::

    [t_{ij}] =
   \begin{bmatrix}
       4 & b & b \\
       b & 7 & 2 \\
       b & 2 & 4
   \end{bmatrix}

Where :math:`b` is unespecified. If
:math:`\sigma_{III} = 3 \; \text{MPa}` and
:math:`\sigma_{I} = 2\sigma_{II}`, determine

(a) the principal stress values
(b) the value of b
(c) the principal stress direction of :math:`\sigma_{II}`

Solving
-------

Let’s import the necessary libraries and declare the stress tensor
given:

.. code:: python

    from sympy import *
    import numpy as np
    
    init_printing()
    
    lamda = symbols('lambda')
    b = symbols('b')
    t = [[4,b,b],[b,7,2],[b,2,4]]
    t




.. math::

    \displaystyle \left[ \left[ 4, \  b, \  b\right], \  \left[ b, \  7, \  2\right], \  \left[ b, \  2, \  4\right]\right]



First, let’s use the algorithm to find the determinant.

.. admonition:: remember the algorithm

   the algorithm to find principal values and directions with index notation is:

   .. math::
      \left( t_{ij} - \lambda \delta_{ij} n_j \right) = 0

Finding the determinant we have:

.. code:: python

    t_lamda = [[4-lamda,b,b],[b,7-lamda,2],[b,2,4-lamda]]
    t_lamda




.. math::

    \displaystyle \left[ \left[ 4 - \lambda, \  b, \  b\right], \  \left[ b, \  7 - \lambda, \  2\right], \  \left[ b, \  2, \  4 - \lambda\right]\right]



.. code:: python

    det = (4 - lamda)*((7-lamda)*(4-lamda) - (2*2)) - b*((b)*(4-lamda) - (2)*(b)) + b*((2)*(b) - (b)*(7-lamda))
    det




.. math::

    \displaystyle - b \left(b \left(4 - \lambda\right) - 2 b\right) + b \left(- b \left(7 - \lambda\right) + 2 b\right) + \left(4 - \lambda\right) \left(\left(4 - \lambda\right) \left(7 - \lambda\right) - 4\right)



Now, we know that :math:`\lambda = 3`, so let’s replace in the
polynomial and solve the equation for this :math:`\lambda`:

.. code:: python

    solve(det.subs(lamda,3),b)




.. math::

    \displaystyle \left[ 0\right]



Then, :math:`b=0`

.. code:: python

    b = 0
    t = [[4,b,b],[b,7,2],[b,2,4]]
    t




.. math::

    \displaystyle \left[ \left[ 4, \  0, \  0\right], \  \left[ 0, \  7, \  2\right], \  \left[ 0, \  2, \  4\right]\right]



.. code:: python

    t = np.array(t)
    np.linalg.eig(t)[0]




.. parsed-literal::

    array([3., 8., 4.])



We have then that :math:`\sigma_{III} = 3 \; \text{MPa}`,
:math:`\sigma_{I} = 8 \; \text{MPa}`, and
:math:`\sigma_{II} = 4 \; \text{MPa}`.

So :math:`\sigma_{I} = 2\sigma_{II}` as expected.

.. code:: python

    np.linalg.eig(t)[1]




.. parsed-literal::

    array([[ 0.        ,  0.        ,  1.        ],
           [ 0.4472136 , -0.89442719,  0.        ],
           [-0.89442719, -0.4472136 ,  0.        ]])



Finally, as seen, the principal direction associated with
:math:`\sigma_{II}` is the vector :math:`[1,0,0]`, or,

.. math:: \hat{n}^{(2)} = \hat{e}_1
