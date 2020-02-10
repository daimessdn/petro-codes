# Calculating pressure value for transient, radial flow, and slightly compressible fluid

## Theorem basis

![diffusivity eq](https://render.githubusercontent.com/render/math?math=%5Cfrac%20%7B%5Cdelta%5E2%20p%7D%20%7B%5Cdelta%20y%5Er%7D%20%2B%20%5Cfrac%201%20r%20%5Cfrac%20%7B%5Cdelta%20p%7D%20%7B%5Cdelta%20r%7D%20%3D%20%5Cfrac%20%7B%20%5Cphi%20%5Cmu%20c_t%20%7D%20%7B0.0002637%20k%7D%20%5Cfrac%20%7B%5Cdelta%20p%7D%20%7B%5Cdelta%20r%7D)

The equation above is the **diffusivity eqution** in case of radial flow (Craft *et al*: 1991: 235). To get the solution of equation, firstly we need one initial condition and two boundary conditions.

- Initial condition: ![IC](https://render.githubusercontent.com/render/math?math=t%20%3D%200%2C%20p%20%3D%20pi)
- First boundary condition: ![IBC](https://render.githubusercontent.com/render/math?math=r%20%3D%20rw%2C%20q%20%3D%20-0.001127%20%5Cfrac%20%7Bk%20h%7D%20%7BB%20%5Cmu%7D%20(2%5Cpi%20r)%20%5Cleft(%5Cfrac%20%7B%5Cdelta%20p%7D%20%7B%5Cdelta%20r%7D%5Cright)_%7Br%20%3D%20rw%7D)
- Second boundary condition: ![OBC](https://render.githubusercontent.com/render/math?math=r%20%3D%20%5Cinfty%2C%20p%20%3D%20p_i)

Matthew and Russell (referenced on Craft *et al*, 1991: 235) gave the solution for determining the pressure after the pressure drop:
<br />

![p (r, t) = p_i - \frac {70.6 q \mu B} {k h} \left\[-E_i \left(- \frac {\phi \mu c_t r^2}{0.00105 k t} \right) \right\]](https://render.githubusercontent.com/render/math?math=p%20(r%2C%20t)%20%3D%20p_i%20-%20%5Cfrac%20%7B70.6%20q%20%5Cmu%20B%7D%20%7Bk%20h%7D%20%5Cleft%5B-E_i%20%5Cleft(-%20%5Cfrac%20%7B%5Cphi%20%5Cmu%20c_t%20r%5E2%7D%7B0.00105%20k%20t%7D%20%5Cright)%20%5Cright%5D)

where p<sub>i</sub> = initial pressure (psia), q = flow rate (STB/day), μ = viscosity (centipoise), B = formation volume factor (bbl/STB), k = permeability (mD), h = depth (feet), ɸ = porosity (pore / bulk volume ratio), c<sub>t</sub> = isothermal compressibility (1/psi), and t = time (hour).

E<sub>i</sub> is the exponential integral function that is denoted by:
<br />

![-E_i(-x) = \int_{x}^{\infty} \frac {e^{-u} du} {u} = ln(x) + \sum_{n=1}^{\infty} \frac{(-x)^n}{n(n!)}](https://render.githubusercontent.com/render/math?math=-E_i(-x)%20%3D%20%5Cint_%7Bx%7D%5E%7B%5Cinfty%7D%20%5Cfrac%20%7Be%5E%7B-u%7D%20du%7D%20%7Bu%7D%20%3D%20ln(x)%20%2B%20%5Csum_%7Bn%3D1%7D%5E%7B%5Cinfty%7D%20%5Cfrac%7B(-x)%5En%7D%7Bn(n!)%7D)

where ![x = \frac {\phi \mu c_t r^2}{0.00105 k t}](https://render.githubusercontent.com/render/math?math=x%20%3D%20%5Cfrac%20%7B%5Cphi%20%5Cmu%20c_t%20r%5E2%7D%7B0.00105%20k%20t%7D)

This program is used to calculate the pressure after got pressure drop based on this theorem with certain time and radius. This program uses **Python 3** with several libraries used: **matplotlib** for creating and showing graphs, **numpy** in this case for saving the calculation results in .csv format, **scipy** in this case for exponential integral function so that we don't need to make the E<sub>i</sub> algorithm, and **math** for the basic mathematical case such as power, exponential (e), trigonometric functions, etc.

## Main program structure
- `problem719-2.py`: main program
- `graph` folder: stores the graphs in normal and semilog scale
- `tables` display the calculation results of tables, including
	- `x-value.csv`: shows x-value results
	- `E-value.csv`: shows Ei-value results
	- `pressure-drop.csv`: shows pressure results

## Usage procedure
In assumptions that we have Python installed,
1. Download the program named "problem719-2.py". You can download this program by clicking that program's file name on this repository, then click "Raw", and "Ctrl + S" for saving the program.
2. Download the "input.in" file. Steps for download the file are same as step 1 given. Put the file along with the "problem719-2.py" program.
3. Create the folder named "graph" and "tables" beside the two files. These are useful for store the graph and table result
4. You can modify the parameter value such as k or h values (or many values) by opening the program with text editor and modify the value.
5. You can modify the time and radius input by clicking "input.in" in text editor and modify them like this.
```py
2		# amount of times, don't type this comment
1		# value of time 1, don't type this comment
10		# value of time 1, don't type this comment
3		# amount of radius, don't type this comment
1		# value of radius 1, don't type this comment
5		# value of radius 2, don't type this comment
10		# value of radius 3, don't type this comment
```
6. Run Terminal or Command Prompt
7. Install Python libraries by typing `pip install matplotlib numpy scipy`
8. Run the program by typing `python problem719-2.py < input.in` (Pyhton 2.7) or `python3 problem719-2.py < input.in` (Pyhton 3)

## Output parameters
The program will create x-value, Ei-value, and pressure result in .csv files named `x-value.csv`, `E-value.csv`, and `pressure-drop.csv` in `tables` folder and also graph pictures in .png files named `normal.png` and `semilog.png` in `graph` folder.

## Reference
Craft, B. C., Murray F. Hawkins, and Ronald E. Terry. 1991. Applied petroleum reservoir engineering. Englewood Cliffs, N.J.: Prentice Hall.