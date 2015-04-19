import requests
import json
import sys

class Lookup(object):

  def __init__(self):
    self.url = 'https://itunes.apple.com/lookup?id='  
    self.headers = {}
    self.headers['User-Agent'] = 'Mozilla/5.0'

  def __del__(self):
    pass

  def lookup(self, aid):
    response = requests.get(self.url+aid, headers = self.headers)
    ret = json.loads(response.text)
    print len(ret['results'])
    return len(ret['results']) , ret

if __name__ == '__main__':
  print sys.argv
  if len(sys.argv) == 1:
    exit('no argument')
  lp = Lookup()
  print lp.lookup(sys.argv[1])
