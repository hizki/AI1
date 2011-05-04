# -*- coding:utf-8 -*-
"""
Created on May 4, 2011

@author: inesmeya
"""

import socket
import sys

host_to_test = {
'INESMEYA-MOBL2' :('run_astar', 1),                
'del12' : 'run_beam' 
                 
}


def main():
    host = socket.gethostname()
    module_name, param =host_to_test[host]
    module = __import__(module_name)
    module.main(param)
    print module_name, param

if __name__ == "__main__":
    main()