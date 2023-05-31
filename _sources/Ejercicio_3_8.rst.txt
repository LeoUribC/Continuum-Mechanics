**Exercise 3.8**
================

Relative to the cartesian axes :math:`Ox_1x_2x_3` a stress field is
given by the matrix

.. math::

   [t_{ij}] =
   \begin{bmatrix}
       (1-x_1^2)x_2 + \frac{2}{3}x_2^3  &  -(4 - x_2^2)x_1 & 0 \\
       -(4 - x_2^2)x_1  &  -\frac{1}{3}(x_2^3 - 12x_2)  &  0 \\
       0  &  0  & (3 - x_1^2)x_2
   \end{bmatrix}

(a) Show that the equilibrium ase satisfied everywhere for zero body
    forces
(b) Determine the stress vector at the point :math:`P(2,-1,6)` of the
    plane whose equation is :math:`3x_1 + 6x_2 + 2x_3 = 12`.

Solving
-------

(a) The equilibrium equations are:

.. math:: \frac{\partial \sigma_{x1x1}}{\partial x_1} + \frac{\partial \sigma_{x1x2}}{\partial x_2} + \frac{\partial \sigma_{x1x3}}{\partial x_3} + fx_1 = 0

.. math:: \frac{\partial \sigma_{x2x1}}{\partial x_1} + \frac{\partial \sigma_{x2x2}}{\partial x_2} + \frac{\partial \sigma_{x2x3}}{\partial x_3} + fx_2 = 0

.. math:: \frac{\partial \sigma_{x3x1}}{\partial x_1} + \frac{\partial \sigma_{x3x2}}{\partial x_2} + \frac{\partial \sigma_{x3x3}}{\partial x_3} + fx_3 = 0

As we have zero body forces, then:

.. math:: fx_1 = fx_2 + fx_3 = 0

As we’re working with symbolic and numerical python libraries, let’s
import them and declare the equations listed above:

.. code:: python

    from sympy import *
    import numpy as np
    
    init_printing()
    
    x1,x2,x3,e1,e2,e3 = symbols('x_1 x_2 x_3 e_1 e_2 e_3')
    
    sigma_x1x1 = (1 - x1**2)*x2 + (2/3)*x2**3
    sigma_x1x2 = - x1*(4-x2**2)
    sigma_x1x3 = 0
    
    sigma_x2x1 = -(4 - x2**2)*x1
    sigma_x2x2 = -(1/3)*(x2**3 - 12*x2)
    sigma_x2x3 = 0
    
    sigma_x3x1 = 0
    sigma_x3x2 = 0
    sigma_x3x3 = (3-x1**2)*x2
    
    fx1,fx2,fx3 = 0,0,0

Let’s calculate derivatives and equilibrium equations:

.. code:: python

    diff(sigma_x1x1,x1) + diff(sigma_x1x2,x2) + diff(sigma_x1x3,x3) + fx1




.. math::

    \displaystyle 0



.. code:: python

    diff(sigma_x2x1,x1) + diff(sigma_x2x2,x2) + diff(sigma_x2x3,x3) + fx2




.. math::

    \displaystyle 0



.. code:: python

    diff(sigma_x3x1,x1) + diff(sigma_x3x2,x2) + diff(sigma_x3x3,x3) + fx3




.. math::

    \displaystyle 0



As seen, all results were 0, then, for zero body forces the equilibrium
equations work as expected.

(b) The direction cosines of the plane are:

.. code:: python

    l = 3/np.sqrt(3**2 + 6**2 + 2**2)
    l




.. math::

    \displaystyle 0.428571428571429



.. code:: python

    m = 6/np.sqrt(3**2 + 6**2 + 2**2)
    m




.. math::

    \displaystyle 0.857142857142857



.. code:: python

    n = 2/np.sqrt(3**2 + 6**2 + 2**2)
    n




.. math::

    \displaystyle 0.285714285714286



Now, let’s take the point :math:`P(2,-1,6)`

.. code:: python

    x_1 = 2
    x_2 = -1
    x_3 = 6

.. code:: python

    sigmax1x1 = sigma_x1x1.subs([(x1,x_1),(x2,x_2),(x3,x_3)])
    sigmax1x1




.. math::

    \displaystyle 2.33333333333333



.. code:: python

    sigmax1x2 = sigma_x1x2.subs([(x1,x_1),(x2,x_2),(x3,x_3)])
    sigmax1x2




.. math::

    \displaystyle -6



.. code:: python

    sigmax2x1 = sigma_x2x1.subs([(x1,x_1),(x2,x_2),(x3,x_3)])
    sigmax2x1




.. math::

    \displaystyle -6



.. code:: python

    sigmax2x2 = sigma_x2x2.subs([(x1,x_1),(x2,x_2),(x3,x_3)])
    sigmax2x2




.. math::

    \displaystyle -3.66666666666667



.. code:: python

    sigmax3x3 = sigma_x3x3.subs([(x1,x_1),(x2,x_2),(x3,x_3)])
    sigmax3x3




.. math::

    \displaystyle 1



Finally, with calculated values and directions cosines, we have:

.. code:: python

    sigmax = sigmax1x1*l + sigmax1x2*m + 0*n
    sigmax




.. math::

    \displaystyle -4.14285714285714



.. code:: python

    sigmay = sigmax2x1*l + sigmax2x2*m + 0*n
    sigmay




.. math::

    \displaystyle -5.71428571428571



.. code:: python

    sigmaz = 0*l + 0*m + sigmax3x3*n
    sigmaz




.. math::

    \displaystyle 0.285714285714286



.. code:: python

    sigmax*e1 + sigmay*e2 + sigmaz*e3




.. math::

    \displaystyle - 4.14285714285714 e_{1} - 5.71428571428571 e_{2} + 0.285714285714286 e_{3}


