#! /usr/bin/env python
# -*- coding: utf-8 -*-

import glob
import sys
sys.path.append('gen-py')

from thbdb import Basic
from thbdb import ttypes

from thrift import Thrift
from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol

if __name__ == '__main__':
    try:
        transport = TSocket.TSocket('localhost', 9090)
        transport = TTransport.TBufferedTransport(transport)
        protocol = TBinaryProtocol.TBinaryProtocol(transport)
        #client = Calculator.Client(protocol)
        client = Basic.Client(protocol)

        transport.open()

        client.put( "test",u"テストバリュー" )
        
        result = client.get(u"test")
        print ("Call get(\"test\") =" , result.decode('utf-8') )

        
        transport.close()

    except Thrift.TException as  tx:
        print ( tx.message )
