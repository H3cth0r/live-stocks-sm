import requests
import asyncio
import websockets
import json


BASE_URL = "http://127.0.0.1:8000/api"
WS_URL = "ws://127.0.0.1:8000/api/ws"
TEST_SYMBOL = "AAPL"

def test_add_stock():
    stock_payload = {
            "symbol": TEST_SYMBOL,
            "name": "Apple Inc :)"
    }

    try:
        response = requests.post(f"{BASE_URL}/stocks/", json=stock_payload)
        if response.status_code == 200:
            print("Success: Stock Added")
            print("Response: ", response.json())
        elif response.status_code == 400:
            print("Success: Stock Was already there")
            print("Response: ", response.json())
        else:
            print("ERROR: Not able to add stock. ", response.status_code)
            print("Response: ", response.text)
    except requests.exceptions.ConnectionError as e:
        print("Exception on creation")
        exit()

def test_get_indicators():
    try:
        response = requests.get(f"{BASE_URL}/stocks/{TEST_SYMBOL}/indicators")
        if response.status_code == 200:
            print("Succes: received indicators")
            data = response.json()
            print("Indicators keys found: ", list(data.keys()))
            print(data)
        else:
            print(f"ERROR: received status code: {response.status_code}")
    except requests.exceptions.ConnectionError as e:
        print("Exception on getting indicators")
        exit()


async def test_websocket_connection():
    uri = f"{WS_URL}/{TEST_SYMBOL}"
    print(f"Connecting to {uri}")
    try:
        async with websockets.connect(uri) as websocket:
            print("Successful ws connection")

            for i in range(3):
                print(f"Waiting for message {i + 1}...")
                message = await websocket.recv()
                print(f"    >Received: {message}")
            print("Successfully received 3 messages. Closing connection")
    except Exception as e:
        print(f"ERRPR: {e}")

def main():
    test_add_stock()
    test_get_indicators()
    asyncio.run(test_websocket_connection())
    print("END")

if __name__ == "__main__":
    main()
