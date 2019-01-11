#!/usr/bin/env python

import asyncio
import pathlib
import ssl
import websockets
import logging
import price
import parser
logging.basicConfig(filename='example.log',level=logging.INFO)


async def load_price():
    url = "wss://price-cmc-04.vndirect.com.vn/realtime/websocket"
    async with websockets.connect(url, ssl=True) as ws:
        logging.info(f"Connected")
        ps = price.Price(ws)
        await ps.subscribe(parser.BA, ["VND", "PNJ"])
        await ps.subscribe(parser.SP, ["VND", "PNJ"])
        await ps.subscribe(parser.DE, ["VN30F1901"])
        await ps.subscribe(parser.MI, ["10", "11", "12", "13", "02", "03"])
        while True:
            msg = await ps.recv()
            logging.info(f"< {str(msg)}")


if __name__ == "__main__":
    logging.info("Start...")
    asyncio.get_event_loop().run_until_complete(load_price())