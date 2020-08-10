import numpy as np

npart = 1000
nx =20
ny =20


s = (nx,ny) #setting matrix dimension

hyst = np.zeros(s) #float64
a = np.zeros(s, dtype=int)#int64

logical = True


#Geometry
al = 8 #domain dimension
ar = 1 #cylinder radius

dx = al/nx
dy = al/ny

dl = dx * 0.5 #verifica se ci passo



#introduce a cilinder
x_axis = range(nx) # from 0 to nx-1
y_axis = range(ny)# from 0 to ny-1
for ix in x_axis:
	for iy in y_axis:
		x = (ix*dx) + (0.5*dx)
		y = (iy*dy) + (0.5*dy)
		
		exist = (x - al/2)**2 + (y - al/2)**2
		
		if (((x - al/2)**2 + (y - al/2)**2) < (al*0.1)):
			a[ix,iy] = 2
			
		if (((x - al/2)**2 + (y - al/2)**2) < (al*0.095)):
			a[ix,iy] = 0
		#nozzle
		if(y > al * 0.6 and y < al * 0.7 and x > al * 0.7):
			a[ix,iy] = 2
		if(y > al * 0.62 and y < al * 0.68 and x > al * 0.72):
			a[ix,iy] = 0
		
		if(y > al * 0.3 and y < al * 0.4 and x > al * 0.7):
			a[ix,iy] = 2
		if(y > al * 0.32 and y < al * 0.38 and x > al * 0.72):
			a[ix,iy] = 0

with open('outfile.txt','wb') as f:
	for line in a:
		np.savetxt(f, line, fmt='%.2f')
