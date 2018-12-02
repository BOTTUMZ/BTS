# -*- coding: utf-8 -*-
from linepy import *
from akad.ttypes import Message
from akad.ttypes import ContentType as Type
from datetime import datetime
from time import sleep
from bs4 import BeautifulSoup
from humanfriendly import format_timespan, format_size, format_number, format_length
import time, random, sys, json, codecs, threading, glob, re, string, os, requests,subprocess, six, ast, pytz, urllib.request, urllib.parse, urllib.error, urllib.parse
from gtts import gTTS
#import html5lib,shutil
#import wikipedia,goslate
#import youtube_dl, pafy, asyncio
from multiprocessing import Pool, Process
from googletrans import Translator
#==============================================================================#
botStart = time.time()
#==============================================================================#
#line = LINE()
#line = LINE("เมล","พาส")
nadya = LINE()
nadya.log("Auth Token : " + str(nadya.authToken))
nadya.log("Timeline Token : " + str(nadya.tl.channelAccessToken))

KAC = [nadya]

nadyaMID = nadya.profile.mid

Bots = [nadyaMID]
creator = ["u9c1a8823e7b9605e031c9f7d39acaa4c","u24d5f93f9113c991342c079005467e2f"]
Owner = ["u9c1a8823e7b9605e031c9f7d39acaa4c"]
admin = ["u9c1a8823e7b9605e031c9f7d39acaa4c"]

nadyaProfile = nadya.getProfile()

nadyaSettings = nadya.getSettings()

oepoll = OEPoll(nadya)

responsename = nadya.getProfile().displayName
#==============================================================================#




with open('Owner.json', 'r') as fp:
    Owner = json.load(fp)
    
with open('admin.json', 'r') as fp:
    admin = json.load(fp)
    
myProfile = {
        "displayName": "",
        "statusMessage": "",
        "pictureStatus": ""
}

ProtectMessage = ["cleanse","group cleansed.","mulai",".winebot",".kickall","mayhem","kick on","Kick","!kickall","nuke","บิน","Kick","กระเด็น","หวด","เซลกากจัง","เตะ","ปลิว","ควย","หี","แตด","เย็ดแม่","เย็ดเข้","ค.วย","สัส","เหี้ย","ไอ้เหี้ย","พ่อมึงตาย","ไอ้เลว","ระยำ","ชาติหมา","หน้าหี","เซลกาก","ไอ้เรส","ไอ้เหี้ยเรส","ไอ่เรส","พ่องตาย","ส้นตีน","แม่มึงอ่ะ","แม่มึงดิ","พ่อมึงดิ","บอทเหี้ย","บอทควย","ควยบอท","บอทนรก","เหี้ยบอท"]

myProfile["displayName"] = nadyaProfile.displayName
myProfile["statusMessage"] = nadyaProfile.statusMessage
myProfile["pictureStatus"] = nadyaProfile.pictureStatus

readOpen = codecs.open("read.json","r","utf-8")
settingsOpen = codecs.open("temp.json","r","utf-8")
#==============================================================================#

read = json.load(readOpen)
settings = json.load(settingsOpen)

#if settings["restartPoint"] != None:
#    nadya.sendMessage(settings["restartPoint"], "Bot kembali aktif")
#    settings["restartBot"] = None

def restartBot():
    print ("[ INFO ] BOT RESETTED")
    backupData()
#    time.sleep(10)
    python = sys.executable
    os.execl(python, python, *sys.argv)
    
def logError(text):
    nadya.log("[ ERROR ] " + str(text))
    time_ = datetime.now()
    with open("errorLog.txt","a") as error:
        error.write("\n[%s] %s" % (str(time), text))
        
def sendMessageWithMention(to, mid):
    try:
        aa = '{"S":"0","E":"3","M":'+json.dumps(mid)+'}'
        text_ = '@x '
        nadya.sendMessage(to, text_, contentMetadata={'MENTION':'{"MENTIONEES":['+aa+']}'}, contentType=0)
    except Exception as error:
        logError(error)

def myhelp():
    myHelp = """╔══════════════════┓
╠═✪〘♥ ✿คำสั่งบอท✿ ♥〙
╚══════════════════┛
╔══════════════════┓
╠❋►บอท,คำสั่ง
╠❋►me
╠❋►แทค
╠❋►sp
╠❋►ข้อมูลบอท
╠❋►จับ
╠❋►ปิดจับ
╠❋►ใครอ่าน
╠❋►ปฏิทิน,เวลา,30
╠❋►เทส
╠❋►สปีด 
╰═❋⭐❄ By:Hack Scan Win™ ⭐❄
〘 line.me/ti/p/~vipscanner_win 〙"""
    return myHelp
#==============================================================================#
def backupData():
    try:
        backup = settings
        f = codecs.open('temp.json','w','utf-8')
        json.dump(backup, f, sort_keys=True, indent=4, ensure_ascii=False)
        backup = read
        f = codecs.open('read.json','w','utf-8')
        json.dump(backup, f, sort_keys=True, indent=4, ensure_ascii=False)
        return True
    except Exception as error:
        logError(error)
        return False
        
def command(text):
    pesan = text.lower()
    if pesan.startswith(settings["keyCommand"]):
        cmd = pesan.replace(settings["keyCommand"],"")
    else:
        cmd = "Undefined command"
    return cmd        


def lineBot(op):
    try:
        if op.type == 0:
            print ("[ 💥 รอรับคำสั่ง 💥 ]")
            return
        if op.type == 5:
            print ("[ 5 ] NOTIFIED ADD CONTACT")
            if settings["autoAdd"] == True:
                nadya.sendMessage(op.param1, "สวัสดี {} ขอบคุณที่แอดมา D".format(str(nadya.getContact(op.param1).displayName)))
                nadya.sendMessage(op.param1, str(settings["ww"]))
                nadya.sendMessage(op.param1, str(settings["comment"]))
                nadya.sendMessage(op.param1, "ต้องการบอทแทค.. ท่านสามารถเชิญผมเข้ากลุ่มได้เลย\n\nแล้วใช้คำสั่ง แทค หรือ /1 ก็สามารถแท็กคนทั้งกลุ่มได้เลยครับ")
        if op.type == 13:
            print ("[ 13 ] NOTIFIED INVITE GROUP")
            group = nadya.getGroup(op.param1)
            if settings["autoJoin"] == True:
                nadya.acceptGroupInvitation(op.param1)
                nadya.sendMessage(op.param1, str(settings["ww"]))
                nadya.sendMessage(op.param1, "ต้องการบอทแทค.. ท่านสามารถเชิญผมเข้ากลุ่มได้เลย\n\nแล้วใช้คำสั่ง แทค หรือ /1 ก็สามารถแท็กคนทั้งกลุ่มได้เลยครับ")
        if op.type == 13:
            print ("[ 13 ] NOTIFIED INVITE INTO GROUP")
            group = nadya.getGroup(op.param1)
            contact = nadya.getContact(op.param2)
            if settings["autoJoin"] == True:
                if settings["autoCancel"]["on"] == False:
                    if len(group.members) > settings["autoCancel"]["members"]:
                        nadya.acceptGroupInvitation(op.param1)
                    else:
                        nadya.rejectGroupInvitation(op.param1)
                else:
                    nadya.acceptGroupInvitation(op.param1)
            gInviMids = []
            for z in group.invitee:
                if z.mid in op.param3:
                    gInviMids.append(z.mid)
            listContact = ""
            if gInviMids != []:
                for j in gInviMids:
                    name_ = nadya.getContact(j).displayName
                    listContact += "\n      + {}".format(str(name_))

            arg = "   Group Name : {}".format(str(group.name))
            arg += "\n   Executor : {}".format(str(contact.displayName))
            arg += "\n   List User Invited : {}".format(str(listContact))
            print (arg)
        if op.type == 17:
           print ("MEMBER JOIN TO GROUP")
           if settings["Wc"] == True:
             if op.param2 in nadyaMID:
                 return
             dan = nadya.getContact(op.param2)
             tgb = nadya.getGroup(op.param1)
             nadya.sendMessage(op.param1,"🌿🌿🌿🌿🍒🍐🍉🌽🌴🍀🌴🌴\n\n*สวัสดี {},\n\n    🙏ยินดีต้อนรับเข้าสู่กลุ่ม🙏\n\n{},\n\n🍁🍁🍁 By.🔥Hack Scan 🔔Win🔔 🍂🍂🍂".format(str(dan.displayName),str(tgb.name)))
             nadya.sendMessage(op.param1, str(settings["welcome"]))
             nadya.sendContact(op.param1, op.param2)
             nadya.sendMessage(op.param1,"สเตตัส\n{}".format(str(dan.statusMessage)))
             nadya.sendImageWithURL(op.param1, "http://dl.profile.line-cdn.net{}".format(dan.picturePath))
             nadya.sendMessage(op.param1, str(settings["comment"]))
             nadya.sendMessage(op.param1, "ต้องการบอทแทค.. ท่านสามารถเชิญผมเข้ากลุ่มได้เลย\n\nแล้วใช้คำสั่ง แทค หรือ /1 ก็สามารถแท็กคนทั้งกลุ่มได้เลยครับ")
        if op.type == 19:
           print ("MEMBER KICKOUT TO GROUP")
           if settings["Nk"] == True:
             if op.param2 in nadyaMID:
                 return
             dan = nadya.getContact(op.param2)
             tgb = nadya.getGroup(op.param1)
             nadya.sendMessage(op.param1,str(settings["kick"]) + "\n\n™ผู้ใช้คนนี้เตะสมาชิก\n\n             {}, คือหยังมันโหดแท้วะΣ(っﾟДﾟ；)っ ".format(str(dan.displayName)))
             nadya.sendContact(op.param1, op.param2)
             nadya.sendMessage(op.param1,"สเตตัส\n{}".format(str(dan.statusMessage)))
             nadya.sendImageWithURL(op.param1, "http://dl.profile.line-cdn.net{}".format(dan.picturePath))
             nadya.sendMessage(op.param1, "ต้องการบอทแทค.. ท่านสามารถเชิญผมเข้ากลุ่มได้เลย\n\nแล้วใช้คำสั่ง แทค หรือ /1 ก็สามารถแท็กคนทั้งกลุ่มได้เลยครับ")
        if op.type == 15:
           print ("MEMBER LEAVE TO GROUP")
           if settings["Lv"] == True:
             if op.param2 in nadyaMID:
                 return
             dan = nadya.getContact(op.param2)
             tgb = nadya.getGroup(op.param1)
             nadya.sendMessage(op.param1,str(settings["bye"]) + "\n {}, ไปซะละ {} \nลาก่อยยย❋".format(str(dan.displayName),str(tgb.name)))
             nadya.sendContact(op.param1, op.param2)
             nadya.sendImageWithURL(op.param1, "http://dl.profile.line-cdn.net{}".format(dan.picturePath))
             nadya.sendMessage(op.param1, "ต้องการบอทแทค.. ท่านสามารถเชิญผมเข้ากลุ่มได้เลย\n\nแล้วใช้คำสั่ง แทค หรือ /1 ก็สามารถแท็กคนทั้งกลุ่มได้เลยครับ")
                
        if op.type == 24:
            print ("[ 24 ] NOTIFIED LEAVE ROOM")
            if settings["autoLeave"] == True:
                nadya.leaveRoom(op.param1)
