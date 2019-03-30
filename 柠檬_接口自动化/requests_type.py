import requests
def my_requests(type,url,data,headers):
    if type =='get':
        res = requests.get(url,data=data,headers=headers)
    elif type == 'post':
        res = requests.post(url,data=data,headers=headers)
    else:
        print("您的请求方式，暂不支持")
        return
    return [res.status_code,res.text]
