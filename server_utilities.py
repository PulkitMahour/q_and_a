def question_page():
	var =  "<html>" + \
	"<head>"+ \
		"<title>Q and A server</title>" +\
	"</head>"+ \
	"<body bgcolor = #40e0d0>" + \
		"<h1><font size = 10> Type the following in the URL for getting the result</font></h1>"+\
			"<ol>" +\
				"<font size = 6, color = black>" "<i>" "<li>" "For check the prime number" "</li>" "</i>""</font>" +\
					"<ul>" +\
						"<li>" "<font size = 5, color = blue>" "/prime/number" "</font>" "</li>" +\
					"</ul>" +\
						"<p>&nbsp;</p>"+\
				"<font size = 6, color = black>" "<i>" "<li>" "For check the nth prime number" "</li>" "</i>" "</font>" +\
					"<ul>" +\
						"<li>" "<font size = 5, color = blue>" "/nth_prime/number" "</font>" "</li>" +\
					"</ul>" +\
						"<p>&nbsp;</p>"+\
				"<font size = 6, color = black>" "<i>" "<li>" "For check the nth sum" "</li>" "</i>" "</font>" +\
					"<ul>" +\
						"<li>" "<font size = 5, color = blue>" "/nth_sum/number" "</font>" "</li>" +\
					"</ul>" +\
						"<p>&nbsp;</p>"+\
				"<font size = 6, color = black>" "<i>" "<li>" "For check the square" "</li>" "</i>" "</font>" +\
					"<ul>" +\
						"<li>" "<font size = 5, color = blue>" "/square/number" "</font>" "</li>" +\
					"</ul>" +\
						"<p>&nbsp;</p>"+\
				"<font size = 6, color = black>" "<i>" "<li>" "For check the sum of square" "</li>" "</i>" "</font>" +\
					"<ul>" +\
						"<li>" "<font size = 5, color = blue>" "/sum_of_squares/number" "</font>" "</li>" +\
					"</ul>" +\
						"<p>&nbsp;</p>"+\
				"<font size = 6, color = black>" "<i>" "<li>" "For check the cube" "</li>" "</i>" "</font>" +\
					"<ul>" +\
						"<li>" "<font size = 5, color = blue>" "/cube/number" "</font>" "</li>" +\
					"</ul>" +\
						"<p>&nbsp;</p>"+\
				"<font size = 6, color = black>" "<i>" "<li>" "For check the sum of cubes" "</li>" "</i>" "</font>" +\
					"<ul>" +\
						"<li>" "<font size = 5, color = blue>" "/sum_of_cubes/number" "</font>" "</li>" +\
					"</ul>" +\
						"<p>&nbsp;</p>"+\
				"<font size = 6, color = black>" "<i>" "<li>" "For check the factorial" "</li>" "</i>" "</font>" +\
					"<ul>" +\
						"<li>" "<font size = 5, color = blue>" "/factorial/number" "</font>" "</li>" +\
					"</ul>" +\
						"<p>&nbsp;</p>"+\
				"<font size = 6, color = black>" "<i>" "<li>" "For check the sum of nth factorial" "</li>" "</i>" "</font>" +\
					"<ul>" +\
						"<li>" "<font size = 5, color = blue>" "/sum_of_factorial/number" "</font>" "</li>" +\
					"</ul>" +\
			"</ol>" +\
	"</body>" + \
	"</html>"

	return var

def one_line_answer(statement, n):
	var1 =  "<html>" + \
	"<head>"+ \
		"<title>Result</title>" +\
	"</head>"+ \
	"<body bgcolor = #Df73ff>" + \
		"<h1><font size = 20>" "<marquee>"+statement+"= "+str(n)+"</marquee>""</font></h1>"+\
	"</body>" + \
	"</html>"

	return var1

def error_page():
	var2 = "<html>" + \
	"<head>"+ \
		"<title>Error</title>" +\
	"</head>"+ \
	"<body bgcolor = #B7410e>" + \
		"<h1><font size = 30>" "<marquee>Something went wrong Please check the input or URL</marquee>""</font></h1>"+\
	"</body>" + \
	"</html>"

	return var2

def making_list(statement, var_lst):
	var3 = "<html>" + \
	"<head>"+ \
		"<title>Result</title>" +\
	"</head>"+ \
	"<body bgcolor = #Df73ff>" + \
	"<h1><font size = 20>" "<marquee>"+statement+"</marquee>""</font></h1>"+\
	"<ul>" 
	for i in var_lst:
		var3 += "<font size = 10>" "<li>" + str(i) + "</li>" "</font>"
		
	var3 += "</ul>" + \
	"</body>" + \
	"</html>"
	return var3

def is_prime(num):
	isprime = True
	for i in range(2,num):
		if (num%i) == 0:
			isprime = False
			break
	if isprime == True:
		return isprime
	else:
		return False

def prime(number):
	x = [ ]
	index = 2
	while index <= number:
		a = is_prime(index)
		if a == True:
			x.append(index)
		index = index + 1
	return x

def squares(number):
	if number == 0:
		return 0
	else:
		return number**2

def cubes(number):
	if number == 0:
		return 0
	else:
		return number**3

def recursive_sum(number):
	if number == 0:
		return 0
	else:
		return number + recursive_sum(number - 1)

def recursive_sum_of_cube(number):
	if number == 0:
		return 0
	else:
		return (number**3 + recursive_sum_of_cube(number-1))

def recursive_sum_of_square(number):
	if number == 0:
		return 0
	else:
		return (number**2 + recursive_sum_of_square(number-1))

def factorial_recursive(number):
	if number == 0:
		return 1
	else:
		return number * factorial_recursive(number - 1)

def sum_of_factorial_recursive(number):
	if number == 0:
		return 0
	else:
		return factorial_recursive(number) + sum_of_factorial_recursive(number-1)