#-------------------------------------------------------------------------------
        if op.type == 26:
            msg = op.message
            if msg.contentType == 13:
                if settings["wblack"] == True:
                    if msg.contentMetadata["mid"] in settings["commentBlack"]:
                        nadya.sendMessage(msg.to,"sudah masuk daftar hitam")
                        settings["wblack"] = False
                    else:
                        settings["commentBlack"][msg.contentMetadata["mid"]] = True
                        settings["wblack"] = False
                        nadya.sendMessage(msg.to,"Itu tidak berkomentar")
                elif settings["dblack"] == True:
                    if msg.contentMetadata["mid"] in settings["commentBlack"]:
                        del settings["commentBlack"][msg.contentMetadata["mid"]]
                        nadya.sendMessage(msg.to,"Done")
                        settings["dblack"] = False
                    else:
                        settings["dblack"] = False
                        nadya.sendMessage(msg.to,"Tidak ada dalam daftar hitam")
#-------------------------------------------------------------------------------
                elif settings["wblacklist"] == True:
                    if msg.contentMetadata["mid"] in settings["blacklist"]:
                        nadya.sendMessage(msg.to,"sudah masuk daftar hitam")
                        settings["wblacklist"] = False
                    else:
                        settings["blacklist"][msg.contentMetadata["mid"]] = True
                        settings["wblacklist"] = False
                        nadya.sendMessage(msg.to,"Done")
                        
                elif settings["dblacklist"] == True:
                    if msg.contentMetadata["mid"] in settings["blacklist"]:
                        del settings["blacklist"][msg.contentMetadata["mid"]]
                        nadya.sendMessage(msg.to,"Done")
                        settings["dblacklist"] = False
                    else:
                        settings["dblacklist"] = False
                        nadya.sendMessage(msg.to,"Done")
                        
                       
#-------------------------------------------------------------------------------
        if op.type == 26:
            msg = op.message
            if msg.contentType == 13:
                if settings["winvite"] == True:
                     if msg._from in Owner:
                         _name = msg.contentMetadata["displayName"]
                         invite = msg.contentMetadata["mid"]
                         groups = nadya.getGroup(msg.to)
                         pending = groups.invitee
                         targets = []
                         for s in groups.members:
                             if _name in s.displayName:
                                 nadya.sendMessage(msg.to,"-> " + _name + " \nทำการเชิญสำเร็จ")
                                 break
                             elif invite in settings["blacklist"]:
                                 nadya.sendMessage(msg.to,"ขออภัย, " + _name +" บุคคนนี้อยู่ในรายการบัญชีดำ")
                                 nadya.sendMessage(msg.to,"ใช้คำสั่ง!, \n➡ล้างดำ➡ดึง" )
                                 break
                             else:
                                 targets.append(invite)
                         if targets == []:
                             pass
                         else:
                             for target in targets:
                                 try:
                                     nadya.findAndAddContactsByMid(target)
                                     nadya.inviteIntoGroup(msg.to,[target])
                                     nadya.sendMessage(msg.to,"เชิญคนนี้สำเร็จแล้ว : \n➡" + _name)
                                     settings["winvite"] = False
                                     break
                                 except:
                                     try:
                                         nadya.findAndAddContactsByMid(invite)
                                         nadya.inviteIntoGroup(op.param1,[invite])
                                         settings["winvite"] = False
                                     except:
                                         nadya.sendMessage(msg.to,"😧ตรวจพบข้อผิดพลาดที่ไม่ทราบสาเหตุ😩อาจเป็นได้ว่าบัญชีของคุณถูกแบนเชิญ😨")
                                         settings["winvite"] = False
                                         break
                                         
        if op.type == 26:
            print ("[ 💫 คำสั่งจากผู้ดูแล 💫 ]")
            msg = op.message
            text = msg.text
            msg_id = msg.id
            receiver = msg.to
            sender = msg._from
            if msg.toType == 0:
                if sender != nadya.profile.mid:
                    to = sender
                else:
                    to = receiver
            else:
                to = receiver
            if msg.contentType == 0:
                if text is None:
                    return
#==============================================================================#
                if msg.text in ('0','help','Help','คำสั่ง'):
                    myHelp = myhelp()
                    nadya.sendMessage(to, str(myHelp))
                    nadya.sendContact(to, "u24d5f93f9113c991342c079005467e2f")
                elif text.lower() == 'texttospeech':
                    helpTextToSpeech = helptexttospeech()
                    nadya.sendMessage(to, str(helpTextToSpeech))
                elif text.lower() == 'translate':
                    helpTranslate = helptranslate()
                    nadya.sendMessage(to, str(helpTranslate))
#=============COMMAND KICKER===========================#
                elif msg.text in ('sp','Sp','สปีด'):
                    start = time.time()
                    nadya.sendMessage(to, "รอสักครู่...")
                    elapsed_time = time.time() - start
                    nadya.sendMessage(to,format(str(elapsed_time)))
                elif text.lower() == 'รีบอท':
                  if msg._from in Owner:
                    nadya.sendMessage(to, "รอสักครู่...")
                    time.sleep(5)
                    nadya.sendMessage(to, "เรียบร้อย")
                    restartBot()
                elif text.lower() == 'บอทออน':
                    timeNow = time.time()
                    runtime = timeNow - botStart
                    runtime = format_timespan(runtime)
                    nadya.sendMessage(to, "ระยะเวลาการทำงานของบอท {}".format(str(runtime)))
                elif text.lower() == 'ข้อมูลบอท':
                    try:
                        arr = []
                        owner = "u24d5f93f9113c991342c079005467e2f"
                        creator = nadya.getContact(owner)
                        contact = nadya.getContact(nadyaMID)
                        grouplist = nadya.getGroupIdsJoined()
                        contactlist = nadya.getAllContactIds()
                        blockedlist = nadya.getBlockedContactIds()
                        ret_ = "╔══[ ข้อมูลบอท ]"
                        ret_ += "\n╠ ชื่อ : {}".format(contact.displayName)
                        ret_ += "\n╠ กลุ่ม : {}".format(str(len(grouplist)))
                        ret_ += "\n╠ เพื่อน : {}".format(str(len(contactlist)))
                        ret_ += "\n╠ Blocked : {}".format(str(len(blockedlist)))
                        ret_ += "\n╠══[ สถานะ Selfbot ]"
                        ret_ += "\n╠ Version : Premium"
                        ret_ += "\n╠ ผู้สร้างบอท : {}".format(creator.displayName)
                        ret_ += "\n╚══[ 🔥Hack Scan 🔔Win🔔 :P ]"
                        nadya.sendMessage(to, str(ret_))
                    except Exception as e:
                        nadya.sendMessage(msg.to, str(e))
#==============================================================================#
                elif text.lower() == 'status':
                    try:
                        ret_ = "╔══[ Status ]"
                        if settings["protect"] == True: ret_ += "\n╠ Protect ✅"
                        else: ret_ += "\n╠ Protect ❌"
                        if settings["qrprotect"] == True: ret_ += "\n╠ Qr Protect ✅"
                        else: ret_ += "\n╠ Qr Protect ❌"
                        if settings["inviteprotect"] == True: ret_ += "\n╠ Invite Protect ✅"
                        else: ret_ += "\n╠ Invite Protect ❌"
                        if settings["cancelprotect"] == True: ret_ += "\n╠ Cancel Protect ✅"
                        else: ret_ += "\n╠ Cancel Protect ❌"
                        if settings["autoAdd"] == True: ret_ += "\n╠ Auto Add ✅"
                        else: ret_ += "\n╠ Auto Add ❌"
                        if settings["autoJoin"] == True: ret_ += "\n╠ Auto Join ✅"
                        else: ret_ += "\n╠ Auto Join ❌"
                        if settings["autoLeave"] == True: ret_ += "\n╠ Auto Leave ✅"
                        else: ret_ += "\n╠ Auto Leave ❌"
                        if settings["autoRead"] == True: ret_ += "\n╠ Auto Read ✅"
                        else: ret_ += "\n╠ Auto Read ❌"
                        if settings["checkSticker"] == True: ret_ += "\n╠ Check Sticker ✅"
                        else: ret_ += "\n╠ Check Sticker ❌"
                        if settings["detectMention"] == True: ret_ += "\n╠ Detect Mention ✅"
                        else: ret_ += "\n╠ Detect Mention ❌"
                        ret_ += "\n╚══[ Status ]"
                        nadya.sendMessage(to, str(ret_))
                    except Exception as e:
                        nadya.sendMessage(msg.to, str(e))
#-------------------------------------------------------------------------------
                elif text.lower() == 'เปิดลิ้ง':
                    if msg._from in Owner:
                        group = nadya.getGroup(to)
                        if group.preventedJoinByTicket == False:
                            nadya.sendMessage(to, "เปิดลิ้งเรียบร้อย")
                        else:
                            group.preventedJoinByTicket = False
                            nadya.updateGroup(group)
                            nadya.sendMessage(to, "เปิดลิ้งเรียบร้อย")
                elif text.lower() == 'ปิดลิ้ง':
                    if msg._from in Owner:
                        group = nadya.getGroup(to)
                        if group.preventedJoinByTicket == True:
                            nadya.sendMessage(to, "ปิดลิ้งเรียบร้อย")
                        else:
                            group.preventedJoinByTicket = True
                            nadya.updateGroup(group)
                            nadya.sendMessage(to, "ปิดลิ้งเรียบร้อย")
#-------------------------------------------------------------------------------
                elif msg.text in [".เปิดแทค"]:
                    settings['detectMention'] = True
                    nadya.sendMessage(msg.to,"Respon enabled.")
                
                elif msg.text in [".ปิดแทค"]:
                    settings['detectMention'] = False
                    nadya.sendMessage(msg.to,"Respon enabled.")

                elif msg.text in ["ตรวจสอบคำหยาบ"]:
                    settings["Aip"] = True
                    nadya.sendMessage(msg.to,"เปิดระบบตรวจสอบคำหยาบกับบอทบิน  ^ω^")

                elif msg.text in ["ปิดตรวจสอบคำหยาบ"]:
                    settings["Aip"] = False
                    nadya.sendMessage(msg.to,"ปิดระบบตรวจสอบคำหยาบกับบอทบินแล้วʕ•ﻌ•ʔ")

                elif msg.text in [".เปิดต้อนรับ"]:
                    settings["Wc"] = False
                    nadya.sendMessage(msg.to,"เปิดต้อนรับสมาชิกเข้ากลุ่มแล้ว")

                elif msg.text in [".ปิดต้อนรับ"]:
                    settings["Wc"] = False
                    nadya.sendMessage(msg.to,"ปิดต้อนรับสมาชิกเข้ากลุ่มแล้ว")
#==============================================================================#
                elif " .ปวดตับ" in msg.text:
                        if msg.toType == 2:
                         _name = msg.text.replace(" .ปวดตับ","")
                         gs = nadya.getGroup(receiver)
                         nadya.sendMessage(receiver,"ต้องรีบไปหาหมอ ô")
                         targets = []
                         for g in gs.members:
                             if _name in g.displayName:
                                 targets.append(g.mid)
                         if targets == []:
                             nadya.sendMessage(receiver,"Not found.")
                         else:
                             for target in targets:
                                 try:
                                     k = [nadya]
                                     random.choice(k).kickoutFromGroup(receiver,[target])
                                     print ((receiver,[g.mid]))
                                 except:
                                     nadya.sendMessage(receiver,"ไปก่อนนะ")
                                     print ("คลีนิค ปิดเรียบร้อย")


                elif msg.text in ["เตะแบน"]:
                  if msg._from in Owner:
                         group = nadya.getGroup(receiver)
                         gMembMids = [contact.mid for contact in group.members]
                         matched_list = []
                         for tag in settings["blacklist"]:
                             matched_list+=[str for str in gMembMids if str == tag]
                         if matched_list == []:
                             nadya.sendMessage(receiver,"❋ไม่พบคนติดแบนในกลุ่มนี้❋")
                         else:
                             for jj in matched_list:
                                 try:
                                     TuMz=[nadya]
                                     kicker=random.choice(TuMz)
                                     kicker.kickoutFromGroup(receiver,[jj])
                                     print((receiver,[jj]))
                                 except:
                                     nadya.sendMessage(receiver,"❋bye 👋 ")
                                     print ("Blacklist di Kick")
