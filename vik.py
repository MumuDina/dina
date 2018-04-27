# -*- coding: utf-8 -*-

import LINETCR
from LINETCR.lib.curve.ttypes import *
from datetime import datetime
import time, random, sys, ast, re, os, io, json, subprocess, threading, string, codecs, requests, ctypes, urllib, urllib2, wikipedia, tempfile
from bs4 import BeautifulSoup
from urllib import urlopen
import requests
from io import StringIO
from threading import Thread
#from gtts import gTTS
from googletrans import Translator

#kk = LINETCR.LINE()
#kk.login(qr=True)
#kk.loginResult()
#cl = LINETCR.LINE()
#cl.login(qr=True)
#cl.loginResult()

#ki = LINETCR.LINE()
#ki.login(qr=True)
#ki.loginResult()

#kk = LINETCR.LINE()
#kk.login(qr=True)
#kk.loginResult()

#kc = LINETCR.LINE()
#kc.login(qr=True)
#kc.loginResult()

#ks = LINETCR.LINE()
#ks.login(qr=True)
#ks.loginResult()

cl = LINETCR.LINE()
cl.login(token="tokenmu")

ki = LINETCR.LINE()
ki.login(token="")

kk = LINETCR.LINE()
kk.login(token="")

kc = LINETCR.LINE()
kc.login(token="")

ks = LINETCR.LINE()
ks.login(token="")

km = LINETCR.LINE()
km.login(token="")

kt = LINETCR.LINE()
kt.login(token="")


cl

print "login success"
reload(sys)
sys.setdefaultencoding('utf-8')

helpMessage =""" 🔯Pasukan ⚛️ F҉bL҉ V҉ic҉ky҉҉ ⚛️

🔯 􀔃􀅕red arrow right􏿿 Command Public
🚬[Me]     
🚬[Mid]   
🚬[All]     
🚬[Gid] 
🚬[Mc:]
🚬[info@]
🚬[You@]  
🚬[Umid@] 
🚬[Uinfo@]
🚬[Mid all]   
🚬[Mid 1/2/3] 
🚬[Respon]
🚬[Spam]   
🚬[Speed] 
🚬[Up]      
🚬[Next]  
🚬[Banlist] 
🚬[Gn ] 
🚬[Cancel] 
🚬[Set] 
🚬[Open]  
🚬[Close] 
🚬[Kagebunshin @] 
🚬[Byakugan @]  
🚬[Kamui @]
🚬[Kai] 
🚬[Kam]  
🔯 􀔃􀅕red arrow right􏿿 Command Private
⏩[Copy @/Myname: ]
⏩[Mybio:/Allbio:]
⏩[Setgroup] 
⏩[Group pict]
⏩[Ban @] 
⏩[Unban @]  
⏩[Kill] 
⏩[Nk @\Tkick @]
⏩[Ulti @]  
⏩[Invite mid] 
⏩[Kick mid] 
⏩[All join] 
⏩[Bye all]
⏩[1/2/3/4 join] 
⏩[Bye 1/2/3/4] 
🔯 􀔃􀅕red arrow right􏿿 Command CekSider
➡[Lurk🔀Read]
➡[Setp🔀Cek]
➡[Cekon🔀Cekoff]


         🔯My Creator : By 􀌂􀄠􏿿􀌂⚛️ F҉bL҉ V҉ic҉ky҉҉ ⚛️

"""

Setgroup =""" Privasi Menu V.1 􀔃􀄆red check mark􏿿

🔍[Protection]
-- Protect on/off
🔍[Protect Group]
-- Qr on/off
🔍[Mid Via Contact]
-- Contact on/off
🔍[Cancel All Invited]
-- Cancel on/off
🔍[No Joinned]
-- Join on/off
🔍[Protectname]
-- Namelock on/off
"""
KAC=[cl,ki,kk,kc,ks,km,kt]
DEF=[ki,kk,kc,ks,km,kt]
mid = cl.getProfile().mid
Amid = ki.getProfile().mid
Bmid = kk.getProfile().mid
Cmid = kc.getProfile().mid
Dmid = ks.getProfile().mid
Emid = km.getProfile().mid
Fmid = kt.getProfile().mid
Bots=[mid,Amid,Bmid,Cmid,Dmid,Emid,Fmid,"u91b4d82e07fbb74ec6d87f1d620f3b8c","u558cccaae1be4f88c4195bb3f94fa585","uf06fbc519f8948de8111fcd548e3e170","u68e7f07df714b6775aaac286f234b218","u86ea447072238d9298f1792a0a3209bd"]
admin=["u91b4d82e07fbb74ec6d87f1d620f3b8c"]
wait = {
    'contact':False,
    'autoJoin':True,
    'autoCancel':{"on":True,"members":1},
    'leaveRoom':True,
    'timeline':False,
    'autoAdd':True,
    'message':"Thanks for add me🙋🙏",
    "lang":"JP",
    "tag":True,
    "comment":"Auto Like By 👻Untul27👻 \n\nhttp://line.me/ti/p/egQaYIQMhd",
    "commentOn":True,
    "commentBlack":{},
    "wblack":False,
    "dblack":False,
    "clock":False,
    "likeOn":True,
    "blacklist":{},
    "wblacklist":False,
    "dblacklist":False,
    "welcome":False,
    "Protectgr":False,
    "Protectjoin":False,
    "pname":{},
    "pro_name":{},
    "protection":False,
    "Protectcancl":False,
    "protectionOn":True,
    "atjointicket":True,
    }

wait2 = {
    'readPoint':{},
    'readMember':{},
    'setTime':{},
    'ROM':{}
    }

cctv={
    "cyduk":{},
    "point":{},
    "sidermem":{}
}

mimic = {
    "copy":False,
    "copy2":False,
    "status":False,
    "target":{}
    }

res = {
    'num':{},
    'us':{},
    'au':{},
}

setTime = {}
setTime = wait2['setTime']

contact = cl.getProfile()
backup = cl.getProfile()
backup.displayName = contact.displayName
backup.statusMessage = contact.statusMessage
backup.pictureStatus = contact.pictureStatus

contact = ki.getProfile()
backup = ki.getProfile()
backup.displayName = contact.displayName
backup.statusMessage = contact.statusMessage
backup.pictureStatus = contact.pictureStatus

contact = kk.getProfile()
backup = kk.getProfile()
backup.displayName = contact.displayName
backup.statusMessage = contact.statusMessage
backup.pictureStatus = contact.pictureStatus

contact = kc.getProfile()
backup = kc.getProfile()
backup.displayName = contact.displayName
backup.statusMessage = contact.statusMessage
backup.pictureStatus = contact.pictureStatus

contact = ks.getProfile()
backup = ks.getProfile()
backup.displayName = contact.displayName
backup.statusMessage = contact.statusMessage
backup.pictureStatus = contact.pictureStatus

contact = km.getProfile()
backup = km.getProfile()
backup.displayName = contact.displayName
backup.statusMessage = contact.statusMessage
backup.pictureStatus = contact.pictureStatus

contact = kt.getProfile()
backup = kt.getProfile()
backup.displayName = contact.displayName
backup.statusMessage = contact.statusMessage
backup.pictureStatus = contact.pictureStatus

def upload_tempimage(client):
     '''
         Upload a picture of a kitten. We don't ship one, so get creative!
     '''
     config = {
         'album': album,
         'name':  'bot auto upload',
         'title': 'bot auto upload',
         'description': 'bot auto upload'
     }

     print("Uploading image... ")
     image = client.upload_from_path(image_path, config=config, anon=False)
     print("Done")
     print()

def restart_program():
    python = sys.executable
    os.execl(python, python, * sys.argv)

mulai = time.time()

def waktu(secs):
    mins, secs = divmod(secs,60)
    hours, mins = divmod(mins,60)
    return '%02d Jam %02d Menit %02d Detik' % (hours, mins, secs)

def yt(query):
    with requests.session() as s:
         isi = []
         if query == "":
             query = "S1B tanysyz"   
         s.headers['user-agent'] = 'Mozilla/5.0'
         url    = 'http://www.youtube.com/results'
         params = {'search_query': query}
         r    = s.get(url, params=params)
         soup = BeautifulSoup(r.content, 'html5lib')
         for a in soup.select('.yt-lockup-title > a[title]'):
            if '&list=' not in a['href']:
                if 'watch?v' in a['href']:
                    b = a['href'].replace('watch?v=', '')
                    isi += ['youtu.be' + b]
         return isi

def mention(to, nama):
    aa = ""
    bb = ""
    strt = int(14)
    akh = int(14)
    nm = nama
    for mm in nm:
      akh = akh + 2
      aa += """{"S":"""+json.dumps(str(strt))+""","E":"""+json.dumps(str(akh))+""","M":"""+json.dumps(mm)+"},"""
      strt = strt + 6
      akh = akh + 4
      bb += "\xe2\x95\xa0 @x \n"
    aa = (aa[:int(len(aa)-1)])
    msg = Message()
    msg.to = to
    msg.text = "\xe2\x95\x94\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\n"+bb+"\xe2\x95\x9a\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90"
    msg.contentMetadata ={'MENTION':'{"MENTIONEES":['+aa+']}','EMTVER':'4'}
    print "[Command] Tag All"
    try:
       cl.sendMessage(msg)
    except Exception as error:
       print error

def cms(string, commands): #/XXX, >XXX, ;XXX, ^XXX, %XXX, $XXX...
    tex = ["+","@","/",">",";","^","%","$","＾","サテラ:","サテラ:","サテラ：","サテラ："]
    for texX in tex:
        for command in commands:
            if string ==command:
                return True
    return False

def upload_tempimage(client):
     '''
         Upload a picture of a kitten. We don't ship one, so get creative!
     '''
     config = {
         'album': album,
         'name':  'bot auto upload',
         'title': 'bot auto upload',
         'description': 'bot auto upload'
     }

     print("Uploading image... ")
     image = cl.upload_from_path(image_path, config=config, anon=False)
     print("Done")
     print()

     return image

def sendMessage(to, text, contentMetadata={}, contentType=0):
    mes = Message()
    mes.to, mes.from_ = to, profile.mid
    mes.text = text
    mes.contentType, mes.contentMetadata = contentType, contentMetadata
    if to not in messageReq:
        messageReq[to] = -1
    messageReq[to] += 1

def sendAudio(self, to, path):
        objectId = self.sendMessage(to=to, text=None, contentType = 3).id
        files = {
            'file': open(path, 'rb'),
        }
        params = {
            'name': 'media',
            'oid': objectId,
            'size': len(open(path, 'rb').read()),
            'type': 'audio',
            'ver': '1.0',
        }
        data = {
            'params': json.dumps(params)
        }
        r = self.server.postContent(self.server.LINE_OBS_DOMAIN + '/talk/m/upload.nhn', data=data, files=files)
        if r.status_code != 201:
            raise Exception('Upload audio failure.')
        return True
        
def sendAudioWithURL(self, to_, url):
        path = 'pythonLiness.data'
        r = requests.get(url, stream=True)
        if r.status_code == 200:
            with open(path, 'w') as f:
                shutil.copyfileobj(r.raw, f)
        else:
            raise Exception('Download Audio failure.')
        try:
            self.sendAudio(to_, path)
        except Exception as e:
            raise e

def sendAudio(self, to, path):
        objectId = self.sendMessage(to=to, text=None, contentType = 3).id
        files = {
            'file': open(path, 'rb'),
        }
        params = {
            'name': 'media',
            'oid': objectId,
            'size': len(open(path, 'rb').read()),
            'type': 'audio',
            'ver': '1.0',
        }
        data = {
            'params': json.dumps(params)
        }
        r = self.server.postContent(self.server.LINE_OBS_DOMAIN + '/talk/m/upload.nhn', data=data, files=files)
        if r.status_code != 201:
            raise Exception('Upload audio failure.')
        return True

def restart_program():
    python = sys.executable
    os.execl(python, python, * sys.argv)

def sendImage(cl, to_, path):
      M = Message(to=to_, text=None, contentType = 1)
      M.contentMetadata = None
      M.contentPreview = None
      M2 = cl.sendMessage(0,M)
      M_id = M2.id
      files = {
         'file': open(path, 'rb'),
      }
      params = {
         'name': 'media',
         'oid': M_id,
         'size': len(open(path, 'rb').read()),
         'type': 'image',
         'ver': '1.0',
      }
      data = {
         'params': json.dumps(params)
      }
      r = cl.post_content('https://obs-sg.line-apps.com/talk/m/upload.nhn', data=data, files=files)
      if r.status_code != 201:
         raise Exception('Upload image failure.')
      return True

def sendImageWithURL(cl, to_, url):
      path = '%s/pythonLine-%i.data' % (tempfile.gettempdir(), randint(0, 9))
      r = requests.get(url, stream=True)
      if r.status_code == 200:
         with open(path, 'w') as f:
            shutil.copyfileobj(r.raw, f)
      else:
         raise Exception('Download image failure.')
      try:
         cl.sendImage(to_, path)
      except:
         try:
            cl.sendImage(to_, path)
         except Exception as e:
            raise e

def NOTIFIED_READ_MESSAGE(op):
    try:
        if op.param1 in wait2['readPoint']:
            Name = cl.getContact(op.param2).displayName
            if Name in wait2['readMember'][op.param1]:
                pass
            else:
                wait2['readMember'][op.param1] += "\n・" + Name
                wait2['ROM'][op.param1][op.param2] = "・" + Name
        else:
            pass
    except:
        pass

def RECEIVE_MESSAGE(op):
    msg = op.message
    try:
        if msg.contentType == 0:
            try:
                if msg.to in wait2['readPoint']:
                    if msg.from_ in wait2["ROM"][msg.to]:
                        del wait2["ROM"][msg.to][msg.from_]
                else:
                    pass
            except:
                pass
        else:
            pass
    except KeyboardInterrupt:
	       sys.exit(0)
    except Exception as error:
        print error
        print ("\n\nRECEIVE_MESSAGE\n\n")
        return
	

