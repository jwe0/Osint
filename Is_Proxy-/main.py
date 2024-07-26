import requests, socket, json, os, time

class Main:
    def __init__(self):
        self.info             = {}
        self.info["Target"]   = ""
        self.info["IsProxy"]  = {}
        self.info['Location'] = {}
        self.files            = os.listdir("Lists")
        self.path             = "Lists/"
        self.target           = ""
        self.amount           = 0

    def ReverseDNS(self):
        try:
            self.info["ReverseDNS"] = socket.gethostbyaddr(self.target)[0]
        except:
            self.info["ReverseDNS"] = ""

    def BasicInfo(self):
        api = "http://ip-api.com/json/{}".format(self.target)
        data = requests.get(api).json()
        if data['status'] != "success":
            return
        self.info['Location']['Country'] = data['country']
        self.info['Location']['City'] = data['city']
        self.info['Location']['Region'] = data['regionName']
        self.info['Location']['ISP'] = data['isp']

    def Check(self):
        for file in self.files:
            nodes = [node.strip() for node in open(self.path + file, 'r').readlines()]
            self.amount += len(nodes)
            if self.target in nodes:
                if "-" in file:
                    self.info["IsProxy"][file.split("-")[0]] = True
                else:
                    self.info["IsProxy"][file.split(".txt")[0]] = True

    def Main(self):
        self.target = input("IP : ")
        self.info["Target"] = self.target
        start = time.time()
        self.BasicInfo()
        self.ReverseDNS()
        self.Check()
        end = time.time()
        self.info["Amounts"] = {}
        self.info["Amounts"]["Total databases"] = len(self.files)
        self.info["Amounts"]["Total nodes"] = self.amount
        self.info["Time"] = round(end - start)
        print(json.dumps(self.info, indent=4))

        
if __name__ == "__main__":
    main = Main()
    main.Main()