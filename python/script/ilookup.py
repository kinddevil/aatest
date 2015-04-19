import requests
import json
import sys
import logging

logging.basicConfig(
  #filename = 'log.log',
  stream = sys.stdout,
  level = logging.DEBUG,
  format = '%(asctime)s.%(msecs)d %(levelname)s %(module)s - %(funcName)s:%(message)s', 
  datefmt='%Y-%m-%d %H:%M:%S'
)
logger = logging.getLogger()

class Lookup(object):

  def __init__(self):
    self.url = 'https://itunes.apple.com/lookup?id='  
    self.headers = {}
    self.headers['User-Agent'] = 'Mozilla/5.0'

  def __del__(self):
    pass

  def lookup(self, aid):
    lens, resp = 0, None
    try:
      response = requests.get(self.url+aid, headers = self.headers)
      ret = json.loads(response.text)
      lens, resp =  len(ret['results']) , ret
    except Exception as e:
      logger.error(unicode(e))
    return lens, resp

if __name__ == '__main__':
  print sys.argv
  if len(sys.argv) == 1:
    exit('no argument')
  lp = Lookup()
  a, b = lp.lookup(sys.argv[1])
  logger.info(str(a) + str(b) )
