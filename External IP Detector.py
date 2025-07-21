import requests

def get_external_ip():
    response = requests.get("https://api.ipify.org")
    print("External IP:", response.text)

if __name__ == "__main__":
    get_external_ip()
