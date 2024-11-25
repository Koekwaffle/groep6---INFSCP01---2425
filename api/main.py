import socketserver
import http.server
import json
from data.dbconn import get_db_connection

class ApiRequestHandler(http.server.BaseHTTPRequestHandler):

    def handle_get_version_1(self, path):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()

            if path[0] == "warehouses":
                if len(path) == 1:
                    cursor.execute("SELECT * FROM warehouses")
                    warehouses = cursor.fetchall()
                    self.send_response(200)
                    self.send_header("Content-type", "application/json")
                    self.end_headers()
                    self.wfile.write(json.dumps(warehouses).encode("utf-8"))
                elif len(path) == 2:
                    warehouse_id = int(path[1])
                    cursor.execute("SELECT * FROM warehouses WHERE id = ?", (warehouse_id,))
                    warehouse = cursor.fetchone()
                    if warehouse:
                        self.send_response(200)
                        self.send_header("Content-type", "application/json")
                        self.end_headers()
                        self.wfile.write(json.dumps(warehouse).encode("utf-8"))
                    else:
                        self.send_response(404)
                        self.end_headers()
                else:
                    self.send_response(404)
                    self.end_headers()
            else:
                self.send_response(404)
                self.end_headers()
        except Exception as e:
            print(f"Error: {e}")
            self.send_response(500)
            self.end_headers()
        finally:
            conn.close()

    def do_GET(self):
        try:
            path = self.path.strip("/").split("/")
            if len(path) > 1 and path[0] == "api" and path[1] == "v1":
                self.handle_get_version_1(path[2:])
            else:
                self.send_response(404)
                self.end_headers()
        except Exception as e:
            print(f"Error processing GET request: {e}")
            self.send_response(500)
            self.end_headers()

if __name__ == "__main__":
    PORT = 3000
    with socketserver.TCPServer(("", PORT), ApiRequestHandler) as httpd:
        print(f"Serving on port {PORT}...")
        httpd.serve_forever()
