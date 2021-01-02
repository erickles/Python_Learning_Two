# Code to be executed in Jupiter Notebook

from ipywidgets import interact, interactive, fixed
import ipywidgets as widgets

def func(x):
    return x**2

interact(func,x='hello')

interact(func,x=10)

interact(func,x=True)

@interact(x=True,y=fixed(1.0))
def g(x,y):
    return (x,y)

interact(func,x=widgets.IntSlider(min=-100,max=100,step=1,value=0))

interact(func,x=(-10,10,1))

@interact(x=(0.0,20.0,0.5))
def h(x=5.0):
    return x

interact(func,x=['hello','option 2','option 3'])

interact(func,x={'one':10,'two':20})

from iPython.display import display
def f(a,b):
    display(a+b)
    return a+b

type(w)

w.children

display(w)

#######################

w = widgets.IntSlider()

from IPython.display import display
display(w)

w.close()

from IPython.display import display
display(w)

print(w.value)

print(w.keys)

w.max = 2000

a = widgets.FloatText()
b = widgets.FloatSlider()

display(a,b)

mylink = widgets.jslink((a,'value'),(b,'value'))

mylink.unlink()

############################################
w = widgets.IntSlider()
display(w)

w.layout.margin = 'auto'
w.layout.height = '75px'

x = widgets.IntSlider(value=15,description='New Slider')
display(x)

x.layout = w.layout

widgets.Button(description='Ordinary Button',button_style='danger')

b1 = widgets.Button(description='Custom Color')

b1.style.button_color = 'lightgreen'

b2 = widgets.Button(description='New')

b2.style = b1.style

s1 = widgets.IntSlider(value=15,description='My Handle')
s1.style.handle_color = 'lightblue'

################################################

# Install the modules below
# pip install NumPy
# pip install Matplotlib
# pip install SciPy

# %matplotlib

# from ipywidgets import interact, interactive
# from IPython.display import clear, output, display, HTML

# import numpy as np
# from scipy import integrate

# from matplotlib import pyplot as plt
# from mpl_toolkits.mplot3d import Axes3D
# from matplotlib.colors import cnames
# from matplotlib import animation