def bot(op):
    try:
        if op.type == 0:
            return
        if op.type == 5:
            if wait["autoAdd"] == True:
                cl.findAndAddContactsByMid(op.param1)
                if (wait["message"] in [""," ","\n",None]):
                    pass
                else:
                    cl.sendText(op.param1,str(wait["message"]))

        #------Protect Group Kick start------#
        if op.type == 11:
          if wait["Protectgr"] == True:
            if cl.getGroup(op.param1).preventJoinByTicket == False:
              if op.param2 in Bots:
                pass
              if op.param2 in admin:
                pass
              else:
                try:
                  ki.sendText(op.param1,ki.getContact(op.param2).displayName + "Jangan Buka Kode QR ")
                  random.choice(DEF).kickoutFromGroup(op.param1,[op.param2])
                  G = ki.getGroup(op.param1)
                  G.preventJoinByTicket = True
                  ki.updateGroup(G)
                except:
                  random.choice(KAC).sendText(op.param1,random.choice(KAC).getContact(op.param2).displayName + "Jangan Buka Kode QR Njiiir")
                  random.choice(DEF).kickoutFromGroup(op.param1,[op.param2])
                  Z = random.choice(KAC).getGroup(op.param1)
                  Z.preventJoinByTicket = True
                  random.choice(KAC).updateGroup(Z)
        #------Protect Group Kick finish-----#

        #------Cancel Invite User start------#
        if op.type == 13:
          if wait["Protectcancl"] == True:
            group = cl.getGroup(op.param1)
            gMembMids = [contact.mid for contact in group.invitee]
            if op.param2 in Bots:
              pass
            if op.param2 in admin:
              pass
            else:
              random.choice(DEF).cancelGroupInvitation(op.param1, gMembMids)
              random.choice(KAC).sendText(op.param1, "Mau Ngundang Siapa Ka?\nKk Bukan Admin\nJadi Aku Cancel😛")
        #------Cancel Invite User Finish------#

        if op.type == 17:
           if wait["welcome"] == True:
            if op.param2 in Bots:
                return
            ginfo = cl.getGroup(op.param1)
            path = "http://dl.profile.line-cdn.net/" + cl.getContact(op.param2).pictureStatus
            cl.sendText(op.param1, "🚩" + cl.getContact(op.param2).displayName + "🚩" + "↪🔯Welcome🔯↩" + "\nTo\n" + str(ginfo.name) + "\n" + "Creator\n" + ginfo.creator.displayName)
            cl.sendImageWithURL(op.param1, path)
            print "MEMBER HAS JOIN THE GROUP"
        if op.type == 15:
           if wait["welcome"] == True:
            if op.param2 in Bots:
                return
            ginfo = cl.getGroup(op.param1)
            path = "http://dl.profile.line-cdn.net/" + cl.getContact(op.param2).pictureStatus
            cl.sendText(op.param1, " ⚠Good Bye⚠\n " + cl.getContact(op.param2).displayName + "\n" + "🔥Good Luck🔥")
            cl.sendImageWithURL(op.param1, path)
            print "MEMBER HAS LEFT THE GROUP"       


        if op.type == 13:
            if op.param3 in mid:
                if op.param2 in Amid:
                    G = cl.getGroup(op.param1)
                    G.preventJoinByTicket = False
                    kt.updateGroup(G)
                    Ticket = kt.reissueGroupTicket(op.param1)
                    cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                    G.preventJoinByTicket = True
                    Amid.updateGroup(G)
                    Ticket = cl.reissueGroupTicket(op.param1)

            if op.param3 in Amid:
                if op.param2 in mid:
                    X = cl.getGroup(op.param1)
                    X.preventJoinByTicket = False
                    cl.updateGroup(X)
                    Ti = cl.reissueGroupTicket(op.param1)
                    ki.acceptGroupInvitationByTicket(op.param1,Ti)
                    X.preventJoinByTicket = True
                    ki.updateGroup(X)
                    Ti = cl.reissueGroupTicket(op.param1)

            if op.param3 in Bmid:
                if op.param2 in Amid:
                    X = cl.getGroup(op.param1)
                    X.preventJoinByTicket = False
                    ki.updateGroup(X)
                    Ti = ki.reissueGroupTicket(op.param1)
                    kk.acceptGroupInvitationByTicket(op.param1,Ti)
                    X.preventJoinByTicket = True
                    kk.updateGroup(X)
                    Ti = ki.reissueGroupTicket(op.param1)

            if op.param3 in Cmid:
                if op.param2 in Bmid:
                    X = cl.getGroup(op.param1)
                    X.preventJoinByTicket = False
                    kk.updateGroup(X)
                    Ti = kk.reissueGroupTicket(op.param1)
                    kc.acceptGroupInvitationByTicket(op.param1,Ti)
                    X.preventJoinByTicket = True
                    kc.updateGroup(X)
                    Ti = kk.reissueGroupTicket(op.param1)

            if op.param3 in Dmid:
                if op.param2 in Cmid:
                    X = cl.getGroup(op.param1)
                    X.preventJoinByTicket = False
                    kc.updateGroup(X)
                    Ti = kc.reissueGroupTicket(op.param1)
                    ks.acceptGroupInvitationByTicket(op.param1,Ti)
                    X.preventJoinByTicket = True
                    kc.updateGroup(X)
                    Ti = ki.reissueGroupTicket(op.param1)

            if op.param3 in Emid:
                if op.param2 in Dmid:
                    X = cl.getGroup(op.param1)
                    X.preventJoinByTicket = False
                    ks.updateGroup(X)
                    Ti = ks.reissueGroupTicket(op.param1)
                    km.acceptGroupInvitationByTicket(op.param1,Ti)
                    X.preventJoinByTicket = True
                    km.updateGroup(X)
                    Ti = ki.reissueGroupTicket(op.param1)

            if op.param3 in Dmid:
                if op.param2 in Cmid:
                    X = cl.getGroup(op.param1)
                    X.preventJoinByTicket = False
                    km.updateGroup(X)
                    Ti = km.reissueGroupTicket(op.param1)
                    kt.acceptGroupInvitationByTicket(op.param1,Ti)
                    X.preventJoinByTicket = True
                    kt.updateGroup(X)
                    Ti = ki.reissueGroupTicket(op.param1)



        if op.type == 13:
            print op.param1
            print op.param2
            print op.param3
            if mid in op.param3:
                G = cl.getGroup(op.param1)
                if wait["autoJoin"] == True:
                    if wait["autoCancel"]["on"] == True:
                        if len(G.members) <= wait["autoCancel"]["members"]:
                            cl.rejectGroupInvitation(op.param1)
                        else:
                            cl.acceptGroupInvitation(op.param1)
                    else:
                        cl.acceptGroupInvitation(op.param1)
                elif wait["autoCancel"]["on"] == True:
                    if len(G.members) <= wait["autoCancel"]["members"]:
                        cl.rejectGroupInvitation(op.param1)
            else:
                Inviter = op.param3.replace("",',')
                InviterX = Inviter.split(",")
                matched_list = []
                for tag in wait["blacklist"]:
                    matched_list+=filter(lambda str: str == tag, InviterX)
                if matched_list == []:
                    pass
                else:
                    cl.cancelGroupInvitation(op.param1, matched_list)
           #------Kick Auto Bl Start----------#
        if op.type == 19:
          if wait["protection"] == True:
                if not op.param2 in Bots:
                    try:
                        gs = cl.getGroup(op.param1)
                        gs = ki.getGroup(op.param1)
                        targets = [op.param2]
                        for target in targets:
                           try:
                                wait["blacklist"][target] = True
                                f=codecs.open('st2__b.json','w','utf-8')
                                json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                           except:
                            return


                    except Exception, e:
                        print e


        if op.type == 11:
          if wait["protection"] == True:
                if not op.param2 in Bots:
                    try:
                        gs = cl.getGroup(op.param1)
                        gs = ki.getGroup(op.param1)
                        targets = [op.param2]
                        for target in targets:
                           try:
                                wait["blacklist"][target] = True
                                f=codecs.open('st2__b.json','w','utf-8')
                                json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                           except:
                            return

                    except Exception, e:
                        print e
        #------Kick Auto Bl Finish---------#
        #-------Kick Bl Join Start---------#
        if op.type == 17:
          if wait["protection"] == True:
            if op.param2 not in Bots:
                joinblacklist = op.param2.replace(".",',')
                joinblacklistX = joinblacklist.split(",")
                matched_list = []
                for tag in wait["blacklist"]:
                    matched_list+=filter(lambda str: str == tag, joinblacklistX)
                if matched_list == []:
                    pass
                else:
                    random.choice(DEF).kickoutFromGroup(op.param1,[op.param2])
         #-------Kick Bl Join Finish--------#                    
        #------Joined User Kick start------#
        if op.type == 17:
           if wait["Protectjoin"] == True:
               if op.param2 not in Bots:
                   random.choice(DEF).kickoutFromGroup(op.param1,[op.param2])
               
        #------Joined User Kick start------#

        if op.type == 11:
            if op.param3 == '1':
                if op.param1 in wait['pname']:
                    try:
                        G = cl.getGroup(op.param1)
                    except:
                        try:
                            G = ki.getGroup(op.param1)
                        except:
                            try:
                                G = kk.getGroup(op.param1)
                            except:
                                try:
                                    G = kc.getGroup(op.param1)
                                except:
                                    try:
                                        G = kk.getGroup(op.param1)
				    except:
					try:
                                            G = ki.getGroup(op.param1)
                                        except:
                                            pass
                    G.name = wait['pro_name'][op.param1]
                    try:
                        cl.updateGroup(G)
                    except:
                        try:
                            ki.updateGroup(G)
                        except:
                            try:
                                kk.updateGroup(G)
                            except:
                                try:
                                    kc.updateGroup(G)
                                except:
                                    try:
                                        ki.updateGroup(G)
                                    except:
                                        try:
                                            cl.updateGroup(G)
                                        except:
                                            pass
                    if op.param2 in ken:
                        pass
                    else:
                        try:
                            ki.kickoutFromGroup(op.param1,[op.param2])
                        except:
                            try:
                                kk.kickoutFromGroup(op.param1,[op.param2])
                            except:
                                try:
                                    kc.kickoutFromGroup(op.param1,[op.param2])
                                except:
                                    try:
                                        cl.kickoutFromGroup(op.param1,[op.param2])
                                    except:
                                        try:
                                            kk.kickoutFromGroup(op.param1,[op.param2])
                                        except:
                                            pass
                                        cl.sendText(op.param1,"Group name lock")
                                        ki.sendText(op.param1,"Haddeuh dikunci Pe'a")
                                        kk.sendText(op.param1,"Wekawekaweka 􀜁􀅔Har Har􏿿")
                                        c = Message(to=op.param1, from_=None, text=None, contentType=13)
                                        c.contentMetadata={'mid':op.param2}
                                        cl.sendMessage(c)
        
        if op.type == 19:
          if wait["protection"] == True:
           if op.param2 not in Bots:
              random.choice(DEF).kickoutFromGroup(op.param1,[op.param2])
              random.choice(KAC).inviteIntoGroup(op.param1,[op.param2])
           else: 
               pass

        if op.type == 19:
          if wait["protection"] == True:
           if op.param3 in admin:
            if op.param2 not in Bots:
              random.choice(DEF).kickoutFromGroup(op.param1,[op.param2])
              random.choice(KAC).inviteIntoGroup(op.param1,[op.param2])
           else:
               pass

        if op.type == 19:
                if mid in op.param3:
                    if op.param2 in Bots:
                        pass
                    try:
                        ki.kickoutFromGroup(op.param1,[op.param2])
                        kc.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                        except:
                            print ("client Kick regulation or Because it does not exist in the group、\n["+op.param1+"]\nの\n["+op.param2+"]\nを蹴る事ができませんでした。\nブラックリストに追加します。")
                        if op.param2 in wait["blacklist"]:
                            pass
                        if op.param2 in wait["whitelist"]:
                            pass
                        else:
                            wait["blacklist"][op.param2] = True
                    G = cl.getGroup(op.param1)
                    G.preventJoinByTicket = False
                    cl.updateGroup(G)
                    Ti = cl.reissueGroupTicket(op.param1)
                    cl.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki.acceptGroupInvitationByTicket(op.param1,Ti)
                    kk.acceptGroupInvitationByTicket(op.param1,Ti)
                    kc.acceptGroupInvitationByTicket(op.param1,Ti)
                    ks.acceptGroupInvitationByTicket(op.param1,Ti)
                    km.acceptGroupInvitationByTicket(op.param1,Ti)
                    kt.acceptGroupInvitationByTicket(op.param1,Ti)

                    X = ki.getGroup(op.param1)
                    X.preventJoinByTicket = True
                    ki.updateGroup(X)
                    Ti = ki.reissueGroupTicket(op.param1)
                    if op.param2 in wait["blacklist"]:
                        pass
                    if op.param2 in wait["whitelist"]:
                        pass
                    else:
                        wait["blacklist"][op.param2] = True

                if Amid in op.param3:
                    if op.param2 in Bots:
                        pass
                    try:
                        cl.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                        except:
                            print ("clientが蹴り規制orグループに存在しない為、\n["+op.param1+"]\nの\n["+op.param2+"]\nを蹴る事ができませんでした。\nブラックリストに追加します。")
                        if op.param2 in wait["blacklist"]:
                            pass
                        if op.param2 in wait["whitelist"]:
                            pass
                        else:
                            wait["blacklist"][op.param2] = True

                    X = ki.getGroup(op.param1)
                    X.preventJoinByTicket = False
                    ki.updateGroup(X)
                    Ti = ki.reissueGroupTicket(op.param1)
                    cl.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki.acceptGroupInvitationByTicket(op.param1,Ti)
                    kk.acceptGroupInvitationByTicket(op.param1,Ti)
                    kc.acceptGroupInvitationByTicket(op.param1,Ti)
                    ks.acceptGroupInvitationByTicket(op.param1,Ti)
                    km.acceptGroupInvitationByTicket(op.param1,Ti)
                    kt.acceptGroupInvitationByTicket(op.param1,Ti)

                    G = cl.getGroup(op.param1)
                    G.preventJoinByTicket = True
                    cl.updateGroup(G)
                    Ticket = cl.reissueGroupTicket(op.param1)
                    if op.param2 in wait["blacklist"]:
                        pass
                    if op.param2 in wait["whitelist"]:
                        pass
                    else:
                        wait["blacklist"][op.param2] = True

                if Bmid in op.param3:
                    if op.param2 in Bots:
                        pass
                    try:
                        kc.kickoutFromGroup(op.param1,[op.param2])
                        km.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                        except:
                            print ("clientが蹴り規制orグループに存在しない為、\n["+op.param1+"]\nの\n["+op.param2+"]\nを蹴る事ができませんでした。\nブラックリストに追加します。")
                        if op.param2 in wait["blacklist"]:
                            pass
                        if op.param2 in wait["whitelist"]:
                            pass
                        else:
                            wait["blacklist"][op.param2] = True

                    X = kc.getGroup(op.param1)
                    X.preventJoinByTicket = False
                    kc.updateGroup(X)
                    Ti = kc.reissueGroupTicket(op.param1)
                    cl.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki.acceptGroupInvitationByTicket(op.param1,Ti)
                    kk.acceptGroupInvitationByTicket(op.param1,Ti)
                    kc.acceptGroupInvitationByTicket(op.param1,Ti)
                    ks.acceptGroupInvitationByTicket(op.param1,Ti)
                    km.acceptGroupInvitationByTicket(op.param1,Ti)
                    kt.acceptGroupInvitationByTicket(op.param1,Ti)

                    G = kk.getGroup(op.param1)
                    G.preventJoinByTicket = True
                    kk.updateGroup(G)
                    Ticket = kk.reissueGroupTicket(op.param1)
                    if op.param2 in wait["blacklist"]:
                        pass
                    if op.param2 in wait["whitelist"]:
                        pass
                    else:
                        wait["blacklist"][op.param2] = True

                if Cmid in op.param3:
                    if op.param2 in Bots:
                        pass
                    try:
                        ki.kickoutFromGroup(op.param1,[op.param2])
                        kt.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                        except:
                            print ("clientが蹴り規制orグループに存在しない為、\n["+op.param1+"]\nの\n["+op.param2+"]\nを蹴る事ができませんでした。\nブラックリストに追加します。")
                        if op.param2 in wait["blacklist"]:
                            pass
                        if op.param2 in wait["whitelist"]:
                            pass
                        else:
                            wait["blacklist"][op.param2] = True

                    X = ki.getGroup(op.param1)
                    X.preventJoinByTicket = False
                    ki.updateGroup(X)
                    Ti = ki.reissueGroupTicket(op.param1)
                    cl.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki.acceptGroupInvitationByTicket(op.param1,Ti)
                    kk.acceptGroupInvitationByTicket(op.param1,Ti)
                    kc.acceptGroupInvitationByTicket(op.param1,Ti)
                    ks.acceptGroupInvitationByTicket(op.param1,Ti)
                    km.acceptGroupInvitationByTicket(op.param1,Ti)
                    kt.acceptGroupInvitationByTicket(op.param1,Ti)
 
                    G = kc.getGroup(op.param1)
                    G.preventJoinByTicket = True
                    kc.updateGroup(G)
                    Ticket = kc.reissueGroupTicket(op.param1)
                    if op.param2 in wait["blacklist"]:
                        pass
                    if op.param2 in wait["whitelist"]:
                        pass
                    else:
                        wait["blacklist"][op.param2] = True

                if Dmid in op.param3:
                    if op.param2 in Bots:
                        pass
                    try:
                        ks.kickoutFromGroup(op.param1,[op.param2])
                        kk.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                        except:
                            print ("clientが蹴り規制orグループに存在しない為、\n["+op.param1+"]\nの\n["+op.param2+"]\nを蹴る事ができませんでした。\nブラックリストに追加します。")
                        if op.param2 in wait["blacklist"]:
                            pass
                        if op.param2 in wait["whitelist"]:
                            pass
                        else:
                            wait["blacklist"][op.param2] = True

                    X = kc.getGroup(op.param1)
                    X.preventJoinByTicket = False
                    kc.updateGroup(X)
                    Ti = kc.reissueGroupTicket(op.param1)
                    cl.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki.acceptGroupInvitationByTicket(op.param1,Ti)
                    kk.acceptGroupInvitationByTicket(op.param1,Ti)
                    kc.acceptGroupInvitationByTicket(op.param1,Ti)
                    ks.acceptGroupInvitationByTicket(op.param1,Ti)
                    km.acceptGroupInvitationByTicket(op.param1,Ti)
                    kt.acceptGroupInvitationByTicket(op.param1,Ti)
 
                    G = ks.getGroup(op.param1)
                    G.preventJoinByTicket = True
                    ks.updateGroup(G)
                    Ticket = ks.reissueGroupTicket(op.param1)
                    if op.param2 in wait["blacklist"]:
                        pass
                    if op.param2 in wait["whitelist"]:
                        pass
                    else:
                        wait["blacklist"][op.param2] = True

                if Emid in op.param3:
                    if op.param2 in Bots:
                        pass
                    try:
                        km.kickoutFromGroup(op.param1,[op.param2])
                        kt.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                        except:
                            print ("clientが蹴り規制orグループに存在しない為、\n["+op.param1+"]\nの\n["+op.param2+"]\nを蹴る事ができませんでした。\nブラックリストに追加します。")
                        if op.param2 in wait["blacklist"]:
                            pass
                        if op.param2 in wait["whitelist"]:
                            pass
                        else:
                            wait["blacklist"][op.param2] = True

                    X = ks.getGroup(op.param1)
                    X.preventJoinByTicket = False
                    ks.updateGroup(X)
                    Ti = ks.reissueGroupTicket(op.param1)
                    cl.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki.acceptGroupInvitationByTicket(op.param1,Ti)
                    kk.acceptGroupInvitationByTicket(op.param1,Ti)
                    kc.acceptGroupInvitationByTicket(op.param1,Ti)
                    ks.acceptGroupInvitationByTicket(op.param1,Ti)
                    km.acceptGroupInvitationByTicket(op.param1,Ti)
                    kt.acceptGroupInvitationByTicket(op.param1,Ti)
 
                    G = km.getGroup(op.param1)
                    G.preventJoinByTicket = True
                    km.updateGroup(G)
                    Ticket = km.reissueGroupTicket(op.param1)
                    if op.param2 in wait["blacklist"]:
                        pass
                    if op.param2 in wait["whitelist"]:
                        pass
                    else:
                        wait["blacklist"][op.param2] = True

                if Fmid in op.param3:
                    if op.param2 in Bots:
                        pass
                    try:
                        ks.kickoutFromGroup(op.param1,[op.param2])
                        ki.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                        except:
                            print ("clientが蹴り規制orグループに存在しない為、\n["+op.param1+"]\nの\n["+op.param2+"]\nを蹴る事ができませんでした。\nブラックリストに追加します。")
                        if op.param2 in wait["blacklist"]:
                            pass
                        if op.param2 in wait["whitelist"]:
                            pass
                        else:
                            wait["blacklist"][op.param2] = True

                    X = km.getGroup(op.param1)
                    X.preventJoinByTicket = False
                    km.updateGroup(X)
                    Ti = km.reissueGroupTicket(op.param1)
                    cl.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki.acceptGroupInvitationByTicket(op.param1,Ti)
                    kk.acceptGroupInvitationByTicket(op.param1,Ti)
                    kc.acceptGroupInvitationByTicket(op.param1,Ti)
                    ks.acceptGroupInvitationByTicket(op.param1,Ti)
                    km.acceptGroupInvitationByTicket(op.param1,Ti)
                    kt.acceptGroupInvitationByTicket(op.param1,Ti)
 
                    G = kt.getGroup(op.param1)
                    G.preventJoinByTicket = True
                    kt.updateGroup(G)
                    Ticket = kt.reissueGroupTicket(op.param1)
                    if op.param2 in wait["blacklist"]:
                        pass
                    if op.param2 in wait["whitelist"]:
                        pass
                    else:
                        wait["blacklist"][op.param2] = True
                 
                    
        if op.type == 13:
            if mid in op.param3:
                G = cl.getGroup(op.param1)
                if wait["autoJoin"] == True:
                    if wait["autoCancel"]["on"] == True:
                        if len(G.members) <= wait["autoCancel"]["members"]:
                            cl.rejectGroupInvitation(op.param1)
                        else:
                            cl.acceptGroupInvitation(op.param1)
                    else:
                        cl.acceptGroupInvitation(op.param1)
                elif wait["autoCancel"]["on"] == True:
                    if len(G.members) <= wait["autoCancel"]["members"]:
                        cl.rejectGroupInvitation(op.param1)
            else:
                Inviter = op.param3.replace("",',')
                InviterX = Inviter.split(",")
                matched_list = []
                for tag in wait["blacklist"]:
                    matched_list+=filter(lambda str: str == tag, InviterX)
                if matched_list == []:
                    pass
                else:
                    cl.cancelGroupInvitation(op.param1, matched_list)
                    
        if op.type == 22:
            if wait["leaveRoom"] == True:
                cl.leaveRoom(op.param1)
        if op.type == 24:
            if wait["leaveRoom"] == True:
                cl.leaveRoom(op.param1)
        if op.type == 26:
            msg = op.message
            if 'MENTION' in msg.contentMetadata.keys() != None:
              if wait ["tag"] == True:
                    contact = cl.getContact(msg.from_)
                    cName = contact.displayName
                    path = "http://dl.profile.line-cdn.net/" + cl.getContact(msg.from_).pictureStatus
                    balas = [cName + "Dont tag me, im busy",cName + " ada apa ngetag?",cName + " PM AJA",cName + "apa😕-_-"]
                    ret_ = "[Auto Respon] " + random.choice(balas)
                    name = re.findall(r'@(\w+)', msg.text)
                    mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                    mentionees = mention['MENTIONEES']
                    for mention in mentionees:
                           if mention['M'] in Bots:
                                  cl.sendText(msg.to,ret_)
                                  cl.sendImageWithURL(msg.to, path)


            if msg.toType == 1:
                if wait["leaveRoom"] == True:
                    cl.leaveRoom(msg.to)
            if msg.contentType == 16:
                url = msg.contentMetadata("line://home/post?userMid="+mid+"&postId="+"new_post")
                cl.like(url[25:58], url[66:], likeType=1001)
        if op.type == 25:
            msg = op.message
            if msg.contentType == 13:
               if wait["wblack"] == True:
                    if msg.contentMetadata["mid"] in wait["commentBlack"]:
                        cl.sendText(msg.to,"already")
                        wait["wblack"] = False
                    else:
                        wait["commentBlack"][msg.contentMetadata["mid"]] = True
                        wait["wblack"] = False
                        cl.sendText(msg.to,"decided not to comment")

               elif wait["dblack"] == True:
                   if msg.contentMetadata["mid"] in wait["commentBlack"]:
                        del wait["commentBlack"][msg.contentMetadata["mid"]]
                        cl.sendText(msg.to,"deleted")
                        ki.sendText(msg.to,"deleted")
                        kk.sendText(msg.to,"deleted")
                        kc.sendText(msg.to,"deleted")
                        wait["dblack"] = False

                   else:
                        wait["dblack"] = False
                        cl.sendText(msg.to,"It is not in the black list")
                        ki.sendText(msg.to,"It is not in the black list")
                        kk.sendText(msg.to,"It is not in the black list")
                        kc.sendText(msg.to,"It is not in the black list")
               elif wait["wblacklist"] == True:
                   if msg.contentMetadata["mid"] in wait["blacklist"]:
                        cl.sendText(msg.to,"already")
                        ki.sendText(msg.to,"already")
                        kk.sendText(msg.to,"already")
                        kc.sendText(msg.to,"already")
                        wait["wblacklist"] = False
                   else:
                        wait["blacklist"][msg.contentMetadata["mid"]] = True
                        wait["wblacklist"] = False
                        cl.sendText(msg.to,"aded")
                        ki.sendText(msg.to,"aded")
                        kk.sendText(msg.to,"aded")
                        kc.sendText(msg.to,"aded")

               elif wait["dblacklist"] == True:
                   if msg.contentMetadata["mid"] in wait["blacklist"]:
                        del wait["blacklist"][msg.contentMetadata["mid"]]
                        cl.sendText(msg.to,"deleted")
                        ki.sendText(msg.to,"deleted")
                        kk.sendText(msg.to,"deleted")
                        kc.sendText(msg.to,"deleted")
                        wait["dblacklist"] = False

                   else:
                        wait["dblacklist"] = False
                        cl.sendText(msg.to,"It is not in the black list")
                        ki.sendText(msg.to,"It is not in the black list")
                        kk.sendText(msg.to,"It is not in the black list")
                        kc.sendText(msg.to,"It is not in the black list")
               elif wait["contact"] == True:
                    msg.contentType = 0
                    cl.sendText(msg.to,msg.contentMetadata["mid"])
                    if 'displayName' in msg.contentMetadata:
                        contact = cl.getContact(msg.contentMetadata["mid"])
                        try:
                            cu = cl.channel.getCover(msg.contentMetadata["mid"])
                        except:
                            cu = ""
                        cl.sendText(msg.to,"[displayName]:\n" + msg.contentMetadata["displayName"] + "\n[mid]:\n" + msg.contentMetadata["mid"] + "\n[statusMessage]:\n" + contact.statusMessage + "\n[pictureStatus]:\nhttp://dl.profile.line-cdn.net/" + contact.pictureStatus + "\n[coverURL]:\n" + str(cu))
                    else:
                        contact = cl.getContact(msg.contentMetadata["mid"])
                        try:
                            cu = cl.channel.getCover(msg.contentMetadata["mid"])
                        except:
                            cu = ""
                        cl.sendText(msg.to,"[displayName]:\n" + contact.displayName + "\n[mid]:\n" + msg.contentMetadata["mid"] + "\n[statusMessage]:\n" + contact.statusMessage + "\n[pictureStatus]:\nhttp://dl.profile.line-cdn.net/" + contact.pictureStatus + "\n[coverURL]:\n" + str(cu))
            elif msg.contentType == 16:
                if wait["timeline"] == True:
                    msg.contentType = 0
                    if wait["lang"] == "JP":
                        msg.text = "post URL\n" + msg.contentMetadata["postEndUrl"]
                    else:
                        msg.text = "URLâ†’\n" + msg.contentMetadata["postEndUrl"]
                    cl.sendText(msg.to,msg.text)
            elif msg.text is None:
                return
            elif msg.text in ["Key","help","Help"]:
              if msg.from_ in Bots:
                if wait["lang"] == "JP":
                    cl.sendText(msg.to,helpMessage)
                else:
                    cl.sendText(msg.to,help)
            elif msg.text in ["Setgroup"]:
              if msg.from_ in admin:
                if wait["lang"] == "JP":
                    cl.sendText(msg.to,Setgroup)
                else:
                    cl.sendText(msg.to,Setgroup)
            elif ("Gn " in msg.text):
                if msg.toType == 2:
                    X = cl.getGroup(msg.to)
                    X.name = msg.text.replace("Gn ","")
                    cl.updateGroup(X)
                else:
                    cl.sendText(msg.to,"It can't be used besides the group.")
            elif ("1 gn " in msg.text):
                if msg.toType == 2:
                    X = cl.getGroup(msg.to)
                    X.name = msg.text.replace("1gn ","")
                    ki.updateGroup(X)
                else:
                    ki.sendText(msg.to,"It can't be used besides the group.")
            elif ("2gn " in msg.text):
                if msg.toType == 2:
                    X = cl.getGroup(msg.to)
                    X.name = msg.text.replace("2gn ","")
                    kk.updateGroup(X)
                else:
                    kk.sendText(msg.to,"It can't be used besides the group.")
            elif ("3gn " in msg.text):
                if msg.toType == 2:
                    X = cl.getGroup(msg.to)
                    X.name = msg.text.replace("3gn ","")
                    kc.updateGroup(X)
                else:
                    kc.sendText(msg.to,"It can't be used besides the group.")
            elif "Kick " in msg.text:
              if msg.from_ in admin:
                midd = msg.text.replace("Kick ","")
                cl.kickoutFromGroup(msg.to,[midd])
            elif "Ckick " in msg.text:
              if msg.from_ in admin:
                midd = msg.text.replace("Mkick ","")
                ki.kickoutFromGroup(msg.to,[midd])
            elif "Bkick " in msg.text:
              if msg.from_ in admin:
                midd = msg.text.replace("Bkick ","")
                kk.kickoutFromGroup(msg.to,[midd])
            elif "Kkick " in msg.text:
              if msg.from_ in admin:
                midd = msg.text.replace("Kkick ","")
                kc.kickoutFromGroup(msg.to,[midd])
            elif "Invite " in msg.text:
              if msg.from_ in admin:
                midd = msg.text.replace("Invite ","")
                cl.findAndAddContactsByMid(midd)
                cl.inviteIntoGroup(msg.to,[midd])
            elif "Cinvite " in msg.text:
              if msg.from_ in admin:
                midd = msg.text.replace("Cinvite ","")
                ki.findAndAddContactsByMid(midd)
                ki.inviteIntoGroup(msg.to,[midd])
            elif "Binvite " in msg.text:
              if msg.from_ in admin:
                midd = msg.text.replace("Binvite ","")
                kk.findAndAddContactsByMid(midd)
                kk.inviteIntoGroup(msg.to,[midd])
            elif "Kinvite " in msg.text:
              if msg.from_ in admin:
                midd = msg.text.replace("Kinvite ","")
                kc.findAndAddContactsByMid(midd)
                kc.inviteIntoGroup(msg.to,[midd])
            elif msg.text in ["All"]:
                msg.contentType = 13
                msg.contentMetadata = {'mid': mid}
                cl.sendMessage(msg)

                msg.contentType = 13
                msg.contentMetadata = {'mid': Amid}
                ki.sendMessage(msg)

                msg.contentType = 13
                msg.contentMetadata = {'mid': Bmid}
                kk.sendMessage(msg)

                msg.contentType = 13
                msg.contentMetadata = {'mid': Cmid}
                kc.sendMessage(msg)

                msg.contentType = 13
                msg.contentMetadata = {'mid': Dmid}
                ks.sendMessage(msg)
            elif msg.text in ["Me"]:
                msg.contentType = 13
                msg.contentMetadata = {'mid': msg.from_}
                cl.sendMessage(msg)
            elif "Myname:" in msg.text:
                string = msg.text.replace("Myname:","")
                if len(string.decode('utf-8')) <= 20:
                    profile = cl.getProfile()
                    profile.displayName = string
                    cl.updateProfile(profile)
                    cl.sendText(msg.to,"Update Names Menjadi : " + string + "")
            elif "Mybio:" in msg.text:
                string = msg.text.replace("Mybio:","")
                if len(string.decode('utf-8')) <= 500:
                    profile = cl.getProfile()
                    profile.statusMessage = string
                    cl.updateProfile(profile)
                    cl.sendText(msg.to,"Update Bio👉" + string + "")
        #----------------Fungsi Start------------------#
            elif msg.text.lower() == 'Bot restart':
              if msg.from_ in admin:
                    print "[Command]Like executed"
                    try:
                        cl.sendText(msg.to,"Restarting...")
                        restart_program()
                    except:
                        cl.sendText(msg.to,"Please wait")
                        restart_program()
                        pass
            elif msg.text.lower() == 'Ifconfig':
              if msg.from_ in admin:
                    botKernel = subprocess.Popen(["ifconfig"], stdout=subprocess.PIPE).communicate()[0]
                    cl.sendText(msg.to, botKernel + "\n\n===SERVER INFO NetStat===")
            elif msg.text.lower() == 'System':
              if msg.from_ in admin:
                    botKernel = subprocess.Popen(["df","-h"], stdout=subprocess.PIPE).communicate()[0]
                    cl.sendText(msg.to, botKernel + "\n\n===SERVER INFO SYSTEM===")
            elif msg.text.lower() == 'Kernel':
              if msg.from_ in admin:
                    botKernel = subprocess.Popen(["uname","-srvmpio"], stdout=subprocess.PIPE).communicate()[0]
                    cl.sendText(msg.to, botKernel + "\n\n===SERVER INFO KERNEL===")
            elif msg.text.lower() == 'Cpu':
              if msg.from_ in admin:
                    botKernel = subprocess.Popen(["cat","/proc/cpuinfo"], stdout=subprocess.PIPE).communicate()[0]
                    cl.sendText(msg.to, botKernel + "\n\n===SERVER INFO CPU===")
            elif msg.text.lower() == 'Runtime':
              if msg.from_ in admin:
                eltime = time.time() - mulai
                van = "Bot sudah berjalan selama "+waktu(eltime)
                cl.sendText(msg.to,van)
        #----------------Fungsi Finish-----------------#
            elif msg.text in ["æ„›ã�®ãƒ—ãƒ¬ã‚¼ãƒ³ãƒˆ","Gift"]:
                msg.contentType = 9
                msg.contentMetadata={'PRDID': 'a0768339-c2d3-4189-9653-2909e9bb6f58',
                                    'PRDTYPE': 'THEME',
                                    'MSGTPL': '5'}
                msg.text = None
                cl.sendMessage(msg)
            elif msg.text in ["æ„›ã�®ãƒ—ãƒ¬ã‚¼ãƒ³ãƒˆ","Cv1 gift"]:
                msg.contentType = 9
                msg.contentMetadata={'PRDID': 'a0768339-c2d3-4189-9653-2909e9bb6f58',
                                    'PRDTYPE': 'THEME',
                                    'MSGTPL': '6'}
                msg.text = None
                ki.sendMessage(msg)
            elif msg.text in ["æ„›ã�®ãƒ—ãƒ¬ã‚¼ãƒ³ãƒˆ","Cv2 gift"]:
                msg.contentType = 9
                msg.contentMetadata={'PRDID': 'a0768339-c2d3-4189-9653-2909e9bb6f58',
                                    'PRDTYPE': 'THEME',
                                    'MSGTPL': '8'}
                msg.text = None
                kk.sendMessage(msg)
            elif msg.text in ["æ„›ã�®ãƒ—ãƒ¬ã‚¼ãƒ³ãƒˆ","Cv3 gift"]:
                msg.contentType = 9
                msg.contentMetadata={'PRDID': 'a0768339-c2d3-4189-9653-2909e9bb6f58',
                                    'PRDTYPE': 'THEME',
                                    'MSGTPL': '10'}
                msg.text = None
                kc.sendMessage(msg)
            elif msg.text in ["æ„›ã�®ãƒ—ãƒ¬ã‚¼ãƒ³ãƒˆ","All gift"]:
                msg.contentType = 9
                msg.contentMetadata={'PRDID': 'a0768339-c2d3-4189-9653-2909e9bb6f58',
                                    'PRDTYPE': 'THEME',
                                    'MSGTPL': '12'}
                msg.text = None
                ki.sendMessage(msg)
                kk.sendMessage(msg)
                kc.sendMessage(msg)
