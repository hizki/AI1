# -*- coding:utf-8 -*-
"""
Created on May 4, 2011

@author: inesmeya
"""

import socket

host_to_test = {
'INESMEYA-MOBL2' :'run_fast',                
'del12' : 'run_beam' 
                 
}


def main():
    host = socket.gethostname()
    module = __import__(host_to_test[host])
    module.main()
    
if __name__ == "__main__":
    main()