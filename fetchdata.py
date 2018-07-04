from urllib import request,parse
import hashlib,string
import random
from datetime import datetime


# 参数初始化 appid 和appkey 待配置
# 若使用示例的appid和appkey 
# 则只能请求测试api来验证请求是否成功！！！！
# 无法使用数据接口!!!!!!!! 
# 请求数据接口会返回签名异常！！！！！
appid='12345678'
appkey='12345678'

# utc时间的 yyyy-mm-dd HH:MM:SS 的格式的字符串 作为时间签名
timestamp=datetime.utcnow().strftime("%Y/%m/%d %H:%M:%S") 

# 随机数，任何都可以
nonce=str(random.randint(1000,1000000))

# 待计算的参数列表
sign_list=[appkey,timestamp,nonce]

# 将参数排序且，连接成一个字符串
sign_list.sort()
sign_str="".join(sign_list)

# 进行两次md5 计算， 取第二次结果作为签名
once_md5=hashlib.md5(sign_str.encode("utf-8")).hexdigest()
twice_md5=hashlib.md5(once_md5.encode("utf-8")).hexdigest()
sign=twice_md5

# 若
# appid='12345678'
# appkey='12345678'
# timestamp='2018/7/4 1:47:46'
# nonce='123456'
# 
# 则按算法应该可以计算出 sign如下
# '351b80be1b2bb188e4f0acba1d62f238'


# 基础的参数 ---任何一个请求都会用上
base_param=[
    ('appid',appid),
    ('timestamp',timestamp),
    ('nonce',nonce),
    ('sign',sign)
    ]




# post请求，请求对应的url 以及传送参数表单
def post(url,param):
    req = request.Request(url)
    with request.urlopen(req, data=  parse.urlencode(param).encode('utf-8')) as f:
        # 输出状态
        print('状态:', f.status, f.reason)

        # 输出响应头
        for k, v in f.getheaders():
            print('%s: %s' % (k, v))
        
        # 输出数据
        print('数据:', f.read().decode('utf-8'))



# 待测试的列表，包含测试名，url和该测试所需的额外参数
paramlist=[
    {
    'testname':'testApi',
    'testurl':'http://data.wiow.net/Api/Test',
    'extends_param':[] ,
    'des':'用来测试签名是否正确的测试接口'
    },
    {
    'testname':'Flow',
    'testurl':'http://data.wiow.net/Api/Flow',
    'extends_param':[('startdt','2018/5/4 14:00:00')] ,
    'des':'获取startdt这天到随后24小时里的流量数据'
    },
    {
    'testname':'FlowByCode',
    'testurl':'http://data.wiow.net/Api/FlowByCode',
    'extends_param':[('startdt','2018/5/4 14:00:00'),('code','116414')] ,
    'des':'获取startdt这天到随后24小时里的编号为116414的流量数据'

    },
    {
    'testname':'FlowDevices',
    'testurl':'http://data.wiow.net/Api/FlowDevices',
    'extends_param':[] ,
    'des':'获取该用户下的所有流量设备'
    },
    {
    'testname':'Pressure',
    'testurl':'http://data.wiow.net/Api/Pressure',
    'extends_param':[('startdt','2018/5/4 14:00:00')] ,
    'des':'获取startdt这天到随后24小时里的压力数据'
    },
    {
    'testname':'PressureByCode',
    'testurl':'http://data.wiow.net/Api/PressureByCode',
    'extends_param':[('startdt','2018/5/4 14:00:00'),('code','116414')] ,
    'des':'获取startdt这天到随后24小时里的编号为116414的流量数据'

    },
    {
    'testname':'PressureDevices',
    'testurl':'http://data.wiow.net/Api/PressureDevices',
    'extends_param':[] ,
    'des':'获取该用户下的所有压力设备'

    } 
]


for test in paramlist:
    print(test['testname'])
    fetch_param=base_param+test['extends_param']
    post(test['testurl'],fetch_param)
