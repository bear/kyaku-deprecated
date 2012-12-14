#!/usr/bin/env python

#
# :copyright: (c) 2012 by Mike Taylor
# :license: BSD 2-Clause
#

from redis import StrictRedis

def getRedis(config):
    host     = '127.0.0.1'
    port     = 6379
    database = 0
    
    if 'host' in config:
        host = config['host']
    if 'port' in config:
        port = config['port']
    if 'database' in config:
        database = config['database']
    
    return StrictRedis(host=host, port=port, db=database)