import sys
import Line_Point

'''
for each input line L
    repeat count times
        rotate L counter clockwise about the origin by angle
        scale L about the origin by factor
        translate L horizontally by delta_x
        translate L vertically by delta_y
        print L to stdout

preconditions
	each file in stdin is a legal lines file
'''

var_list = ['angle', 'factor', 'count', 'delta_x', 'delta_y']
option_map = {'angle':'-a', 'factor':'-f', 'count':'-n', 'delta_x':'-x', 'delta_y':'-y'}
option_vals = {'-a':'0.0','-f':'1.0','-n':'1','-x':'0.0','-y':'0.0'}

options_list = []
files_list = []

# break command line input into options list and files list
start_options = end_options = i = 1
while(i<len(sys.argv)):
    val = sys.argv[i]
    if not val.startswith('-'):
        files_list = sys.argv[end_options:]
        break
    i += 2
    end_options = i

# files list and options list now populated 
options_list = sys.argv[start_options:end_options]

# update option values, check for duplicates and illegal options
for i in range(0,len(options_list),2):
    option = options_list[i]
    if option in option_vals:
        option_vals[option] = options_list[i+1]
        if option in options_list[i+2:]:
            print >> sys.stderr, 'Duplicate option:', option
            sys.exit()  
    else:
        print >> sys.stderr, 'Illegal option:', option
        sys.exit()

# assign option values to relevant variables, check for valid values
for variable in var_list:
    value = option_vals[option_map[variable]]
    try:
        if variable == 'count' or variable == 'spoke':
            globals()[variable]=int(value)
        else:
            globals()[variable]=float(option_vals[option_map[variable]])
    except ValueError:
        print >> sys.stderr,'Illegal option value:',option_map[variable],option_vals[option_map[variable]]
        sys.exit() 

# read lines from files and perform rotate, scale, translate on them
if len(files_list)>0:
    for file in files_list:
        try:
        	f = open(file,'r')
        except IOError:
        	print >> sys.stderr, 'Cannot open file:', file
        	sys.exit()
        for x in f:
        	x = x.replace('\n', '') # remove line terminator: Linux
        	x = x.replace('\r\n', '') # remove line terminator: Windows
        with open(file) as open_file:
            file_data = open_file.readlines()
            for file_line in file_data:
                L = file_line.split()
                point0 = Line_Point.Point(float(L[1]), float(L[2]))
                point1 = Line_Point.Point(float(L[3]), float(L[4]))
                line = Line_Point.Line(point0, point1)
                for i in range(count):
                    line.rotate(angle)
                    line.scale(factor)
                    line.translate(delta_x,delta_y)
                    print ('line', line)
                    
                    
# read lines from stdin and perform rotate, scale, translate on them
else:       
    for line in sys.stdin:
        L = line.split()
        point0 = Line_Point.Point(float(L[1]), float(L[2]))
        point1 = Line_Point.Point(float(L[3]), float(L[4]))
        line = Line_Point.Line(point0, point1)
        for i in range(count):
            line.rotate(angle)
            line.scale(factor)
            line.translate(delta_x,delta_y)
            print ('line', line)
            
            
            
