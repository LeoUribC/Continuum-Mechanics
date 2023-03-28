**Problem 3.29**
================

In a continuum, the stress field relative to the axes :math:`Ox_1x_2x_3`
is given by

.. math::

    [t_{ij}] =
   \begin{bmatrix}
       x_1^2x_2 & x_1(1 - x_2^2) & 0 \\
       x_1(1 - x_2^2) & \frac{1}{3}(x_2^2 - 3x_2) & 0 \\
       0 & 0 & 2x_3^2
   \end{bmatrix}

| Determine
| (a) the body force distribution if the equilibrium equations are to be
  satisfied throughtout the field
| (b) the principal stresses at :math:`P(a,0,2\sqrt a)`
| (c) the maximum shear stress at :math:`P`
| (d) the principal deviator stresses at :math:`P`

Solving
-------

(a) Equilibrium equations are given by:

.. math:: t_{ij}+ \rho b_{i} = 0

.. math:: \frac{\partial t_{x1x1}}{\partial x_1} + \frac{\partial t_{x1x2}}{\partial x_2} + \frac{\partial t_{x1x3}}{\partial x_3} + \rho b_{1} = 0

.. math:: \frac{\partial t_{x2x1}}{\partial x_1} + \frac{\partial t_{x2x2}}{\partial x_2} + \frac{\partial t_{x2x3}}{\partial x_3} + \rho b_{2} = 0

.. math:: \frac{\partial t_{x3x1}}{\partial x_1} + \frac{\partial t_{x3x2}}{\partial x_2} + \frac{\partial t_{x3x3}}{\partial x_3} + \rho b_{3} = 0

.. code:: python

    from sympy import *
    
    init_printing()
    
    x1,x2,x3,rho, b1,b2,b3 = symbols('x_1 x_2 x_3 rho b_1 b_2 b_3')
    
    t_x1x1 = x1**2 * x2
    t_x1x2 = x1*(1-x2**2)
    t_x1x3 = 0
    t_x2x1 = x1*(1-x2**2)
    t_x2x2 = (1/3)*(x2**2 - 3*x2)
    t_x2x3 = 0
    t_x3x1 = 0
    t_x3x2 = 0
    t_x3x3 = 2*x3**2
    

Now, we calculate the equilibrium equations with the necessary
derivatives, solving for every :math:`b_i`:

:math:`b_1`

.. code:: python

    solve(diff(t_x1x1,x1) + diff(t_x1x2,x2) + diff(t_x1x3,x3) + rho*b1,b1)




.. math::

    \displaystyle \left[ 0\right]



:math:`b_2`

.. code:: python

    solve(diff(t_x2x1,x1) + diff(t_x2x2,x2) + diff(t_x2x3,x3) + rho*b2,b2)




.. math::

    \displaystyle \left[ \frac{0.333333333333333 x_{2} \cdot \left(3.0 x_{2} - 2.0\right)}{\rho}\right]



:math:`b_3`

.. code:: python

    solve(diff(t_x3x1,x1) + diff(t_x3x2,x2) + diff(t_x3x3,x3) + rho*b3,b3)




.. math::

    \displaystyle \left[ - \frac{4 x_{3}}{\rho}\right]



Now, lets build our matrix :math:`t_{ij}` evaluated at
:math:`P(a,0,2\sqrt a)`

.. math::

    [t_{ij}] \Bigr|_P =
   \begin{bmatrix}
       a^2 \cdot 0 & a(1 - 0^2) & 0 \\
       a(1 - 0^2) & \frac{1}{3}(0^2 - 3\cdot 0) & 0 \\
       0 & 0 & 2(2\sqrt a)^2
   \end{bmatrix}

Then we have

.. math::

    [t_{ij}]\Bigr|_P =
   \begin{bmatrix}
       0 & a & 0 \\
       a & 0 & 0 \\
       0 & 0 & 8a
   \end{bmatrix}

.. code:: python

    import numpy as np
    a = symbols('a')
    t_P = np.array([[0,1,0],[1,0,0],[0,0,8]])
    np.linalg.eig(t_P)[0] * a




.. parsed-literal::

    array([1.0*a, -1.0*a, 8.0*a], dtype=object)



Now for the maximum shear strees at :math:`P(a,0,2\sqrt a)`, we know
that

.. math::  \sigma_s = \frac{1}{2} \left| \sigma_{max} - \sigma_{min} \right| 

.. code:: python

    (1/2) * abs(8*a - (-1*a))




.. math::

    \displaystyle 4.5 \left|{a}\right|



Finally, let’s find the principal deviator stresses at :math:`P`

We know that

.. math:: \sigma_M = \frac{t_{ij}}{3} = \frac{8a}{3} = \frac{T_{kk}}{3}

We define deviatoric stress to be

.. math::

    S = T\Bigr|_P - \frac{T_{kk}}{3} I, \quad
   [S] =
   \begin{bmatrix}
       -\frac{8}{3}a -s & a & 0 \\
       a & -\frac{8}{3}a -s & 0 \\
       0 & 0 & \frac{16a}{3} -s
   \end{bmatrix}

Now, in order to obtain the principal stresses, we do :math:`s=0`

.. math::

    [S] =
   \begin{bmatrix}
       -\frac{8}{3}a  & a & 0 \\
       a & -\frac{8}{3}a  & 0 \\
       0 & 0 & \frac{16a}{3} 
   \end{bmatrix}

.. code:: python

    S = np.array([[-8/3, 1,0],
                  [1,-8/3,0],
                  [0,0,16/3]])
    print(S)


.. parsed-literal::

    [[-2.66666667  1.          0.        ]
     [ 1.         -2.66666667  0.        ]
     [ 0.          0.          5.33333333]]
    

.. code:: python

    np.linalg.eig(S)[0] * a




.. parsed-literal::

    array([-1.66666666666667*a, -3.66666666666667*a, 5.33333333333333*a],
          dtype=object)



