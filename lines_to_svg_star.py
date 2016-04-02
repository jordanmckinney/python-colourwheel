import sys

SVG_HEADER = "<svg xmlns=\"http://www.w3.org/2000/svg\" version=\"1.1\""" width=\"500\" height=\"500\">\n" 
SVG_BOUNDING_BOX_THEME = "<rect x=\"0\" y=\"0\" width=\"500\" height=\"500\""" style=\"stroke:#000;fill:#000\" />\n"
SVG_BOUNDING_BOX_NO_THEME = "<rect x=\"0\" y=\"0\" width=\"500\" height=\"500\""" style=\"stroke:#000;fill:none\" />\n"
SVG_FOOTER = "</svg>\n"
CANVAS_HEIGHT = 500
CANVAS_WIDTH = 500

theme_50shadesofpink = ['#ff00a9','#fb9f9f','#ff0065','#ffbfd3','#fb5858'] # http://www.color-hex.com/color-palette/1880
theme_icrecream = ['#6b3e26','#ffc5d9','#c2f2d0','#fdf5c9','#ffcb85'] # http://www.color-hex.com/color-palette/660
theme_pastel = ['#a8e6cf','#dcedc1','#ffd3b6','#ffaaa5','#ff8b94'] # http://www.color-hex.com/color-palette/2922
theme_vicecity = ['#00ecff','#7cff00','#e3ff00','#ffb400','#fd00ff'] # http://www.color-hex.com/color-palette/7648
themes = {'1':theme_50shadesofpink,'2':theme_icrecream,'3':theme_pastel,'4':theme_vicecity}

# function to check if string is number
def is_num(string):
    try:
        float(string)
        return True
    except ValueError:
        return False

# function to print error message 
def print_error(line, carat, line_num ):
	sys.stderr.write('Error in line '+line_num+':\n'+3*' '+line+ carat*' '+'^\n')
	
# function to print line
def print_line(x0,y0,x1,y1,color):
	if use_theme:
		print("<line stroke-linecap=\"round\" x1=\"%d\" y1=\"%d\" x2=\"%d\" y2=\"%d\""" style=\"stroke:%s;stroke-width:10\" />" % (x0,y0,x1,y1,color))
	else:
		print("<line x1=\"%d\" y1=\"%d\" x2=\"%d\" y2=\"%d\""" style=\"stroke:#000\" />" % (x0,y0,x1,y1))

#print svg header
sys.stdout.write(SVG_HEADER)

arg_len = len(sys.argv)
file_index = arg_len-1
use_theme = True

# check whether themes will be used
if arg_len < 3:
	use_theme = False
	sys.stdout.write(SVG_BOUNDING_BOX_NO_THEME)
else:
	sys.stdout.write(SVG_BOUNDING_BOX_THEME)

#check for legal file 
try:
	lines_file = open(sys.argv[file_index], 'r')
except IOError:
	sys.stderr.write('Cannot open: ' + sys.argv[file_index] + '\n')
	sys.exit()

# set default theme, then chosen theme
theme = themes['1']
if use_theme:
	theme = themes[sys.argv[1]]

#iterate through each line in lines file
for line_num, line in enumerate(lines_file):
	carat_pos = 3
	line_num += 1
	str_line_num = str(line_num)
	line_error = False
	accepted_chars = ['-', '\n', ' ']

	if not line.startswith('line'):
		print_error(line, carat_pos, str_line_num)
		continue
	
	for i in range(4,len(line)):
		if line[i] in accepted_chars:
			continue
		elif not is_num(line[i]):
			carat_pos += i
			print_error(line, carat_pos, str_line_num)
			line_error = True
			break
	if line_error:
		continue
	
	L = line.split()
	
	# check for too many or too few items
	if not len(L) == 5:
		for i,item in enumerate(L):
			carat_pos+=len(L[i])
		carat_pos+=len(L)-2
		print_error(line, carat_pos, str_line_num)
		continue	
	
	x0,y0,x1,y1 = float(L[1]), float(L[2]), float(L[3]), float(L[4])
	x0 += CANVAS_WIDTH/2
	y0 = -y0 + CANVAS_HEIGHT/2
	x1 += CANVAS_WIDTH/2
	y1 = -y1 + CANVAS_HEIGHT/2		
	
	values = [x0, y0, x1, y1]
	carat_pos = 8
	
	# check for out of range values
	for val in values:
		if val > 500 or val < 0:
			print_error(line, carat_pos, str_line_num)
		carat_pos += len(str(val))
	
	color = theme[line_num%5]
	print_line(x0,y0,x1,y1,color)

sys.stdout.write(SVG_FOOTER)
