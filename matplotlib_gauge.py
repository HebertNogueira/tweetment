import os, sys
import matplotlib
from matplotlib import cm
from matplotlib import pyplot as plt
import numpy as np
from matplotlib.patches import Circle, Wedge, Rectangle

class MatplotlibGauge:

	def gauge(polarity=1, tweetWord=False): 

		# COnversao da polaridade para a posicao da seta
		gauge_arrow = float(polarity+100.01)
		gauge_arrow = int(gauge_arrow*100)
		gauge_arrow = int(gauge_arrow-9900)
	
		N = 201 #Quantidade de posicoes no Gauge
		colors='RdYlGn' #Colormap para as cores do Gauge

		#Realiza o gradiente de cores
		cmap = cm.get_cmap(colors, N)
		cmap = cmap(np.arange(N))
		colors = cmap[::-1,:].tolist()

		fig, ax = plt.subplots()

		start = np.linspace(0,180,N+1, endpoint=True)[0:-1]
		end = np.linspace(0,180,N+1, endpoint=True)[1::]
		mid_points = start + ((end-start)/2.)
		degree_range = np.c_[start, end], mid_points


		ang_range, mid_points = degree_range

		patches = []
		for ang, c in zip(ang_range, colors): 
			# sectors
			patches.append(Wedge((0.,0.), .4, *ang, facecolor='w', lw=2))
			# arcs
			patches.append(Wedge((0.,0.), .4, *ang, width=0.10, facecolor=c, lw=2, alpha=0.8))

		[ax.add_patch(p) for p in patches]

		# Configuracoes da seta
		pos = mid_points[abs(gauge_arrow - N)]

		ax.arrow(0, 0, 0.260 * np.cos(np.radians(pos)), 0.260 * np.sin(np.radians(pos)), \
					width=0.02, head_width=0.02, head_length=0.05, fc='444', ec='444')
		ax.add_patch(Circle((0, 0), radius=0.01, facecolor='444'))

		ax.set_frame_on(False)
		ax.axes.set_xticks([])
		ax.axes.set_yticks([])
		ax.axis('equal')
		plt.tight_layout()
		if (tweetWord != False):
			print (os.getcwd())
			fig.savefig(os.getcwd() + '/static/img/gauge', dpi=100)
		return tweetWord