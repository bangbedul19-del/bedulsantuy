import http.server, socketserver, os, sys
PORT = 1010
os.chdir(os.path.dirname(os.path.abspath(__file__)))
print(f'Open Dia: http://localhost:{PORT}/dia-spoof-tests.html')
with socketserver.TCPServer(('', PORT), http.server.SimpleHTTPRequestHandler) as s:
    try: s.serve_forever()
    except KeyboardInterrupt: sys.exit(0)
