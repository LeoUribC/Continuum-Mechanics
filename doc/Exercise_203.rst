Exercise 20.3
=============

Show that the right side of (20.4) can be written as:

.. math::
   \rho \frac{ dv_j }{dt} = \frac{\partial}{\partial t} \left( \rho v_j \right) +
   \frac{\partial}{\partial x_i} \left( \rho v_i v_j \right) \tag{1}

and use this result to derive the equation for the balance of linear momentum for a
control volume fixed in space.


**Solving**
-----------

Note that (20.4) is given by:

.. math::
   \frac{ \partial \sigma_{ij} }{ \partial x_i } + \rho b_j = \rho \frac{ dv_j }{dt}

Taking the right side of :math:`(1)` by making the partial derivatives, the process
is as follows:

.. math::
    \begin{align}
        \frac{\partial}{\partial t} (\rho v_j) + \frac{\partial}{\partial x_i} (\rho v_i v_j) &= \\
        \rho\frac{\partial v_j}{\partial t} + v_j\frac{\partial \rho}{\partial t} +
        v_j\frac{\partial}{\partial x_i} (\rho v_i) + (\rho v_i)\frac{\partial v_j}{\partial x_i} &= \\
        v_j \left\{ \frac{\partial\rho}{\partial t} + \frac{\partial}{\partial x_i}(\rho v_i) \right\} +
        \rho \left\{ \frac{\partial v_j}{\partial t} + v_i\frac{\partial v_j}{\partial x_i} \right\} &= 
        \rho \frac{dv_j}{dt}
    \end{align}

Note that the first term vanishes because of mass conservation, leaving

.. math::
    \rho \left\{ \frac{\partial v_j}{\partial t} + v_i\frac{\partial v_j}{\partial x_i} \right\} = 
    \rho \frac{dv_j}{dt} \tag{2}

Now that we have this result, the next step is to consider all the forces acting
on a *control volume* for its balance of linear momentum fixed in space, which is
followed by the expression

.. math::
    \sum \vec{F} = \sum \vec{F}_{\text{body}} + \sum \vec{F}_{\text{surface}}


.. admonition:: Control surface and volume
    :class: tip

    A control surface is a surface that is defined to analyze the flow of a fluid or
    the behaviour of a continuous medium. The control surface can be arbitrarily
    selected to enclose a specific region. It can be an imaginary surface, such as a
    mathematical or geometric surface, or it can be a physical surface, like a wall,
    a plate, or an object. A control volume is a collection of points in space
    located within a closed control surface.


The expression above considers the **body force** :math:`\sum \vec{F}_{\text{body}}`
and the **surface forces** :math:`\sum \vec{F}_{\text{surface}}` which following
the continuum basis we already know they can be rewritten as

.. math::
    \sum \vec{F} = \int_{v(t)} \rho \text{b} dv + \int_{a(t)} \text{t} da \tag{3}

The surface forces can be either pressure, viscosity or others, in this case, we'll
only consider the **traction**. Note that this surface force is acting on the
surface that encloses the control volume, later it'll be necessary to apply the
divergence theorem to analize the volume.

Following the main objective, it is necessary to consider the Newton's Second Law
fixing the space for the volume, this is carried out by differentiating the linear
momentum and adding **the flux of momentum through the boundary into the volume**.
This is,

.. math::
    \sum \vec{F} = \frac{\partial}{\partial t} \int_{ \text{CV} } \rho\vec{ \text{v} } \; dv +
    \int_{ \text{CS} } \hat{\text{n}} \cdot \vec{ \text{v} } \left( \rho \vec{ \text{v} } \right) \; da
    \tag{4}

This considers the total flux of momentum through the control volume
(:math:`\text{CV}`) enclosed by a control surface (:math:`\text{CS}`).


.. admonition:: Flux of momentum
    :class: tip

    The net rate of momentum flow out of the control surface per unit mass flow rate
    (the flux of momentum through the boundary) refers to the amount of momentum
    flowing through a control surface relative to the mass flow passing through that
    surface.


We can now compare equations :math:`(3)` and :math:`(4)` as follows:

.. math::
    \begin{align}
        \int_{v(t)} \rho \text{b} \; dv + \int_{a(t)} \text{t} \; da &=
        \frac{\partial}{\partial t} \int_{ \text{CV} } \rho\vec{ \text{v} } \; dv +
        \int_{ \text{CS} } \hat{\text{n}} \cdot \vec{ \text{v} } \left( \rho \vec{ \text{v} } \right) \; da \\
        \int_{v(t)} \rho \text{b} \; dv + \int_{a(t)} \text{t} \; da -
        \int_{ \text{CS} } \hat{\text{n}} \cdot \vec{ \text{v} } \left( \rho \vec{ \text{v} } \right) \; da &=
        \frac{\partial}{\partial t} \int_{ \text{CV} } \rho\vec{ \text{v} } \; dv
    \end{align}

