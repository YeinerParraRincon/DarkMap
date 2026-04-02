import socket
import argparse
from concurrent.futures import ThreadPoolExecutor


def Banner():
    print("""
\033[95m\033[1m
  ██████╗  █████╗ ██████╗ ██╗  ██╗███╗   ███╗ █████╗ ██████╗ 
  ██╔══██╗██╔══██╗██╔══██╗██║ ██╔╝████╗ ████║██╔══██╗██╔══██╗
  ██║  ██║███████║██████╔╝█████╔╝ ██╔████╔██║███████║██████╔╝
  ██║  ██║██╔══██║██╔══██╗██╔═██╗ ██║╚██╔╝██║██╔══██║██╔═══╝ 
  ██████╔╝██║  ██║██║  ██║██║  ██╗██║ ╚═╝ ██║██║  ██║██║     
  ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝╚═╝     ╚═╝╚═╝  ╚═╝╚═╝     
\033[0m
\033[96m  [ DarkMap — Port Scanner | Ethical Hacking Tool ]\033[0m
\033[2m  by Yeiner Parra Rincón | SENA ADSO\033[0m
\033[93m  ⚠️  Uso educativo y autorizado únicamente\033[0m
""")
    

def scanear_puerto(ip,puerto):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(1)
    
    try:
        sock.connect((ip,puerto))
        return True
    except Exception:
        return False
    finally:
        sock.close()

def scanear_ip(ip):
    with ThreadPoolExecutor(max_workers=100) as executor:
        for puerto in range(1,100):
            executor.submit(imprimir_resultado,ip,puerto)

def imprimir_resultado(ip,puerto):
    if scanear_puerto(ip,puerto):
        print(f"[+] Puerto {puerto} ABIERTO")



parser = argparse.ArgumentParser()
parser.add_argument("-i","--ip", help="IP OBJETIVO")

if __name__ == "__main__":
    Banner()

    args = parser.parse_args()


    if args.ip:
        scanear_ip(args.ip)
    else:
        print("Usa -i para indicar la Ip")