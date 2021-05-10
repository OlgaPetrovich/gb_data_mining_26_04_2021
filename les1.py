from pathlib import Path
import requests

temp_file = Path(__file__).parent.joinpath("temp.html")


url = "https://5ka.ru/special_offers/"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:88.0) Gecko/20100101 Firefox/88.0"
}

response = requests.get(url, headers=headers)
temp_file.write_bytes(response.content)
