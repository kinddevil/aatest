#!/usr/bin/env python 
import paramiko 
from datetime import datetime
 
#hostname='192.168.0.102' 
hostname='172.28.102.250' 
username='root' 
password='abc' 
 
#port=22 
if __name__=='__main__': 
        paramiko.util.log_to_file('paramiko.log') 
        s=paramiko.SSHClient() 
        #s.load_system_host_keys() 
        s.set_missing_host_key_policy(paramiko.AutoAddPolicy()) 
        try:
          s.connect(hostname = hostname,username=username, password=password) 
          stdin,stdout,stderr=s.exec_command('ifconfig;free;df -h')
          print stdout.read()

        except:
          print "fuck"
          f = file('paramiko.log','w')
          f.write(" ".join([str(datetime.now()), "fuck\n"]))
          f.close()
        else:
          print "how"
        finally:
          print "super fuck"
        s.close()
