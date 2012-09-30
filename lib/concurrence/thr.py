import concurrence.io
from thrift.transport.TTransport import TTransportBase, TTransportException
import socket

# Example:
# from concurrence.thr import Socket
# sock = Socket((("localhost", 9160),))
# trans = TTransport.TFramedTransport(sock)
# proto = TBinaryProtocol.TBinaryProtocolAccelerated(trans)
# client = Client(proto)
#
# Note: you must use Framed Transport to use thrift with nonblocking sockets

class Socket(TTransportBase):
    "Thrift Socket implemetation on top of the Concurrence"

    def __init__(self, hosts):
        self.hosts = hosts
        self.handle = None
        self.timeout = -1

    def setTimeout(self, ms):
        if ms is None:
            self.timeout = -1
        else:
            self.timeout = ms / 1000.0

    def open(self):
        try:
            for host in self.hosts:
                try:
                    self.handle = concurrence.io.Socket.connect(host, self.timeout)
                    self.stream = concurrence.io.BufferedStream(self.handle)
                except socket.error as e:
                    if host is not self.hosts[-1]:
                        continue
                    else:
                        raise e
                    break
        except socket.error as e:
            message = "Could not connect to thrift socket"
            raise TTransportException(TTransportException.NOT_OPEN, message)

    def close(self):
        if self.handle:
            self.handle.close()
            self.handle = None
            self.stream = None

    def isOpen(self):
        return self.handle is not None

    def write(self, buff):
        self.stream.writer.write_bytes(buff)

    def flush(self):
        self.stream.writer.flush()

    def read(self, sz):
        buff = self.stream.reader.read_bytes(sz)
        if len(buff) != sz:
            raise TTransportException("Thrift socket read %d bytes instead of %d" % (len(buff), sz))
        return buff