#==============================================================================#
                elif text.lower() == 'ข้อความเข้า':
                    nadya.sendMessage(msg.to, str(settings["welcome"]))
                elif text.lower() == 'มึงไปไหนมา':
                    nadya.sendMessage(msg.to, str(settings["oo"]))
                elif text.lower() == '001':
                    nadya.sendMessage(msg.to, str(settings["1"]))
                elif text.lower() == '002':
                    nadya.sendMessage(msg.to, str(settings["2"]))
                elif text.lower() == '003':
                    nadya.sendMessage(msg.to, str(settings["3"]))
                elif text.lower() == '004':
                    nadya.sendMessage(msg.to, str(settings["4"]))
                elif text.lower() == '9':
                    nadya.sendMessage(msg.to, str(settings["9"]))
                    nadya.sendContact(to, "u24d5f93f9113c991342c079005467e2f")
                elif text.lower() == 'hi':
                    nadya.sendMessage(msg.to, str(settings["hi"]))
                    nadya.sendContact(to, "u24d5f93f9113c991342c079005467e2f")
                elif text.lower() == '.รอบที่4':
                    nadya.sendMessage(msg.to, str(settings["ll"]))
                    nadya.sendContact(to, "u24d5f93f9113c991342c079005467e2f")
                elif text.lower() == '.รอบที่3':
                    nadya.sendMessage(msg.to, str(settings["mm"]))
                    nadya.sendContact(to, "u24d5f93f9113c991342c079005467e2f")
                elif text.lower() == '.รอบที่1':
                    nadya.sendMessage(msg.to, str(settings["vv"]))
                    nadya.sendContact(to, "u24d5f93f9113c991342c079005467e2f")
                elif text.lower() == '.รอบที่2':
                    nadya.sendMessage(msg.to, str(settings["nn"]))
                    nadya.sendContact(to, "u24d5f93f9113c991342c079005467e2f")

                elif 'h: ' in msg.text:
                  if msg._from in admin and Owner:
                     spl = msg.text.replace('h: ','')
                     if spl in [""," ","\n",None]:
                         nadya.sendMessage(msg.to, "❋ตั้งข้อความเรียบร้อยแล้ว❋")
                     else:
                          settings["คำสั่ง"] = spl
                          nadya.sendMessage(msg.to, "เรียบร้อย❋\n\n{}".format(str(spl)))
                elif 'w: ' in msg.text:
                  if msg._from in admin and Owner:
                     spl = msg.text.replace('w: ','')
                     if spl in [""," ","\n",None]:
                         nadya.sendMessage(msg.to, "❋ตั้งข้อความเรียบร้อยแล้ว❋")
                     else:
                          settings["welcome"] = spl
                          nadya.sendMessage(msg.to, "เรียบร้อย❋\n\n{}".format(str(spl)))
                elif '2: ' in msg.text:
                  if msg._from in admin and Owner:
                     spl = msg.text.replace('2: ','')
                     if spl in [""," ","\n",None]:
                         nadya.sendMessage(msg.to, "❋ตั้งข้อความเรียบร้อยแล้ว❋")
                     else:
                          settings["nn"] = spl
                          nadya.sendMessage(msg.to, "เรียบร้อย❋\n\n{}".format(str(spl)))
                elif 'hi: ' in msg.text:
                  if msg._from in admin and Owner:
                     spl = msg.text.replace('hi: ','')
                     if spl in [""," ","\n",None]:
                         nadya.sendMessage(msg.to, "❋ตั้งข้อความเรียบร้อยแล้ว❋")
                     else:
                          settings["hi"] = spl
                          nadya.sendMessage(msg.to, "เรียบร้อย❋\n\n{}".format(str(spl)))
                elif 'ex: ' in msg.text:
                  if msg._from in admin and Owner:
                     spl = msg.text.replace('ex: ','')
                     if spl in [""," ","\n",None]:
                         nadya.sendMessage(msg.to, "❋ตั้งข้อความเรียบร้อยแล้ว❋")
                     else:
                          settings["bye"] = spl
                          nadya.sendMessage(msg.to, "เรียบร้อย❋\n\n{}".format(str(spl)))
                elif 'cm: ' in msg.text:
                  if msg._from in admin and Owner:
                     spl = msg.text.replace('cm: ','')
                     if spl in [""," ","\n",None]:
                         nadya.sendMessage(msg.to, "❋ตั้งข้อความเรียบร้อยแล้ว❋")
                     else:
                          settings["comment"] = spl
                          nadya.sendMessage(msg.to, "เรียบร้อย❋\n\n{}".format(str(spl)))
#-------------------------------------------------------------------------------
                elif msg.text.lower().startswith("เพิ่มแอด "):
                    if msg._from in Owner:
                        key = eval(msg.contentMetadata["MENTION"])
                        key["MENTIONEES"][0]["M"]
                        targets = []
                        for x in key["MENTIONEES"]:
                            targets.append(x["M"])
                        for target in targets:
                            try:
                                Owner[target] = True
                                f=codecs.open('admin.json','w','utf-8')
                                json.dump(Owner, f, sort_keys=True, indent=4,ensure_ascii=False)
                                nadya.sendMessage(msg.to,"☢-Bot-☢\nจดจำ\nเรียบร้อยคับ")
                            except:
                                pass
                    else:
                        nadya.sendMessage(msg.to,"Owner Permission Required")

                elif msg.text.lower().startswith("ลบแอด "):
                    if msg._from in Owner:
                        key = eval(msg.contentMetadata["MENTION"])
                        key["MENTIONEES"][0]["M"]
                        targets = []
                        for x in key["MENTIONEES"]:
                            targets.append(x["M"])
                        for target in targets:
                            try:
                                del Owner[target]
                                f=codecs.open('admin.json','w','utf-8')
                                json.dump(Owner, f, sort_keys=True, indent=4,ensure_ascii=False)
                                nadya.sendMessage(msg.to,"☢-Bot-☢\nลบออก\nเรียบร้อย")
                            except:
                                pass
                    else:
                        nadya.sendMessage(msg.to,"Owner Permission Required")
#-------------------------------------------------------------------------------
#                elif msg.text.lower().startswith("เพิ่มแอด "):
 #                   if msg._from in Owner:
  #                      targets = []
   #                     key = eval(msg.contentMetadata["MENTION"])
    #                    key["MENTIONEES"][0]["M"]
     #                   for x in key["MENTIONEES"]:
      #                      targets.append(x["M"])
       #                 for target in targets:
        #                    try:
         #                       admin[target] = True
          #                      f=codecs.open('admin.json','w','utf-8')
           #                     json.dump(admin, f, sort_keys=True, indent=4,ensure_ascii=False)
            #                    nadya.sendMessage(msg.to,"Admin ☢-Bot-☢\nAdd\nExecuted")
             #                   break
              #              except:
               #                 nadya.sendMessage(msg.to,"Added Target Fail !")
                #                break
                 #   else:
                  #      nadya.sendMessage(msg.to,"Owner Permission Required")
#
 #               elif msg.text.lower().startswith("ลบแอด "):
  #                  if msg._from in Owner:
   #                     targets = []
    #                    key = eval(msg.contentMetadata["MENTION"])
     #                   key["MENTIONEES"][0]["M"]
      #                  for x in key["MENTIONEES"]:
       #                     targets.append(x["M"])
        #                for target in targets:
         #                   try:
          #                      del admin[target]
           #                     f=codecs.open('admin.json','w','utf-8')
            #                    json.dump(admin, f, sort_keys=True, indent=4,ensure_ascii=False)
             #                   nadya.sendMessage(msg.to,"☢-Bot-☢\nลบออก\nเรียบร้อย")
              #                  break
               #             except:
                #                nadya.sendMessage(msg.to,"Deleted Target Fail !")
                 #           break
                  #  else:
                   #     nadya.sendMessage(msg.to,"Owner Permission Required")
#-------------------------------------------------------------------------------
                elif text.lower() == 'เปิดระบบป้องกัน':
                    if msg._from in Owner:
                        settings["protect"] = True
                        settings["qrprotect"] = True
                        settings["inviteprotect"] = True
                        settings["cancelprotect"] = True
                        nadya.sendMessage(msg.to,"➲ All Protect Set To On")
                    else:
                        nadya.sendMessage(msg.to,"Just for Owner")
                        		            
                elif text.lower() == 'ปิดระบบป้องกัน':
                    if msg._from in Owner:
                        settings["protect"] = False
                        settings["qrprotect"] = False
                        settings["inviteprotect"] = False
                        settings["cancelprotect"] = False
                        nadya.sendMessage(msg.to,"➲ All Protect Set To Off")
                    else:
                        nadya.sendMessage(msg.to,"Just for Owner")
#-------------------------------------------------------------------------------
                elif text.lower() == 'autoadd on':
                    settings["autoadd"] = True
                    nadya.sendMessage(to, "Berhasil mengaktifkan Auto Add")
                elif text.lower() == 'autoadd off':
                    settings["autoAdd"] = False
                    nadya.sendMessage(to, "Berhasil menonaktifkan Auto Add")
                elif text.lower() == 'autojoin on':
                  if msg._from in Owner:    
                    settings["autoJoin"] = True
                    nadya.sendMessage(to, "Berhasil mengaktifkan Auto Join")
                elif text.lower() == 'autojoin off':
                  if msg._from in Owner:    
                    settings["autoJoin"] = False
                    nadya.sendMessage(to, "Berhasil menonaktifkan Auto Join")
                elif text.lower() == 'autoleave on':
                  if msg._from in Owner:
                    settings["autoLeave"] = True
                    nadya.sendMessage(to, "Berhasil mengaktifkan Auto Leave")
                elif text.lower() == 'autoleave off':
                  if msg._from in Owner:
                    settings["autoLeave"] = False
                    nadya.sendMessage(to, "Berhasil menonaktifkan Auto Leave")
                elif text.lower() == 'autoread on':
                    settings["autoRead"] = True
                    nadya.sendMessage(to, "Berhasil mengaktifkan Auto Read")
                elif text.lower() == 'autoread off':
                    settings["autoRead"] = False
                    nadya.sendMessage(to, "Berhasil menonaktifkan Auto Read")
                elif text.lower() == 'checksticker on':
                    settings["checkSticker"] = True
                    nadya.sendMessage(to, "Berhasil mengaktifkan Check Details Sticker")
                elif text.lower() == 'checksticker off':
                    settings["checkSticker"] = False
                    nadya.sendMessage(to, "Berhasil menonaktifkan Check Details Sticker")
                elif text.lower() == 'detectmention on':
                    settings["datectMention"] = True
                    nadya.sendMessage(to, "Berhasil mengaktifkan Detect Mention")
                elif text.lower() == 'detectmention off':
                    settings["datectMention"] = False
                    nadya.sendMessage(to, "Berhasil menonaktifkan Detect Mention")
                elif text.lower() == 'autojoinlink on':
                    settings["autoJoinTicket"] = True
                    nadya.sendMessage(to, "Berhasil mengaktifkan Auto Join Link")
                elif text.lower() == 'autojoinlink off':
                    settings["autoJoinTicket"] = False
                    nadya.sendMessage(to, "Berhasil menonaktifkan Auto Join Link")                    
