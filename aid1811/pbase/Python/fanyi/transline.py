import hashlib 
import random
import http.client #模拟上网行为
import urllib.parse
import json

appid="20181208000245482"
serectKey="zh1qcppxHrnzrr0_QaY0"
from_lang="auto" #待翻译的文本语言,auto表示自动检测
to_lang="auto" #输出结果的语言,en表示英语

def translate():#获取待翻译的文本
    fin = open("/home/tarena/aid1811/pbasce/fanyi/待翻译.txt","r",encoding="utf-8")#提取
    fout = open("/home/tarena/aid1811/pbasce/fanyi/待翻译.txt","w",encoding="utf-8")#写入
    #读取文本中的内容
    for eachline in fin:
        #去掉空格
        q=eachline.strip()
        #加密
        salt=random.randint(0,1000)
        #编写签名
        sign=appid+q+str(salt)+serectKey  #appid+q+salt+密钥
        m1=hashlib.md5()
        m1.update(sign.encode("utf-8"))
        sign = m1.hexdigect()
        print(sign)
   #访问路进的拼接　/api/trans/vip/translate?q=apple&from=en&to=zh&appid=2015063000000001&salt=1435660288&sign=f89f9594663708c1605f3d736d01d2d4
        my_url = "/api/trans/vip/translate"+"?q="+urllib.parse.quote(q)+"&from="+from_lang+"&to="+to_lang+"&appid="+appid+"&salt="+str(salt)+"&sign="+sign

   #向百度发起请求
    httpClient = http.client.HTTPConnection("api.fanyi.baidu.com")
    response = httpClient.request("GET",my_url)
    response=httpClient.getresponse().read().decode("utf-8")
    print(response)
    print(type(response))
    res = json.loads(response)
    print(res)
    try:
        target = res["trans_result"][0]["dst"]
        fout.write(target+"\n")
    except KeyError:
        print("忽略空行：")
    fin.close()
    fout.close()




if __name__ == "__main__":
    translate()