#==================================================
            elif "All rename:" in msg.text:
              if msg.from_ in admin:
                string = msg.text.replace("All rename:","")
                if len(string.decode('utf-8')) <= 200:
                    profile = ki.getProfile()
                    profile.displayName = string
                    ki.updateProfile(profile)
                if len(string.decode('utf-8')) <= 200:
                    profile = kk.getProfile()
                    profile.displayName = string
                    kk.updateProfile(profile)
                if len(string.decode('utf-8')) <= 200:
                    profile = kc.getProfile()
                    profile.displayName = string
                    kc.updateProfile(profile)
                if len(string.decode('utf-8')) <= 200:
                    profile = ks.getProfile()
                    profile.displayName = string
                    ks.updateProfile(profile)
                    cl.sendText(msg.to,"change name: "+string+"\nsucces")
            elif msg.text.lower() == 'Allbio:':
              if msg.from_ in admin:
                string = msg.text.lower().replace("allbio:","")
                if len(string.decode('utf-8')) <= 5000:
                    profile = ki.getProfile()
                    profile.statusMessage = string
                    ki.updateProfile(profile)
                if len(string.decode('utf-8')) <= 5000:
                    profile = kk.getProfile()
                    profile.statusMessage = string
                    kk.updateProfile(profile)
                if len(string.decode('utf-8')) <= 5000:
                    profile = kc.getProfile()
                    profile.statusMessage = string
                    kc.updateProfile(profile)
                if len(string.decode('utf-8')) <= 5000:
                    profile = cl.getProfile()
                    profile.statusMessage = string
                    cl.updateProfile(profile)
                    cl.sendText(msg.to,"successfully turn it into: " + string + "")
            elif "Bot1 rename:" in msg.text:
              if msg.from_ in admin:
                string = msg.text.replace("Bot1 rename:","")
                if len(string.decode('utf-8')) <= 200:
                    profile = cl.getProfile()
                    profile.displayName = string
                    cl.updateProfile(profile)
                    cl.sendText(msg.to,"change name: "+string+"\nsucces")
            elif "Bot2 rename:" in msg.text:
              if msg.from_ in admin:
                string = msg.text.replace("Bot4 rename:","")
                if len(string.decode('utf-8')) <= 200:
                    profile = ki.getProfile()
                    profile.displayName = string
                    ki.updateProfile(profile)
                    ki.sendText(msg.to,"change name: "+string+"\nsucces")
            elif "Bot3 rename:" in msg.text:
              if msg.from_ in admin:
                string = msg.text.replace("Bot5 rename:","")
                if len(string.decode('utf-8')) <= 200:
                    profile = kk.getProfile()
                    profile.displayName = string
                    kk.updateProfile(profile)
                    kk.sendText(msg.to,"change name: "+string+"\nsucces")
            elif "Bot4 rename:" in msg.text:
              if msg.from_ in admin:
                string = msg.text.replace("Bot6 rename:","")
                if len(string.decode('utf-8')) <= 200:
                    profile = kc.getProfile()
                    profile.displayName = string
                    kc.updateProfile(profile)
                    kc.sendText(msg.to,"change name: "+string+"\nsucces")   
