#!/usr/bin/python3

import argparse
import wallet.genRngPasswd as genRngPasswd
from wallet.wallet import Wallet
import wallet.wallet as wallet
import os
from http.server import HTTPServer, BaseHTTPRequestHandler
from http.cookies import SimpleCookie
import html


def _html(message) -> bytes:
    """
    @summary This just generates an HTML document that includes `message`
          in the body. Override, or re-write this do do more interesting stuff.
    """
    content = f"<html><head><meta charset='utf-8'></head><body><h1>{message}</h1></body></html>"
    return content.encode("utf8")  # NOTE: must return a bytes object!


class S(BaseHTTPRequestHandler):
    # header de base
    def _set_headers(self, mime_type="text/html"):
        self.send_response(200)
        self.send_header("Content-mime_type", "{}".format(mime_type))
        self.end_headers()

    def do_HEAD(self):
        self._set_headers()

    def do_GET(self):
        cookies = SimpleCookie(self.headers.get('Cookie'))

        # then use somewhat like a dict, e.g:
        # username = cookies['username'].value
        if "mainpassword" not in cookies.keys() and self.path.split(".")[-1] not in ["css", "js", "png"] and os.path.isfile(fileWallet):
            if not os.path.isfile(fileWallet):
                self.path = "/"
            else:
                self.path = "/login.htm"

        # page d'ajout
        if self.path == "/":
            self.path = "/index.htm"
            if not os.path.isfile(fileWallet):
                print("creation du wallet")
                self.send_response(302)
                self.send_header('Location', "/create.htm")
                self.end_headers()
            else:
                self._set_headers("text/"+self.path[1:].split(".")[-1])
                with open("web_wallet/" + self.path[1:], "r") as f:
                    self.wfile.write(f.read().encode("utf8"))
        # call a l'api pour un passwd aléatoire
        elif self.path == "/randompasswd":
            self._set_headers("text/plain")
            self.wfile.write(genRngPasswd.random_string(20).encode("utf8"))
        # Affichage
        elif self.path == "/view":
            if w.lock:
                w.unlock(cookies["mainpassword"].value)
            if not w.lock:
                self.do_HEAD()
                liste = [w.get_acount(a) for a in w.get_applications()]
                print(liste)
                liste_disp = ""
                with open("web_wallet/acount.template") as template:
                    content = template.read()
                    for e in liste:
                        liste_disp += content.format(acount=e)

                with open("web_wallet/view.htm") as f:
                    content = f.read()
                    content = content.format(liste_acount=liste_disp)
                    self.wfile.write(content.encode("utf8"))

        else:
            # page non spéciale
            if self.path.endswith(("woff", "woff2", "ttf")):
                self._set_headers("font/"+self.path.split(".")[-1])
                if os.path.isfile("web_wallet/" + self.path[1:].split("?")[0]):
                    with open("web_wallet/" + self.path[1:].split("?")[0], "rb") as f:
                        self.wfile.write(f.read())
            else:
                self._set_headers()

            if os.path.isfile("web_wallet/" + self.path[1:].split("?")[0]):
                with open("web_wallet/" + self.path[1:].split("?")[0], "r") as f:
                    self.wfile.write(f.read().encode("utf8"))
            # 404
            else:
                print(self.path)
                self.wfile.write(_html("<html><body><h1>404</h1></body></html>"))

    def do_POST(self):
        cookies = SimpleCookie(self.headers.get('Cookie'))

        # Doesn't do anything with posted data
        content_length = int(self.headers['Content-Length'])  # <--- Gets the size of data
        post_data = self.rfile.read(content_length)  # <--- Gets the data itself
        data = post_data.decode("utf8").split("&")
        data = {x.split("=")[0]: x.split("=")[1] for x in data}

        # page de création du wallet
        if self.path == "/create":
            # le wallet n'existe pas
            if not os.path.isfile(fileWallet):
                if all(elem in list(data.keys()) for elem in ["name", "main_password"]):
                    w.create_wallet(data["name"], data["main_password"])
                    self.send_response(302)
                    self.send_header('Refresh', "3; url=/")
                    self.end_headers()
                    self.wfile.write(_html("<h1>wallet Crée</h1>"))
                else:
                    self._set_headers()
                    self.wfile.write(_html("<h1>saisie du formulaire non valide</h1>"))
            # le wallet existe dejà
            else:
                self._set_headers()
                self.wfile.write(_html("<h1>Le wallet existe déjà</h1>"))

        # page d'ajout d'une entrée au wallet
        elif self.path == "/action":
            if all(elem in list(data.keys()) for elem in ["application", "name", "password"]):
                if w.unlock( cookies["mainpassword"].value):
                    if w.create_acount(data["application"], data["name"], html.unescape(data["password"])):
                        self.do_HEAD()
                        self.wfile.write(_html(
                            "<h1>entrée ajouté au wallet</h1><a href='/'><button>retour</button> </a>"))
                    else:
                        self.do_HEAD()
                        self.wfile.write(_html(
                            "Imposible de creer le compte<a href='/'><button>retour</button> </a>"))
                else:
                    self.do_HEAD()
                    self.wfile.write(_html(
                        "<h1>Mot de passe incorrecte</h1><a href='/'><button>retour</button> </a>"))
            else:
                self.do_HEAD()
                self.wfile.write(
                    _html(f"<h1>saisie du formulaire non valide</h1>{list(data.keys())}"))
        # page de login
        elif self.path == "/login":
            if all(elem in list(data.keys()) for elem in ["mainpassword"]):
                if w.unlock(data["mainpassword"]):
                    cookies["mainpassword"] = data["mainpassword"]
                    self.send_response(200)
                    self.send_header("Set-Cookie", cookies.output(header=""))
                    self.send_header('Refresh', "0; url=/")
                    self.end_headers()
                    self.wfile.write(_html("bon login"))
                else:
                    self.send_response(200)
                    self.send_header('Refresh', "2; url=/login.htm?failed=true")
                    self.end_headers()
                    self.wfile.write(_html(
                        "<h1>Mot de passe incorrecte</h1><a href='/'><button>retour</button> </a>"))

        # 404
        else:
            self.wfile.write(_html("<h1>requettes post non géré</h1>"))


def run(server_class=HTTPServer, handler_class=S, addr="0.0.0.0", port=80):
    server_address = (addr, port)
    httpd = server_class(server_address, handler_class)

    print(f"Starting httpd server on {addr}:{port}")
    httpd.serve_forever()


if __name__ == "__main__":
    fileWallet = "wallet.json"
    w = Wallet(fileWallet)

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
