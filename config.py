import os
import ProxyCloud

BOT_TOKEN =  os.environ.get('bot_token','2055511005:AAGxr5efMPPeB_qEfpPErIaEplyNxWcYflg')
API_ID =  os.environ.get('api_id','7618603')
API_HASH = os.environ.get('api_hash','5646106d87debbd9becfb7f13856763f')
SPLIT_FILE = 1024 * 1024 * int(os.environ.get('split_file','99'))
ROOT_PATH = 'root/'
ACCES_USERS = ('Krixt0')
PROXY = ProxyCloud.parse(os.environ.get('proxy_enc','http://KDGDJDYDJDLDFDYDKDKDDDYDJDJDHDRDDDLDDDLD'))

if PROXY:
  print(f'Proxy {PROXY.as_dict_proxy()}')