#==============================================================================#
                elif text.lower() == "ทีม":
                    nadya.sendMessage(msg.to,responsename)
                    ki.sendMessage(msg.to,responsename2)
                    ki2.sendMessage(msg.to,responsename3)
                    ki3.sendMessage(msg.to,responsename4)
                    ki4.sendMessage(msg.to,responsename5)
                    
                elif msg.text.lower() == 'mybot':
                    if msg._from in Owner:
                        nadya.sendContact(to, nadyaMID)
                        ki.sendContact(to, kiMID)
                        ki2.sendContact(to, ki2MID)
                        ki3.sendContact(to, ki3MID)
                        ki4.sendContact(to, ki4MID)
                        
                elif text.lower() in ["ไปๆ"]:
                  if msg._from in Owner:    
                    ki.leaveGroup(msg.to)
                    ki2.leaveGroup(msg.to)
                    ki3.leaveGroup(msg.to)
                    ki4.leaveGroup(msg.to)
               
                elif text.lower() in ["มาๆ"]:
                  if msg._from in Owner:    
                    G = nadya.getGroup(msg.to)
                    ginfo = nadya.getGroup(msg.to)
                    G.preventedJoinByTicket = False
                    nadya.updateGroup(G)
                    invsend = 0
                    Ticket = nadya.reissueGroupTicket(msg.to)
                    ki.acceptGroupInvitationByTicket(msg.to,Ticket)
                    ki2.acceptGroupInvitationByTicket(msg.to,Ticket)
                    ki3.acceptGroupInvitationByTicket(msg.to,Ticket)
                    ki4.acceptGroupInvitationByTicket(msg.to,Ticket)
                    G = nadya.getGroup(msg.to)
                    G.preventedJoinByTicket = True
                    nadya.updateGroup(G)
                    G.preventedJoinByTicket(G)
                    nadya.updateGroup(G)
                
#==============================================================================#
                elif msg.text in ProtectMessage:
                    settings["Aip"] == True
                    random.choice(KAC).kickoutFromGroup(receiver,[sender])
                    nadya.sendMessage(msg.to,"ตรวจพบคำสั่งของบอทลบกลุ่ม\n           หรือ\n ตรวจพบคำพูดหยาบคายไม่สุภาพ\nจำเป็นต้องนำออกเพื่อความปลอดภัย\nและความสงบสุขของสมาชิก (｀・ω・´)")
#==============================================================================#
                elif msg.text in ["555","5555","55+","5","55555"]:
                    nadya.sendMessage(msg.to, "หัวเราะวันละนิดจิตแจ่มใส")
                    nadya.sendMessage(receiver, None, contentMetadata={'mid': sender}, contentType=13)
                elif text.lower() == 'me':
                    nadya.sendMessage(receiver, None, contentMetadata={'mid': sender}, contentType=13)
                elif msg.text in ("u9c1a8823e7b9605e031c9f7d39acaa4c"):
                    nadya.sendMessage(receiver, None, contentMetadata={'mid': sender}, contentType=13)
                elif text.lower() == 'mymid':
                    nadya.sendMessage(msg.to,"[MID]\n" +  nadyaMID)
                elif text.lower() == 'ชื่อ':
                    me = nadya.getContact(nadyaMID)
                    nadya.sendMessage(msg.to,"[DisplayName]\n" + me.displayName)
                elif text.lower() == 'สเตตัส':
                    me = nadya.getContact(nadyaMID)
                    nadya.sendMessage(msg.to,"[StatusMessage]\n" + me.statusMessage)
                elif text.lower() == 'รูป':
                    me = nadya.getContact(nadyaMID)
                    nadya.sendImageWithURL(msg.to,"http://dl.profile.line-cdn.net/" + me.pictureStatus)
                elif text.lower() == 'myvideoprofile':
                    me = nadya.getContact(nadyaMID)
                    nadya.sendVideoWithURL(msg.to,"http://dl.profile.line-cdn.net/" + me.pictureStatus + "/vp")
                elif text.lower() == 'mycover':
                    me = nadya.getContact(nadyaMID)
                    cover = nadya.getProfileCoverURL(nadyaMID)    
                    nadya.sendImageWithURL(msg.to, cover)
                elif msg.text.lower().startswith("stealcontact "):
                    if 'MENTION' in msg.contentMetadata.keys()!= None:
                        names = re.findall(r'@(\w+)', text)
                        mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                        mentionees = mention['MENTIONEES']
                        lists = []
                        for mention in mentionees:
                            if mention["M"] not in lists:
                                lists.append(mention["M"])
                        for ls in lists:
                            contact = nadya.getContact(ls)
                            mi_d = contact.mid
                            nadya.sendContact(msg.to, mi_d)
                elif msg.text.lower().startswith("stealmid "):
                    if 'MENTION' in msg.contentMetadata.keys()!= None:
                        names = re.findall(r'@(\w+)', text)
                        mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                        mentionees = mention['MENTIONEES']
                        lists = []
                        for mention in mentionees:
                            if mention["M"] not in lists:
                                lists.append(mention["M"])
                        ret_ = "[ Mid User ]"
                        for ls in lists:
                            ret_ += "\n{}" + ls
                        nadya.sendMessage(msg.to, str(ret_))
                elif msg.text.lower().startswith("stealname "):
                    if 'MENTION' in msg.contentMetadata.keys()!= None:
                        names = re.findall(r'@(\w+)', text)
                        mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                        mentionees = mention['MENTIONEES']
                        lists = []
                        for mention in mentionees:
                            if mention["M"] not in lists:
                                lists.append(mention["M"])
                        for ls in lists:
                            contact = nadya.getContact(ls)
                            nadya.sendMessage(msg.to, "[ Display Name ]\n" + contact.displayName)
                elif msg.text.lower().startswith("stealbio "):
                    if 'MENTION' in msg.contentMetadata.keys()!= None:
                        names = re.findall(r'@(\w+)', text)
                        mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                        mentionees = mention['MENTIONEES']
                        lists = []
                        for mention in mentionees:
                            if mention["M"] not in lists:
                                lists.append(mention["M"])
                        for ls in lists:
                            contact = nadya.getContact(ls)
                            nadya.sendMessage(msg.to, "[ Status Message ]\n{}" + contact.statusMessage)
                elif msg.text.lower().startswith("stealpicture "):
                    if 'MENTION' in msg.contentMetadata.keys()!= None:
                        names = re.findall(r'@(\w+)', text)
                        mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                        mentionees = mention['MENTIONEES']
                        lists = []
                        for mention in mentionees:
                            if mention["M"] not in lists:
                                lists.append(mention["M"])
                        for ls in lists:
                            path = "http://dl.profile.nadya.naver.jp/" + nadya.getContact(ls).pictureStatus
                            nadya.sendImageWithURL(msg.to, str(path))
                elif msg.text.lower().startswith("stealvideoprofile "):
                    if 'MENTION' in msg.contentMetadata.keys()!= None:
                        names = re.findall(r'@(\w+)', text)
                        mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                        mentionees = mention['MENTIONEES']
                        lists = []
                        for mention in mentionees:
                            if mention["M"] not in lists:
                                lists.append(mention["M"])
                        for ls in lists:
                            path = "http://dl.profile.nadya.naver.jp/" + nadya.getContact(ls).pictureStatus + "/vp"
                            nadya.sendImageWithURL(msg.to, str(path))
                elif msg.text.lower().startswith("stealcover "):
                    if line != None:
                        if 'MENTION' in msg.contentMetadata.keys()!= None:
                            names = re.findall(r'@(\w+)', text)
                            mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                            mentionees = mention['MENTIONEES']
                            lists = []
                            for mention in mentionees:
                                if mention["M"] not in lists:
                                    lists.append(mention["M"])
                            for ls in lists:
                                path = nadya.getProfileCoverURL(ls)
                                nadya.sendImageWithURL(msg.to, str(path))
                elif msg.text.lower().startswith("cloneprofile "):
                  if msg._from in Owner:    
                    if 'MENTION' in msg.contentMetadata.keys()!= None:
                        names = re.findall(r'@(\w+)', text)
                        mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                        mentionees = mention['MENTIONEES']
                        for mention in mentionees:
                            contact = mention["M"]
                            break
                        try:
                            nadya.cloneContactProfile(contact)
                            nadya.sendMessage(msg.to, "Berhasil clone member tunggu beberapa saat sampai profile berubah")
                        except:
                            nadya.sendMessage(msg.to, "Gagal clone member")
                elif text.lower() == 'restoreprofile':
                  if msg._from in Owner:    
                    try:
                        nadyaProfile.displayName = str(myProfile["displayName"])
                        nadyaProfile.statusMessage = str(myProfile["statusMessage"])
                        nadyaProfile.pictureStatus = str(myProfile["pictureStatus"])
                        nadya.updateProfileAttribute(8, nadyaProfile.pictureStatus)
                        nadya.updateProfile(nadyaProfile)
                        nadya.sendMessage(msg.to, "Berhasil restore profile tunggu beberapa saat sampai profile berubah")
                    except:
                        nadya.sendMessage(msg.to, "Gagal restore profile")
