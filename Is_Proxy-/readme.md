# Is Proxy?
> *Fully python based proxy checker*

Checks if an IP address is a common proxy from a list of IP databases.

## Features
- Checks common VPN and proxy databases
- ReverseDNS to check for domains linked
- Basic location lookup with the `ip-api.com` api
- Easily scalable by adding more files to the List directory

## Example result
```json
{
    "Target": "5.226.142.180",
    "IsProxy": {
        "NORDVPN": true
    },
    "Location": {
        "Country": "United Kingdom",
        "City": "London",
        "Region": "England",
        "ISP": "Hydra Communications Ltd"
    },
    "ReverseDNS": "180.142.226.5.baremetal.zare.com",
    "Amounts": {
        "Total databases": 227,
        "Total nodes": 34121
    },
    "Time": 0
}
```