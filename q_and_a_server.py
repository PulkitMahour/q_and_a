from http.server import BaseHTTPRequestHandler, HTTPServer
import os

def making_page():
	var =  "<html>" + \
	"<head>"+ \
		"<title>Q and A server</title>" +\
	"</head>"+ \
	"<body bgcolor = #5B3E8A" + \
		"<h1><font size = 10> Type the following in the URL for getting the result</h1>"+\
			"<ol>" +\
				"<font size = 6, color = black>" "<i>" "<li>" "For check the prime number" "</li>" "</i>" +\
					"<ul>" +\
						"<li>" "<font size = 5, color = blue>" "/prime/number" "</li>" +\
					"</ul>" +\
						"<p>&nbsp;</p>"+\
				"<font size = 6, color = black>" "<i>" "<li>" "For check the nth prime number" "</li>" "</i>" +\
					"<ul>" +\
						"<li>" "<font size = 5, color = blue>" "/nth_prime/number" "</li>" +\
					"</ul>" +\
						"<p>&nbsp;</p>"+\
				"<font size = 6, color = black>" "<i>" "<li>" "iska pata nahi" "</li>" "</i>" +\
					"<ul>" +\
						"<li>" "<font size = 5, color = blue>" "For check the prime number" "</li>" +\
					"</ul>" +\
						"<p>&nbsp;</p>"+\
				"<font size = 6, color = black>" "<i>" "<li>" "For check the nth sum" "</li>" "</i>" +\
					"<ul>" +\
						"<li>" "<font size = 5, color = blue>" "/nth_sum/number" "</li>" +\
					"</ul>" +\
			"</ol>" +\
	"</body>" + \
	"</html>"

	return var


class handler(BaseHTTPRequestHandler):
	def do_GET(self):
		self.send_response(200)
		self.send_header('Content-type','text/html')
		self.end_headers()
		viewer = making_page()
		self.wfile.write(bytes(viewer,'utf-8'))
		if "prime" in self.path[1:]:
			print("haa sahi hai")

try:
	with HTTPServer(('localhost', 4444), handler) as server:
		server.serve_forever()
except KeyboardInterrupt:
	pass