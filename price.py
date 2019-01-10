from contextlib import  contextmanager
import parser

# message type
BA = "BA"
SP = "SP"
DE = "DERIVATIVE_OPT"
MI = "MI"

class Price():

    def __init__(self, ws):
        self.ws = ws

    def subscribe(self, type, symbol_list):
        msg = '{"type":"registConsumer","data":{"sequence":0,"params":{"name":"{}","codes":[{}]}}}'.format(type, ','.join(symbol_list))
        self.ws.send(msg)

    async def recv(self):
        data = await self.ws.recv()
        return parser.load(data)


@contextmanager
def connect(url=''):
    async with websockets.connect(
            'wss://price-hn02.vndirect.com.vn/realtime/websocket', ssl=True) as websocket:
        yield Price(ws)

