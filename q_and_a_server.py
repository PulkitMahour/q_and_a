from http.server import BaseHTTPRequestHandler, HTTPServer
import os
from server_utilities import *


class handler(BaseHTTPRequestHandler):
	def do_GET(self):
		self.send_response(200)
		self.send_header('Content-type','text/html')
		self.end_headers()

		if self.path[1:] == '':
			self.wfile.write(bytes(question_page(),'utf-8'))

		elif "nth_prime" in self.path[1:]:
			b = self.path.replace('nth_prime', '').replace('/','')
			if b.isnumeric():
				lst = prime(int(b))
				self.wfile.write(bytes(str(making_list("The nth prime numbers are : ",lst)),'utf-8'))

		elif "sum_of_squares" in self.path[1:]:
			e = self.path.replace('sum_of_squares', '').replace('/','')
			if e.isnumeric():
				self.wfile.write(bytes(one_line_answer(f"The nth sum of squares of {e} ", recursive_sum_of_square(int(e))), 'utf-8'))
			else:
				self.wfile.write(bytes(error_page(), 'utf-8'))

		elif "sum_of_factorial" in self.path[1:]:
			i = self.path.replace('sum_of_factorial', '').replace('/','')
			if i.isnumeric():
				self.wfile.write(bytes(one_line_answer(f"The sum of nth factorial of {i} ", sum_of_factorial_recursive(int(i))), 'utf-8'))
			else:
				self.wfile.write(bytes(error_page(), 'utf-8'))

		elif "sum_of_cubes" in self.path[1:]:
			g = self.path.replace('sum_of_cubes', '').replace('/','')
			if g.isnumeric():
				self.wfile.write(bytes(one_line_answer(f"The nth sum of cubes of {g} ", recursive_sum_of_cube(int(g))), 'utf-8'))
			else:
				self.wfile.write(bytes(error_page(), 'utf-8'))

		elif "prime" in self.path[1:]:
			a = self.path.replace('prime', '').replace('/','')
			if a.isnumeric():	
				self.wfile.write(bytes(one_line_answer(f"{a} is a Prime Number ??? ", is_prime(int(a))),'utf-8'))
			else:
				self.wfile.write(bytes(error_page(), 'utf-8'))

		elif "nth_sum" in self.path[1:]:
			c = self.path.replace('nth_sum', '').replace('/','')
			if c.isnumeric():
				self.wfile.write(bytes(one_line_answer(f"The nth sum of {c} ", recursive_sum(int(c))), 'utf-8'))
			else:
				self.wfile.write(bytes(error_page(), 'utf-8'))

		elif "square" in self.path[1:]:
			d = self.path.replace('square', '').replace('/','')
			if d.isnumeric():
				self.wfile.write(bytes(one_line_answer(f"The square of {d} ", squares(int(d))), 'utf-8'))
			else:
				self.wfile.write(bytes(error_page(), 'utf-8'))

		elif "cube" in self.path[1:]:
			f = self.path.replace('cube', '').replace('/','')
			if f.isnumeric():
				self.wfile.write(bytes(one_line_answer(f"The cube of {f} ", cubes(int(f))), 'utf-8'))
			else:
				self.wfile.write(bytes(error_page(), 'utf-8'))

		elif "factorial" in self.path[1:]:
			h = self.path.replace('factorial', '').replace('/','')
			if h.isnumeric():
				self.wfile.write(bytes(one_line_answer(f"The factorial of {h} ", factorial_recursive(int(h))), 'utf-8'))
			else:
				self.wfile.write(bytes(error_page(), 'utf-8'))

		else:
			self.wfile.write(bytes(error_page(), 'utf-8'))


try:
	with HTTPServer(('localhost', 4444), handler) as server:
		server.serve_forever()
except KeyboardInterrupt:
	pass