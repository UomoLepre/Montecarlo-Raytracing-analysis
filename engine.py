import numpy as np
import math, random

npart = 100
nx = 40
ny = 40

s = (nx, ny)  # setting matrix dimension

hyst = np.zeros(s)  # float64

a = np.zeros(s, dtype=int)  # int64

logical = True

# Geometry
al = 8  # domain dimension
ar = 1  # cylinder radius

dx = al / nx
dy = al / ny

dl = dx * 0.5  # verifica se ci passo

# introduce a cilinder
x_axis = range(nx)  # from 0 to nx-1
y_axis = range(ny)  # from 0 to ny-1

for i in x_axis:
	for j in y_axis:
		hyst[i,j] = 7
		
# exploring space
for ix in x_axis:
	for iy in y_axis:
		x = (ix * dx) + (0.5 * dx)
		y = (iy * dy) + (0.5 * dy)

		exist = (x - al / 2) ** 2 + (y - al / 2) ** 2

		if (((x - al / 2) ** 2 + (y - al / 2) ** 2) < (al * 0.1)):
		    a[ix, iy] = 2

		if (((x - al / 2) ** 2 + (y - al / 2) ** 2) < (al * 0.095)):
		    a[ix, iy] = 0

		# nozzle
		if (y > al * 0.6 and y < al * 0.7 and x > al * 0.7):
		    a[ix, iy] = 2
		if (y > al * 0.62 and y < al * 0.68 and x > al * 0.72):
		    a[ix, iy] = 0

		if (y > al * 0.3 and y < al * 0.4 and x > al * 0.7):
		    a[ix, iy] = 2
		if (y > al * 0.32 and y < al * 0.38 and x > al * 0.72):
		    a[ix, iy] = 0

escape = 0

pi = 3.1415926535
part = range(npart)  # from 0 to npart-1

#start move
for i in part:
	# implementing sources
	weight = 1  # initial weight
	x = al * 0.9
	y = al * 0.5
	z = 0
	mu = 2 * (random.uniform(0, 1)) - 1
	phi = 2 * pi * random.uniform(0, 1)



	while True:
		#print("i: ", i, " x: ", x, " y: ", y," mu: " , mu," phi: ", phi)
		st = math.sqrt(1 - (mu ** 2))

		deltaz = dl * mu
		deltax = dl * st * math.cos(phi)
		deltay = dl * st * math.sin(phi)

		xold = x
		yold = y
		zold = z

		x = x + deltax
		y = y + deltay
		z = z + deltaz

		# check for obstacles

		ix = int(x / dx)
		iy = int(y / dy) 
		
	
		
		if (ix >= 0 and ix < nx and iy >= 0 and iy < ny):
			hyst[ix, iy] = hyst[ix, iy] + weight
		'''
		# collisions with gas atoms
		if random.uniform(0, 1) < 1 - math.exp(-dl):
			mu = 2 * (random.uniform(0, 1) ) - 1
			phi = 2 * pi * random.uniform(0, 1)
			st = math.sqrt(1 - mu ** 2)
			'''
			
		
			
        	# am i out of domain?
		if (ix < 0 or ix >= nx-1 or iy < 0 or iy >= ny-1):
			break
		else:

			# am I inside absorbing obstacle?
			if (a[ix, iy] == 1):
				break

			# am I inside diffusing obstacle?
			if (a[ix, iy] == 2):
				while True:					
					x = xold
					y = yold
					z = zold

					mu = 2 * (random.uniform(0, 1)) - 1
					phi = 2 * pi * random.uniform(0, 1)
					st = math.sqrt(1 - mu ** 2)

					deltaz = dl * mu
					deltax = dl * st * math.cos(phi)
					deltay = dl * st * math.sin(phi)

					x = x + deltax
					y = y + deltay
					z = z + deltaz

					ix = int(x / dx) 
					iy = int(y / dy) 

					if (a[ix, iy] == 0):
						break

	escape = escape + weight

escape = escape / npart

#end move

#hyst = np.divide(hyst, npart * dx * (dy + 0.00001))

for ix in x_axis:
    for iy in y_axis:
        if (a[ix, iy] != 0):
            hyst[ix, iy] = -1

#Print Function
def matprint(mat, fmt="g"):
    col_maxes = [max([len(("{:"+fmt+"}").format(x)) for x in col]) for col in mat.T]
    for x in mat:
        for i, y in enumerate(x):
            print(("{:"+str(col_maxes[i])+fmt+"}").format(y), end="  ")
        print("")

matprint(hyst)	