#==================================================
            elif msg.text in ["Kalender","Time","Waktu"]:
                timeNow = datetime.now()
                timeHours = datetime.strftime(timeNow,"(%H:%M)")
                day = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday","Friday", "Saturday"]
                hari = ["Minggu", "Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu"]
                bulan = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
                inihari = datetime.today()
                hr = inihari.strftime('%A')
                bln = inihari.strftime('%m')
                for i in range(len(day)):
                    if hr == day[i]: hasil = hari[i]
                for k in range(0, len(bulan)):
                    if bln == str(k): blan = bulan[k-1]
                rst = hasil + ", " + inihari.strftime('%d') + " - " + blan + " - " + inihari.strftime('%Y') + "\nJam : [ " + inihari.strftime('%H:%M:%S') + " ]"
                cl.sendText(msg.to, rst)
            elif msg.text in ["Cancel","cancel"]:
                if msg.toType == 2:
                    X = cl.getGroup(msg.to)
                    if X.invitee is not None:
                        gInviMids = [contact.mid for contact in X.invitee]
                        cl.cancelGroupInvitation(msg.to, gInviMids)
                    else:
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"No one is inviting")
                        else:
                            cl.sendText(msg.to,"Sorry, nobody absent")
                else:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Can not be used outside the group")
                    else:
                        cl.sendText(msg.to,"Not for use less than group")
            elif msg.text in ["Cv cancel","Bot cancel"]:
                if msg.toType == 2:
                    G = ki.getGroup(msg.to)
                    if G.invitee is not None:
                        gInviMids = [contact.mid for contact in G.invitee]
                        ki.cancelGroupInvitation(msg.to, gInviMids)
                    else:
                        if wait["lang"] == "JP":
                            ki.sendText(msg.to,"No one is inviting")
                        else:
                            ki.sendText(msg.to,"Sorry, nobody absent")
                else:
                    if wait["lang"] == "JP":
                        ki.sendText(msg.to,"Can not be used outside the group")
                    else:
                        ki.sendText(msg.to,"Not for use less than group")
            #elif "gurl" == msg.text:
                #print cl.getGroup(msg.to)
                ##cl.sendMessage(msg)
            elif msg.text in ["Open","Open url"]:
                if msg.toType == 2:
                    X = cl.getGroup(msg.to)
                    X.preventJoinByTicket = False
                    cl.updateGroup(X)
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Invite by link open")
                    else:
                        cl.sendText(msg.to,"Already open")
                else:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Can not be used outside the group")
                    else:
                        cl.sendText(msg.to,"Not for use less than group")
            elif msg.text in ["C open","Cv1 link on"]:
                if msg.toType == 2:
                    X = cl.getGroup(msg.to)
                    X.preventJoinByTicket = False
                    ki.updateGroup(X)
                    if wait["lang"] == "JP":
                        ki.sendText(msg.to,"Done")
                    else:
                        ki.sendText(msg.to,"already open")
                else:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Can not be used outside the group")
                    else:
                        cl.sendText(msg.to,"Not for use less than group")
            elif msg.text in ["B open","Cv2 link on"]:
                if msg.toType == 2:
                    X = kk.getGroup(msg.to)
                    X.preventJoinByTicket = False
                    kk.updateGroup(X)
                    if wait["lang"] == "JP":
                        kk.sendText(msg.to,"Done")
                    else:
                        kk.sendText(msg.to,"already open")
                else:
                    if wait["lang"] == "JP":
                        kk.sendText(msg.to,"Can not be used outside the group")
                    else:
                        kk.sendText(msg.to,"Not for use less than group")
            elif msg.text in ["K open","Cv3 link on"]:
                if msg.toType == 2:
                    X = kc.getGroup(msg.to)
                    X.preventJoinByTicket = False
                    kc.updateGroup(X)
                    if wait["lang"] == "JP":
                        kc.sendText(msg.to,"Done Chivas")
                    else:
                        kc.sendText(msg.to,"already open")
                else:
                    if wait["lang"] == "JP":
                        kc.sendText(msg.to,"Can not be used outside the group")
                    else:
                        kc.sendText(msg.to,"Not for use less than group")
            elif msg.text in ["Close","close url"]:
                if msg.toType == 2:
                    X = cl.getGroup(msg.to)
                    X.preventJoinByTicket = True
                    cl.updateGroup(X)
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Invite by link Close")
                    else:
                        cl.sendText(msg.to,"Already close")
                else:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Can not be used outside the group")
                    else:
                        cl.sendText(msg.to,"Not for use less than group")
            elif msg.text in ["Cclose","Cv1 link off"]:
                if msg.toType == 2:
                    X = ki.getGroup(msg.to)
                    X.preventJoinByTicket = True
                    ki.updateGroup(X)
                    if wait["lang"] == "JP":
                        ki.sendText(msg.to,"Done")
                    else:
                        ki.sendText(msg.to,"already close")
                else:
                    if wait["lang"] == "JP":
                        ki.sendText(msg.to,"Can not be used outside the group")
                    else:
                        ki.sendText(msg.to,"Not for use less than group")
            elif msg.text in ["Bclose","Cv2 link off"]:
                if msg.toType == 2:
                    X = kk.getGroup(msg.to)
                    X.preventJoinByTicket = True
                    kk.updateGroup(X)
                    if wait["lang"] == "JP":
                        kk.sendText(msg.to,"Done")
                    else:
                        kk.sendText(msg.to,"already close")
                else:
                    if wait["lang"] == "JP":
                        kk.sendText(msg.to,"Can not be used outside the group")
                    else:
                        kk.sendText(msg.to,"Not for use less than group")
            elif msg.text in ["Kclose","Cv3 link off"]:
                if msg.toType == 2:
                    X = kc.getGroup(msg.to)
                    X.preventJoinByTicket = True
                    kc.updateGroup(X)
                    if wait["lang"] == "JP":
                        kc.sendText(msg.to,"Done")
                    else:
                        kc.sendText(msg.to,"already close")
                else:
                    if wait["lang"] == "JP":
                        kc.sendText(msg.to,"Can not be used outside the group")
                    else:
                        kc.sendText(msg.to,"Not for use less than group")
            elif "jointicket " in msg.text.lower():
		rplace=msg.text.lower().replace("jointicket ")
		if rplace == "on":
			wait["atjointicket"]=True
		elif rplace == "off":
			wait["atjointicket"]=False
		cl.sendText(msg.to,"Auto Join Group by Ticket is %s" % str(wait["atjointicket"]))
            elif '/ti/g/' in msg.text.lower():
		link_re = re.compile('(?:line\:\/|line\.me\/R)\/ti\/g\/([a-zA-Z0-9_-]+)?')
		links = link_re.findall(msg.text)
		n_links=[]
		for l in links:
			if l not in n_links:
				n_links.append(l)
		for ticket_id in n_links:
			if wait["atjointicket"] == True:
				group=cl.findGroupByTicket(ticket_id)
				cl.acceptGroupInvitationByTicket(group.mid,ticket_id)
				cl.sendText(msg.to,"Sukses join ke grup %s" % str(group.name))
            elif msg.text == "Ginfo":
                if msg.toType == 2:
                    ginfo = cl.getGroup(msg.to)
                    try:
                        gCreator = ginfo.creator.displayName
                    except:
                        gCreator = "Error"
                    if wait["lang"] == "JP":
                        if ginfo.invitee is None:
                            sinvitee = "0"
                        else:
                            sinvitee = str(len(ginfo.invitee))
                        if ginfo.preventJoinByTicket == True:
                            u = "close"
                        else:
                            u = "open"
                        cl.sendText(msg.to,"[group name]\n" + str(ginfo.name) + "\n[gid]\n" + msg.to + "\n[group creator]\n" + gCreator + "\n[profile status]\nhttp://dl.profile.line.naver.jp/" + ginfo.pictureStatus + "\nmembers:" + str(len(ginfo.members)) + "members\npending:" + sinvitee + "people\nURL:" + u + "it is inside")
                    else:
                        cl.sendText(msg.to,"[group name]\n" + str(ginfo.name) + "\n[gid]\n" + msg.to + "\n[group creator]\n" + gCreator + "\n[profile status]\nhttp://dl.profile.line.naver.jp/" + ginfo.pictureStatus)
                else:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Can not be used outside the group")
                    else:
                        cl.sendText(msg.to,"Not for use less than group")
            elif "Gid" == msg.text:
                cl.sendText(msg.to,msg.to)
            elif "Mid" == msg.text:
                cl.sendText(msg.to,mid)
            elif "Mid all" == msg.text:
                cl.sendText(msg.to,mid)
                ki.sendText(msg.to,Amid)
                kk.sendText(msg.to,Bmid)
                kc.sendText(msg.to,Cmid)
                ks.sendText(msg.to,Dmid)
                km.sendText(msg.to,Emid)
                kt.sendText(msg.to,Fmid)
            elif "Mid 1" == msg.text:
                ki.sendText(msg.to,mid)
            elif "Mid 2" == msg.text:
                kk.sendText(msg.to,Amid)
            elif "Mid 3" == msg.text:
                kc.sendText(msg.to,Bmid)
            elif msg.text in ["Wkwkwk","Wkwk","Wk","wkwkwk","wkwk","wk"]:
                msg.contentType = 7
                msg.text = None
                msg.contentMetadata = {
                                     "STKID": "100",
                                     "STKPKGID": "1",
                                     "STKVER": "100" }
                cl.sendMessage(msg)
                ki.sendMessage(msg)
                kk.sendMessage(msg)
            elif msg.text in ["Hehehe","Hehe","He","hehehe","hehe","he"]:
                msg.contentType = 7
                msg.text = None
                msg.contentMetadata = {
                                     "STKID": "10",
                                     "STKPKGID": "1",
                                     "STKVER": "100" }
                ki.sendMessage(msg)
                kk.sendMessage(msg)
            elif msg.text in ["Galau"]:
                msg.contentType = 7
                msg.text = None
                msg.contentMetadata = {
                                     "STKID": "9",
                                     "STKPKGID": "1",
                                     "STKVER": "100" }
                ki.sendMessage(msg)
                kk.sendMessage(msg)
            elif msg.text in ["You"]:
                msg.contentType = 7
                msg.text = None
                msg.contentMetadata = {
                                     "STKID": "7",
                                     "STKPKGID": "1",
                                     "STKVER": "100" }
                ki.sendMessage(msg)
                kk.sendMessage(msg)
            elif msg.text in ["Hadeuh"]:
                msg.contentType = 7
                msg.text = None
                msg.contentMetadata = {
                                     "STKID": "6",
                                     "STKPKGID": "1",
                                     "STKVER": "100" }
                ki.sendMessage(msg)
                kk.sendMessage(msg)
            elif msg.text in ["Please"]:
                msg.contentType = 7
                msg.text = None
                msg.contentMetadata = {
                                     "STKID": "4",
                                     "STKPKGID": "1",
                                     "STKVER": "100" }
                ki.sendMessage(msg)
                kk.sendMessage(msg)
            elif msg.text in ["Haaa"]:
                msg.contentType = 7
                msg.text = None
                msg.contentMetadata = {
                                     "STKID": "3",
                                     "STKPKGID": "1",
                                     "STKVER": "100" }
                ki.sendMessage(msg)
                kk.sendMessage(msg)
            elif msg.text in ["Lol"]:
                msg.contentType = 7
                msg.text = None
                msg.contentMetadata = {
                                     "STKID": "110",
                                     "STKPKGID": "1",
                                     "STKVER": "100" }
                ki.sendMessage(msg)
                kk.sendMessage(msg)
            elif msg.text in ["Hmmm","Hmm","Hm","hmmm","hmm","hm"]:
                msg.contentType = 7
                msg.text = None
                msg.contentMetadata = {
                                     "STKID": "101",
                                     "STKPKGID": "1",
                                     "STKVER": "100" }
                ki.sendMessage(msg)
            elif msg.text in ["Welcome"]:
                msg.contentType = 7
                msg.text = None
                msg.contentMetadata = {
                                     "STKID": "247",
                                     "STKPKGID": "3",
                                     "STKVER": "100" }
                ki.sendMessage(msg)
                kk.sendMessage(msg)
            elif msg.text in ["TL: "]:
                tl_text = msg.text.replace("TL: ","")
                cl.sendText(msg.to,"line://home/post?userMid="+mid+"&postId="+cl.new_post(tl_text)["result"]["post"]["postInfo"]["postId"])
            elif msg.text in ["Cn:"]:
                string = msg.text.replace("Cn:","")
                if len(string.decode('utf-8')) <= 20:
                    profile = cl.getProfile()
                    profile.displayName = string
                    cl.updateProfile(profile)
                    cl.sendText(msg.to,"name " + string + " done")
            elif msg.text in ["1rename:"]:
                string = msg.text.replace("Crename:","")
                if len(string.decode('utf-8')) <= 20:
                    profile_B = ki.getProfile()
                    profile_B.displayName = string
                    ki.updateProfile(profile_B)
                    ki.sendText(msg.to,"name " + string + " done")
            elif msg.text in ["2rename:"]:
                string = msg.text.replace("Brename:","")
                if len(string.decode('utf-8')) <= 20:
                    profile_B = kk.getProfile()
                    profile_B.displayName = string
                    kk.updateProfile(profile_B)
                    kk.sendText(msg.to,"name " + string + " done")
            elif msg.text in ["Mc:"]:
                mmid = msg.text.replace("Mc:","")
                msg.contentType = 13
                msg.contentMetadata = {"mid":mmid}
                cl.sendMessage(msg)
            elif msg.text in ["Join on","join on"]:
              if msg.from_ in admin:
                if wait["Protectjoin"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"kick Joined Group On")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["Protectjoin"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"kick Joined Group On")
                    else:
                        cl.sendText(msg.to,"done")
            elif msg.text in ["Join off","join off"]:
              if msg.from_ in admin:
                if wait["Protectjoin"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"kick Joined Group Off")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["Protectjoin"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"kick Joined Group Off")
                    else:
                        cl.sendText(msg.to,"done")
            elif msg.text in ["Cancel on","cancel on"]:
              if msg.from_ in admin:
                if wait["Protectcancl"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Cancel All Invited On")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["Protectcancl"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Cancel All Invited On")
                    else:
                        cl.sendText(msg.to,"done")
            elif msg.text in ["Cancel off","cancel off"]:
              if msg.from_ in admin:
                if wait["Protectcancl"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Cancel All Invited Off")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["Protectcancl"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Cancel All Invited Off")
                    else:
                        cl.sendText(msg.to,"done")
            elif msg.text in ["Qr on","qr on"]:
              if msg.from_ in admin:
                if wait["Protectgr"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Protect Group On")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["Protectgr"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Protect Group On")
                    else:
                        cl.sendText(msg.to,"done")
            elif msg.text in ["Qr off","qr off"]:
              if msg.from_ in admin:
                if wait["Protectgr"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Protect Group Off")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["Protectgr"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Protect Group Off")
                    else:
                        cl.sendText(msg.to,"done")
            elif msg.text in ["Protect On","Protection on"]:
              if msg.from_ in admin:
                if wait["protection"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Protection Kicker On")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["protection"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Protection Kicker On")
                    else:
                        cl.sendText(msg.to,"done")
            elif msg.text in ["Protect Off","Protection off"]:
              if msg.from_ in admin:
                if wait["protection"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Protection Kicker Off")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["protection"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Protection Kicker Off")
                    else:
                        cl.sendText(msg.to,"done") 
            elif "Namelock on" in msg.text:
                if msg.to in wait['pname']:
                    cl.sendText(msg.to,"Turned on")
                else:
                    cl.sendText(msg.to,"Already on")
                    wait['pname'][msg.to] = True
                    wait['pro_name'][msg.to] = cl.getGroup(msg.to).name
            elif "Namelock off" in msg.text:
                if msg.to in wait['pname']:
                    cl.sendText(msg.to,"Turn off")
                    del wait['pname'][msg.to]
                else:
                    cl.sendText(msg.to,"Already off")
            elif msg.text in ["Wc on","wc on"]:
              if msg.from_ in admin:
                if wait["welcome"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Welcome On")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["welcome"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Welcome On")
                    else:
                        cl.sendText(msg.to,"done")
            elif msg.text in ["Wc off","wc off"]:
              if msg.from_ in admin:
                if wait["welcome"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Welcome Off")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["welcome"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Welcome Off")
                    else:
                        cl.sendText(msg.to,"done")
            elif msg.text in ["Tag on","tag on"]:
              if msg.from_ in admin:
                if wait["tag"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Auto tag On")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["tag"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Auto tag On")
                    else:
                        cl.sendText(msg.to,"done")
            elif msg.text in ["Tag off","tag off"]:
              if msg.from_ in admin:
                if wait["tag"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Auto tag Off")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["tag"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Auto tag Off")
                    else:
                        cl.sendText(msg.to,"done")
            elif msg.text in ["Contact On","Contact on","contact on"]:
              if msg.from_ in admin:
                if wait["contact"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Cek Mid Send Contact On")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["contact"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Cek Mid Send Contact On")
                    else:
                        cl.sendText(msg.to,"done")
            elif msg.text in ["Contact Off","Contact off","contact off"]:
              if msg.from_ in admin:
                if wait["contact"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Cek Mid Send Contact Off")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["contact"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Cek Mid Send Contact Off")
                    else:
                        cl.sendText(msg.to,"done")
            elif msg.text in ["è‡ªå‹•å�‚åŠ :ã‚ªãƒ³","Jojon on","Auto join:on","è‡ªå‹•å�ƒåŠ ï¼šé–‹"]:
                if wait["autoJoin"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already on")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["autoJoin"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already on")
                    else:
                        cl.sendText(msg.to,"done")
            elif msg.text in ["è‡ªå‹•å�‚åŠ :ã‚ªãƒ•","Jojon off","Auto join:off","è‡ªå‹•å�ƒåŠ ï¼šé—œ"]:
                if wait["autoJoin"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already off")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["autoJoin"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already off")
                    else:
                        cl.sendText(msg.to,"done")
            elif msg.text in ["Gcancel:"]:
                try:
                    strnum = msg.text.replace("Gcancel:","")
                    if strnum == "off":
                        wait["autoCancel"]["on"] = False
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"Invitation refused turned off\nTo turn on please specify the number of people and send")
                        else:
                            cl.sendText(msg.to,"å…³äº†é‚€è¯·æ‹’ç»�ã€‚è¦�æ—¶å¼€è¯·æŒ‡å®šäººæ•°å�‘é€�")
                    else:
                        num =  int(strnum)
                        wait["autoCancel"]["on"] = True
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,strnum + "The group of people and below decided to automatically refuse invitation")
                        else:
                            cl.sendText(msg.to,strnum + "ä½¿äººä»¥ä¸‹çš„å°�ç»„ç”¨è‡ªåŠ¨é‚€è¯·æ‹’ç»�")
                except:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Value is wrong")
                    else:
                        cl.sendText(msg.to,"Bizarre ratings")
            elif msg.text in ["å¼·åˆ¶è‡ªå‹•é€€å‡º:ã‚ªãƒ³","Leave on","Auto leave:on","å¼·åˆ¶è‡ªå‹•é€€å‡ºï¼šé–‹"]:
                if wait["leaveRoom"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already on")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["leaveRoom"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"done")
                    else:
                        cl.sendText(msg.to,"è¦�äº†å¼€ã€‚")
            elif msg.text in ["å¼·åˆ¶è‡ªå‹•é€€å‡º:ã‚ªãƒ•","Leave off","Auto leave:off","å¼·åˆ¶è‡ªå‹•é€€å‡ºï¼šé—œ"]:
                if wait["leaveRoom"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already off")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["leaveRoom"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"done")
                    else:
                        cl.sendText(msg.to,"already")
            elif msg.text in ["å…±æœ‰:ã‚ªãƒ³","Share on","Share on"]:
                if wait["timeline"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already on")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["timeline"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"done")
                    else:
                        cl.sendText(msg.to,"è¦�äº†å¼€ã€‚")
            elif msg.text in ["å…±æœ‰:ã‚ªãƒ•","Share off","Share off"]:
                if wait["timeline"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already off")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["timeline"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"done")
                    else:
                        cl.sendText(msg.to,"è¦�äº†å…³æ–­ã€‚")
            elif msg.text in ["Set"]:
                md = ""
                if wait["protection"] == True: md+="􀔃􀆑lock􏿿  Protection\n"
                else: md+="🃏 Protection Off\n"
                if wait["Protectjoin"] == True: md+="􀔃􀆑lock􏿿  Block Join\n"
                else: md+="🃏 Block Join Off\n"
                if wait["Protectgr"] == True: md+="􀔃􀆑lock􏿿   Block Group\n"
                else: md+="🃏 Block Group Off\n"
                if wait['pname'] == {}: md+="🃏 􀔃􀆑Namelock Off\n"
                else: md+="🔄  Namelock On\n"
                if wait["Protectcancl"] == True: md+="􀔃􀆑lock􏿿 Cancel All Invited\n"
                else: md+="🃏 Cancel All Invited Off\n"
                if wait["contact"] == True: md+="🆗 Contact    : on\n"
                else: md+="🃏 Contact    : off\n"
                if wait["autoJoin"] == True: md+="🆗 Auto join : on\n"
                else: md +="🃏 Auto join : off\n"
                if wait["autoCancel"]["on"] == True:md+="🆗 Group cancel :" + str(wait["autoCancel"]["members"]) + "\n"
                else: md+= "🃏 Group cancel : off\n"
                if wait["leaveRoom"] == True: md+="🆗 Auto leave    : on\n"
                else: md+="🃏 Auto leave : off\n"
                if wait["welcome"] == True: md+="🆗 Welcome    : on\n"
                else: md+="🃏 Welcome : off\n"
                if wait["timeline"] == True: md+="🆗 Share   : on\n"
                else:md+="🃏 Share   : off\n"
                if wait["autoAdd"] == True: md+="🆗 Auto add : on\n"
                else:md+="🃏 Auto add : off\n"
                if wait["tag"] == True: md+="🆗 Tag : on\n"
                else:md+="🃏 Tag : off\n"
                if wait["likeOn"] == True: md+="🆗 Auto like : on\n"
                else:md+="🃏 Auto like : off\n"
                if wait["commentOn"] == True: md+="🆗 Comment : on\n"
                else:md+="🃏 Comment : off\n"
                cl.sendText(msg.to,md)
            elif "album merit " in msg.text:
                gid = msg.text.replace("album merit ","")
                album = cl.getAlbum(gid)
                if album["result"]["items"] == []:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"There is no album")
                    else:
                        cl.sendText(msg.to,"ç›¸å†Œæ²¡åœ¨ã€‚")
                else:
                    if wait["lang"] == "JP":
                        mg = "The following is the target album"
                    else:
                        mg = "ä»¥ä¸‹æ˜¯å¯¹è±¡çš„ç›¸å†Œ"
                    for y in album["result"]["items"]:
                        if "photoCount" in y:
                            mg += str(y["title"]) + ":" + str(y["photoCount"]) + "sheet\n"
                        else:
                            mg += str(y["title"]) + ":0sheet\n"
                    cl.sendText(msg.to,mg)
            elif "album " in msg.text:
                gid = msg.text.replace("album ","")
                album = cl.getAlbum(gid)
                if album["result"]["items"] == []:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"There is no album")
                    else:
                        cl.sendText(msg.to,"ç›¸å†Œæ²¡åœ¨ã€‚")
                else:
                    if wait["lang"] == "JP":
                        mg = "The following is the target album"
                    else:
                        mg = "ä»¥ä¸‹æ˜¯å¯¹è±¡çš„ç›¸å†Œ"
                    for y in album["result"]["items"]:
                        if "photoCount" in y:
                            mg += str(y["title"]) + ":" + str(y["photoCount"]) + "sheet\n"
                        else:
                            mg += str(y["title"]) + ":0sheet\n"
            elif "album remove " in msg.text:
                gid = msg.text.replace("album remove ","")
                albums = cl.getAlbum(gid)["result"]["items"]
                i = 0
                if albums != []:
                    for album in albums:
                        cl.deleteAlbum(gid,album["id"])
                        i += 1
                if wait["lang"] == "JP":
                    cl.sendText(msg.to,str(i) + "Deleted albums")
                else:
                    cl.sendText(msg.to,str(i) + "åˆ é™¤äº†äº‹çš„ç›¸å†Œã€‚")
            elif msg.text in ["Group id"]:
                gid = cl.getGroupIdsJoined()
                h = ""
                for i in gid:
                    h += "[%s]:\n%s\n" % (cl.getGroup(i).name,i)
                cl.sendText(msg.to,h)
            elif msg.text in ["Cancelall"]:
                gid = cl.getGroupIdsInvited()
                for i in gid:
                    cl.rejectGroupInvitation(i)
                if wait["lang"] == "JP":
                    cl.sendText(msg.to,"All invitations have been refused")
                else:
                    cl.sendText(msg.to,"æ‹’ç»�äº†å…¨éƒ¨çš„é‚€è¯·ã€‚")
            elif "album removeat’" in msg.text:
                gid = msg.text.replace("album removeat’","")
                albums = cl.getAlbum(gid)["result"]["items"]
                i = 0
                if albums != []:
                    for album in albums:
                        cl.deleteAlbum(gid,album["id"])
                        i += 1
                if wait["lang"] == "JP":
                    cl.sendText(msg.to,str(i) + "Albums deleted")
                else:
                    cl.sendText(msg.to,str(i) + "åˆ é™¤äº†äº‹çš„ç›¸å†Œã€‚")
            elif msg.text in ["è‡ªå‹•è¿½åŠ :ã‚ªãƒ³","Add on","Auto add:on","è‡ªå‹•è¿½åŠ ï¼šé–‹"]:
                if wait["autoAdd"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already on")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["autoAdd"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"done")
                    else:
                        cl.sendText(msg.to,"è¦�äº†å¼€ã€‚")
            elif msg.text in ["è‡ªå‹•è¿½åŠ :ã‚ªãƒ•","Add off","Auto add:off","è‡ªå‹•è¿½åŠ ï¼šé—œ"]:
                if wait["autoAdd"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already off")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["autoAdd"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"done")
                    else:
                        cl.sendText(msg.to,"è¦�äº†å…³æ–­ã€‚")
            elif "Message change: " in msg.text:
                wait["message"] = msg.text.replace("Message change: ","")
                cl.sendText(msg.to,"message changed")
            elif "Message add: " in msg.text:
                wait["message"] = msg.text.replace("Message add: ","")
                if wait["lang"] == "JP":
                    cl.sendText(msg.to,"message changed")
                else:
                    cl.sendText(msg.to,"doneã€‚")
            elif msg.text in ["Message","è‡ªå‹•è¿½åŠ å•�å€™èªžç¢ºèª�"]:
                if wait["lang"] == "JP":
                    cl.sendText(msg.to,"message change to\n\n" + wait["message"])
                else:
                    cl.sendText(msg.to,"The automatic appending information is set as followsã€‚\n\n" + wait["message"])
            elif "Comment:" in msg.text:
                c = msg.text.replace("Comment:","")
                if c in [""," ","\n",None]:
                    cl.sendText(msg.to,"message changed")
                else:
                    wait["comment"] = c
                    cl.sendText(msg.to,"changed\n\n" + c)
            elif "Add comment:" in msg.text:
                c = msg.text.replace("Add comment:","")
                if c in [""," ","\n",None]:
                    cl.sendText(msg.to,"String that can not be changed")
                else:
                    wait["comment"] = c
                    cl.sendText(msg.to,"changed\n\n" + c)
            elif msg.text in ["ã‚³ãƒ¡ãƒ³ãƒˆ:ã‚ªãƒ³","Comment on","Comment:on","è‡ªå‹•é¦–é �ç•™è¨€ï¼šé–‹"]:
                if wait["commentOn"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"done")
                    else:
                        cl.sendText(msg.to,"already on")
                else:
                    wait["commentOn"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"done")
                    else:
                        cl.sendText(msg.to,"è¦�äº†å¼€ã€‚")
            elif msg.text in ["ã‚³ãƒ¡ãƒ³ãƒˆ:ã‚ªãƒ•","Comment on","Comment off","è‡ªå‹•é¦–é �ç•™è¨€ï¼šé—œ"]:
                if wait["commentOn"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"done")
                    else:
                        cl.sendText(msg.to,"already off")
                else:
                    wait["commentOn"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"done")
                    else:
                        cl.sendText(msg.to,"è¦�äº†å…³æ–­ã€‚")
            elif msg.text in ["Comment","ç•™è¨€ç¢ºèª�"]:
                cl.sendText(msg.to,"message changed to\n\n" + str(wait["comment"]))
            elif msg.text in ["Gurl"]:
                if msg.toType == 2:
                    x = cl.getGroup(msg.to)
                    if x.preventJoinByTicket == True:
                        x.preventJoinByTicket = False
                        cl.updateGroup(x)
                    gurl = cl.reissueGroupTicket(msg.to)
                    cl.sendText(msg.to,"line://ti/g/" + gurl)
                else:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Can't be used outside the group")
                    else:
                        cl.sendText(msg.to,"Not for use less than group")
            elif msg.text in ["Cv1 gurl"]:
                if msg.toType == 2:
                    x = cl.getGroup(msg.to)
                    if x.preventJoinByTicket == True:
                        x.preventJoinByTicket = False
                        ki.updateGroup(x)
                    gurl = ki.reissueGroupTicket(msg.to)
                    ki.sendText(msg.to,"line://ti/g/" + gurl)
                else:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Can't be used outside the group")
                    else:
                        cl.sendText(msg.to,"Not for use less than group")
            elif msg.text in ["Cv2 gurl"]:
                if msg.toType == 2:
                    x = cl.getGroup(msg.to)
                    if x.preventJoinByTicket == True:
                        x.preventJoinByTicket = False
                        kk.updateGroup(x)
                    gurl = kk.reissueGroupTicket(msg.to)
                    kk.sendText(msg.to,"line://ti/g/" + gurl)
                else:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Can't be used outside the group")
                    else:
                        cl.sendText(msg.to,"Not for use less than group")
            elif msg.text in ["Cv3 gurl"]:
                if msg.toType == 2:
                    x = cl.getGroup(msg.to)
                    if x.preventJoinByTicket == True:
                        x.preventJoinByTicket = False
                        kc.updateGroup(x)
                    gurl = kc.reissueGroupTicket(msg.to)
                    kc.sendText(msg.to,"line://ti/g/" + gurl)
                else:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Can't be used outside the group")
                    else:
                        cl.sendText(msg.to,"Not for use less than group")
            elif msg.text in ["Comment bl "]:
                wait["wblack"] = True
                cl.sendText(msg.to,"add to comment bl")
            elif msg.text in ["Comment wl "]:
                wait["dblack"] = True
                cl.sendText(msg.to,"wl to comment bl")
            elif msg.text in ["Comment bl confirm"]:
                if wait["commentBlack"] == {}:
                    cl.sendText(msg.to,"confirmed")
                else:
                    cl.sendText(msg.to,"Blacklist")
                    mc = ""
                    for mi_d in wait["commentBlack"]:
                        mc += "" +cl.getContact(mi_d).displayName + "\n"
                    cl.sendText(msg.to,mc)

            elif msg.text in ["Clear ban"]:
                 if msg.from_ in admin:
                   wait["blacklist"] = {}
                   cl.sendText(msg.to,"Clear All Ban Done")                    
        #-------------Fungsi Jam on/off Start-------------------#            
            elif msg.text in ["Jam on"]:
                if wait["clock"] == True:
                    kc.sendText(msg.to,"Bot 4 jam on")
                else:
                    wait["clock"] = True
                    now2 = datetime.now()
                    nowT = datetime.strftime(now2,"(%H:%M)")
                    profile = kc.getProfile()
                    profile.displayName = wait["cName4"] + nowT
                    kc.updateProfile(profile)
                    kc.sendText(msg.to,"Jam Selalu On")
            elif msg.text in ["Jam off"]:
                if wait["clock"] == False:
                    kc.sendText(msg.to,"Bot 4 jam off")
                else:
                    wait["clock"] = False
                    kc.sendText(msg.to,"Jam Sedang Off")
         #-------------Fungsi Jam on/off Finish-------------------#           

         #-------------Fungsi Change Clock Start------------------#
            elif msg.text in ["Change clock"]:
                n = msg.text.replace("Change clock","")
                if len(n.decode("utf-8")) > 13:
                    kc.sendText(msg.to,"changed")
                else:
                    wait["cName"] = n
                    kc.sendText(msg.to,"changed to\n\n" + n)
         #-------------Fungsi Change Clock Finish-----------------#      
     
#-------------------------------------------------------
            elif "Gift @" in msg.text:
                _name = msg.text.replace("Gift @","")
                _nametarget = _name.rstrip(' ')
                gs = cl.getGroup(msg.to)
                for g in gs.members:
                    if _nametarget == g.displayName:
                    	msg.contentType = 9
                        msg.contentMetadata={'PRDID': '89131c1a-e549-4bd5-9e60-e24de0d2e252',
                                    'PRDTYPE': 'THEME',
                                    'MSGTPL': '10'}
                        msg.text = None
                        cl.sendMessage(msg.to,g)
#===========================================        
         #-------------Fungsi Jam Update Start---------------------#            
            elif msg.text in ["Jam Update"]:
                if wait["clock"] == True:
                    now2 = datetime.now()
                    nowT = datetime.strftime(now2,"(%H:%M)")
                    profile = kc.getProfile()
                    profile.displayName = wait["cName4"] + nowT
                    kc.updateProfile(profile)
                    kc.sendText(msg.to,"Sukses update")
                else:
                    kc.sendText(msg.to,"Aktifkan jam terlebih dulu")
         #-------------Fungsi Jam Update Finish-------------------#

            elif msg.text == "Setp":
                    cl.sendText(msg.to, "Setpoint Telah Dipasang")
                    try:
                        del wait2['readPoint'][msg.to]
                        del wait2['readMember'][msg.to]
                    except:
                        pass
                    now2 = datetime.now()
                    wait2['readPoint'][msg.to] = msg.id
                    wait2['readMember'][msg.to] = ""
                    wait2['setTime'][msg.to] = datetime.today().strftime('%Y-%m-%d %H:%M:%S')
                    wait2['ROM'][msg.to] = {}
                    print wait2

            elif msg.text == "Cek":
                    if msg.to in wait2['readPoint']:
                        if wait2["ROM"][msg.to].items() == []:
                            chiya = ""
                        else:
                            chiya = ""
                            for rom in wait2["ROM"][msg.to].items():
                                print rom
                                chiya += rom[1] + "\n"

                        cl.sendText(msg.to, "==== Tercyduk ==== %s\n\n==== Bukti Nyata ====\n%s\n\nSetpoint Pada :\n[%s]"  % (wait2['readMember'][msg.to],chiya,setTime[msg.to]))
                    else:
                        cl.sendText(msg.to, "Setpoint Dulu dudul 􀜁􀅔🙊� 「Setp」")
                    pass             
              #-----------------------------------------------------------------------

#-----------------------------------------------
         #----------------Fungsi Join Group Start-----------------------#
            elif msg.text in ["👍","Woy","All join"]:
              if msg.from_ in admin:
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        G.preventJoinByTicket = False
                        cl.updateGroup(G)
                        invsend = 0
                        Ticket = cl.reissueGroupTicket(msg.to)
                        ki.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.2)
                        kk.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.2)
                        kc.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.2)
                        ks.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.2)
                        km.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.2)
                        kt.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.2)
                        G = cl.getGroup(msg.to)
                        G.preventJoinByTicket = True
                        cl.updateGroup(G)
                        print "Bot Complete"
                        G.preventJoinByTicket(G)
                        cl.updateGroup(G)

            elif msg.text in ["1 join","Blek"]:
              if msg.from_ in admin:
                  x = cl.getGroup(msg.to)
                  x.preventJoinByTicket = False
                  cl.updateGroup(x)
                  invsend = 0
                  Ti = cl.reissueGroupTicket(msg.to)
                  ki.acceptGroupInvitationByTicket(msg.to,Ti)
                  G = cl.getGroup(msg.to)
                  G.preventJoinByTicket = True
                  cl.updateGroup(G)
                  Ticket = cl.reissueGroupTicket(msg.to)

            elif msg.text in ["2 join","Ndil"]:
              if msg.from_ in admin:
                  x = cl.getGroup(msg.to)
                  x.preventJoinByTicket = False
                  cl.updateGroup(x)
                  invsend = 0
                  Ti = cl.reissueGroupTicket(msg.to)
                  kk.acceptGroupInvitationByTicket(msg.to,Ti)
                  G = cl.getGroup(msg.to)
                  G.preventJoinByTicket = True
                  cl.updateGroup(G)
                  Ticket = cl.reissueGroupTicket(msg.to)

            elif msg.text in ["3 join","Dal"]:
              if msg.from_ in admin:
                  x = cl.getGroup(msg.to)
                  x.preventJoinByTicket = False
                  cl.updateGroup(x)
                  invsend = 0
                  Ti = cl.reissueGroupTicket(msg.to)
                  kc.acceptGroupInvitationByTicket(msg.to,Ti)
                  G = cl.getGroup(msg.to)
                  G.preventJoinByTicket = True
                  cl.updateGroup(G)
                  Ticket = cl.reissueGroupTicket(msg.to)

            elif msg.text in ["4 join","Wor"]:
              if msg.from_ in admin:
                  x = cl.getGroup(msg.to)
                  x.preventJoinByTicket = False
                  cl.updateGroup(x)
                  invsend = 0
                  Ti = cl.reissueGroupTicket(msg.to)
                  ks.acceptGroupInvitationByTicket(msg.to,Ti)
                  G = cl.getGroup(msg.to)
                  G.preventJoinByTicket = True
                  cl.updateGroup(G)
                  Ticket = cl.reissueGroupTicket(msg.to)
                  
    #----------------------Fungsi Join Group Finish---------------#

    #-------------Fungsi Leave Group Start---------------#
            elif msg.text in ["Bye all","👎","Hus"]:
              if msg.from_ in admin:
                if msg.toType == 2:
                    ginfo = cl.getGroup(msg.to)
                    try:
                        ki.leaveGroup(msg.to)
                        kk.leaveGroup(msg.to)
                        kc.leaveGroup(msg.to)
                        ks.leaveGroup(msg.to)
                        km.leaveGroup(msg.to)
                        kt.leaveGroup(msg.to)
                    except:
                        pass
            elif msg.text in ["Bye 1","Ciblek hus"]:
              if msg.from_ in admin:
                if msg.toType == 2:
                    ginfo = cl.getGroup(msg.to)
                    try:
                        ki.leaveGroup(msg.to)
                    except:
                        pass
            elif msg.text in ["Bye 2","Brindil hus"]:
              if msg.from_ in admin:
                if msg.toType == 2:
                    ginfo = cl.getGroup(msg.to)
                    try:
                        kk.leaveGroup(msg.to)
                    except:
                        pass
            elif msg.text in ["Bye 3","Kadal hus"]:
              if msg.from_ in admin:
                if msg.toType == 2:
                    ginfo = cl.getGroup(msg.to)
                    try:
                        kc.leaveGroup(msg.to)
                    except:
                        pass
            elif msg.text in ["Bye 4","Bawor hus"]:
              if msg.from_ in admin:
                if msg.toType == 2:
                    ginfo = cl.getGroup(msg.to)
                    try:
                        ks.leaveGroup(msg.to)
                    except:
                        pass
            elif msg.text in ["@bye"]:
                if msg.toType == 2:
                    ginfo = cl.getGroup(msg.to)
                    try:
                        cl.leaveGroup(msg.to)
                    except:
                        pass
    #-------------Fungsi Leave Group Finish---------------#
