import base64
import os

from aliyunsdkcore.client import AcsClient
from aliyunsdkcore.request import CommonRequest

img_file = 'img.jpg'
b64_img = base64.b64encode(open(img_file, 'rb').read()).decode('ascii')
b64_filename = base64.b64encode(img_file.encode('latin-1')).decode('ascii')


client = AcsClient(os.getenv("ACCESSKEYID"), os.getenv("ACCESSKEYSECRET"), 'ap-northeast-1')
request = CommonRequest()
request.set_domain('imagesearch.ap-northeast-1.aliyuncs.com')
request.set_version('2018-01-20')
request.set_method('POST')
request.set_protocol_type('HTTPS')
request.set_uri_pattern('/item/add')
request.add_query_param('instanceName', 'imagesearch001')
params = {
    'item_id': '1000',
    'cat_id': '0',
    'cust_content': '{k:v}',
    'pic_list': b64_filename
}

params[b64_filename] = b64_img

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
