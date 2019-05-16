# Import necessary module
import json
from urllib import request

class Where_am_I:
    def __init__(self, data):

        try:
            self.myURL = json.load(request.urlopen(data))
        except Exception as e:
            print(e)
        else:
            print('Got your location')
    def myIp(self):
        print(f'My IP address is {self.myURL["ip"]}')
    def myAdd(self):
        print(f'Current I am in {self.myURL["city"]}, {self.myURL["region"]}')

def main():
    #Location Tracking URl
    locURL = 'http://ipinfo.io/json'
    trackApp = Where_am_I(locURL)
    trackApp.myIp()
    trackApp.myAdd()

if __name__ == '__main__':
    main()
