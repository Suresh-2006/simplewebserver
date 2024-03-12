from http.server import HTTPServer, BaseHTTPRequestHandler
content = """
<html>
    <head>
        <title align="center">TOP SOFTWARE COMPANIES</title>

    </head>
    <body align="center" bgcolor="lightgreen">
        <table border="3" cellspacing="4" align="center" bgcolor="cyan" height="300" width "500">
            <caption>Top Five Revenue Generating Software Companies</caption>
            <tr>
                <th>Rank</th>
                <th>Name</th>
                <th>Revenue</th>
            </tr>
            <tr>
                <td>1</td>
                <td>Apple</td>
                <td>$385.70 B</td>
            </tr>
            <tr>
                <td>2</td>
                <td>Alphabet(Google)</td>
                <td>$307.39 B</td>
            </tr>
            <tr>
                <td>3</td>
                <td>Microsoft</td>
                <td>$227.58 B</td>
            </tr>
            <tr>
                <td>4</td>
                <td>Oracle</td>
                <td>$51.62 B</td>
            </tr>
        </table>
    </body>
</html>
    
"""
class myhandler(BaseHTTPRequestHandler):
    def do_GET(self):
        print("request received")
        self.send_response(200)
        self.send_header('content-type', 'text/html; charset=utf-8')
        self.end_headers()
        self.wfile.write(content.encode())
server_address = ('',8000)
httpd = HTTPServer(server_address,myhandler)
print("my webserver is running...")
httpd.serve_forever()