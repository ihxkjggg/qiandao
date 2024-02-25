import base64
import requests, urllib3
import time

urllib3.disable_warnings()
# 请求获取cooks
url1='http://yqjd.meiri100.cn/login/index'
hearer={
"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
"Accept-Language": "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7",
"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36",
"Accept-Encoding": "gzip, deflate",
"Host": "yqjd.meiri100.cn",
"Connection": "Keep-Alive",
"Upgrade-Insecure-Requests":"1"
}
resp_0 = requests.get(url=url1,headers=hearer, verify=False)


# 拿到cooks在准备登录
hearer['Referer']='http://yqjd.meiri100.cn/login/index'
hearer['Cookie']=resp_0.headers['Set-Cookie']
data={"username":"1518443","password":"yxq199"}
url2="http://yqjd.meiri100.cn/login/login_ok"
resp_0 = requests.post(url=url2,headers=hearer, verify=False,data=data)


# 登录成功跳转
timestamp = int(time.time())
url3=f"http://yqjd.meiri100.cn/taskIssue/index?_={timestamp}"
resp_0 = requests.get(url=url3,headers=hearer, verify=False)
url4="http://yqjd.meiri100.cn/grade/signin_page"
resp_0 = requests.get(url=url4,headers=hearer, verify=False)

print(resp_0)