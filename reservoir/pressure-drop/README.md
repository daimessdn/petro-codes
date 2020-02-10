# Calculating pressure value for transient, radial flow, and slightly compressible fluid

![diffusivity eq](https://render.githubusercontent.com/render/math?math=%5Cfrac%20%7B%5Cdelta%5E2%20p%7D%20%7B%5Cdelta%20y%5Er%7D%20%2B%20%5Cfrac%201%20r%20%5Cfrac%20%7B%5Cdelta%20p%7D%20%7B%5Cdelta%20r%7D%20%3D%20%5Cfrac%20%7B%20%5Cphi%20%5Cmu%20c_t%20%7D%20%7B0.0002637%20k%7D%20%5Cfrac%20%7B%5Cdelta%20p%7D%20%7B%5Cdelta%20r%7D)

The equation above is the **diffusivity eqution** in case of radial flow (Craft and Hawkins: 1991: 235). To get the solution of equation, firstly we need one initial condition and two boundary conditions.

- Initial condition: ![IC](https://render.githubusercontent.com/render/math?math=t%20%3D%200%2C%20p%20%3D%20pi)
- First boundary condition: ![IBC](https://render.githubusercontent.com/render/math?math=r%20%3D%20rw%2C%20q%20%3D%20-0.001127%20%5Cfrac%20%7Bk%20h%7D%20%7BB%20%5Cmu%7D%20(2%5Cpi%20r)%20%5Cleft(%5Cfrac%20%7B%5Cdelta%20p%7D%20%7B%5Cdelta%20r%7D%5Cright)_%7Br%20%3D%20rw%7D)
- Second boundary condition: ![OBC](https://render.githubusercontent.com/render/math?math=r%20%3D%20%5Cinfty%2C%20p%20%3D%20p_i)

Matthew and Russell (referenced on Craft and Hawkins, 1991: 235) gave the solution:

<br />
![p (r, t) = p_i - \frac {70.6 q \mu B} {k h} \left\[-E_i \left(- \frac {\phi \mu c_t r^2}{0.00105 k t} \right) \right\]](https://render.githubusercontent.com/render/math?math=p%20(r%2C%20t)%20%3D%20p_i%20-%20%5Cfrac%20%7B70.6%20q%20%5Cmu%20B%7D%20%7Bk%20h%7D%20%5Cleft%5B-E_i%20%5Cleft(-%20%5Cfrac%20%7B%5Cphi%20%5Cmu%20c_t%20r%5E2%7D%7B0.00105%20k%20t%7D%20%5Cright)%20%5Cright%5D)

where 