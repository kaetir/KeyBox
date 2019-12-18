#!/usr/bin/python3

import argparse
import wallet.genRngPasswd
import wallet.wallet
import os
from http.server import HTTPServer, BaseHTTPRequestHandler


class S(BaseHTTPRequestHandler):
    def _set_headers(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()

    def _html(self, message):
        """This just generates an HTML document that includes `message`
        in the body. Override, or re-write this do do more interesting stuff.
        """
        content = f"<html><body><h1>{message}</h1></body></html>"
        return content.encode("utf8")  # NOTE: must return a bytes object!

    def do_GET(self):
        # page d'ajout
        if(self.path == "/"):
            self.path = "/index.htm"
            if not os.path.isfile(fileWallet):
                print("creation du wallet")
                self.send_response(302)
                self.send_header('Location', "/create.htm")
                self.end_headers()
            else:
                self._set_headers()
                with open(self.path[1:], "r") as f:
                    self.wfile.write(self._html(f.read()))
        # call a l'api pour un passwd aléatoire
        elif(self.path == "/randompasswd"):
            self._set_headers()
            self.wfile.write(genRngPasswd.random_string(20).encode("utf8"))
        # on renvoie le json
        elif(self.path == "/view"):
            self.send_response(200)
            self.send_header('Content-Type', 'application/json')
            self.end_headers()
            self.wfile.write(bytes(wallet.walletJson.json.dumps(wallet.walletJson.get_entries(fileWallet)), "utf8"))
        
        else:
            # page non spéciale
            self._set_headers()
            if os.path.isfile(self.path[1:]):
                with open(self.path[1:], "r") as f:
                    self.wfile.write(self._html(f.read()))
            # 404
            else:
                print(self.path)
                self.wfile.write(self._html("<html><body><h1>404</h1></body></html>"))

    def do_HEAD(self):
        self._set_headers()

    def do_POST(self):
        # Doesn't do anything with posted data
        content_length = int(self.headers['Content-Length']) # <--- Gets the size of data
        post_data = self.rfile.read(content_length) # <--- Gets the data itself
        
        # page de création du wallet
        if(self.path == "/create"):
            data = post_data.decode("utf8").split("&") 
            data = {x.split("=")[0]:x.split("=")[1] for x in data}
            # le wallet n'existe pas
            if not os.path.isfile(fileWallet):
                if all(elem in  list(data.keys())  for elem in ["name", "main_password"]) :
                    wallet.createWallet(fileWallet, data["name"], data["main_password"] )
                    self.send_response(302)
                    self.send_header('Refresh', "3; url=/")
                    self.end_headers()
                    self.wfile.write(self._html("<meta charset='utf-8'><h1>wallet Crée</h1>"))
                else:
                    self._set_headers()
                    self.wfile.write(self._html("<meta charset='utf-8'><h1>saisie du formulaire non valide</h1>"))
            # le wallet existe dejà
            else:
                self._set_headers()
                self.wfile.write(self._html("<meta charset='utf-8'><h1>Le wallet existe déjà</h1>"))

        # page d'ajout d'une entrée au wallet
        elif(self.path == "/action.py"):
            data = post_data.decode("utf8").split("&") 
            data = {x.split("=")[0]:x.split("=")[1] for x in data}
            if all( elem in list(data.keys()) for elem in ["application", "name", "password", "mainpassword"] ):
                if wallet.walletJson.getHashedPasswwd(fileWallet) == wallet.hash(data["mainpassword"]).hexdigest() :                 
                    wallet.createAcount(fileWallet,data["application"],data["name"],data["password"], data["mainpassword"])
                    self.wfile.write(self._html("<meta charset='utf-8'><h1>entrée ajouté au wallet</h1><a href='/'><button>retour</button> </a>"))
                else:
                    self.wfile.write(self._html("<meta charset='utf-8'><h1>Mot de passe incorrecte</h1><a href='/'><button>retour</button> </a>"))
            else:
                self.wfile.write(self._html(f"<meta charset='utf-8'><h1>saisie du formulaire non valide</h1>{list(data.keys())}"))
        # 404
        else:
            self.wfile.write(self._html("<meta charset='utf-8'><h1>requettes post non géré</h1>"))
        

def run(server_class=HTTPServer, handler_class=S, addr="0.0.0.0", port=80):
    server_address = (addr, port)
    httpd = server_class(server_address, handler_class)

    print(f"Starting httpd server on {addr}:{port}")
    httpd.serve_forever()


if __name__ == "__main__":

    fileWallet = "walletWeb.json"

    parser = argparse.ArgumentParser(description="Run a simple HTTP server")
    parser.add_argument(
        "-l",
        "--listen",
        default="0.0.0.0",
        help="Specify the IP address on which the server listens",
    )
    parser.add_argument(
        "-p",
        "--port",
        type=int,
        default=80,
        help="Specify the port on which the server listens",
    )
    args = parser.parse_args()
    run(addr=args.listen, port=args.port)