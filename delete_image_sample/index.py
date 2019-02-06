import base64
import os

from aliyunsdkcore.client import AcsClient
from aliyunsdkcore.request import CommonRequest

client = AcsClient(os.getenv("ACCESSKEYID"), os.getenv("ACCESSKEYSECRET"), 'ap-northeast-1')
request = CommonRequest()
request.set_domain('imagesearch.ap-northeast-1.aliyuncs.com')
request.set_version('2018-01-20')
request.set_method('POST')
request.set_protocol_type('HTTPS')
request.set_uri_pattern('/item/delete')
request.add_query_param('instanceName', 'imagesearch001')
params = {
    'item_id': '1000',
}

start_offset = 0;
content = ""

meta = ""
for k in params:
    meta = "{}{},{},{}#".format(meta,k,start_offset,start_offset+len(params[k]))
    start_offset += len(params[k])
    content = "{}{}".format(content,params[k])

body = meta[:-1] + "^" + content


request.set_content(body)
response = client.do_action_with_exception(request)
print (response)