#==============================================================================#
                elif text.lower() == 'ผู้สร้างกลุ่ม':
                    group = nadya.getGroup(to)
                    GS = group.creator.mid
                    nadya.sendContact(to, GS)
                elif text.lower() == 'ไอดีกลุ่ม':
                    gid = nadya.getGroup(to)
                    nadya.sendMessage(to, "[ID Group : ]\n" + gid.id)
                elif text.lower() == 'รูปกลุ่ม':
                    group = nadya.getGroup(to)
                    path = "http://dl.profile.line-cdn.net/" + group.pictureStatus
                    nadya.sendImageWithURL(to, path)
                elif text.lower() == 'ชื่อกลุ่ม':
                    gid = nadya.getGroup(to)
                    nadya.sendMessage(to, "[ชื่อกลุ่มคือ : ]\n" + gid.name)
                elif text.lower() == 'groupticket':
                    if msg.toType == 2:
                        group = nadya.getGroup(to)
                        if group.preventedJoinByTicket == False:
                            ticket = nadya.reissueGroupTicket(to)
                            nadya.sendMessage(to, "[ Group Ticket ]\nhttps://line.me/R/ti/g/{}".format(str(ticket)))
                        else:
                            nadya.sendMessage(to, "Grup qr tidak terbuka silahkan buka terlebih dahulu dengan perintah {}openqr".format(str(settings["keyCommand"])))
                elif text.lower() == 'มุด':
                    if msg.toType == 2:
                        group = nadya.getGroup(to)
                        if group.preventedJoinByTicket == False:
                            nadya.sendMessage(to, "Grup qr sudah terbuka")
                        else:
                            group.preventedJoinByTicket = False
                            nadya.updateGroup(group)
                            nadya.sendMessage(to, "Berhasil membuka grup qr")
                elif text.lower() == '.ปิดมุด':
                    if msg.toType == 2:
                        group = nadya.getGroup(to)
                        if group.preventedJoinByTicket == True:
                            nadya.sendMessage(to, "Grup qr sudah tertutup")
                        else:
                            group.preventedJoinByTicket = True
                            nadya.updateGroup(group)
                            nadya.sendMessage(to, "Berhasil menutup grup qr")
                elif text.lower() == 'ข้อมูลกลุ่ม':
                    group = nadya.getGroup(to)
                    try:
                        gCreator = group.creator.displayName
                    except:
                        gCreator = "Tidak ditemukan"
                    if group.invitee is None:
                        gPending = "0"
                    else:
                        gPending = str(len(group.invitee))
                    if group.preventedJoinByTicket == True:
                        gQr = "Tertutup"
                        gTicket = "Tidak ada"
                    else:
                        gQr = "Terbuka"
                        gTicket = "https://line.me/R/ti/g/{}".format(str(nadya.reissueGroupTicket(group.id)))
                    path = "http://dl.profile.line-cdn.net/" + group.pictureStatus
                    ret_ = "╔══[ ข้อมูลกลุ่ม ]"
                    ret_ += "\n╠ ชื่อกลุ่ม : {}".format(str(group.name))
                    ret_ += "\n╠ ID Group : {}".format(group.id)
                    ret_ += "\n╠ ผู้สร้างกลุ่ม : {}".format(str(gCreator))
                    ret_ += "\n╠ จำนวนสมาชิก : {}".format(str(len(group.members)))
                    ret_ += "\n╠ Jumlah Pending : {}".format(gPending)
                    ret_ += "\n╠ Group Qr : {}".format(gQr)
                    ret_ += "\n╠ Group Ticket : {}".format(gTicket)
                    ret_ += "\n╚══[ 🔥Hack Scan 🔔Win🔔 ]"
                    nadya.sendMessage(to, str(ret_))
                    nadya.sendImageWithURL(to, path)
                elif text.lower() == 'สมาชิก':
                    if msg.toType == 2:
                        group = nadya.getGroup(to)
                        ret_ = "╔══[ รายชื่อสมาชิก ]"
                        no = 0 + 1
                        for mem in group.members:
                            ret_ += "\n╠ {}. {}".format(str(no), str(mem.displayName))
                            no += 1
                        ret_ += "\n╚══[ จำนวนทั้งหมด {} ]".format(str(len(group.members)))
                        nadya.sendMessage(to, str(ret_))
                elif text.lower() == '#glist':
                        groups = nadya.groups
                        ret_ = "╔══[ Group List ]"
                        no = 0 + 1
                        for gid in groups:
                            group = nadya.getGroup(gid)
                            ret_ += "\n╠ {}. {} | {}".format(str(no), str(group.name), str(len(group.members)))
                            no += 1
                        ret_ += "\n╚══[ ทั้งหมด {} กลุ่ม ]".format(str(len(groups)))
                        nadya.sendMessage(to, str(ret_))
#=======================================================================================
                elif msg.text.lower().startswith("bye "):
                    if msg._from in Owner:
                       targets = []
                       key = eval(msg.contentMetadata["MENTION"])
                       key["MENTIONEES"][0]["M"]
                       for x in key["MENTIONEES"]:
                           targets.append(x["M"])
                       for target in targets:
                           try:
                               random.choice(KAC).kickoutFromGroup(msg.to,[target])
                           except:
                               random.choice(KAC).sendMessage(msg.to,"Error")
#=======================================================================================
                elif text.lower() == 'ล้างบัญชีดำ':
                    if msg._from in Owner:
                        settings["blacklist"] = {}
                        nadya.sendMessage(msg.to,"Blacklist Dibersihkan")
    
                elif text.lower() == 'เพิ่มดำ':
                    if msg._from in Owner:
                        settings["wblacklist"] = True
                        nadya.sendMessage(msg.to,"Send Contact")
         
                elif msg.text in ["เพิ่มขาว"]:
                    if msg._from in Owner:
                        settings["dblacklist"] = True
                        nadya.sendMessage(msg.to,"Send Contact")
#-------------------------------------------------------------------------------
                elif msg.text.lower() == "ล้างเชิญ":
                    if msg.toType == 2:
                        group = nadya.getGroup(msg.to)
                        gMembMids = [contact.mid for contact in group.invitee]
                        for i in gMembMids:
                            random.choice(KAC).cancelGroupInvitation(msg.to,[i])
                elif msg.text in [".เชิญ"]:
                        settings["winvite"] = True
                        nadya.sendMessage(msg.to,"ส่งคอนแทคเพื่อเชิญได้เลยคับ")
#-------------------------------------------------------------------------------
                elif text.lower() == 'บัญชีดำ':
                    if msg._from in Owner:
                        if settings["blacklist"] == {}:
                            nadya.sendMessage(msg.to,"Tidak Ada Banlist")
                        else:
                            nadya.sendMessage(msg.to,"Daftar Banlist")
                            num=1
                            msgs="══════════List Blacklist═════════"
                            for mi_d in settings["blacklist"]:
                                msgs+="\n[%i] %s" % (num, nadya.getContact(mi_d).displayName)
                                num=(num+1)
                            msgs+="\n══════════List Blacklist═════════\n\nผู้ติดบัญชีดำทั้งหมด :  %i" % len(settings["blacklist"])
                            nadya.sendMessage(msg.to, msgs)
#=======================================================================================
                elif text.lower() == 'แอดมิน':
                    if msg._from in Owner:
                        if settings["Owner"] == {}:
                            nadya.sendMessage(msg.to,"กรุณาลองใหม่อีกครั้ง")
                        else:
                            nadya.sendMessage(msg.to,"กรุณารอสักครู่.......")
                            num=1
                            msgs="══════════🔥Hack Scan 🔔Win🔔 admin list═════════"
                            for mi_d in settings["Owner"]:
                                msgs+="\n[%i] %s" % (num, nadya.getContact(mi_d).displayName)
                                num=(num+1)
                            msgs+="\n══════════admin list By. 🔥Hack Scan 🔔Win🔔═════════\n\nจำนวนทั้งหมด :  %i" % len(settings["Owner"])
                            nadya.sendMessage(msg.to, msgs)
#=======================================================================================
                elif msg.text in ('/1','แทค'):
                    group = nadya.getGroup(msg.to)
                    nama = [contact.mid for contact in group.members]
                    k = len(nama)//20
                    for a in range(k+1):
                        txt = u''
                        s=0
                        b=[]
                        for i in group.members[a*20 : (a+1)*20]:
                            b.append({"S":str(s), "E" :str(s+6), "M":i.mid})
                            s += 7
                            txt += u'@Alin \n'
                        nadya.sendMessage(to, text=txt, contentMetadata={u'MENTION': json.dumps({'MENTIONEES':b})}, contentType=0)
                        nadya.sendMessage(receiver, "◀▷◀▷◀▷◀▷◀▷◀▷◀▷◀▷")
                    else:
                        nadya.sendMessage(to, "*ทั้งหมด {} คน*".format(str(len(nama))))          
#=======================================================================================
#=======================================================================================
                elif msg.text in ["ปฏิทิน","วัน","วันที่","วันนี้","วันอะไร","วันที่เท่าไร","ลืมวันที่","เวลา","30","กด30","กด 30"]:
                    tz = pytz.timezone("Asia/Jakarta")
                    timeNow = datetime.now(tz=tz)
                    day = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday","Friday", "Saturday"]
                    hari = ["วันอาทิตย์", "วันจันทร์", "วันอังคาร", "วันพุธ", "วันพฤหัสบดี", "วันศุกร์", "วันเสาร์"]
                    bulan = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
                    hr = timeNow.strftime("%A")
                    bln = timeNow.strftime("%m")
                    for i in range(len(day)):
                        if hr == day[i]: hasil = hari[i]
                    for k in range(0, len(bulan)):
                        if bln == str(k): bln = bulan[k-1]
                    readTime = "🌴ปฏิทินโดย 🔥Hack Scan 🔔Win🔔🌴\n\n🌿🌸🍃🌸🍃🌸🍃🌸🍃🌸🍃🌸🌿" + "\n\n🍁" + hasil + "\n🍁 ที่ " + timeNow.strftime('%d') + " - " + bln + " - " + timeNow.strftime('%Y')  + "\n🍁 เวลา :[ " + timeNow.strftime('%H:%M:%S') + " ]" + "🌿🌸🍃🌸🍃🌸🍃🌸🍃🌸🍃🌸🌿" + "\n\nBY: 🔥Hack Scan 🔔Win🔔➣ "
                    nadya.sendMessage(msg.to, readTime)
#=======================================================================================
                elif text.lower() == 'จับ':
                  if msg._from in Owner:
                    tz = pytz.timezone("Asia/Jakarta")
                    timeNow = datetime.now(tz=tz)
                    day = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday","Friday", "Saturday"]
                    hari = ["วันอาทิตย์", "วันจันทร์", "วันอังคาร", "วันพุธ", "วันพฤหัสบดี", "วันศุกร์", "วันเสาร์"]
                    bulan = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
                    hr = timeNow.strftime("%A")
                    bln = timeNow.strftime("%m")
                    for i in range(len(day)):
                        if hr == day[i]: hasil = hari[i]
                    for k in range(0, len(bulan)):
                        if bln == str(k): bln = bulan[k-1]
                    readTime = hasil + ", " + timeNow.strftime('%d') + " - " + bln + " - " + timeNow.strftime('%Y') + "\nเวลา  [ " + timeNow.strftime('%H:%M:%S') + " ]"
                    if msg.to in read['readPoint']:
                            try:
                                del read['readPoint'][msg.to]
                                del read['readMember'][msg.to]
                                del read['readTime'][msg.to]
                            except:
                                pass
                            read['readPoint'][msg.to] = msg.id
                            read['readMember'][msg.to] = ""
                            read['readTime'][msg.to] = datetime.now().strftime('%H:%M:%S')
                            read['ROM'][msg.to] = {}
                            with open('read.json', 'w') as fp:
                                json.dump(read, fp, sort_keys=True, indent=4)
                                nadya.sendMessage(msg.to,"กำลังนับคนอ่าน\n(｡◕‿◕｡)")
                    else:
                        try:
                            del read['readPoint'][msg.to]
                            del read['readMember'][msg.to]
                            del read['readTime'][msg.to]
                        except:
                            pass
                        read['readPoint'][msg.to] = msg.id
                        read['readMember'][msg.to] = ""
                        read['readTime'][msg.to] = datetime.now().strftime('%H:%M:%S')
                        read['ROM'][msg.to] = {}
                        with open('read.json', 'w') as fp:
                            json.dump(read, fp, sort_keys=True, indent=4)
                            nadya.sendMessage(msg.to, "เริ่มนับคนอ่าน\n(｡◕‿◕｡)\n" + readTime)
                            

                elif text.lower() == 'ใครอ่าน':
                  if msg._from in Owner:
                    tz = pytz.timezone("Asia/Jakarta")
                    timeNow = datetime.now(tz=tz)
                    day = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday","Friday", "Saturday"]
                    hari = ["วันอาทิตย์", "วันจันทร์", "วันอังคาร", "วันพุธ", "วันพฤหัสบดี", "วันศุกร์", "วันเสาร์"]
                    bulan = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
                    hr = timeNow.strftime("%A")
                    bln = timeNow.strftime("%m")
                    for i in range(len(day)):
                        if hr == day[i]: hasil = hari[i]
                    for k in range(0, len(bulan)):
                        if bln == str(k): bln = bulan[k-1]
                    readTime = hasil + ", " + timeNow.strftime('%d') + " - " + bln + " - " + timeNow.strftime('%Y') + "\nเวลา  [ " + timeNow.strftime('%H:%M:%S') + " ]"
                    if receiver in read['readPoint']:
                        if list(read["ROM"][receiver].items()) == []:
                            nadya.sendMessage(receiver,"รายชื่อคนที่อ่าน \nNone")
                        else:
                            chiya = []
                            for rom in list(read["ROM"][receiver].items()):
                                chiya.append(rom[1])
                            cmem = nadya.getContacts(chiya) 
                            zx = ""
                            zxc = ""
                            zx2 = []
                            xpesan = 'รายชื่อคนที่อ่าน \n'
                        for x in range(len(cmem)):
                            xname = str(cmem[x].displayName)
                            pesan = ''
                            pesan2 = pesan+"@c\n"
                            xlen = str(len(zxc)+len(xpesan))
                            xlen2 = str(len(zxc)+len(pesan2)+len(xpesan)-1)
                            zx = {'S':xlen, 'E':xlen2, 'M':cmem[x].mid}
                            zx2.append(zx)
                            zxc += pesan2
                        text = xpesan+ zxc + "\nเวลาที่อ่าน \n" + readTime
                        try:
                            nadya.sendMessage(receiver, text, contentMetadata={'MENTION':str('{"MENTIONEES":'+json.dumps(zx2).replace(' ','')+'}')}, contentType=0)
                        except Exception as error:
                            print (error)
                        pass
                    else:
                        nadya.sendMessage(receiver,"สั่ง (มอง) แล้วสั่ง (ไครอ่าน) \n(^人^")
