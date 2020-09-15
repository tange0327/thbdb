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
        args = sys.argv
        transport = TSocket.TSocket(args[1], args[2])
        transport = TTransport.TBufferedTransport(transport)
        protocol = TBinaryProtocol.TBinaryProtocol(transport)
        client = Basic.Client(protocol)

        transport.open()

        print(client.get(args[3]))

        transport.close()

    except Thrift.TException as tx:
        print(tx.message)
        transport.close()
