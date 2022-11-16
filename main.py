import websocket
import threading
import time
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import json
import pandas as pd
import datetime
import random

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

x = []
y = []

# create and modify a pandas dataframe on each websocket message
# read the pandas dataframe in the animate function and plot f(x)

def on_message(ws, message):
    """
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
    print(df)"""
    #print(message)
    x.append(datetime.datetime.now())
    y.append(random.randint(0, 10))

def animate(i, x, y):
    ax.clear()
    ax.plot(x, y)
    plt.subplots_adjust(bottom=0.30)

def on_error(ws, error):
    print(error)

def on_close(ws, close_status_code, close_msg):
    print("### closed ###")

def on_open(ws):
    print("Opened connection")

def wsthread():
    # websocket.enableTrace(True)
    ws = websocket.WebSocketApp("wss://stream.binance.com:9443/ws/bnbusdt@depth5@1000ms",
                                on_open=on_open,
                                on_message=on_message,
                                on_error=on_error,
                                on_close=on_close)
    ws.run_forever()

if __name__ == "__main__":
    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)
    t = threading.Thread(target=wsthread)
    t.start()

    ani = animation.FuncAnimation(fig, animate, fargs=(x, y), interval=100)
    plt.show()