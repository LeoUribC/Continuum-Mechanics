**Exercise 1**
==============

Let’s deduce the maximum shear stress equations and values. Let us begin
by defining the form of the traction tensor
:math:`\text{t}^{ (\hat{\text{n}}) }` and use it to define the normal
stress value. This is given by:

.. math::  \text{t}^{ (\hat{\text{n}}) } = \text{T} \cdot \hat{\text{n}}, \quad \text{then} \quad \sigma_N = \text{t}^{ (\hat{\text{n}}) } \cdot \hat{ \text{n} } 

From this, we can see that if

.. math::  \text{t}^{ (\hat{\text{n}}) } = \sigma_I n_1 \hat{e}_1^* + \sigma_{II} n_2 \hat{e}_2^* + \sigma_{III} n_3 \hat{e}_3^* 

Then

.. math::  \sigma_N = \sigma_{I}n_1^2 + \sigma_{II}n_2^2 + \sigma_{III}n_3^2 \tag{1} 

We’ll use ``sympy`` library to determine this first result. Importing
this library along ``numpy`` for other calculations:

.. code:: ipython3

    import sympy as sp
    import numpy as np

Now, we proceed to declare symbolic variables that we’ll use from now on
in this problem:

.. code:: ipython3

    s1, s2, s3, n1, n2, n3 = sp.symbols('\sigma_{I}, \sigma_{II}, \sigma_{III}, n_1, n_2, n_3')
    
    # declaring the normal vector and the stress tensor
    n = sp.Matrix([n1, n2, n3])
    
    tij = sp.Matrix(
        [
            [s1, 0, 0],
            [0, s2, 0],
            [0, 0, s3]
        ]
    )
    
    # traction vector
    tin = tij*n
    tin




.. math::

    \displaystyle \left[\begin{matrix}\sigma_{I} n_{1}\\\sigma_{II} n_{2}\\\sigma_{III} n_{3}\end{matrix}\right]



After doing the calculation to find :math:`\sigma_N` we have:

.. code:: ipython3

    # finding normal stress value
    sn = tin.T*n  # it's necessary to transpose the traction
    sn = sn[0]  # extracting the only element in the remaining result
    sn




.. math::

    \displaystyle \sigma_{III} n_{3}^{2} + \sigma_{II} n_{2}^{2} + \sigma_{I} n_{1}^{2}



Now, knowing the definition of the **shear stress componen**
:math:`\sigma_S` as:

.. math::  \sigma_S^2 = \text{t}_i^{ (\hat{ \text{n} }) }\text{t}_i^{ (\hat{ \text{n} }) } - \sigma_N^2 

Let’s construct this component:

.. code:: ipython3

    # calculation of shear stress component
    ss = (tin.T*tin)[0] - sn**2
    ss




.. math::

    \displaystyle \sigma_{III}^{2} n_{3}^{2} + \sigma_{II}^{2} n_{2}^{2} + \sigma_{I}^{2} n_{1}^{2} - \left(\sigma_{III} n_{3}^{2} + \sigma_{II} n_{2}^{2} + \sigma_{I} n_{1}^{2}\right)^{2}



We now know may express :math:`n_3^2` in terms of :math:`n_1, n_2`
knowing that :math:`n_i n_i = 1`, :math:`n_3^2` becomes
:math:`n_3^2 = 1 - n_1^2 - n_2^2`. With this in mind we have:

.. code:: ipython3

    # substitute in ss where values are n_3 for the expression above
    ss = ss.subs( n3, 1-n1**2-n2**2 )
    ss




.. math::

    \displaystyle \sigma_{III}^{2} \left(- n_{1}^{2} - n_{2}^{2} + 1\right)^{2} + \sigma_{II}^{2} n_{2}^{2} + \sigma_{I}^{2} n_{1}^{2} - \left(\sigma_{III} \left(- n_{1}^{2} - n_{2}^{2} + 1\right)^{2} + \sigma_{II} n_{2}^{2} + \sigma_{I} n_{1}^{2}\right)^{2}



In order to get the *stationary*, we must find the derivatives and equal
them to 0 and solve the resultating system. This with the help of sympy
becomes:

.. code:: ipython3

    # finding the derivatives of ss respect with n1 and n2
    # then simplifying the expression
    ss_n1 = ss.diff(n1).simplify()
    ss_n2 = ss.diff(n2).simplify()
    
    # defining the system
    ss_n1_equation = sp.Eq(ss_n1, 0)
    ss_n2_equation = sp.Eq(ss_n2, 0)
    
    display(ss_n1_equation, ss_n2_equation)



.. math::

    \displaystyle 2 n_{1} \cdot \left(2 \sigma_{III}^{2} \left(n_{1}^{2} + n_{2}^{2} - 1\right) + \sigma_{I}^{2} - 2 \cdot \left(2 \sigma_{III} \left(n_{1}^{2} + n_{2}^{2} - 1\right) + \sigma_{I}\right) \left(\sigma_{III} \left(n_{1}^{2} + n_{2}^{2} - 1\right)^{2} + \sigma_{II} n_{2}^{2} + \sigma_{I} n_{1}^{2}\right)\right) = 0



.. math::

    \displaystyle 2 n_{2} \cdot \left(2 \sigma_{III}^{2} \left(n_{1}^{2} + n_{2}^{2} - 1\right) + \sigma_{II}^{2} - 2 \cdot \left(2 \sigma_{III} \left(n_{1}^{2} + n_{2}^{2} - 1\right) + \sigma_{II}\right) \left(\sigma_{III} \left(n_{1}^{2} + n_{2}^{2} - 1\right)^{2} + \sigma_{II} n_{2}^{2} + \sigma_{I} n_{1}^{2}\right)\right) = 0


Solving the system for :math:`n_1, n_2` we have:

.. code:: ipython3

    # solving for n1, n2
    sp.solve([ss_n1_equation, ss_n2_equation], [n1, n2], implicit=True)




.. parsed-literal::

    {n_1: 0, n_2: 0}



As expected, this is a trivial solution for the system. If we take
:math:`n_1=0` for both equations, let’s see the results for :math:`n_2`:

.. code:: ipython3

    # taking n1=0
    ss_n1_equation = ss_n1_equation.subs(n1, 0)
    ss_n2_equation = ss_n2_equation.subs(n1, 0)
    
    # solving for n2
    sp.solve([ss_n2_equation, ss_n1_equation], n2, implicit=True)




.. parsed-literal::

    {n_2: 0}



