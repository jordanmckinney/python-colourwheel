import sys
import math
import Line_Point

'''
purpose
	write to stdout a star with s points and first center at (x0,y0)
preconditions
	None
'''

# process the command line arguments
if len(sys.argv) != 4:
	print >> sys.stderr, 'Syntax: ' + sys.argv[0] + ' x0 y0 s'
	sys.exit(1)
try:
	x0 = float(sys.argv[1])
	y0 = float(sys.argv[2])
	s = int(sys.argv[3])
except ValueError:
	print >> sys.stderr, 'Syntax: ' + sys.argv[0] + ' x0 y0 s'
	sys.exit(2)
if s < 1:
	print >> sys.stderr, 'Syntax: ' + sys.argv[0] + ' x0 y0 s'

# generate s lines, each rotated by the central angle

p0 = Line_Point.Point(x0, y0)
p1 = Line_Point.Point(p0.x, p0.y+25)
central_angle = 2 * math.pi / s
while s > 0:
	print( 'line', Line_Point.Line(p0, p1))
	p1.rotate(central_angle)
	s = s - 1
