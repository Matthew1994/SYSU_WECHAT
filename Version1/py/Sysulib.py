#coding=utf-8
import urllib
import urllib2
import cookielib
import time
import hashlib

reqUrl = r"http://202.116.64.108:8991/F/-"

#mylib post form
func = "login-session"
login_source = "bor-info"
bor_library= "ZSU50"
bor_id = "13331143"
bor_verification = "254297"


cj = cookielib.CookieJar()
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
opener.addheaders = [('User-agent','Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1)')]

def mylib(userName, password):
    data = urllib.urlencode({'func':func, 'login_source':login_source,
                            'bor_library':bor_library,'bor_id':bor_id, 
                            'bor_verification':bor_verification})
    try:
        res = opener.open(reqUrl, data)
        return res.read()
    except urllib2.URLError as e:
        if hasattr(e, 'code'):
            print u'登陆失败！'+'Error code:',e.code
        elif hasattr(e, 'reason'):
            print u'登陆失败！'+'Reason:',e.reason
        return False;