#------------------------------ BROADCAST PC --------------------------------
            elif "Bc " in msg.text:
                if msg.from_ in admin:
                    broadcasttxt = msg.text.replace("/bc ", "")
                    orang = cl.getAllContactIds()
                    for manusia in orang:
                        cl.sendText(manusia,(broadcasttxt))
                        print "[Command] BC Contact"
#----------------------------------------------------------------------------
#----------------------------- BROADCAST Group ------------------------------
            elif "Bcgc " in msg.text:
                if msg.from_ in admin:
                    broadcasttxt = msg.text.replace("/bcgc ", "")
                    orang = cl.getGroupIdsJoined()
                    for manusia in orang:
                        cl.sendText(manusia,(broadcasttxt))
                        print "[Command] BC Grup"
#----------------------------------------------------------------------------
#-------------------------------- WELCOME -----------------------------------
            elif msg.text in ["Kam","kam"]:
                ginfo = cl.getGroup(msg.to)
                cl.sendText(msg.to,"Selamat Datang Di Grup " + str(ginfo.name))
                cl.sendText(msg.to,"Owner Grup " + str(ginfo.name) + " :\n" + ginfo.creator.displayName )
#----------------------------------------------------------------------------
#----------------------------- TAG ALL MEMBER -------------------------------
            elif msg.text in ["Mentional","😘"]:
			      group = cl.getGroup(msg.to)
			      nama = [contact.mid for contact in group.members]
			      nm1, nm2, nm3, nm4, jml = [], [], [], [], len(nama)
			      if jml <= 100:
			         mention(msg.to, nama)
			      if jml > 100 and jml < 200:
			         for i in range (0, 99):
			                nm1 += [nama[i]]
			         mention(msg.to, nm1)
			         for j in range (100, len(nama)-1):
			                nm2 += [nama[j]]
			         mention(msg.to, nm2)
			      if jml > 200 and jml < 300:
			         for i in range (0, 99):
			                nm1 += [nama[i]]
			         mention(msg.to, nm1)
			         for j in range (100, 199):
			                nm2 += [nama[j]]
			         mention(msg.to, nm2)
			         for k in range (200, len(nama)-1):
			                nm3 += [nama[k]]
			         mention(msg.to, nm3)       
			      if jml > 300 and jml < 400:
			         for i in range (0, 99):
			                nm1 += [nama[i]]
			         mention(msg.to, nm1)
			         for j in range (100, 199):
			                nm2 += [nama[j]]
			         mention(msg.to, nm2)
			         for k in range (200, 299):
			                nm3 += [nama[k]]
			         mention(msg.to, nm3)           
			         for l in range (300, len(nama)-1):
			             nm4 += [nama[l]]
			         mention(msg.to, nm4)
			      msg = Message()
			      msg.text = "Done:"+str(jml)
			      msg.to = msg.to
			      cl.sendMessage(msg)
#----------------------------------------------------------------------------
    #-------------Fungsi Tag All Start---------------#
            elif msg.text in ["Next","Kuchiyose no jutsu"]:
                  group = cl.getGroup(msg.to)
                  nama = [contact.mid for contact in group.members]

                  cb = ""
                  cb2 = ""
                  strt = int(0)
                  akh = int(0)
                  for md in nama:
                      akh = akh + int(6)

                      cb += """{"S":"""+json.dumps(str(strt))+""","E":"""+json.dumps(str(akh))+""","M":"""+json.dumps(md)+"},"""

                      strt = strt + int(7)
                      akh = akh + 1
                      cb2 += "@nrik \n"

                  cb = (cb[:int(len(cb)-1)])
                  msg.contentType = 0
                  msg.text = cb2
                  msg.contentMetadata ={'MENTION':'{"MENTIONEES":['+cb+']}','EMTVER':'4'}

                  try:
                      cl.sendMessage(msg)
                  except Exception as error:
                      print error
    #-------------Fungsi Tag All Finish-------------#                                                                                                   

#-------------------Fungsi Spam Start----------------------#
            elif "Spam " in msg.text:
            	if msg.from_ in admin:
                   txt = msg.text.split(" ")
                   jmlh = int(txt[2])
                   teks = msg.text.replace("Spam "+str(txt[1])+" "+str(jmlh)+ " ","")
                   tulisan = jmlh * (teks+"\n")
                  #Keke cantik <3
                   if txt[1] == "on":
                        if jmlh <= 1000:
                             for x in range(jmlh):
                                   cl.sendText(msg.to, teks)
                        else:
                               cl.sendText(msg.to, "Out of range! ")
                   elif txt[1] == "off":
                         if jmlh <= 2000:
                               cl.sendText(msg.to, tulisan)
                         else:
                               cl.sendText(msg.to, "Out of range! ")
     #----------------------Fungsi Spam Finish-------------------------------#
#------------------------------- Kerang Ajaib -------------------------------
            elif "/apakah " in msg.text.lower():
                apk = msg.text.replace("/apakah ","")
                rnd = ['Ya','Tidak']
                p = random.choice(rnd)
                ki.sendText(msg.to,p)
                print "[Command] Kerang Ajaib"
