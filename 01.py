# -*- coding: utf8 -*-
from aliyunsdkcore.client import AcsClient
from aliyunsdkcore.acs_exception.exceptions import ClientException
from aliyunsdkcore.acs_exception.exceptions import ServerException
from aliyunsdkecs.request.v20140526 import DescribeInstancesRequest
from aliyunsdkecs.request.v20140526 import StopInstanceRequest
# 创建AcsClient实例
client = AcsClient(
   "LTAI7G0ILr3MeK78",
   "iFMvVjrokyM4cmI4TQ0xqY0Jcdz9Qi",
   "cn-beijing"
);
# 创建request，并设置参数
request = DescribeInstancesRequest.DescribeInstancesRequest()
request.set_PageSize(10)
# 发起API请求并显示返回值
response = client.do_action_with_exception(request)
print (request)