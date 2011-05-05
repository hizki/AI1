# -*- coding:utf-8 -*-
"""
Created on May 4, 2011

@author: inesmeya
"""

import socket
import sys

host_to_test = {
'INESMEYA-MOBL2' :('run_astar', [1]),                
'INESMEYA-MOBL2' : ('run_fast',[]) ,

'del15' : ('run_astar',[1]), #easy
'del14' : ('run_astar',[2]), #midl
'del14' : ('run_astar',[3]), #heavy                 
}


def main():
    host = socket.gethostname()
    module_name, param_list = host_to_test[host]
    module = __import__(module_name)
    module.cmain(*param_list)
    print module_name, param_list

if __name__ == "__main__":
    main()