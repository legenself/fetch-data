# 接入文档

## 签名方式
在申请到appid和appkey以后，即可开始制作签名

需要准备的参数有，appkey，timestamp，nonce

appkey已经获得

timestamp是当前的utc时间 格式如下 2017/1/5 8:09:55

nonce 是一个随机字符串都可以

将appkey，timestamp，nonce 按照字典顺序排列并连接起来

```
若
appid='12345678'
appkey='12345678'
timestamp='2018/7/4 1:47:46'
nonce='123456'

则连接结果为
'123456123456782018/7/4 1:47:46'
```
对结果进行两次MD5计算
就可得出签名sign作为请求参数


## 请求

以testapi为例

请求参数类型
```
Content-Type: application/x-www-form-urlencoded; charset=UTF-8
```
post的表单参数 form data
```
appid: 12345678
timestamp: 2018/7/4 7:18:13
nonce: 123456
sign: 3aa746e64984dd0047e08c1281640b9b
```
请求应该如下
```

Content-Type: application/x-www-form-urlencoded;charset=utf-8

appid=12345678&timestamp=2018%2F7%2F4+7%3A18%3A13&nonce=123456&sign=3aa746e64984dd0047e08c1281640b9b
```
