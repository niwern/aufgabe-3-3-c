import math
import csv

h = 1.6	# in Metern
v = 10 	# in Metern pro Sekunde
g = 9.81	# in Metern pro Sekunde im Quadrat
winkel = []	# Liste mit Winkeln
sx = []	# Liste mit Reichweiten
dStats = [] # Genauigkeit



def abs(a):
	if a < 0:
		return -a
	return a

def getMax(a, b):
	if a > b:
		return a
	return b	

def frange(x, y, jump):
    while x < y:
    	winkel.appendx
    	x += jump

def findMax(array):
	max = array[0]
	maxi = 0
	for i in range(len(array)):
		if array[i] > max:
			max = array[i]
			maxi = i
	print("Unter dem Winkel \n {0} Grad wurde die maximale Reichweite \n {1} erzielt.".format(winkel[maxi], max))

def calcSx(w):
	w = math.radians(w)
	s = math.cos(w) * v * (math.sin(w)*v/g + math.sqrt((math.sin(w)*v/g)**2 + 2*h/g))
	return s

def printStats():
	data1 = [winkel, sx, dStats]
	print("\t".join(['Winkel', 'Reichweite', 'Toleranz']))
	for i in range(len(winkel)):
    		print("\t".join([str(theValue[i]) for theValue in data1]))

def printLog():
	data1 = [winkel, sx, dStats]
	with open("Output.csv", "w") as csvfile:
		fieldnames = ['Winkel', 'Reichweite', 'Toleranz']
		writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

		writer.writeheader()
		for i in range(len(winkel)):
			writer.writerow({'Winkel': winkel[i], 'Reichweite': sx[i], 'Toleranz': dStats[i]})
			# text_file.writerow(";".join([str(theValue[i]) for theValue in data1]))
		#text_file.close()


#	for i in range(len(winkel)):
#		print("Winkel - Reichweite - Toleranz : {0} - {1} - {2}".format(winkel[i], sx[i], dStats[i]))

def getHightest(x1, d):
	x2 = x1 - d
	x3 = x1 + d

	y1 = calcSx(x1)
	y2 = calcSx(x2)
	y3 = calcSx(x3)

	# for the stats
	winkel.append(math.radians(x1))
	sx.append(y1)
	dStats.append(math.radians(d))

	if d < 0.00001:
		printStats()
		printLog()
		findMax(sx)
	elif getMax(y2, y3) < y1:
		getHightest(x1, d/2)
	elif y2 > y3:
		getHightest(x2, d)
	else:
		getHightest(x3, d)

# Ausrechnen fuer eine Liste 
def calcForList():
	x = 0	# Startwert
	y = 90	# Stoppwert
	jump = 0.001	# Praezision
	while x < y:
		winkel.append(x)
		x += jump

	for w in winkel:
		sx.append(calcSx(w))
	findMax(sx)

# start
getHightest(0, 10.0)









