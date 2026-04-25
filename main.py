# hate netherlands ip))
# ]OXCBRawkURpo74P

from fnmatch import fnmatch
from requests import get as rget

my_ip = rget('https://api.ipify.org').text

ips = [
]

for x in range(90, 96):
    ips.append(f"103.{x}.*.*")

for x in range(16, 20):
    ips.append(f"2.{x}.*.*")

ips.append("213.75.*.*")
ips.append("185.*.*.*")

print(ips)

for ip in ips:
    if fnmatch(my_ip, ip):
        print('Netherland!!!')