#----------------------------------------------------------------------------
            elif "Group pict" in msg.text:
              if msg.from_ in admin:
					group = cl.getGroup(msg.to)
					path = "http://dl.profile.line-cdn.net/" + group.pictureStatus
                                        cl.sendImageWithURL(msg.to,path)
         #----------------Fungsi Banned Kick Target Start-----------------------#
            elif msg.text in ["Kill "]:
              if msg.from_ in admin:
                if msg.toType == 2:
                    group = ki.getGroup(msg.to)
                    gMembMids = [contact.mid for contact in group.members]
                    matched_list = []
                    for tag in wait["blacklist"]:
                        matched_list+=filter(lambda str: str == tag, gMembMids)
                    if matched_list == []:
                        kk.sendText(msg.to,"Selamat tinggal")
                        kc.sendText(msg.to,"Jangan masuk lagi􀨁􀆷devil smile􏿿")
                        return
                    for jj in matched_list:
                        try:
                            klist=[ki,kk,kc]
                            kicker=random.choice(klist)
                            kicker.kickoutFromGroup(msg.to,[jj])
                            print (msg.to,[jj])
                        except:
                            pass
         #----------------Fungsi Banned Kick Target Finish----------------------#                
            
            elif "🆘" in msg.text:
              if msg.from_ in Bots:
                if msg.toType == 2:
                    print "ok"
                    _name = msg.text.replace("🆘","")
                    gs = ki.getGroup(msg.to)
                    gs = cl.getGroup(msg.to)
                    cl.sendText(msg.to,"permisi om tante 😈")
                    msg.contentType = 13
                    msg.contentMetadata = {'mid': mid}
                    cl.sendMessage(msg)
                    targets = []
                    for g in gs.members:
                        if _name in g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        cl.sendText(msg.to,"Not found")
                    else:
                        for target in targets:
                          if target not in Bots:
                            try:
                                klist=[ks,kc,kk,ki,cl]
                                kicker=random.choice(klist)
                                kicker.kickoutFromGroup(msg.to,[target])
                                print (msg.to,[g.mid])
                            except:
                                    pass

        #----------------Fungsi Kick User Target Start----------------------#
            elif "Nk " in msg.text:
                  if msg.from_ in admin:
                       nk0 = msg.text.replace("Nk ","")
                       nk1 = nk0.lstrip()
                       nk2 = nk1.replace("@","")
                       nk3 = nk2.rstrip()
                       _name = nk3
                       gs = cl.getGroup(msg.to)
                       gs = ki.getGroup(msg.to)
                       gs = kk.getGroup(msg.to)
                       gs = kc.getGroup(msg.to)
                       gs = ks.getGroup(msg.to)
                       gs = km.getGroup(msg.to)
                       gs = kt.getGroup(msg.to)
                       targets = []
                       for s in gs.members:
                           if _name in s.displayName:
                              targets.append(s.mid)
                       if targets == []:
                           sendMessage(msg.to,"user does not exist")
                           pass
                       else:
                           for target in targets:
                                try:
                                    klist=[cl,ki,kk,kc,ks,km,kt]
                                    kicker=random.choice(klist)
                                    kicker.kickoutFromGroup(msg.to,[target])
                                    print (msg.to,[g.mid])
                                except:
                                    pass
        #----------------Fungsi Kick User Target Finish----------------------#         
   #-----------------------------------------------------------
	    elif "Ulti " in msg.text:
                  if msg.from_ in admin:
                       ulti0 = msg.text.replace("Ulti ","")
                       ulti1 = ulti0.lstrip()
                       ulti2 = ulti1.replace("@","")
                       ulti3 = ulti2.rstrip()
                       _name = ulti3
                       gs = cl.getGroup(msg.to)
                       ginfo = cl.getGroup(msg.to)
                       gs.preventJoinByTicket = False
                       cl.updateGroup(gs)
                       invsend = 0
                       Ticket = cl.reissueGroupTicket(msg.to)
                       ki.acceptGroupInvitationByTicket(msg.to,Ticket)
                       time.sleep(0.2)
                       targets = []
                       for s in gs.members:
                           if _name in s.displayName:
                              targets.append(s.mid)
                       if targets == []:
                           sendMessage(msg.to,"user does not exist")
                           pass
                       else:
                           for target in targets:
                                try:
                                    ki.kickoutFromGroup(msg.to,[target])
                                    print (msg.to,[g.mid])
                                except:
                                    ki.sendText(msg.to,"Selamat Jalan👻")
                                    ki.sendText(msg.to,"Done, See u :*")
                                    ki.leaveGroup(msg.to)
                                    gs = cl.getGroup(msg.to)
                        	    gs.preventJoinByTicket = True
                        	    cl.updateGroup(gs)
                                    gs.preventJoinByTicket(gs)
                        	    cl.updateGroup(gs)
   #-----------------------------------------------------------

   #-----------------------------------------------------------
            elif "Tkick" in msg.text:
                if msg.contentMetadata is not None:
                    targets = []
                    key = eval(msg.contentMetadata["MENTION"])
                    key["MENTIONEES"][0]["M"]
                    for x in key["MENTIONEES"]:
                        targets.append(x["M"])
                    for target in targets:
                        try:
                            cl.kickoutFromGroup(msg.to,[target])
                        except:
                           ki.kickoutFromGroup(msg.to,[target])
                    else:
                        pass
#-----------------------------------------------------------    
            elif "You" in msg.text:
                key = eval(msg.contentMetadata["MENTION"])
                key1 = key["MENTIONEES"][0]["M"]                
                mmid = cl.getContact(key1)
                msg.contentType = 13
                msg.contentMetadata = {"mid": key1}
                cl.sendMessage(msg)        								
#----------------------------------------------------------      
            elif "Blacklist @ " in msg.text:
                _name = msg.text.replace("Blacklist @ ","")
                _kicktarget = _name.rstrip(' ')
                gs = ki2.getGroup(msg.to)
                targets = []
                for g in gs.members:
                    if _kicktarget == g.displayName:
                        targets.append(g.mid)
                        if targets == []:
                            cl.sendText(msg.to,"Not found")
                        else:
                            for target in targets:
                                try:
                                    wait["blacklist"][target] = True
                                    f=codecs.open('st2__b.json','w','utf-8')
                                    json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                                    k3.sendText(msg.to,"Succes Cv")
                                except:
                                    ki.sendText(msg.to,"error")
            
            #----------------Fungsi Banned User Target Start-----------------------#
            elif "Ban @" in msg.text:
              if msg.from_ in admin:
                if msg.toType == 2:
                    print "[Banned] Sukses"
                    _name = msg.text.replace("Banned @","")
                    _nametarget = _name.rstrip('  ')
                    gs = cl.getGroup(msg.to)
                    gs = ki.getGroup(msg.to)
                    gs = kk.getGroup(msg.to)
                    gs = kc.getGroup(msg.to)
                    targets = []
                    for g in gs.members:
                        if _nametarget == g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        cl.sendText(msg.to,"Dilarang Banned Bot")
                        ki.sendText(msg.to,"Dilarang Banned Bot")
                        kk.sendText(msg.to,"Dilarang Banned Bot")
                        kc.sendText(msg.to,"Dilarang Banned Bot")
                    else:
                        for target in targets:
                            try:
                                wait["blacklist"][target] = True
                                f=codecs.open('st2__b.json','w','utf-8')
                                json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                                cl.sendText(msg.to,"Akun telah sukses di banned")
                            except:
                                ki.sendText(msg.to,"Error")
            #----------------Fungsi Banned User Target Finish-----------------------# 
            elif msg.text in ["List"]: #Melihat List Group yang di Join
              if msg.from_ in admin:
                 gids = cl.getGroupIdsJoined()
                 h = ""
                 for i in gids:
                  #####gn = cl.getGroup(i).name
                  h += "[🔥]%s Member\n" % (cl.getGroup(i).name   +"👉"+str(len(cl.getGroup(i).members)))
                 cl.sendText(msg.to,"=======[List Group]======\n"+ h +"Total Group :"+str(len(gids)))

            elif msg.text in ["List2"]: #Melihat List Group + ID Groupnya (Gunanya Untuk Perintah InviteMeTo:)
              if msg.from_ in admin:
                gid = cl.getGroupIdsJoined()
                h = ""
                for i in gid:
                  h += "[%s]:%s\n" % (cl.getGroup(i).name,i)
                  cl.sendText(msg.to,h)
                           
            #----------------Fungsi Unbanned User Target Start-----------------------#
            elif "Unban @" in msg.text:
              if msg.from_ in admin:
                if msg.toType == 2:
                    print "[Unban] Sukses"
                    _name = msg.text.replace("Unban @","")
                    _nametarget = _name.rstrip('  ')
                    gs = cl.getGroup(msg.to)
                    gs = ki.getGroup(msg.to)
                    gs = kk.getGroup(msg.to)
                    gs = kc.getGroup(msg.to)
                    targets = []
                    for g in gs.members:
                        if _nametarget == g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        cl.sendText(msg.to,"Tidak Ditemukan.....")
                        ki.sendText(msg.to,"Tidak Ditemukan.....")
                        kk.sendText(msg.to,"Tidak Ditemukan.....")
                        kc.sendText(msg.to,"Tidak Ditemukan.....")
                    else:
                        for target in targets:
                            try:
                                del wait["blacklist"][target]
                                f=codecs.open('st2__b.json','w','utf-8')
                                json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                                cl.sendText(msg.to,"Akun Bersih Kembali")
                            except:
                                ki.sendText(msg.to,"Error")
           #----------------Fungsi Unbanned User Target Finish-----------------------#
				
        #-------------Fungsi Spam Start---------------------#
            elif msg.text in ["Up","up","Up Chat","Up chat","up chat","Upchat","upchat"]:
                cl.sendText(msg.to,"Kini Ku Harus Bernafas Tanpamu")
                cl.sendText(msg.to,"Yang meninggikan diriku yang slalu")
                cl.sendText(msg.to,"Lemah Tanpa Dirimu")
                cl.sendText(msg.to,"Yang kelembutan Hatinya harus tersakiti")
                cl.sendText(msg.to,"Oleh kekalahanku Melawan Egoku")
                cl.sendText(msg.to,"Kuakui Aku yang memulai segalanya")
                cl.sendText(msg.to,"Tapi lihat kini akulah yang paling terluka")
                cl.sendText(msg.to,"Bila Harus kisah cinta ini ku akhiri")
                cl.sendText(msg.to,"Kan Kuakhiri sbgai satu jalan")
                cl.sendText(msg.to,"Yang Terbaik Untuk Kitaa Berdua")
                cl.sendText(msg.to,"Kini Ku harus berjalan Tanpamu")
                cl.sendText(msg.to,"Yang merelakan hidupnya yang slalu")
                cl.sendText(msg.to,"Indah Tanpa Diriku")
                cl.sendText(msg.to,"Ampuni Aku yang tlah Hancurkan sgalanya")
                cl.sendText(msg.to,"Tapi Percayalah Ku Tak ingin")
                cl.sendText(msg.to,"Engkau Terlukaaaaaaa")
                cl.sendText(msg.to,"Bila Harus kisah cinta ini ku akhiri")
                cl.sendText(msg.to,"Kan Kuakhiri sbgai satu jalan")
                cl.sendText(msg.to,"Yang Terbaik Untuk Kitaa Berdua")
                cl.sendText(msg.to,"Dan Kau Harus Temukan Cinta ")
                cl.sendText(msg.to,"Yang Pasti")
                cl.sendText(msg.to,"Yang Tak seperti ")
                cl.sendText(msg.to,"Aku Yang Jauh Dari ")
                cl.sendText(msg.to,"Harapanmuuu oooooo")
                cl.sendText(msg.to,"AKu Yang Jauh Dari")
                cl.sendText(msg.to,"Harapanmuuu")
                cl.sendText(msg.to,"ooooooooo")
                cl.sendText(msg.to,"Bernafas Tanpamuuu")
                cl.sendText(msg.to,"👏👏👏👏👏👏👏")
                cl.sendText(msg.to,"I will Always love You")

            elif msg.text == "Up2":
                    cl.sendText(msg.to,"3")
                    cl.sendText(msg.to,"2")
                    cl.sendText(msg.to,"1")
                    cl.sendText(msg.to,"👻🔥🔥🔥💥🔥🔥🔥👻")
                    cl.sendText(msg.to,"Ku mengejar bus yang mulai berjalan")
                    cl.sendText(msg.to,"Ku ingin ungkapkan kepada dirimu")
                    cl.sendText(msg.to,"Kabut dalam hatiku telah menghilang")
                    cl.sendText(msg.to,"Dan hal yang penting bagiku pun terlihat")
                    cl.sendText(msg.to,"Walaupun jawaban itu sebenarnya begitu mudah")
                    cl.sendText(msg.to,"Tetapi entah mengapa diriku melewatkannya")
                    cl.sendText(msg.to,"Untukku menjadi diri sendiri")
                    cl.sendText(msg.to,"Ku harus jujur, pada perasaanku")
                    cl.sendText(msg.to,"Ku suka dirimu ku suka")
                    cl.sendText(msg.to,"Ku berlari sekuat tenaga")
                    cl.sendText(msg.to,"Ku suka selalu ku suka")
                    cl.sendText(msg.to,"Ku teriak sebisa suaraku")
                    cl.sendText(msg.to,"Ku suka dirimu ku suka")
                    cl.sendText(msg.to,"Walau susah untukku bernapas")
                    cl.sendText(msg.to,"Tak akan ku sembunyikan")
                    cl.sendText(msg.to,"Oogoe daiyamondo~")
                    cl.sendText(msg.to,"Saat ku sadari sesuatu menghilang")
                    cl.sendText(msg.to,"Hati ini pun resah tidak tertahankan")
                    cl.sendText(msg.to,"Sekarang juga yang bisa ku lakukan")
                    cl.sendText(msg.to,"Merubah perasaan ke dalam kata kata")
                    cl.sendText(msg.to,"Mengapa sedari tadi")
                    cl.sendText(msg.to,"Aku hanya menatap langit")
                    cl.sendText(msg.to,"Mataku berkaca kaca")
                    cl.sendText(msg.to,"Berlinang tak bisa berhenti")
                    cl.sendText(msg.to,"Di tempat kita tinggal, didunia ini")
                    cl.sendText(msg.to,"Dipenuhi cinta, kepada seseorang")
                    cl.sendText(msg.to,"Ku yakin ooo ku yakin")
                    cl.sendText(msg.to,"Janji tak lepas dirimu lagi")
                    cl.sendText(msg.to,"Ku yakin ooo ku yakin")
                    cl.sendText(msg.to,"Akhirnya kita bisa bertemu")
                    cl.sendText(msg.to,"Ku yakin ooo ku yakin")
                    cl.sendText(msg.to,"Ku akan bahagiakan dirimu")
                    cl.sendText(msg.to,"Ku ingin kau mendengarkan")
                    cl.sendText(msg.to,"Oogoe daiyamondo~")
                    cl.sendText(msg.to,"Jika jika kamu ragu")
                    cl.sendText(msg.to,"Takkan bisa memulai apapun")
                    cl.sendText(msg.to,"Ungkapkan perasaanmu")
                    cl.sendText(msg.to,"Jujurlah dari sekarang juga")
                    cl.sendText(msg.to,"Jika kau bersuar")
                    cl.sendText(msg.to,"Cahaya kan bersinar")
                    cl.sendText(msg.to,"Ku suka dirimu ku suka")
                    cl.sendText(msg.to,"Ku berlari sekuat tenaga")
                    cl.sendText(msg.to,"Ku suka selalu ku suka")
                    cl.sendText(msg.to,"Ku teriak sebisa suaraku")
                    cl.sendText(msg.to,"Ku suka dirimu ku suka")
                    cl.sendText(msg.to,"Sampaikan rasa sayangku ini")
                    cl.sendText(msg.to,"Ku suka selalu ku suka")
                    cl.sendText(msg.to,"Ku teriakkan ditengah angin")
                    cl.sendText(msg.to,"Ku suka dirimu ku suka")
                    cl.sendText(msg.to,"Walau susah untuk ku bernapas")
                    cl.sendText(msg.to,"Tak akan ku sembunyikan")
                    cl.sendText(msg.to,"Oogoe daiyamondo~")
                    cl.sendText(msg.to,"Katakan dengan berani")
                    cl.sendText(msg.to,"Jika kau diam kan tetap sama")
                    cl.sendText(msg.to,"Janganlah kau merasa malu")
                    cl.sendText(msg.to,"“Suka” itu kata paling hebat!")
                    cl.sendText(msg.to,"“Suka” itu kata paling hebat!")
                    cl.sendText(msg.to,"“Suka” itu kata paling hebat!")
                    cl.sendText(msg.to,"Ungkapkan perasaanmu")
                    cl.sendText(msg.to,"Jujurlah dari sekarang juga..")
                    cl.sendText(msg.to,"Anugerah terindah adalah ketika kita masih diberikan waktu untuk berkumpul bersama orang-orang yang kita sayangi.")
                    cl.sendText(msg.to,"Cuma dirimu seorang yang bisa meluluhkan hati ini. Kamulah yang terindah dalam hidupku.")
                    cl.sendText(msg.to,"Aku ingin meraih kembali cintamu menjadi kenyataan. Saat diriku dalam siksaan cinta, dirimu melenggang pergi tanpa pernah memikirkan aku.")
                    cl.sendText(msg.to,"Tak ada yang salah dengan CINTA. Karena ia hanyalah sebuah kata dan kita sendirilah yang memaknainya.")
                    cl.sendText(msg.to,"Mencintaimu adalah inginku. memilikimu adalah dambaku. meski jarak jadi pemisah, hati tak akan bisa terpisah.")
                    cl.sendText(msg.to,"Dalam cinta ada bahagia, canda, tawa, sedih, kecewa, terluka, semua itu tidak akan terlupakan dalam hal cinta, itu yang artinya cinta.")
                    cl.sendText(msg.to,"Seseorang yang berarti, tak akan dengan mudah kamu miliki. Jika kamu sungguh mencintai, jangan pernah berhenti berusaha untuk hati.")
                    cl.sendText(msg.to,"Jika esok pagi menjelang, akan aku tantang matahari yang terbangun dari tidur lelap nya.")
                    cl.sendText(msg.to,"Ketulusan cinta hanya dapat dirasakan mereka yang benar-benar mempunyai hati tulus dalam cinta.")
                    cl.sendText(msg.to,"Kamu tak perlu menjadikan dirimu cantik/ganteng untuk bisa memilikiku, kamu hanya perlu menunjukkan bahwa aku membutuhkanmu.")
                    cl.sendText(msg.to,"Ada seribu hal yang bisa membuatku berpikir ununtuk meninggalkanmu, namun ada satu kata yang membuatku tetap disini. Aku Cinta Kamu.")
                    cl.sendText(msg.to,"Aku pernah jatuhkan setetes air mata di selat Sunda. Di hari aku bisa menemukannya lagi, itulah waktunya aku berhenti mencintaimu.")
                    cl.sendText(msg.to,"Cinta adalah caraku bercerita tentang dirimu, caraku menatap kepergian mu dan caraku tersenyum, saat menatap indah wajahmu.")
                    cl.sendText(msg.to,"Datang dan pergi seperti angin tidak beraturan dan arah merasakan cinta dalam kehidupan kadang ku bahagia kadang ku bersedih.")
                    cl.sendText(msg.to,"Cinta adalah caraku bercerita tentang dirimu, caraku menatap kepergian mu dan caraku tersenyum, saat menatap indah wajahmu.")
                    cl.sendText(msg.to,"Saat jarak memisahkan, satu yang harus kamu ketahui. Akan aku jaga cinta ini ununtukmu.")
                    cl.sendText(msg.to,"Bersandarlah di pundaku sampai kau merasakan kenyamanan, karena sudah keharusan bagiku ununtuk memberikanmu rasa nyaman.")
                    cl.sendText(msg.to,"Air mata merupakan satu-satunya cara bagimana mata berbicara ketika bibir tidak mampu menjelaskan apa yang membuatmu terluka.")
                    cl.sendText(msg.to,"Hidup tidak bisa lebih baik tanpa ada cinta, tapi cinta dengan cara yang salah akan membuat hidupmu lebih buruk.")
                    cl.sendText(msg.to,"Mencintaimu hanya butuh waktu beberapa detik, namun untuk melupakanmu butuh waktu seumur hidupku.")
                    cl.sendText(msg.to,"Hidup tidak bisa lebih baik tanpa ada cinta, tapi cinta dengan cara yang salah akan membuat hidupmu lebih buruk.")
                    cl.sendText(msg.to,"Mencintaimu hanya butuh waktu beberapa detik, namun ununtuk melupakanmu butuh waktu seumur hidupku.")
                    cl.sendText(msg.to,"Cinta merupakan keteguhan hati yang ditambatkan pada kemanusiaan yang menghubungkan masa lalu, masa kini dan masa depan.")
                    cl.sendText(msg.to,"Ketika mencintai seseorang, cintailah apa adanya. Jangan berharap dia yang sempurna, karena kesempurnaan adalah ketika mencinta tanpa syarat.")
                    cl.sendText(msg.to,"Cinta bukanlah tentang berapa lama kamu mengenal seseorang, tapi tentang seseorang yang membuatmu tersenyum sejak kamu mengenalnya.")
                    cl.sendText(msg.to,"Ketika mereka bertanya tentang kelemahanku, aku ingin mengatidakan bahwa kelemahanku itul adalah kamu. Aku merindukanmu di mana-mana dan aku sanagat mencintaimu.")
                    cl.sendText(msg.to,"Kehadiranmu dalam hidupku, aku tahu bahwa aku bisa menghadapi setiap tantangan yang ada di hadapanku, terima kasih telah menjadi kekuatanku.")
                    cl.sendText(msg.to,"Meneriakkan namamu di deras hujan, memandangmu dari kejauhan, dan berdo’a di hening malam. Cinta dalam diam ini lah yang mampu kupertahankan.")
                    cl.sendText(msg.to,"Perempuan selalu menjaga hati orang yang dia sayangsehingga hati dia sendiri tersiksa. inilah pengorbanan perempuan ununtuk lelaki yang tidak pernah sadar.")
                    cl.sendText(msg.to,"Ketika kau belum bisa mengambil keputusan ununtuk tetap bertahan dengan perasaan itu, sabarlah, cinta yang akan menguatkanmu.")
                    cl.sendText(msg.to,"Aku tidak akan pernah menjajikan ununtuk sebuah perasaan, tapi aku bisa menjanjikan ununtuk sebuah kesetiaan.")
                    cl.sendText(msg.to,"Cinta yang sebenarnya tidak buta, cinta yaitu adalah hal yang murni, luhur serta diharapkan. Yang buta itu jika cinta itu menguasai dirimu tanpa adanya suatu pertimbangan.")
                    cl.sendText(msg.to,"Aku tercipta dalam waktu, ununtuk mengisi waktu, selalu memperbaiki diri di setiap waktu, dan semua waktu ku adalah ununtuk mencintai kamu.")
                    cl.sendText(msg.to,"Cinta akan indah jika berpondasikan dengan kasih sang pencipta. Karena sesungguhnya Cinta berasal dari-Nya Dan cinta yang paling utama adalah cinta kepada Yang Kuasa.")
                    cl.sendText(msg.to,"Bagi aku, dalam hidup ini, hidup hanya sekali, cinta sekali dan matipun juga sekali. Maka tidak ada yang namanya mendua.")
                    cl.sendText(msg.to,"Tuhan..jagalah ia yang jauh disana, lindungi tiap detik hidup yang ia lewati,sayangi dia melebihi engkau menyayangiku.")
                    cl.sendText(msg.to,"Kapan kau akan berhenti menyakitiku, lelah ku hadapi semua ini tapi aku tidak bisa memungkiri aku sangat mencintaimu.")
                    cl.sendText(msg.to,"Ketidakutan terbesar dalam hidupku bukan kehilanganmu, tapi melihat dirimu kehilangan kebahagiaanmu.")
                    cl.sendText(msg.to,"Cinta yang sesungguhnya akan mengatidakan aku butuh kamu karna aku siap ununtuk mencintaimu dan menjalani suka duka bersamamu")
                    cl.sendText(msg.to,"Seseorang pacar yang baik adalah dia yang JUJUR dan tidak pernah membuat kamu selalu bertanya-tanya atau selalu mencurigai dia")
                    cl.sendText(msg.to,"Cinta bukanlah sebuah kata cinta, yang sebenarnya adalah cinta yang menyentuh hati dan perasaan")
                    cl.sendText(msg.to,"Kau datang di saat ke egoisan akan cinta tengah mendera. Membawa cahaya dan kedamaian, membuatku tidak mudah menyerah ununtuk merengkuh kisah cinta bersamamu")
                    cl.sendText(msg.to,"Aku sangat menyukai kebersamaan karena kebersamaan mengajarkan kita tentang suka dan duka di lalui bersama")
                    cl.sendText(msg.to,"Mungkin Tuhan sengaja memberi kita berjumpa dengan orang yang salah sebelum menemui insan yang betul supaya apabila kita akhirnya menemui insan yang betul, kita akan tahu bagaimana ununtuk bersyukur dengan pemberian dan hikmah di balik pemberian tersebut.")
                    cl.sendText(msg.to,"Getaran di hatiku yang lama haus akan belaianmu seperti saat dulu dan kau bisikan kata ‘aku cinta padamu’ aku merindukannya")
                    cl.sendText(msg.to,"Terkadang air mata adalah tanda kebahagiaan yang tidak terucapkan. Dan senyuman adalah tanda sakit yang mencoba ununtuk kuat")
                    cl.sendText(msg.to,"Dicintai dan disayangi kamu adalah anugerah terindah yang tuhan berikan padaku.")
                    cl.sendText(msg.to,"Mencintai kamu butuh waktu beberapa detik, Namun melupakanmu butuh waktu ku seumur hidup.")
                    cl.sendText(msg.to,"Datang dan pergi seperti angin tidak beraturan dan arah merasakan cinta dalam kehidupan kadang aku bahagia dan juga kadang aku bersedih.")
                    cl.sendText(msg.to,"Air mata merupakan satu-satunya cara bagimana mata berbicara ketika bibir tidak mampu lagi menjelaskan apa yang membuatmu terluka.")
                    cl.sendText(msg.to,"Jauh sebelum bertemu denganmu, aku telah mengenalmu dalam doaku.")
                    cl.sendText(msg.to,"Mungkin dia tidak sadar bahwa aku itu cemburu dan mungkin juga dia tidak merasa bahwa aku sangat terluka, tidak mendengar bahwa hatiku sedang menangis.")
                    cl.sendText(msg.to,"Kehadirmu membawa cinta, memberi bahagia, dan juga rasa rindu yang tiada pernah ada akhirnya.")
                    cl.sendText(msg.to,"Aku nngak mau jadi wakil rakyat, aku maunya jadi wali murid yang ngambil raport anak kita besok.")
                    cl.sendText(msg.to,"Seperti hujan yang turun di tanah yang tandus, seperti itulah arti hadirmu dengan cinta dan kasih sayang untukku.")
                    cl.sendText(msg.to,"Tanda-tanda cinta adalah ketika anda merasa bahwa kebahagiaan orang tersebut lebih penting daripada kebahagiaanmu sendiri.")
                    cl.sendText(msg.to,"Cinta tidak hanya apa yang anda rasakan, tetapi apa yang harus anda lakukan.")
                    cl.sendText(msg.to,"Cinta adalah sebuah kekuatan untuk melihat kesamaan dan tidak kesamaan.")
                    cl.sendText(msg.to,"Cinta adalah pengalaman penuh emosi yang dirasakan banyak orang tetapi hanya beberapa orang saja yang bisa menikmatinya.")
                    cl.sendText(msg.to,"Cinta adalah berbagi. Karena walau ada di dua raga yang berbeda, setiap pasangan hanya memiliki satu hati.")
                    cl.sendText(msg.to,"Saat kita berjauhan, sebenarnya hanya raga kitalah yang jauh. Namun hati kita selalu dekat, karena hatiku ada di hatimu.")
                    cl.sendText(msg.to,"Cinta datang dengan pengorbanan yang akan memberikan petunjuk siapa diri kita yang sebenarnya.")
                    cl.sendText(msg.to,"Cinta begitu lembut dan merdu, namun jangan kau gunankan untuk merayu. Karena rayuan hanyalah akan mengosongkan makna kecintaan yang sesungguhnya.")
                    cl.sendText(msg.to,"Cinta bukanlah penuntutan, penguasaan, pemaksaan, dan pengintimidasian. Tak lain itu hanyalah cara manusia mendefinisikannya. Karena cinta adalah perjuangan, pengorbanan, tanggungjawab, kejujuran, dan keikhlasan.")
                    cl.sendText(msg.to,"Derajat cinta hanya bisa diukur dengan seberapa besar “Pemberian” yang kita korbankan.")

            elif msg.text in ["Up3","up3"]:
                msg.contentType = 7
                msg.text = None
                msg.contentMetadata = {
                                     "STKID": "4",
                                     "STKPKGID": "1",
                                     "STKVER": "100" }
                cl.sendMessage(msg)
                cl.sendText(msg.to,"Ribuan kilo jalan yang kau tempuh")
                cl.sendText(msg.to,"Lewati rintang untuk aku anakmu")
                cl.sendText(msg.to,"Ibuku sayang masih terus berjalan walau tapak kaki, penuh darah... penuh nanah")
                cl.sendText(msg.to,"Seperti udara... kasih yang engkau berikan. Tak mampu ku membalas...ibu...ibu")
                cl.sendText(msg.to,"Ingin kudekat dan menangis di pangkuanmu")
                cl.sendText(msg.to,"Sampai aku tertidur, bagai masa kecil dulu")
                cl.sendText(msg.to,"Lalu doa-doa baluri sekujur tubuhku dengan apa membalas...ibu...ibu....")
                cl.sendText(msg.to,"Seperti udara... kasih yang engkau berikan")
                cl.sendText(msg.to,"Tak mampu ku membalas...ibu...ibu")
                cl.sendText(msg.to,"~~~The end~~~")
                cl.sendText(msg.to,"👏👏👏👏👏👏👏👏👏👏 yeeeey ")

            elif msg.text in ["Up4","up4"]:
                msg.contentType = 7
                msg.text = None
                msg.contentMetadata = {
                                     "STKID": "9",
                                     "STKPKGID": "1",
                                     "STKVER": "100" }
                cl.sendMessage(msg)
                cl.sendText(msg.to,"🎤... 1")
                cl.sendText(msg.to,"🎤....2")
                cl.sendText(msg.to,"🎤... 3")
                cl.sendText(msg.to,"Apa salah dan dosaku, sayang cinta suciku kau buang-buang lihat jurus yang kan ku berikan jaran goyang, jaran goyang")
                cl.sendText(msg.to,"Sayang, janganlah kau waton serem hubungan kita semula adem tapi sekarang kecut bagaikan asem semar mesem, semar mesem")
                cl.sendText(msg.to,"Jurus yang sangat ampuh, teruji terpercaya tanpa anjuran dokter, tanpa harus muter-muter cukup siji solusinya, pergi ke mbah dukun saja langsung sambat, ?Mbah, saya putus cinta?")
                cl.sendText(msg.to,"Kalau tidak berhasil, pakai jurus yang kedua semar mesem namanya, jaran goyang jodohnya cen rodok ndagel syarate, penting di lakoni wae ndang di cubo, mesthi kasil terbukti kasiate, genjrot")
                cl.sendText(msg.to,"Dan dudidam aku padamu, I love you i can?t stop loving you oh darling jaran goyang menunggumu")
                cl.sendText(msg.to,"Apa salah dan dosaku, sayang, cinta suciku kau buang-buang lihat jurus yang kan ku berikan, jaran goyang, jaran goyang sayang, janganlah kau waton serem, hubungan kita semula adem tapi sekarang kecut bagaikan asem, semar mesem, semar mesem")
                cl.sendText(msg.to,"Wes cukup stop mandekko disek sek sek jangan bicara jangan berisek sek sek sek ayo ndang mangkat ndukun, rasah kakean ngelamun ndukun, ndukun , ndukun ayo ndukun and slow, woles woles baby baby rasakno aku wes wani perih baby")
                cl.sendText(msg.to,"Rungokno, ku alami hal sama dengan dirimu bojoku mencampakkan diriku, podo bojomu podo tanggamu")
                cl.sendText(msg.to,"Dan dudidam aku padamu, I love you i can?t stop loving you oh darling jaran goyang menunggumu")
                cl.sendText(msg.to,"Apa salah dan dosaku, sayang, cinta suciku kau buang-buang lihat jurus yang kan ku berikan, jaran goyang, jaran goyang sayang, janganlah kau waton serem, hubungan kita semula adem tapi sekarang kecut bagaikan asem, semar mesem, semar mesem")
                cl.sendText(msg.to,"Ini terakhir, cara tuk dapatkan kamu jika ini gagal, kan ku racuni dirimu")
                cl.sendText(msg.to,"Apa salah dan dosaku, sayang, cinta suciku kau buang-buang lihat jurus yang kan ku berikan, jaran goyang, jaran goyang sayang, janganlah kau waton serem, hubungan kita semula adem tapi sekarang kecut bagaikan asem, semar mesem, semar mesem")
                cl.sendText(msg.to,"🎤🎤👏👏👏👏👏👏👏😘😘😘😘")
					
        #-------------Fungsi Spam Finish---------------------#

                            
            elif "Say " in msg.text.lower():
                say = msg.text.lower().replace("say ","")
                lang = 'id'
                tts = gTTS(text=say, lang=lang)
                tts.save("hasil.mp3")
                cl.sendAudio(msg.to,"hasil.mp3")
                


        #-------------Fungsi Broadcast Start------------#
            elif "B " in msg.text:
				bctxt = msg.text.replace("B ","")
				ki.sendText(msg.to,(bctxt))
				kk.sendText(msg.to,(bctxt))
				kc.sendText(msg.to,(bctxt))
       #--------------Fungsi Broadcast Finish-----------#

            elif msg.text in ["Cv say hi"]:
                ki.sendText(msg.to,"Hi buddy 􀜁􀅔Har Har􏿿")
                kk.sendText(msg.to,"Hi buddy 􀜁􀅔Har Har􏿿")
                kc.sendText(msg.to,"Hi buddy 􀜁􀅔Har Har􏿿")