We must now apply the divergence theorem to all the parts that are expressed in terms
of the surface. To the term containing the traction, it is necessary to express it as
the definition with the stress tensor :math:`\sigma` and the normal direction
:math:`\hat{\text{n}}`. By doing so we have:

.. math::
    \begin{align}
        \int_{v(t)} \rho \text{b} \; dv + \int_{a(t)} \sigma \cdot \hat{\text{n}} \; da -
        \int_{\text{CV}} \nabla \cdot \left\{ \vec{ \text{v} } \left( \rho \vec{ \text{v} } \right) \right\} \; dv &=
        \frac{\partial}{\partial t} \int_{ \text{CV} } \rho\vec{ \text{v} } \; dv \\
        \int_{v(t)} \rho \text{b} \; dv + \int_{v(t)} \nabla \cdot \sigma \; dv -
        \int_{\text{CV}} \nabla \cdot \left\{ \vec{ \text{v} } \left( \rho \vec{ \text{v} } \right) \right\} \; dv &=
        \int_{ \text{CV} } \rho \frac{\partial}{\partial t} \vec{ \text{v} } \; dv
    \end{align}

Note that in the right term the derivative was moved inside the integral, this was
possible because of Reynold's Theorem. With this expression, we can now get rid of
all the integrals leading to the following form:

.. math::
    \rho\text{b} + \nabla\cdot\sigma - \nabla \cdot \left\{ \vec{\text{v}}(\rho\vec{\text{v}}) \right\} =
    \rho\frac{ \partial \vec{\text{v}} }{\partial t}

Rewritting the above with index notation we have

.. math::
    \rho b_j + \sigma_{ij,i} - \left\{ \vec{\text{v}}(\rho\vec{\text{v}}) \right\}_{,i} =
    \rho\frac{\partial v_j}{\partial t}

Applying the divergence to the third term and doing the development with index
notation, we have

.. math::
    \rho b_j + \sigma_{ij,i} - \left\{ v_{j,i}\left( \rho v_i \right) + v_j\left( \rho v_i \right)_{,i} \right\} =
    \rho\frac{\partial v_j}{\partial t}

Writting the divergence with the operand :math:`\partial/\partial x_i` the expression
is as follows:

.. math::
    \rho b_j + \sigma_{ij,i} - \left\{ \left( \rho v_i \right)\frac{\partial v_j}{\partial x_i} + v_j \frac{\partial}{\partial x_i} \left( \rho v_i \right) \right\} =
    \rho\frac{\partial v_j}{\partial t} \tag{5}

Now, using :math:`(2)` we can leave the term containing the time partial derivative
on the left side and replace the expression on the right side of :math:`(5)`, leaving
that

.. math::
    \rho b_j + \sigma_{ij,i} - \left\{ \left( \rho v_i \right)\frac{\partial v_j}{\partial x_i} + v_j \frac{\partial}{\partial x_i} \left( \rho v_i \right) \right\} =
    \rho\frac{d v_j}{d t} - \left( \rho v_i \right) \frac{\partial v_j}{\partial x_i}

Note that the last term of the right side vanishes with the same term on the left,
leaving the expression

.. math::
    \rho b_j + \sigma_{ij,i} - v_j \frac{\partial}{\partial x_i} \left( \rho v_i \right) =
    \rho\frac{d v_j}{d t}

In this last form, we can rewrite the partial derivative in index notation, or we can
rewrite all the expression into conventional notation, this is:

.. math::
    \begin{align}
        \rho b_j + \sigma_{ij,i} - v_j \left( \rho v_i \right)_{,i} =
        \rho\frac{d v_j}{d t} \qquad& \text{Index notation} \\
        \rho\mathbf{b} + \nabla \cdot \overline{\overline{\mathbf{\sigma}}} - \mathbf{v}\nabla\cdot\left( \rho \mathbf{v} \right) =
        \rho\mathbf{\dot{v}} \qquad& \text{Conventional notation}
    \end{align}

This equation shows how body forces, stress and flux of velocity in the medium that
transports the linear momentum in a particular direction affects its rate of change,
showing that the right side of (20.4) could be rewritten as stated in the problem by
obtaining the equation for the balance of linear momentum for a control volume
fixed in space.