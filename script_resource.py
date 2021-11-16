import psutil
import requests

def main():

    URL = r"http://localhost:3000/api/history"

    resource = {
        "ip": socket.gethostbyname(socket.gethostname()),
        "cpu" :  psutil.cpu_times(),
        "memory" : psutil.virtual_memory(),
        "disk" : psutil.disk_usage('/'),
    }

    #send requests api to host servers
    requests.post(URL ,json=resource)

if __name__ == "__main__":
    main()









    