#-----------------------------------------------

            elif msg.text in ["Cv say hinata pekok"]:
                ki.sendText(msg.to,"Hinata pekok 􀜁􀅔Har Har􏿿")
                kk.sendText(msg.to,"Hinata pekok 􀜁􀅔Har Har􏿿")
                kc.sendText(msg.to,"Hinata pekok 􀜁􀅔Har Har􏿿")
            elif msg.text in ["Cv say didik pekok"]:
                ki.sendText(msg.to,"Didik pekok 􀜁􀅔Har Har􏿿")
                kk.sendText(msg.to,"Didik pekok 􀜁􀅔Har Har􏿿")
                kc.sendText(msg.to,"Didik pekok 􀜁􀅔Har Har􏿿")
            elif msg.text in ["Cv say bobo ah","Bobo dulu ah"]:
                ki.sendText(msg.to,"Have a nice dream Cv 􀜁􀅔Har Har􏿿")
                kk.sendText(msg.to,"Have a nice dream Cv 􀜁􀅔Har Har􏿿")
                kc.sendText(msg.to,"Have a nice dream Cv 􀜁􀅔Har Har􏿿")
            elif msg.text in ["Cv say chomel pekok"]:
                ki.sendText(msg.to,"Chomel pekok 􀜁􀅔Har Har􏿿")
                kk.sendText(msg.to,"Chomel pekok 􀜁􀅔Har Har􏿿")
                kc.sendText(msg.to,"Chomel pekok 􀜁􀅔Har Har􏿿")
            elif msg.text in ["#welcome"]:
                ki.sendText(msg.to,"Selamat datang di INi bukan Grup")
                kk.sendText(msg.to,"Jangan nakal ok!")
#-----------------------------------------------
            elif msg.text in ["PING","Ping","ping"]:
                ki.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                kk.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                kc.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
#-----------------------------------------------
            elif msg.text in ["Salam"]:
                cl.sendText(msg.to,"السَّلاَمُ عَلَيْكُمْ وَرَحْمَةُ اللهِ وَبَرَكَاتُهُ")
                ki.sendText(msg.to,"Assalamu'alaikum")
            elif msg.text in ["Jawab"]:
                cl.sendText(msg.to,"وَعَلَيْكُمْ السَّلاَمُ وَرَحْمَةُ اللهِوَبَرَكَاتُهُ")
                ki.sendText(msg.to,"Wa'alaikumsallam.Wr,Wb")

#---------------------------------- SONG ------------------------------------
                              
            elif "Music " in msg.text:
                try:
                    songname = msg.text.lower().replace("Music ","")
                    params = {'songname': songname}
                    r = requests.get('http://ide.fdlrcn.com/workspace/yumi-apis/joox?' + urllib.urlencode(params))
                    data = r.text
                    data = json.loads(data)
                    for song in data:
                        hasil = 'This is Your Music\n'
                        hasil += 'Judul : ' + song[0]
                        hasil += '\nDurasi : ' + song[1]
                        hasil += '\nLink Download : ' + song[4]
                        cl.sendText(msg.to, hasil)
                        cl.sendText(msg.to, "Please Wait for audio...")
                        cl.sendAudioWithURL(msg.to, song[4])
                except Exception as njer:
                        cl.sendText(msg.to, str(njer))

#----------------------------------------------------------------------------
#--------------------------------- INSTAGRAM --------------------------------
            elif "/ig " in msg.text.lower():
                arg = msg.text.split(' ');
                nk0 = msg.text.replace("/ig ","")
                nk1 = nk0.rstrip('  ')
                if len(arg) > 1:
                    proc = subprocess.Popen('curl -s https://www.instagram.com/'+nk1+'/?__a=1',shell=True, stdout=subprocess.PIPE)
                    x = proc.communicate()[0]
                    parsed_json = json.loads(x)
                    if(len(x) > 10):
                        username = (parsed_json['user']['username'])
                        fullname = (parsed_json['user']['full_name'])
                        followers = (parsed_json['user']['followed_by']['count'])
                        following = (parsed_json['user']['follows']['count'])
                        media = (parsed_json['user']['media']['count'])
                        bio = (parsed_json['user']['biography'])
                        url = (parsed_json['user']['external_url'])
                        cl.sendText(msg.to,"Profile "+username+"\n\nUsername : "+username+"\nFull Name : "+fullname+"\nFollowers : "+str(followers)+"\nFollowing : "+str(following))
                        print '[Command] Instagram'
                    else:
                        cl.sendText(msg.to,"Not Found...")
                else:
                    cl.sendText(msg.to,"Contoh /ig hairu.ones")
#----------------------------------------------------------------------------
#--------------------------------- YOUTUBE ----------------------------------
            elif "Youtube " in msg.text:
                query = msg.text.replace("Youtube ","")
                with requests.session() as s:
                    s.headers['user-agent'] = 'Mozilla/5.0'
                    url = 'http://www.youtube.com/results'
                    params = {'search_query': query}
                    r = s.get(url, params=params)
                    soup = BeautifulSoup(r.content, 'html5lib')
                    hasil = ""
                    for a in soup.select('.yt-lockup-title > a[title]'):
                        if '&list=' not in a['href']:
                            hasil += ''.join((a['title'],'\nhttp://www.youtube.com' + a['href'],'\n\n'))
                    cl.sendText(msg.to,hasil)
                    print '[Command] Youtube Search'
#----------------------------------------------------------------------------
#--------------------------------- TRANSLATE --------------------------------
            elif "/translate-en " in msg.text:
                txt = msg.text.replace("/translate-en ","")
                try:
                    gs = goslate.Goslate()
                    trs = gs.translate(txt,'en')
                    cl.sendText(msg.to,trs)
                    print '[Command] Translate EN'
                except:
                    cl.sendText(msg.to,'Error.')

            elif "/translate-id " in msg.text:
                txt = msg.text.replace("/translate-en ","")
                try:
                    gs = goslate.Goslate()
                    trs = gs.translate(txt,'id')
                    cl.sendText(msg.to,trs)
                    print '[Command] Translate ID'
                except:
                    cl.sendText(msg.to,'Error.')
#----------------------------------------------------------------------------
       #-------------Fungsi Respon Start---------------------#
            elif msg.text in ["Respon","Shinobi","Respon Dong","respon dong"]:
                cl.sendText(msg.to,"Absen")
                ki.sendText(msg.to,"1 Hadir boss..")
                kk.sendText(msg.to,"2 Hadir boss..")
                kc.sendText(msg.to,"3 Hadir boss..")
                ks.sendText(msg.to,"4 Hadir boss..")
                km.sendText(msg.to,"5 Hadir boss..")
                kt.sendText(msg.to,"6 Hadir boss..")
      #-------------Fungsi Respon Finish---------------------#

      #-------------Fungsi Balesan Respon Start---------------------#
            elif msg.text in ["Ini Apa","ini apa","Apaan Ini","apaan ini"]:
                ki.sendText(msg.to,"Ya gitu deh intinya mah 􀨁􀅴questioning􏿿")

      #-------------Fungsi Balesan Respon Finish---------------------#

       #-------------Fungsi Speedbot Start---------------------#
            elif msg.text in ["Sp","Speed","speedbot"]:
                start = time.time()
                cl.sendText(msg.to, "█████████▒90%")
                elapsed_time = time.time() - start
                cl.sendText(msg.to, "%sseconds" % (elapsed_time))
      #-------------Fungsi Speedbot Finish---------------------#

            elif msg.text in ["Lurk"]:
                 if msg.toType == 2:
                    cl.sendText(msg.to, "lurking on")
                    try:
                        del wait2['readPoint'][msg.to]
                        del wait2['readMember'][msg.to]
                    except:
                        pass
                    wait2['readPoint'][msg.to] = msg.id
                    wait2['readMember'][msg.to] = ""
                    wait2['setTime'][msg.to] = datetime.today().strftime('%Y-%m-%d %H:%M:%S')
                    wait2['ROM'][msg.to] = {}
                    print "set point"



                    
            elif msg.text in ["Read"]:
                 if msg.toType == 2:
                    print "\nSider check aktif..."
                    if msg.to in wait2['readPoint']:
                        if wait2["ROM"][msg.to].items() == []:
                            chiya = ""
                        else:
                            chiya = ""
                            for rom in wait2["ROM"][msg.to].items():
                                print rom
                                chiya += rom[1] + "\n"

                        cl.sendText(msg.to, "People Who Read In Group\n____________________________%s\n\nPeople Who're Not in Chat\n\n%s\n\n===========================\nIn the last seen point:\n[%s]\n===========================\n" % (wait2['readMember'][msg.to],chiya,setTime[msg.to]))
                        print "\nReading Point Set..."
                        try:
                            del wait2['readPoint'][msg.to]
                            del wait2['readMember'][msg.to]
                        except:
                            pass
                        wait2['readPoint'][msg.to] = msg.id
                        wait2['readMember'][msg.to] = ""
                        wait2['setTime'][msg.to] = datetime.today().strftime('%Y-%m-%d %H:%M:%S')
                        wait2['ROM'][msg.to] = {}
                        print "lukers"
                        cl.sendText(msg.to, "Auto set reading point")
                    else:
                        cl.sendText(msg.to, "Set reading point first")

      #-------------Fungsi Banned Send Contact Start------------------#
            elif msg.text in ["Ban"]:
                wait["wblacklist"] = True
                cl.sendText(msg.to,"send contact")
                ki.sendText(msg.to,"send contact")
                kk.sendText(msg.to,"send contact")
                kc.sendText(msg.to,"send contact")
            elif msg.text in ["Unban"]:
                wait["dblacklist"] = True
                cl.sendText(msg.to,"send contact")
                ki.sendText(msg.to,"send contact")
                kk.sendText(msg.to,"send contact")
                kc.sendText(msg.to,"send contact")
      #-------------Fungsi Banned Send Contact Finish------------------#
            elif msg.text in ["backup2","Kai2"]:
                try:
                    ki.updateDisplayPicture(backup.pictureStatus)
                    ki.updateProfile(backup)
                    ki.sendText(msg.to, "Bunshin Kai2")
                except Exception as e:
                    ki.sendText(msg.to, str(e))
            elif msg.text in ["backup3","Kai3"]:
                try:
                    kk.updateDisplayPicture(backup.pictureStatus)
                    kk.updateProfile(backup)
                    kk.sendText(msg.to, "Bunshin Kai3")
                except Exception as e:
                    kk.sendText(msg.to, str(e))
            elif msg.text in ["backup4","Kai4"]:
                try:
                    kc.updateDisplayPicture(backup.pictureStatus)
                    kc.updateProfile(backup)
                    kc.sendText(msg.to, "Bunshin Kai4")
                except Exception as e:
                    kc.sendText(msg.to, str(e))
            elif msg.text in ["backup5","Kai5"]:
                try:
                    ks.updateDisplayPicture(backup.pictureStatus)
                    ks.updateProfile(backup)
                    ks.sendText(msg.to, "Bunshin Kai5")
                except Exception as e:
                    ks.sendText(msg.to, str(e))