#=======================================================================================
                elif msg.text.lower().startswith("แปลเสียง "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'th'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    nadya.sendAudio(msg.to,"hasil.mp3")
#==============================================================================#
                elif text.lower() == 'กลับมา':
                    ginvited = nadya.ginvited
                    if ginvited != [] and ginvited != None:
                        for gid in ginvited:
                            nadya.rejectGroupInvitation(gid)
                            nadya.sendMessage(to, "Berhasil tolak sebanyak {} undangan".format(str(len(ginvited))))
                    else:
                        nadya.sendMessage(to, "Tidak ada undangan yang tertunda")
                elif text.lower() == 'ล้างแชท':
                    nadya.removeAllMessages(op.param2)
                    nadya.sendMessage(to, "Berhasil hapus semua chat")

                elif text.lower() == 'time':
                    nadya.sendMessage(to, "Goblok cek sendiri di tanggal jangan manja")

                elif msg.text.lower().startswith("#gbc: "):
                    if msg._from in Owner:
                        sep = text.split(" ")
                        bc = text.replace(sep[0] + " ","")
                        saya = nadya.getGroupIdsJoined()
                        for group in saya:
                           ret_ = "{}".format(str(bc))
                           text = ret_ + ""
                           nadya.sendMessage(group, text)
                    
                elif msg.text.lower().startswith("gbc: "):   
                    sep = text.split(" ")
                    txt = text.replace(sep[0] + " ","")
                    groups = nadya.groups
                    for group in groups:
                        nadya.sendMessage(group, "[ Broadcast ]\n{}".format(str(txt)))
                        nadya.sendMessage(to, "ส่งแล้ว ทั้งหมด {} กลุ่ม".format(str(len(groups))))

                elif msg.text.lower().startswith("#fbc: "):   
                    sep = text.split(" ")
                    txt = text.replace(sep[0] + " ","")
                    friends = nadya.friends
                    for friend in friends:
                        nadya.sendMessage(friend, "[ Broadcast ]\n{}".format(str(txt)))
                        nadya.sendMessage(to, "Berhasil broadcast ke {} teman".format(str(len(friends))))
                elif msg.text.lower().startswith("#abc: "):   
                    sep = text.split(" ")
                    txt = text.replace(sep[0] + " ","")
                    friends = nadya.friends
                    groups = nadya.groups
                    for group in groups:
                        nadya.sendMessage(group, "[ Broadcast ]\n{}".format(str(txt)))
                        nadya.sendMessage(to, "Berhasil broadcast ke {} group".format(str(len(groups))))
                    for friend in friends:
                        nadya.sendMessage(friend, "[ Broadcast ]\n{}".format(str(txt)))
                        nadya.sendMessage(to, "Berhasil broadcast ke {} teman".format(str(len(friends))))                             
                                    
#===============================================================================[nadyaMID - kiMID]
        if op.type == 19:
            print ("[ 19 ] KICKOUT NADYA MESSAGE")
            try:
                if op.param3 in nadyaMID:
                    if op.param2 in kiMID:
                        G = ki.getGroup(op.param1)
#                        ginfo = ki.getGroup(op.param1)
                        G.preventedJoinByTicket = False
                        ki.updateGroup(G)
                        invsend = 0
                        Ticket = ki.reissueGroupTicket(op.param1)
                        nadya.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G = ki.getGroup(op.param1)
                        G.preventedJoinByTicket = True
                        ki.updateGroup(G)
                        G.preventedJoinByTicket(G)
                        ki.updateGroup(G)
                    else:
                        G = ki.getGroup(op.param1)
#                        ginfo = ki.getGroup(op.param1)
                        ki.kickoutFromGroup(op.param1,[op.param2])
                        G.preventedJoinByTicket = False
                        ki.updateGroup(G)
                        invsend = 0
                        Ticket = ki.reissueGroupTicket(op.param1)
                        nadya.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G = ki.getGroup(op.param1)
                        G.preventedJoinByTicket = True
                        ki.updateGroup(G)
                        G.preventedJoinByTicket(G)
                        ki.updateGroup(G)
                        settings["blacklist"][op.param2] = True
#-------------------------------------------------------------------------------[nadyaMID - ki2MID]
                elif op.param3 in nadyaMID:
                    if op.param2 in ki2MID:
                        G = ki2.getGroup(op.param1)
#                        ginfo = ki2.getGroup(op.param1)
                        G.preventedJoinByTicket = False
                        ki2.updateGroup(G)
                        invsend = 0
                        Ticket = ki2.reissueGroupTicket(op.param1)
                        nadya.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G = ki2.getGroup(op.param1)
                        G.preventedJoinByTicket = True
                        ki2.updateGroup(G)
                        G.preventedJoinByTicket(G)
                        ki2.updateGroup(G)
                    else:
                        G = ki2.getGroup(op.param1)
#                        ginfo = ki2.getGroup(op.param1)
                        ki2.kickoutFromGroup(op.param1,[op.param2])
                        G.preventedJoinByTicket = False
                        ki2.updateGroup(G)
                        invsend = 0
                        Ticket = ki2.reissueGroupTicket(op.param1)
                        nadya.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G = ki2.getGroup(op.param1)
                        G.preventedJoinByTicket = True
                        ki2.updateGroup(G)
                        G.preventedJoinByTicket(G)
                        ki2.updateGroup(G)
                        settings["blacklist"][op.param2] = True
#-------------------------------------------------------------------------------[nadyaMID - ki3MID]
                elif op.param3 in nadyaMID:
                    if op.param2 in ki3MID:
                        G = ki3.getGroup(op.param1)
#                        ginfo = ki3.getGroup(op.param1)
                        G.preventedJoinByTicket = False
                        ki3.updateGroup(G)
                        invsend = 0
                        Ticket = ki3.reissueGroupTicket(op.param1)
                        nadya.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G = ki3.getGroup(op.param1)
                        G.preventedJoinByTicket = True
                        ki3.updateGroup(G)
                        G.preventedJoinByTicket(G)
                        ki3.updateGroup(G)
                    else:
                        G = ki3.getGroup(op.param1)
#                        ginfo = ki3.getGroup(op.param1)
                        ki3.kickoutFromGroup(op.param1,[op.param2])
                        G.preventedJoinByTicket = False
                        ki3.updateGroup(G)
                        invsend = 0
                        Ticket = ki3.reissueGroupTicket(op.param1)
                        nadya.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G = ki3.getGroup(op.param1)
                        G.preventedJoinByTicket = True
                        ki3.updateGroup(G)
                        G.preventedJoinByTicket(G)
                        ki3.updateGroup(G)
                        settings["blacklist"][op.param2] = True
#-------------------------------------------------------------------------------[nadyaMID - ki4MID]
                elif op.param3 in nadyaMID:
                    if op.param2 in ki4MID:
                        G = ki4.getGroup(op.param1)
#                        ginfo = ki4.getGroup(op.param1)
                        G.preventedJoinByTicket = False
                        ki4.updateGroup(G)
                        invsend = 0
                        Ticket = ki4.reissueGroupTicket(op.param1)
                        nadya.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G = ki4.getGroup(op.param1)
                        G.preventedJoinByTicket = True
                        ki4.updateGroup(G)
                        G.preventedJoinByTicket(G)
                        ki4.updateGroup(G)
                    else:
                        G = ki4.getGroup(op.param1)
#                        ginfo = ki4.getGroup(op.param1)
                        ki4.kickoutFromGroup(op.param1,[op.param2])
                        G.preventedJoinByTicket = False
                        ki4.updateGroup(G)
                        invsend = 0
                        Ticket = ki4.reissueGroupTicket(op.param1)
                        nadya.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G = ki4.getGroup(op.param1)
                        G.preventedJoinByTicket = True
                        ki4.updateGroup(G)
                        G.preventedJoinByTicket(G)
                        ki4.updateGroup(G)
                        settings["blacklist"][op.param2] = True
#===============================================================================[kiMID nadyaMID]
                if op.param3 in kiMID:
                    if op.param2 in nadyaMID:
                        G = nadya.getGroup(op.param1)
#                        ginfo = nadya.getGroup(op.param1)
                        G.preventedJoinByTicket = False
                        nadya.updateGroup(G)
                        invsend = 0
                        Ticket = nadya.reissueGroupTicket(op.param1)
                        nadya.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G = nadya.getGroup(op.param1)
                        G.preventedJoinByTicket = True
                        nadya.updateGroup(G)
                        G.preventedJoinByTicket(G)
                        nadya.updateGroup(G)
                    else:
                        G = nadya.getGroup(op.param1)
#                        ginfo = nadya.getGroup(op.param1)
                        nadya.kickoutFromGroup(op.param1,[op.param2])
                        G.preventedJoinByTicket = False
                        nadya.updateGroup(G)
                        invsend = 0
                        Ticket = nadya.reissueGroupTicket(op.param1)
                        nadya.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G = nadya.getGroup(op.param1)
                        G.preventedJoinByTicket = True
                        nadya.updateGroup(G)
                        G.preventedJoinByTicket(G)
                        nadya.updateGroup(G)
                        settings["blacklist"][op.param2] = True
#-------------------------------------------------------------------------------[kiMID ki2MID]
                elif op.param3 in kiMID:
                    if op.param2 in ki2MID:
                        G = ki2.getGroup(op.param1)
#                        ginfo = ki2.getGroup(op.param1)
                        G.preventedJoinByTicket = False
                        ki2.updateGroup(G)
                        invsend = 0
                        Ticket = ki2.reissueGroupTicket(op.param1)
                        nadya.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G = ki2.getGroup(op.param1)
                        G.preventedJoinByTicket = True
                        ki2.updateGroup(G)
                        G.preventedJoinByTicket(G)
                        ki2.updateGroup(G)
                    else:
                        G = ki2.getGroup(op.param1)
#                        ginfo = ki2.getGroup(op.param1)
                        ki2.kickoutFromGroup(op.param1,[op.param2])
                        G.preventedJoinByTicket = False
                        ki2.updateGroup(G)
                        invsend = 0
                        Ticket = ki2.reissueGroupTicket(op.param1)
                        nadya.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G = ki2.getGroup(op.param1)
                        G.preventedJoinByTicket = True
                        ki2.updateGroup(G)
                        G.preventedJoinByTicket(G)
                        ki2.updateGroup(G)
                        settings["blacklist"][op.param2] = True
#-------------------------------------------------------------------------------[kiMID ki3MID]
                elif op.param3 in kiMID:
                    if op.param2 in ki3MID:
                        G = ki3.getGroup(op.param1)
#                        ginfo = ki3.getGroup(op.param1)
                        G.preventedJoinByTicket = False
                        ki3.updateGroup(G)
                        invsend = 0
                        Ticket = ki3.reissueGroupTicket(op.param1)
                        nadya.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G = ki3.getGroup(op.param1)
                        G.preventedJoinByTicket = True
                        ki3.updateGroup(G)
                        G.preventedJoinByTicket(G)
                        ki3.updateGroup(G)
                    else:
                        G = ki3.getGroup(op.param1)
#                        ginfo = ki3.getGroup(op.param1)
                        ki3.kickoutFromGroup(op.param1,[op.param2])
                        G.preventedJoinByTicket = False
                        ki3.updateGroup(G)
                        invsend = 0
                        Ticket = ki3.reissueGroupTicket(op.param1)
                        nadya.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G = ki3.getGroup(op.param1)
                        G.preventedJoinByTicket = True
                        ki3.updateGroup(G)
                        G.preventedJoinByTicket(G)
                        ki3.updateGroup(G)
                        settings["blacklist"][op.param2] = True
#-------------------------------------------------------------------------------[kiMID ki4MID]
                elif op.param3 in kiMID:
                    if op.param2 in ki4MID:
                        G = ki4.getGroup(op.param1)
#                        ginfo = ki4.getGroup(op.param1)
                        G.preventedJoinByTicket = False
                        ki4.updateGroup(G)
                        invsend = 0
                        Ticket = ki4.reissueGroupTicket(op.param1)
                        nadya.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G = ki4.getGroup(op.param1)
                        G.preventedJoinByTicket = True
                        ki4.updateGroup(G)
                        G.preventedJoinByTicket(G)
                        ki4.updateGroup(G)
                    else:
                        G = ki4.getGroup(op.param1)
#                        ginfo = ki4.getGroup(op.param1)
                        ki4.kickoutFromGroup(op.param1,[op.param2])
                        G.preventedJoinByTicket = False
                        ki4.updateGroup(G)
                        invsend = 0
                        Ticket = ki4.reissueGroupTicket(op.param1)
                        nadya.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G = ki4.getGroup(op.param1)
                        G.preventedJoinByTicket = True
                        ki4.updateGroup(G)
                        G.preventedJoinByTicket(G)
                        ki4.updateGroup(G)
                        settings["blacklist"][op.param2] = True
#===============================================================================[ki2MID nadyaMID]
                if op.param3 in ki2MID:
                    if op.param2 in nadyaMID:
                        G = nadya.getGroup(op.param1)
#                        ginfo = nadya.getGroup(op.param1)
                        G.preventedJoinByTicket = False
                        nadya.updateGroup(G)
                        invsend = 0
                        Ticket = nadya.reissueGroupTicket(op.param1)
                        nadya.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G = nadya.getGroup(op.param1)
                        G.preventedJoinByTicket = True
                        nadya.updateGroup(G)
                        G.preventedJoinByTicket(G)
                        nadya.updateGroup(G)
                    else:
                        G = nadya.getGroup(op.param1)
#                        ginfo = nadya.getGroup(op.param1)
                        nadya.kickoutFromGroup(op.param1,[op.param2])
                        G.preventedJoinByTicket = False
                        nadya.updateGroup(G)
                        invsend = 0
                        Ticket = nadya.reissueGroupTicket(op.param1)
                        nadya.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G = nadya.getGroup(op.param1)
                        G.preventedJoinByTicket = True
                        nadya.updateGroup(G)
                        G.preventedJoinByTicket(G)
                        nadya.updateGroup(G)
                        settings["blacklist"][op.param2] = True
#-------------------------------------------------------------------------------[ki2MID kiMID]
                elif op.param3 in ki2MID:
                    if op.param2 in kiMID:
                        G = ki.getGroup(op.param1)
#                        ginfo = ki.getGroup(op.param1)
                        G.preventedJoinByTicket = False
                        ki.updateGroup(G)
                        invsend = 0
                        Ticket = ki.reissueGroupTicket(op.param1)
                        nadya.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G = ki.getGroup(op.param1)
                        G.preventedJoinByTicket = True
                        ki.updateGroup(G)
                        G.preventedJoinByTicket(G)
                        ki.updateGroup(G)
                    else:
                        G = ki.getGroup(op.param1)
#                        ginfo = ki.getGroup(op.param1)
                        ki.kickoutFromGroup(op.param1,[op.param2])
                        G.preventedJoinByTicket = False
                        ki.updateGroup(G)
                        invsend = 0
                        Ticket = ki.reissueGroupTicket(op.param1)
                        nadya.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G = ki.getGroup(op.param1)
                        G.preventedJoinByTicket = True
                        ki.updateGroup(G)
                        G.preventedJoinByTicket(G)
                        ki.updateGroup(G)
                        settings["blacklist"][op.param2] = True
#-------------------------------------------------------------------------------[ki2MID ki3MID]
                elif op.param3 in ki2MID:
                    if op.param2 in ki3MID:
                        G = ki3.getGroup(op.param1)
#                        ginfo = ki3.getGroup(op.param1)
                        G.preventedJoinByTicket = False
                        ki3.updateGroup(G)
                        invsend = 0
                        Ticket = ki3.reissueGroupTicket(op.param1)
                        nadya.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G = ki3.getGroup(op.param1)
                        G.preventedJoinByTicket = True
                        ki3.updateGroup(G)
                        G.preventedJoinByTicket(G)
                        ki3.updateGroup(G)
                    else:
                        G = ki3.getGroup(op.param1)
#                        ginfo = ki3.getGroup(op.param1)
                        ki3.kickoutFromGroup(op.param1,[op.param2])
                        G.preventedJoinByTicket = False
                        ki3.updateGroup(G)
                        invsend = 0
                        Ticket = ki3.reissueGroupTicket(op.param1)
                        nadya.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G = ki3.getGroup(op.param1)
                        G.preventedJoinByTicket = True
                        ki3.updateGroup(G)
                        G.preventedJoinByTicket(G)
                        ki3.updateGroup(G)
                        settings["blacklist"][op.param2] = True
#-------------------------------------------------------------------------------[ki2MID ki4MID]
                elif op.param3 in ki2MID:
                    if op.param2 in ki4MID:
                        G = ki4.getGroup(op.param1)
#                        ginfo = ki4.getGroup(op.param1)
                        G.preventedJoinByTicket = False
                        ki4.updateGroup(G)
                        invsend = 0
                        Ticket = ki4.reissueGroupTicket(op.param1)
                        nadya.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G = ki4.getGroup(op.param1)
                        G.preventedJoinByTicket = True
                        ki4.updateGroup(G)
                        G.preventedJoinByTicket(G)
                        ki4.updateGroup(G)
                    else:
                        G = ki4.getGroup(op.param1)
#                        ginfo = ki4.getGroup(op.param1)
                        ki4.kickoutFromGroup(op.param1,[op.param2])
                        G.preventedJoinByTicket = False
                        ki4.updateGroup(G)
                        invsend = 0
                        Ticket = ki4.reissueGroupTicket(op.param1)
                        nadya.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G = ki4.getGroup(op.param1)
                        G.preventedJoinByTicket = True
                        ki4.updateGroup(G)
                        G.preventedJoinByTicket(G)
                        ki4.updateGroup(G)
                        settings["blacklist"][op.param2] = True
#===============================================================================[ki3MID nadyaMID]
                if op.param3 in ki3MID:
                    if op.param2 in nadyaMID:
                        G = nadya.getGroup(op.param1)
#                        ginfo = nadya.getGroup(op.param1)
                        G.preventedJoinByTicket = False
                        nadya.updateGroup(G)
                        invsend = 0
                        Ticket = nadya.reissueGroupTicket(op.param1)
                        nadya.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G = nadya.getGroup(op.param1)
                        G.preventedJoinByTicket = True
                        nadya.updateGroup(G)
                        G.preventedJoinByTicket(G)
                        nadya.updateGroup(G)
                    else:
                        G = nadya.getGroup(op.param1)
#                        ginfo = nadya.getGroup(op.param1)
                        nadya.kickoutFromGroup(op.param1,[op.param2])
                        G.preventedJoinByTicket = False
                        nadya.updateGroup(G)
                        invsend = 0
                        Ticket = nadya.reissueGroupTicket(op.param1)
                        nadya.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G = nadya.getGroup(op.param1)
                        G.preventedJoinByTicket = True
                        nadya.updateGroup(G)
                        G.preventedJoinByTicket(G)
                        nadya.updateGroup(G)
                        settings["blacklist"][op.param2] = True
#-------------------------------------------------------------------------------[ki3MID kiMID]
                elif op.param3 in ki3MID:
                    if op.param2 in kiMID:
                        G = ki.getGroup(op.param1)
#                        ginfo = ki.getGroup(op.param1)
                        G.preventedJoinByTicket = False
                        ki.updateGroup(G)
                        invsend = 0
                        Ticket = ki.reissueGroupTicket(op.param1)
                        nadya.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G = ki.getGroup(op.param1)
                        G.preventedJoinByTicket = True
                        ki.updateGroup(G)
                        G.preventedJoinByTicket(G)
                        ki.updateGroup(G)
                    else:
                        G = ki.getGroup(op.param1)
#                        ginfo = ki.getGroup(op.param1)
                        ki.kickoutFromGroup(op.param1,[op.param2])
                        G.preventedJoinByTicket = False
                        ki.updateGroup(G)
                        invsend = 0
                        Ticket = ki.reissueGroupTicket(op.param1)
                        nadya.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G = ki.getGroup(op.param1)
                        G.preventedJoinByTicket = True
                        ki.updateGroup(G)
                        G.preventedJoinByTicket(G)
                        ki.updateGroup(G)
                        settings["blacklist"][op.param2] = True
#-------------------------------------------------------------------------------[ki3MID ki2MID]
                elif op.param3 in ki3MID:
                    if op.param2 in ki2MID:
                        G = ki2.getGroup(op.param1)
#                        ginfo = ki2.getGroup(op.param1)
                        G.preventedJoinByTicket = False
                        ki2.updateGroup(G)
                        invsend = 0
                        Ticket = ki2.reissueGroupTicket(op.param1)
                        nadya.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G = ki2.getGroup(op.param1)
                        G.preventedJoinByTicket = True
                        ki2.updateGroup(G)
                        G.preventedJoinByTicket(G)
                        ki2.updateGroup(G)
                    else:
                        G = ki2.getGroup(op.param1)
#                        ginfo = ki2.getGroup(op.param1)
                        ki2.kickoutFromGroup(op.param1,[op.param2])
                        G.preventedJoinByTicket = False
                        ki2.updateGroup(G)
                        invsend = 0
                        Ticket = ki2.reissueGroupTicket(op.param1)
                        nadya.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G = ki2.getGroup(op.param1)
                        G.preventedJoinByTicket = True
                        ki2.updateGroup(G)
                        G.preventedJoinByTicket(G)
                        ki2.updateGroup(G)
                        settings["blacklist"][op.param2] = True
#-------------------------------------------------------------------------------[ki3MID ki4MID]
                elif op.param3 in ki3MID:
                    if op.param2 in ki4MID:
                        G = ki4.getGroup(op.param1)
#                        ginfo = ki4.getGroup(op.param1)
                        G.preventedJoinByTicket = False
                        ki4.updateGroup(G)
                        invsend = 0
                        Ticket = ki4.reissueGroupTicket(op.param1)
                        nadya.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G = ki4.getGroup(op.param1)
                        G.preventedJoinByTicket = True
                        ki4.updateGroup(G)
                        G.preventedJoinByTicket(G)
                        ki4.updateGroup(G)
                    else:
                        G = ki4.getGroup(op.param1)
#                        ginfo = ki4.getGroup(op.param1)
                        ki4.kickoutFromGroup(op.param1,[op.param2])
                        G.preventedJoinByTicket = False
                        ki4.updateGroup(G)
                        invsend = 0
                        Ticket = ki4.reissueGroupTicket(op.param1)
                        nadya.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G = ki4.getGroup(op.param1)
                        G.preventedJoinByTicket = True
                        ki4.updateGroup(G)
                        G.preventedJoinByTicket(G)
                        ki4.updateGroup(G)
                        settings["blacklist"][op.param2] = True
#===============================================================================[ki4MID nadyaMID]
                if op.param3 in ki4MID:
                    if op.param2 in nadyaMID:
                        G = nadya.getGroup(op.param1)
#                        ginfo = nadya.getGroup(op.param1)
                        G.preventedJoinByTicket = False
                        nadya.updateGroup(G)
                        invsend = 0
                        Ticket = nadya.reissueGroupTicket(op.param1)
                        nadya.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G = nadya.getGroup(op.param1)
                        G.preventedJoinByTicket = True
                        nadya.updateGroup(G)
                        G.preventedJoinByTicket(G)
                        nadya.updateGroup(G)
                    else:
                        G = nadya.getGroup(op.param1)
#                        ginfo = nadya.getGroup(op.param1)
                        nadya.kickoutFromGroup(op.param1,[op.param2])
                        G.preventedJoinByTicket = False
                        nadya.updateGroup(G)
                        invsend = 0
                        Ticket = nadya.reissueGroupTicket(op.param1)
                        nadya.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G = nadya.getGroup(op.param1)
                        G.preventedJoinByTicket = True
                        nadya.updateGroup(G)
                        G.preventedJoinByTicket(G)
                        nadya.updateGroup(G)
                        settings["blacklist"][op.param2] = True
#-------------------------------------------------------------------------------[ki4MID kiMID]
                elif op.param3 in ki4MID:
                    if op.param2 in kiMID:
                        G = ki.getGroup(op.param1)
#                        ginfo = ki.getGroup(op.param1)
                        G.preventedJoinByTicket = False
                        ki.updateGroup(G)
                        invsend = 0
                        Ticket = ki.reissueGroupTicket(op.param1)
                        nadya.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G = ki.getGroup(op.param1)
                        G.preventedJoinByTicket = True
                        ki.updateGroup(G)
                        G.preventedJoinByTicket(G)
                        ki.updateGroup(G)
                    else:
                        G = ki.getGroup(op.param1)
#                        ginfo = ki.getGroup(op.param1)
                        ki.kickoutFromGroup(op.param1,[op.param2])
                        G.preventedJoinByTicket = False
                        ki.updateGroup(G)
                        invsend = 0
                        Ticket = ki.reissueGroupTicket(op.param1)
                        nadya.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G = ki.getGroup(op.param1)
                        G.preventedJoinByTicket = True
                        ki.updateGroup(G)
                        G.preventedJoinByTicket(G)
                        ki.updateGroup(G)
                        settings["blacklist"][op.param2] = True
#-------------------------------------------------------------------------------[ki4MID ki2MID]
                elif op.param3 in ki4MID:
                    if op.param2 in ki2MID:
                        G = ki2.getGroup(op.param1)
#                        ginfo = ki2.getGroup(op.param1)
                        G.preventedJoinByTicket = False
                        ki2.updateGroup(G)
                        invsend = 0
                        Ticket = ki2.reissueGroupTicket(op.param1)
                        nadya.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G = ki2.getGroup(op.param1)
                        G.preventedJoinByTicket = True
                        ki2.updateGroup(G)
                        G.preventedJoinByTicket(G)
                        ki2.updateGroup(G)
                    else:
                        G = ki2.getGroup(op.param1)
#                        ginfo = ki2.getGroup(op.param1)
                        ki2.kickoutFromGroup(op.param1,[op.param2])
                        G.preventedJoinByTicket = False
                        ki2.updateGroup(G)
                        invsend = 0
                        Ticket = ki2.reissueGroupTicket(op.param1)
                        nadya.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G = ki2.getGroup(op.param1)
                        G.preventedJoinByTicket = True
                        ki2.updateGroup(G)
                        G.preventedJoinByTicket(G)
                        ki2.updateGroup(G)
                        settings["blacklist"][op.param2] = True
#-------------------------------------------------------------------------------[ki4MID ki3MID]
                elif op.param3 in ki4MID:
                    if op.param2 in ki3MID:
                        G = ki3.getGroup(op.param1)
#                        ginfo = ki3.getGroup(op.param1)
                        G.preventedJoinByTicket = False
                        ki3.updateGroup(G)
                        invsend = 0
                        Ticket = ki3.reissueGroupTicket(op.param1)
                        nadya.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G = ki3.getGroup(op.param1)
                        G.preventedJoinByTicket = True
                        ki3.updateGroup(G)
                        G.preventedJoinByTicket(G)
                        ki3.updateGroup(G)
                    else:
                        G = ki3.getGroup(op.param1)
#                        ginfo = ki3.getGroup(op.param1)
                        ki3.kickoutFromGroup(op.param1,[op.param2])
                        G.preventedJoinByTicket = False
                        ki3.updateGroup(G)
                        invsend = 0
                        Ticket = ki3.reissueGroupTicket(op.param1)
                        nadya.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G = ki3.getGroup(op.param1)
                        G.preventedJoinByTicket = True
                        ki3.updateGroup(G)
                        G.preventedJoinByTicket(G)
                        ki3.updateGroup(G)
                        settings["blacklist"][op.param2] = True
                        
                elif op.param2 not in Bots:
                    if op.param2 in admin:
                        pass
                    elif settings["protect"] == True:
                        settings["blacklist"][op.param2] = True
                        random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                        random.choice(KAC).inviteIntoGroup(op.param1,[op.param3])
                        random.choice(KAC).sendMessage(op.param1,"Don't Play bro...!")
                        
                else:
                    pass
            except:
                pass
#==============================================================================#
        if op.type == 13:
            if op.param2 not in Bots:
                if op.param2 in admin:
                    pass
                elif settings["inviteprotect"] == True:
                    settings["blacklist"][op.param2] = True
                    random.choice(KAC).cancelGroupInvitation(op.param1,[op.param3])
                    random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                    if op.param2 not in Bots:
                        if op.param2 in admin:
                            pass
                        elif settings["cancelprotect"] == True:
                            settings["blacklist"][op.param2] = True
                            random.choice(KAC).cancelGroupInvitation(op.param1,[op.param3])	
#-------------------------------------------------------------------------------
        if op.type == 11:
            if op.param2 not in Bots:
                if op.param2 in admin and Bots and Owner:
                    pass
                elif settings["qrprotect"] == True:
                    settings["blacklist"][op.param2] = True
                    G = ki.getGroup(op.param1)
                    G.preventedJoinByTicket = True
                    ki.updateGroup(G)
                    random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                else:
                    nadya.sendMessage(op.param1,"Qr under protect")
            else:
                nadya.sendMessage(op.param1,"")
#==============================================================================#
#==============================================================================#
        if op.type == 26:
            msg = op.message
            text = msg.text
            msg_id = msg.id
            receiver = msg.to
            sender = msg._from
            if msg.toType == 0:
                if sender != nadya.profile.mid:
                    to = sender
                else:
                    to = receiver
            else:
                to = receiver
                if settings["autoRead"] == True:
                    nadya.sendChatChecked(to, msg_id)
                if to in read["readPoint"]:
                    if sender not in read["ROM"][to]:
                        read["ROM"][to][sender] = True
                if sender in settings["mimic"]["target"] and settings["mimic"]["status"] == True and settings["mimic"]["target"][sender] == True:
                    text = msg.text
                    if text is not None:
                        nadya.sendMessage(msg.to,text)
                if msg.contentType == 0 and sender not in nadyaMID and msg.toType == 2:
                    if 'MENTION' in msg.contentMetadata.keys()!= None:
                        names = re.findall(r'@(\w+)', text)
                        mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                        mentionees = mention['MENTIONEES']
                        lists = []
                        for mention in mentionees:
                            if nadyaMID in mention["M"]:
                                if settings["detectMention"] == True:
                                    contact = nadya.getContact(sender)
                                    nadya.sendMessage(to, "       **-™ระบบตอบอัตโนมัติ™-**\n\n      แทคมาทัก....หรือแทคมารักจ๊ะ\n\n            「™Auto Respon」 ")
                                    sendMessageWithMention(to, contact.mid)
                                    nadya.sendContact(to, contact.mid)
                                    break
                if msg.contentType == 0:
                    if text is None:
                        return
                    if "/ti/g/" in msg.text.lower():
                        if settings["autoJoinTicket"] == True:
                            link_re = re.compile('(?:line\:\/|line\.me\/R)\/ti\/g\/([a-zA-Z0-9_-]+)?')
                            links = link_re.findall(text)
                            n_links = []
                            for l in links:
                                if l not in n_links:
                                    n_links.append(l)
                            for ticket_id in n_links:
                                group = nadya.findGroupByTicket(ticket_id)
                                nadya.acceptGroupInvitationByTicket(group.id,ticket_id)
                                nadya.sendMessage(to, "มุดลิ้งเข้าไปในกลุ่ม👉 %s 👈 เรียบร้อยแล้ว" % str(group.name))
                                break
                        
        if op.type == 55:
            print ("[ 🔥Hack Scan 🔔Win🔔 ]")
#            print ("[💕ตรวจพบคำสั่ง💞]")
            if op.param1 in read["readPoint"]:
                _name = nadya.getContact(op.param2).displayName
                tz = pytz.timezone("Asia/Jakarta")
                timeNow = datetime.now(tz=tz)
                timeHours = datetime.strftime(timeNow," (%H:%M)")
                read["readMember"][op.param1][op.param2] = str(_name) + str(timeHours)
        backupData()
    except Exception as error:
        logError(error)
#==============================================================================#
# Auto join if BOT invited to group
def NOTIFIED_INVITE_INTO_GROUP(op):
    try:
        nadya.acceptGroupInvitation(op.param1)
        ki.acceptGroupInvitation(op.param1)
        ki2.acceptGroupInvitation(op.param1)
        ki3.acceptGroupInvitation(op.param1)
        ki4.acceptGroupInvitation(op.param1)
    except Exception as e:
        nadya.log("[NOTIFIED_INVITE_INTO_GROUP] ERROR : " + str(e))
# Auto kick if BOT out to group
def NOTIFIED_KICKOUT_TO_GROUP(op):
    try:
        if op.param2 not in Bots:
            random.choice(KAC).kickoutFromGroup(op.param1,op.param2)
        else:
            pass
    except Exception as e:
        nadya.log("[NOTIFIED_KICKOUT_TO_GROUP] ERROR : " + str(e))

while True:
    try:
        ops = oepoll.singleTrace(count=50)
        if ops is not None:
            for op in ops:
                lineBot(op)
                oepoll.setRevision(op.revision)
    except Exception as e:
        logError(e)       
