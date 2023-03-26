New wild notebook appeared!
===========================

We’re going to try the compatibility between the jupyter notebooks and
the docs in the files. so let’s try out some testing notebook!

.. code:: ipython3

    import numpy as np
    import sympy as sp
    import matplotlib.pyplot as plt

.. code:: ipython3

    time = np.arange(0, 2*np.pi+0.1, 0.1)
    
    plt.plot(time, np.sin(time))
    plt.grid(); plt.xlabel("time (s)"); plt.ylabel("sin() function")
    plt.show()



.. image:: /source/notebook_files/notebook_2_0.png


Let’s try out some latex:

.. math::  \lim_{h \to 0} \frac{f(x + h) - f(x)}{h} = \frac{df(x)}{dx} 

.. code:: ipython3

    # function with derivative
    x = sp.symbols('x')
    y = sp.exp(2*x) + x**2
    
    y.diff(x)  # 1st order derivative




.. math::

    \displaystyle 2 x + 2 e^{2 x}


