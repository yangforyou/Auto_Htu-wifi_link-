import requests
import re
import time

url = 'http://10.101.2.199/portalAuthAction.do'

playload = {
    "wlanuserip": "10.105.241.184", "wlanacname": "HSD-BRAS-SR8808/X-2", "chal_id": "", "chal_vector": "",
    "auth_type": "PAP", "seq_id": "",
    "req_id": "", "wlanacIp": "10.101.2.35", "ssid": "", "vlan": "", "mac": "", "message": "", "bank_acct": "",
    "isCookies": "", "version": "0", "authkey": "88----89", "url": "",
    "usertime": "0", "listpasscode": "0", "listgetpass": "0", "getpasstype": "0", "randstr": "7253", "domain": "",
    "isRadiusProxy": "true", "usertype": "0", "isHaveNotice": "0", "times": "12",
    "weizhi": "0", "smsid": "1", "freeuser": "", "freepasswd": "", "listwxauth": "0", "templatetype": "1",
    "tname": "shida_pc_portal_mubiao_V2.1", "logintype": "0",
    "act": "", "is189": "false", "terminalType": "", "checkterminal": "true", "portalpageid": "261",
    "listfreeauth": "0", "viewlogin": "1", "userid": "2022124076@lt",
    "authGroupId": "", "userName": "2022124076", "passwd": "wangt123", "useridtemp": "2022124076@lt"
}

resp = requests.post(url, data=playload)
resp.decode = 'utf-8'
obj = re.compile(r'alert(?P<info>.*?);', re.S)
result = obj.finditer(resp.text)
for i in result:
    alert = i.group('info')[2:-2]
if alert == 'Limit Users Err':
    print(alert)
    time.sleep(5)
    print('请等待五秒')
    resp = requests.post(url, data=playload)
else:
    print("登陆成功")