#=================================================
            elif "Kagebunshin2 " in msg.text:
                if msg.from_ in admin:
                    midd = eval(msg.contentMetadata["MENTION"])
                    mata = midd["MENTIONEES"][0]["M"]
                    try:
                        ki.CloneContactProfile(mata)
                        ki.sendText(msg.to, "Kagebunshin No Jutsu2")
                    except Exception as e:
                                print e 
            elif "Kagebunshin3 " in msg.text:
                if msg.from_ in admin:
                    midd = eval(msg.contentMetadata["MENTION"])
                    mata = midd["MENTIONEES"][0]["M"]
                    try:
                        kk.CloneContactProfile(mata)
                        kk.sendText(msg.to, "Kagebunshin No Jutsu3")
                    except Exception as e:
                                print e 
            elif "Kagebunshin4 " in msg.text:
                if msg.from_ in admin:
                    midd = eval(msg.contentMetadata["MENTION"])
                    mata = midd["MENTIONEES"][0]["M"]
                    try:
                        kc.CloneContactProfile(mata)
                        kc.sendText(msg.to, "Kagebunshin No Jutsu4")
                    except Exception as e:
                                print e 
            elif "Kagebunshin5 " in msg.text:
                if msg.from_ in admin:
                    midd = eval(msg.contentMetadata["MENTION"])
                    mata = midd["MENTIONEES"][0]["M"]
                    try:
                        ks.CloneContactProfile(mata)
                        ks.sendText(msg.to, "Kagebunshin No Jutsu4")
                    except Exception as e:
                                print e 
#-----------------------------------------------      
            elif "Copy @" in msg.text:
               if msg.from_ in admin: 
                if msg.toType == 2:
                    print "[Copy]"
                    _name = msg.text.replace("Copy @","")
                    _nametarget = _name.rstrip('  ')                    
                    gs = cl.getGroup(msg.to)                    
                    targets = []
                    for g in gs.members:
                        if _nametarget == g.displayName:
                            targets.append(g.mid)
                    if targets == []:                        
                        cl.sendText(msg.to,"Tidak Ada Target ")                        
                    else:
                        for target in targets:
                            try:
                                contact = cl.getContact(target).statusMessage                                
                                contact2 = cl.getContact(target).displayName
                                contact3 = cl.getContact(target).pictureStatus
                                copy = cl.getProfile()
                                copy.statusMessage = contact                                
                                copy.displayName = contact2
                                copy.pictureStatus = contact3
                                cl.updateProfile(copy)
                                cl.sendText(msg.to, "Copy Done")
                            except:                                
                                pass                                               

#-----------------------------------------------   
            elif "Kagebunshin " in msg.text:
                if msg.from_ in admin:
                    midd = eval(msg.contentMetadata["MENTION"])
                    mata = midd["MENTIONEES"][0]["M"]
                    try:
                        cl.CloneContactProfile(mata)
                        cl.sendText(msg.to, "Kagebunshin No Jutsu")
                    except Exception as e:
                                print e                                                

            elif msg.text in ["abackup","Kai"]:
                try:
                    cl.updateDisplayPicture(backup.pictureStatus)
                    cl.updateProfile(backup)
                    cl.sendText(msg.to, "Bunshin Kai")
                except Exception as e:
                    cl.sendText(msg.to, str(e))

            elif "Byakugan " in msg.text:
                if msg.from_ in admin:
                    midd = eval(msg.contentMetadata["MENTION"])
                    mata = midd["MENTIONEES"][0]["M"]
                    try:
                            contact = cl.getContact(mata)
                            path = "http://dl.profile.line-cdn.net/" + contact.pictureStatus
                            cl.sendImageWithURL(msg.to, path)
                    except Exception as e:
                                print e   

            elif "Kamui " in msg.text:
                if msg.from_ in admin:
                    midd = eval(msg.contentMetadata["MENTION"])
                    mata = midd["MENTIONEES"][0]["M"]
                    try:
                            contact = cl.getContact(mata)
                            cu = cl.channel.getCover(mata)          
                            path = str(cu)
                            cl.sendImageWithURL(msg.to, path)
                    except Exception as e:
                                print e  
#----------------------------------------------------------------------------
                              
            elif "Umid" in msg.text:
                key = eval(msg.contentMetadata["MENTION"])
                key1 = key["MENTIONEES"][0]["M"]
                contact = cl.getContact(key1)
                cu = cl.channel.getCover(key1)
                try:
                    cl.sendText(msg.to,contact.mid)
                except:
                    cl.sendText(msg.to,contact.mid)

#--------------------------------------------------------
            elif "Ustatus " in msg.text:
                key = eval(msg.contentMetadata["MENTION"])
                key1 = key["MENTIONEES"][0]["M"]
                contact = cl.getContact(key1)
                cu = cl.channel.getCover(key1)
                try:
                    cl.sendText(msg.to,contact.statusMessage)
                except:
                    cl.sendText(msg.to,contact.statusMessage)
#--------------------------------------------------------
            elif "Info @" in msg.text:
              if msg.from_ in admin:
                nama = msg.text.replace("Info @","")
                target = nama.rstrip(' ')
                tob = cl.getGroup(msg.to)
                for g in tob.members:
                    if target == g.displayName:
                        gjh= cl.getContact(g.mid)
                        try:
                            cover = cl.channel.getCover(g.mid)
                        except:
                            cover = ""
                        cl.sendText(msg.to,"[Display Name]:\n" + gjh.displayName + "\n[Mid]:\n" + gjh.mid + "\n[BIO]:\n" + gjh.statusMessage + "\n[pict profile]:\nhttp://dl.profile.line-cdn.net/" + gjh.pictureStatus + "\n[Cover]:\n" + str(cover))
                    else:
                        pass
#-------------------------------------------

            elif msg.text.lower() == 'Bot restart':
                if msg.from_ in admin:
                    print "[Command]Like executed"
                    try:
                        cl.sendText(msg.to,"Restarting...")
                        restart_program()
                    except:
                        cl.sendText(msg.to,"Please wait")
                        restart_program()
                        pass
      
      #-------------Fungsi Bannlist Start------------------#          
            elif msg.text in ["Banlist"]:
                if wait["blacklist"] == {}:
                    cl.sendText(msg.to,"nothing")
                else:
                    cl.sendText(msg.to,"Blacklist user")
                    mc = ""
                    for mi_d in wait["blacklist"]:
                        mc += "->" +cl.getContact(mi_d).displayName + "\n"
                    cl.sendText(msg.to,mc)
      #-------------Fungsi Bannlist Finish------------------# 

	    elif msg.text in ["Like on"]:
                 if wait["likeOn"] == True:
                     if wait["lang"] == "JP":
                         cl.sendText(msg.to,"Done。")
                 else:
                     wait["likeOn"] = True
                     if wait["lang"] == "JP":
                         cl.sendText(msg.to,"Already。")
            elif msg.text in ["いいね:オフ","Like off"]:
                 if wait["likeOn"] == False:
                     if wait["lang"] == "JP":
                         cl.sendText(msg.to,"Done。")
                 else:
                     wait["likeOn"] = False
                     if wait["lang"] == "JP": 
                        cl.sendText(msg.to,"Already。")
            elif msg.from_ in mimic["target"] and mimic["status"] == True and mimic["target"][msg.from_] == True:
            	text = msg.text
            	if text is not None:
            		cl.sendText(msg.to,text)
            	else:
            		if msg.contentType == 7:
            			msg.contentType = 7
            			msg.text = None
            			msg.contentMetadata = {
            							 	 "STKID": "6",
            							 	 "STKPKGID": "1",
            							 	 "STKVER": "100" }
            			cl.sendMessage(msg)
            		elif msg.contentType == 13:
            			msg.contentType = 13
            			msg.contentMetadata = {'mid': msg.contentMetadata["mid"]}
            			cl.sendMessage(msg)
            elif "Mimic:" in msg.text:
            	if msg.from_ in admin:
            		cmd = msg.text.replace("Mimic:","")
            		if cmd == "on":
            			if mimic["status"] == False:
            				mimic["status"] = True
            				cl.sendText(msg.to,"Mimic on")
            			else:
            				cl.sendText(msg.to,"Mimic already on")
            		elif cmd == "off":
            			if mimic["status"] == True:
            				mimic["status"] = False
            				cl.sendText(msg.to,"Mimic off")
            			else:
            				cl.sendText(msg.to,"Mimic already off")
            		elif "add:" in cmd:
            			target0 = msg.text.replace("Mimic:add:","")
            			target1 = target0.lstrip()
            			target2 = target1.replace("@","")
            			target3 = target2.rstrip()
            			_name = target3
            			gInfo = cl.getGroup(msg.to)
            			targets = []
            			for a in gInfo.members:
            				if _name == a.displayName:
            					targets.append(a.mid)
            			if targets == []:
            				cl.sendText(msg.to,"No targets")
            			else:
            				for target in targets:
            					try:
            						mimic["target"][target] = True
            						cl.sendText(msg.to,"Success added target")
            						#cl.sendMessageWithMention(msg.to,target)
            						break
            					except:
            						cl.sendText(msg.to,"Failed")
            						break
            		elif "del:" in cmd:
            			target0 = msg.text.replace("Mimic:del:","")
            			target1 = target0.lstrip()
            			target2 = target1.replace("@","")
            			target3 = target2.rstrip()
            			_name = target3
            			gInfo = cl.getGroup(msg.to)
            			targets = []
            			for a in gInfo.members:
            				if _name == a.displayName:
            					targets.append(a.mid)
            			if targets == []:
            				cl.sendText(msg.to,"No targets")
            			else:
            				for target in targets:
            					try:
            						del mimic["target"][target]
            						cl.sendText(msg.to,"Success deleted target")
            						#cl.sendMessageWithMention(msg.to,target)
            						break
            					except:
            						cl.sendText(msg.to,"Failed!")
			elif cmd == "ListTarget":
            			if mimic["target"] == {}:
            				cl.sendText(msg.to,"No target")
                    	else:
                    		lst = "<<Lit Target>>"
                    		total = len(mimic["target"])
                    		for a in mimic["target"]:
                				if mimic["target"][a] == True:
                					stat = "On"
                				else:
                					stat = "Off"
                				lst += "\n->" + cl.getContact(mi_d).displayName + " | " + stat
                                cl.sendText(msg.to,lst + "\nTotal:" + total)
      
            elif msg.text in ["Cek ban"]:
                if msg.toType == 2:
                    group = cl.getGroup(msg.to)
                    gMembMids = [contact.mid for contact in group.members]
                    matched_list = []
                    for tag in wait["blacklist"]:
                        matched_list+=filter(lambda str: str == tag, gMembMids)
                    cocoa = ""
                    for mm in matched_list:
                        cocoa += mm + "\n"
                    cl.sendText(msg.to,cocoa + "")
            elif msg.text in ["Kill ban"]:
                if msg.toType == 2:
                    group = cl.getGroup(msg.to)
                    gMembMids = [contact.mid for contact in group.members]
                    matched_list = []
                    for tag in wait["blacklist"]:
                        matched_list+=filter(lambda str: str == tag, gMembMids)
                    if matched_list == []:
                        cl.sendText(msg.to,"There was no blacklist user")
                        ki.sendText(msg.to,"There was no blacklist user")
                        kk.sendText(msg.to,"There was no blacklist user")
                        kc.sendText(msg.to,"There was no blacklist user")
                        return
                    for jj in matched_list:
                        cl.kickoutFromGroup(msg.to,[jj])
                        ki.kickoutFromGroup(msg.to,[jj])
                        kk.kickoutFromGroup(msg.to,[jj])
                        kc.kickoutFromGroup(msg.to,[jj])
                    cl.sendText(msg.to,"Blacklist emang pantas tuk di usir")
                    ki.sendText(msg.to,"Blacklist emang pantas tuk di usir")
                    kk.sendText(msg.to,"Blacklist emang pantas tuk di usir")
                    kc.sendText(msg.to,"Blacklist emang pantas tuk di usir")
            elif msg.text in ["Clear"]:
                if msg.toType == 2:
                    group = cl.getGroup(msg.to)
                    gMembMids = [contact.mid for contact in group.invitee]
                    for _mid in gMembMids:
                        cl.cancelGroupInvitation(msg.to,[_mid])
                    cl.sendText(msg.to,"I pretended to cancel and canceled.")
            elif "random: " in msg.text:
              if msg.from_ in admin:
                if msg.toType == 2:
                    strnum = msg.text.replace("random: ","")
                    source_str = 'abcdefghijklmnopqrstuvwxyz1234567890@:;./_][!&%$#)(=~^|'
                    try:
                        num = int(strnum)
                        group = cl.getGroup(msg.to)
                        for var in range(0,num):
                            name = "".join([random.choice(source_str) for x in xrange(10)])
                            time.sleep(0.01)
                            group.name = name
                            cl.updateGroup(group)
                    except:
                        cl.sendText(msg.to,"Error")
            elif "albumat'" in msg.text:
                try:
                    albumtags = msg.text.replace("albumat'","")
                    gid = albumtags[:6]
                    name = albumtags.replace(albumtags[:34],"")
                    cl.createAlbum(gid,name)
                    cl.sendText(msg.to,name + "created an album")
                except:
                    cl.sendText(msg.to,"Error")

            elif "Cekon" in msg.text:
                try:
                    del cctv['point'][msg.to]
                    del cctv['sidermem'][msg.to]
                    del cctv['cyduk'][msg.to]
                except:
                    pass
                cctv['point'][msg.to] = msg.id
                cctv['sidermem'][msg.to] = ""
                cctv['cyduk'][msg.to]=True
                cl.sendText(msg.to,"Siap cek On")
                
            elif "Cekoff" in msg.text:
                if msg.to in cctv['point']:
                    cctv['cyduk'][msg.to]=False
                    cl.sendText(msg.to, cctv['sidermem'][msg.to])
                else:
                    cl.sendText(msg.to, "Heh belom di On") 

        if op.param3 == "1":
            if op.param1 in wait2["pro_name"]:
                group = cl.getGroup(op.param1)
                try:
					group.name = wait["pro_name"][op.param1]
					cl.updateGroup(group)
					cl.sendText(op.param1, "Groupname protect now")
					wait["blacklist"][op.param2] = True
					f=codecs.open('st2__b.json','w','utf-8')
					json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                except Exception as e:
                    print e
                    pass		

	if op.type == 55:
		print "[NOTIFIED_READ_MESSAGE]"
	try:
				if op.param1 in wait2['readPoint']:
					Nama = cl.getContact(op.param2).displayName
					if Nama in wait2['readMember'][op.param1]:
						pass
					else:
						wait2['readMember'][op.param1] += "\n-> " + Nama
						wait2['ROM'][op.param1][op.param2] = "-> " + Nama
						wait2['setTime'][msg.to] = datetime.today().strftime('%Y-%m-%d %H:%M:%S')
				else:
					cl.sendText
	except:
		 pass            

        if op.type == 26:
            msg = op.message
            try:
                if msg.contentType == 0:
                    try:
                        if msg.to in wait2['readPoint']:
                            if msg.from_ in wait2["ROM"][msg.to]:
                                del wait2["ROM"][msg.to][msg.from_]
                        else:
                            pass
                    except:
                        pass
                else:
                    pass

            except KeyboardInterrupt:
                sys.exit(0)
            except Exception as error:
                print error
                print ("\n\nRECEIVE_MESSAGE\n\n")
                return

        if op.type == 55:
                try:
                    if cctv['cyduk'][op.param1]==True:
                        if op.param1 in cctv['point']:
                            Name = cl.getContact(op.param2).displayName
                            path = "http://dl.profile.line-cdn.net/" + cl.getContact(op.param2).pictureStatus
                            if Name in cctv['sidermem'][op.param1]:
                                pass
                            else:
                                cctv['sidermem'][op.param1] += "\n~ " + Name
                                #cl.mention(op.param1, op.param2)
                                if " " in Name:
                                    nick = Name.split(' ')
                                    if len(nick) == 2:
                                        cl.sendText(op.param1, 'Salken '+nick[0])
                                        cl.sendImageWithURL(op.param1, path)
                                    else:
                                        cl.sendText(op.param1, 'Salam '+nick[1])
                                        cl.sendImageWithURL(op.param1, path)
                                else:
                                    cl.sendText(op.param1, 'Hai '+Name)
                                    cl.sendImageWithURL(op.param1, path)
                        else:
                            cl.sendText(op.param1, 'Jangan ngintip '+Name)
                            cl.sendImageWithURL(op.param1, path)
                    else:
                        pass
                except:
                    pass

        else:
            pass
		
        if op.type == 59:
            print op


    except Exception as error:
        print error


def a2():
    now2 = datetime.now()
    nowT = datetime.strftime(now2,"%M")
    if nowT[14:] in ["10","20","30","40","50","00"]:
        return False
    else:
        return True

def autoSta():
     count = 1
     while True:
         try:
            for posts in cl.activity(1)["result"]["posts"]:
              if posts["postInfo"]["liked"] is False:
                 if wait["likeOn"] == True:
                    cl.like(posts["userInfo"]["writerMid"], posts["postInfo"]["postId"], 1001)
                    if wait["commentOn"] == True:
                       if posts["userInfo"]["writerMid"] in wait["commentBlack"]:
                          pass
                       else:
                           cl.comment(posts["userInfo"]["writerMid"],posts["postInfo"]["postId"],wait["comment"])
         except:
             count += 1
             if(count == 50):
                 sys.exit(0)
             else:
                 pass
thread1 = threading.Thread(target=autoSta) 
thread1.daemon = True 
thread1.start()
while True:
    try:
        Ops = cl.fetchOps(cl.Poll.rev, 5)
    except EOFError:
        raise Exception("It might be wrong revision\n" + str(cl.Poll.rev))

    for Op in Ops:
        if (Op.type != OpType.END_OF_OPERATION):
            cl.Poll.rev = max(cl.Poll.rev, Op.revision)
            bot(Op)
