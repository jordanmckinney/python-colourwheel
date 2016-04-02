# $# is the number of command line arguments, NOT including the script name
# $1: is the first argument, AFTER the script itself

if [ $# -ne 3 ];
	then echo "Please enter: 'stars.sh X Y Z' where X = # points on star (1+), Y = # of spokes (1+), Z = theme number"
	exit
fi

# star at origin as basis for all others
python generate_star.py 0.0 0.0 $1 > star.txt

# generate 5th star 
python rotate_scale_translate.py -x 0.0 -y 220.0 -f 0.05 -n 1 < star.txt > star5.txt

# generate 4th star 
python rotate_scale_translate.py -x 0.0 -y 185.0 -f 0.3 -n 1 < star.txt > star4.txt

# generate 3rd star 
python rotate_scale_translate.py -x 0.0 -y 150.0 -f 0.5 -n 1 < star.txt > star3.txt

# generate 2nd star 
python rotate_scale_translate.py -x 0.0 -y 105.0 -f 0.7 -n 1 < star.txt > star2.txt

# generate 1st star 
python rotate_scale_translate.py -x 0.0 -y 50.0 -f 1.2 -n 1 < star.txt > star1.txt

# combine 4 stars and rotate
cat star5.txt star4.txt star3.txt star2.txt star1.txt > stars0.txt
python transform_star.py -z $2 < stars0.txt > stars.txt

# generate SVG
python lines_to_svg_star.py $3 stars.txt > stars.svg
