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


def annoted_scatter_plot(x, y, alpha  =0.5, color = "r", save_file = "scatter_plot", format = "pdf", show = True, grid = False, xlabel = "x", ylabel = "y", title = "Scatter Plot"):
	fig = plt.figure(1,figsize =(8,5))
	ax = fig.add_subplot(111,autoscale_on = False,xlim=(-1, 5), ylim=(-4, 3))
	line, = ax.plot(x,y,lw = 3, color = 'purple')
	from matplotlib.patches import Ellipse
	el = Ellipse((2, -1), 0.5, 0.5)
	ax.add_patch(el)
	'''
	more styles can be viewd here: [matplotlib.pyplot.axvline](http://matplotlib.org/api/pyplot_api.html#matplotlib.pyplot.axvline)
	source code can be viewed here: [http://matplotlib.org/mpl_examples/pylab_examples/annotation_demo2.py]
	'''
	ax.annotate('arrowstyle', xy=(0, 1), xycoords='data',
                xytext=(-50, 30), textcoords='offset points',
                arrowprops=dict(arrowstyle="->")
                )
	ax.annotate('arc3', xy=(0.5, -1), xycoords='data',
                xytext=(-30, -30), textcoords='offset points',
                arrowprops=dict(arrowstyle="->",
                                connectionstyle="arc3,rad=.2")
                )
	ax.annotate('fancy', xy=(2., -1), xycoords='data', xytext=(-100, 60), textcoords='offset points',size=20, arrowprops=dict(arrowstyle="fancy", fc="0.6", ec="none",patchB=el,connectionstyle="angle3,angleA=0,angleB=-90"),)
	plt.show()

def main():

	t = np.arange(0.0, 5.0, 0.01)
	s = np.cos(2*np.pi*t)
	annoted_scatter_plot(t,s)

if __name__ == "__main__":
	main()