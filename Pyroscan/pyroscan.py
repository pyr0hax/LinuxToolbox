#Author: Jaco van Zyl
#Email: jvanzyl5@outlook.com

#!/usr/bin/python

from socket import *
import optparse
from threading import *

def connScan(tgtHost, tgtPort):
    try:
        sock = socket(AF_INET, SOCK_STREAM)
        sock.connect((tgtHost, tgtPort))
        print(' [+] %d/tcp Open') % tgtPort
    except:
        print('[-] %d/tcp Closed') % tgtPort
    finally:
        sock.close()

def portScan(tgtHost, tgtPorts):
    try:
        tgtIP = gethostbyname(tgtHost)
    except:
        print('Unknown Host %s ') %tgtHost
    try:
        tgtName = gethostbyaddr(tgtIP)
        print('[+] Scan Results for: ') + tgtName[0]
    except:
        print('[+] Scan Results For ') + tgtIP
    setdefaulttimeout(1)
    for tgtPort in tgtPorts:
        t = Thread(target=connScan, args=(tgtHost, int(tgtPort)))
        t.start()

def main():
    print("""
  _____            _____     ___             _    _          __   __
 |  __ \          |  __ \   / _ \           | |  | |         \ \ / /
 | |__) |  _   _  | |__) | | | | |          | |__| |   __ _   \ V / 
 |  ___/  | | | | |  _  /  | | | |          |  __  |  / _` |   > <  
 | |      | |_| | | | \ \  | |_| |          | |  | | | (_| |  / . \ 
 |_|       \__, | |_|  \_\  \___/           |_|  |_|  \__,_| /_/ \_\\
            __/ |                   ______                          
           |___/                   |______|                         
    """)
    parser = optparse.OptionParser('Usage of program: ' + '-H < target host > -p < target port >. Example: ./pyroscan.py -H server.example.com -p 21,22,25,80')
    parser.add_option('-H', dest='tgtHost', type='string', help='Specify target host.')
    parser.add_option('-p', dest='tgtPort', type='string', help='Specify target ports seperated by comma.')
    (options, args) = parser.parse_args()
    tgtHost = options.tgtHost
    tgtPorts = str(options.tgtPort).split(',')
    if (tgtHost == None) | (tgtPorts[0] == None):
        print(parser.usage)
        exit(0)
    portScan(tgtHost, tgtPorts)

if __name__ == '__main__':
    main()
