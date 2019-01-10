import json

def arr2ba(arr):
    return {
        "time": arr[0],
        "code": arr[1],
        "bidPrice01": float(arr[2]),
        "bidQtty01": float(arr[3]),
        "bidPrice02": float(arr[4]),
        "bidQtty02": float(arr[5]),
        "bidPrice03": float(arr[6]),
        "bidQtty03": float(arr[7]),
        "offerPrice01": float(arr[8]),
        "offerQtty01": float(arr[9]),
        "offerPrice02": float(arr[10]),
        "offerQtty02": float(arr[11]),
        "offerPrice03": float(arr[12]),
        "offerQtty03": float(arr[13]),
        "accumulatedVol": float(arr[14]),
        "matchPrice": float(arr[15]),
        "matchQtty": float(arr[16]),
        "matchValue": float(arr[17]),
        "totalOfferQtty": float(arr[18]),
        "totalBidQtty": float(float(arr[19])),
    }

def arr2sp(arr):
    return {
        "floorCode": arr[0],
        "tradingDate": arr[1],
        "time": arr[2],
        "code": arr[3],
        "companyName": arr[4],
        "stockType": arr[5],
        "totalRoom": float(arr[6]),
        "currentRoom": float(arr[7]),
        "basicPrice": float(arr[8]),
        "openPrice": float(arr[9]),
        "closePrice": float(arr[10]),
        "currentPrice": float(arr[11]),
        "currentQtty": float(arr[12]),
        "highestPrice": float(arr[13]),
        "lowestPrice": float(arr[14]),
        "ceilingPrice": float(arr[15]),
        "floorPrice": float(arr[16]),
        "averagePrice": float(arr[17]),
        "accumulatedVal": float(arr[18]),
        "buyForeignQtty": float(arr[19]),
        "sellForeignQtty": float(arr[20]),
        "projectOpen": float(arr[21]),
        "sequence": arr[22],
    }


def arr2mi(arr):
    return {
        "marketID": arr[0],
        "totalTrade": float(arr[1]),
        "totalShareTraded": float(arr[2]),
        "totalValueTraded": float(arr[3]),
        "advance": float(arr[4]),
        "decline": float(arr[5]),
        "noChange": float(arr[6]),
        "indexValue": float(arr[7]),
        "changed": float(arr[8]),
        "tradingTime": arr[9],
        "tradingDate": arr[10],
        "floorCode": arr[11],
        "marketIndex": float(arr[12]),
        "priorMarketIndex": float(arr[13]),
        "highestIndex": float(arr[14]),
        "lowestIndex": float(arr[15]),
        "shareTraded": float(arr[16]),
        "status": arr[17],
        "sequence": arr[18],
        "predictionMarketIndex": float(arr[19]),
    }


def arr2de(arr):
    return {
        "accumulatedVal": float(arr[0]),
        "accumulatedVol": float(arr[1]),
        "basicPrice": float(arr[2]),
        "bidPrice01": float(arr[3]),
        "bidPrice02": float(arr[4]),
        "bidPrice03": float(arr[5]),
        "bidQtty01": float(arr[6]),
        "bidQtty02": float(arr[7]),
        "bidQtty03": float(arr[8]),
        "buyForeignQtty": float(arr[9]),
        "ceilingPrice": float(arr[10]),
        "code": arr[11],
        "currentPrice": float(arr[12]),
        "currentQtty": float(arr[13]),
        "highestPrice": float(arr[14]),
        "lastTradingDate": arr[15],
        "lowestPrice": float(arr[16]),
        "matchPrice": float(arr[17]),
        "matchQtty": float(arr[18]),
        "offerPrice01": float(arr[19]),
        "offerPrice02": float(arr[20]),
        "offerPrice03": float(arr[21]),
        "offerQtty01": float(arr[22]),
        "offerQtty02": float(arr[23]),
        "offerQtty03": float(arr[24]),
        "openInterest": float(arr[25]),
        "openPrice": float(arr[26]),
        "sellForeignQtty": float(arr[27]),
        "tradingSessionId": arr[28],
        "bidPrice04": float(arr[29]),
        "bidPrice05": float(arr[30]),
        "bidPrice06": float(arr[31]),
        "bidPrice07": float(arr[32]),
        "bidPrice08": float(arr[33]),
        "bidPrice09": float(arr[34]),
        "bidPrice10": float(arr[35]),
        "bidQtty04": float(arr[36]),
        "bidQtty05": float(arr[37]),
        "bidQtty06": float(arr[38]),
        "bidQtty07": float(arr[39]),
        "bidQtty08": float(arr[40]),
        "bidQtty09": float(arr[41]),
        "bidQtty10": float(arr[42]),
        "offerPrice04": float(arr[43]),
        "offerPrice05": float(arr[44]),
        "offerPrice06": float(arr[45]),
        "offerPrice07": float(arr[46]),
        "offerPrice08": float(arr[47]),
        "offerPrice09": float(arr[48]),
        "offerPrice10": float(arr[49]),
        "offerQtty04": float(arr[50]),
        "offerQtty05": float(arr[51]),
        "offerQtty06": float(arr[52]),
        "offerQtty07": float(arr[53]),
        "offerQtty08": float(arr[54]),
        "offerQtty09": float(arr[55]),
        "offerQtty10": float(arr[56]),
        "time": arr[57],
        "floorPrice": float(arr[58]),
    }

arr_map = {
    "BA": arr2ba,
    "SP": arr2sp,
    "MI": arr2mi,
}

def load(msg):
    obj = json.loads(msg)
    arr = obj.get("data").split("|")
    if obj["type"] not in arr_map:
        raise KeyError("Unsupported msg type")
    try:
        return arr_map.get(obj["type"])(arr)
    except KeyError:
        raise KeyError("Array may not have enough items to convert to object, check input message")
