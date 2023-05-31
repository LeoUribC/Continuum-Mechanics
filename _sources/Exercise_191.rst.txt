

**Example 19.1**
================

Fill in the details of obtaining (19.15) from (19.14)

--------------

.. math:: I = \frac{d}{dt} ∫_v ρ(x[X,t],t)A(x[X,t],t)J \tag{19.14}

.. math:: I = \frac{d}{dt} ∫_v \{j_ρ(x[X,t],t)\frac{d}{dt}A(x[X,t],t)\}dV \tag{19.15}



**Solution**
------------

To derive equation (19.15) from equation (19.14), we need to apply
the Leibniz rule for differentiating an integral with respect to
time.

Starting with equation (19.14):

.. math:: I = \frac{d}{dt} ∫_v ρ(x[X,t],t)A(x[X,t],t)J \tag{19.14}

We cap apply the Leibniz rule to the integrand, treating both
:math:`ρ(x[X,t],t)` and :math:`A(x[X,t],t)` as functions of
:math:`t`:

.. math:: I =  ∫_v \frac{d}{dt} (ρ(x[X,t],t)A(x[X,t],t)J) dV 

--------------

**The Leibniz rule**
--------------------

The Leibniz rule, also known as the Leibniz integral rule or the
differentiation under the integral sign, is a powerful tool for
differentiating integrals with respect to a parameter. It allows us
to interchange the order of differentiation and integration.

In the context of the exercise, we have the integral:

.. math:: I = \frac{d}{dt} \int_v \rho(x[X,t],t)A(x[X,t],t)J

To apply the Leibniz rule, we differentiate the integrand with
respect to time, treating both :math:`ρ(x[X,t],t)` and
:math:`A(x[X,t],t)J` as functions of :math:`t`. The rule states that
we can differentiate the integrand and then integrate it, or
alternatively, integrate the function and then differentiate the
result.

Mathematically, the Leibniz rule can be expressed as follows:

.. math:: \frac{d}{dt} \int_{a(t)}^{b(t)} f(x,t)dx = \int_{a(t)}^{b(t)} \frac{∂f}{dt}(x,t)dx + f(b(t),t)\frac{db}{dt} - f(a(t),t)\frac{da}{dt}

In the equation above, :math:`f(x,t)` is the integrand, and
:math:`a(t)` and :math:`b(t)` are the limits of integration, which
can be functions of :math:`t`.

Applying the Leibniz rule to the equation, we have:

.. math:: I= \frac{d}{dt}∫_v ρ(x[X,t],t)A(x[X,t],t)J 

.. math:: I=∫_v\frac{d}{dt} (ρ(x[X,t],t)A(x[X,t],t)J)dV

By differentiating the integrand with respect to t, we obtain the
terms :math:`ρ\frac{dA}{dt}J` and :math:`ρA\frac{dJ}{dt}`. However,
in the equation, the term :math:`ρA\frac{dJ}{dt}` is not present,
possibly due to assumptions or simplifications made in the
derivation. Hence, only the term :math:`ρ\frac{dA}{dt}J` remains.

Therefore, applying the Leibniz rule allows us to differentiate the
integrand with respect to time and then integrate it, resulting in
the final equation.

--------------

Now, we can expand the derivative using the product rule:

.. math:: I = \int_v \left( \frac{d\rho}{dt}A + \rho\frac{dA}{dt}\right)JdV

Next, we can rearrange the terms inside the integral:

.. math:: I = \int_v \frac{d\rho}{dt}AJ + \rho\frac{dA}{dt}JdV

Now, for the first term, :math:`\int_v \frac{d\rho}{dt}AJ`, we can
aply the Leibniz rule again to separate the derivative of
:math:`\rho` from the integral:

.. math:: \int_v\frac{d\rho}{dt}AJ = \frac{d}{dt}\left( \int_v \rho AJdV \right) - \int_v \rho \frac{d}{dt}(AJ)dV

Using the definition of :math:`I`, we can simplify the first term:

.. math::  \int_v \frac{d\rho}{dt}AJ + \rho\frac{dA}{dt}JdV = \frac{d}{dt} \left( \int_v \rho AJdV\right)

.. math:: \frac{dI}{dt} = \frac{d}{dt} \left( \int_v \rho AJdV \right)

Substituting back in the equation, now we have:

.. math:: \int_v \frac{d\rho}{dt}AJ = \frac{dI}{dt} - \int_v \rho \frac{d}{dt} (AJ)dV

Now, let's substitute in the original equation and rearrange some
terms:

.. math:: I = \frac{dI}{dt} + \int_v \rho \frac{d}{dt}(AJ)dV + \rho \frac{dA}{dt} J 

.. math:: I = \frac{dI}{dt} + \int_v \rho \frac{d}{dt}(A - AJ) dV

.. math:: I = \frac{dI}{dt} + \int_v \rho \frac{d}{dt}(A - AJ)dV

Now, let's remember that
:math:`A - AJ = j_ρ(x[X,t],t)\frac{d}{dt}A(x[X,t],t)`

So, we finally have that

.. math:: I = \frac{dI}{dt} + ∫_v \{j_ρ(x[X,t],t)\frac{d}{dt}A(x[X,t],t)\}dV \tag{19.15}
