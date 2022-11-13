import websocket
import _thread
import time
import rel
import json
import pandas as pd

# Order Flow Trading Stategy
# Microstructure analysis of the market

# compute imbalance
# spread
# aggressors pressure
# exhaustion of buyers/sellers
# identify areas of longer term liquidity
# calculate volume profile
# price wants to go to where the volume is

# responsive buyer trigger buy

def on_message(ws, message):
    msg = json.loads(message)
    bids_data = [(float(price), float(vol)) for price, vol in msg["bids"]]
    asks_data = [(float(price), float(vol)) for price, vol in msg["asks"]]
    bid_total_vol = sum(vol for price, vol in bids_data)
    ask_total_vol = sum(vol for price, vol in asks_data)
    best_bid = bids_data[0]
    best_ask = asks_data[0]
    threshold = 100
    imbalance = bid_total_vol - ask_total_vol
    spread = 0 # compute the spread
    apply_strategy = 1 if tension > threshold else 0
    d = {"bids vol": [bid_total_vol], "asks vol": [ask_total_vol], "best bid": [best_bid], "best ask": [best_ask], "apply": [apply_strategy]}
    df = pd.DataFrame(data=d)
    print(df)

def on_error(ws, error):
    print(error)

def on_close(ws, close_status_code, close_msg):
    print("### closed ###")

def on_open(ws):
    print("Opened connection")

if __name__ == "__main__":
    #websocket.enableTrace(True)
    ws = websocket.WebSocketApp("wss://stream.binance.com:9443/ws/bnbusdt@depth5@100ms",
                              on_open=on_open,
                              on_message=on_message,
                              on_error=on_error,
                              on_close=on_close)

    ws.run_forever(dispatcher=rel, reconnect=5)  # Set dispatcher to automatic reconnection, 5 second reconnect delay if connection closed unexpectedly
    rel.signal(2, rel.abort)  # Keyboard Interrupt
    rel.dispatch()