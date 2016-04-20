import numpy as np 
import matplotlib.pyplot as plt
import pandas as pd 

def scatter(x, y, alpha  =0.5, color = "r", save_file = "scatter_plot", format = "pdf", show = True, grid = False, xlabel = "x", ylabel = "y", title = "Scatter Plot"):
	'''
	input: X, Y
	output: scatter plot 
	'''
	fig = plt.Figure()
	fig.set_canvas(plt.gcf().canvas)
	plt.scatter(x,y, alpha=0.5,color = color)
	if grid:
		plt.grid(True)
	plt.xlabel(xlabel)
	plt.ylabel(ylabel)
	plt.title(title)
	if show:
		plt.show()
		
	fig.savefig(save_file + "." + format, format = format)