#!/usr/bin/env python

import asyncio
import pathlib
import ssl
import websockets
import logging
import price
logging.basicConfig(filename='example.log',level=logging.INFO)

async def load_price():
    async with price.connect(url="wss://price-hn02.vndirect.com.vn/realtime/websocket") as ps:
        ps.subscribe(price.BA, ["VND", "SSI"])
        ps.subscribe(price.SP, ["VND", "SSI"])
        ps.subscribe(price.DE, ["VN30F1901"])
        ps.subscribe(price.MI, ["10", "11", "12", "13", "02", "03"])
        while True:
            msg = await ps.recv()
            logging.info(f"< {str(msg)}")


asyncio.get_event_loop().run_until_complete(load_price())
asyncio.get_event_loop().run_forever()