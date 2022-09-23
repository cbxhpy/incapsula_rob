
def get_reese84( ):
    url = "http://127.0.0.1:8888/incap/reese84"

    data = {
        "key": "<<your key>>",
        "url":"https://7net.omni7.jp/ed-first-come-enforme-That-to-colme-would-my-Hye?d=7net.omni7.jp"
    }
    response = requests.post(url=url, json=data)
    r_data = response.json()["resp_data"]
    return r_data
if __name__ == '__main__':
    for _ in range(10):
        print(f"get_reese84={get_reese84()}")
