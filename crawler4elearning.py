#this is made by xxxddd12xd
import base64
import urllib.request as req
import requests
import urllib.parse

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36'
}

craw_mode=int(input("1=學生作業 2=教材 3=尋找最新流水號 4=圖片/影片 5=圖片/影片/文字/壓縮檔:"))
if craw_mode==1:
    #轉換流水號
    print("==流水號尾:555590,last updated 2020/4/30==")
    serial_start=input("輸入流水號頭:")
    serial_end=input("輸入流水號尾:")
    for i in range(int(serial_start),int(serial_end)):

        b=base64.b64encode(str.encode(str(i)))
        c=bytes.decode(b)


        url="http://elearning.nuk.edu.tw/m_stujobs/p_stujobs_p2_files.php?"+c
        #得到redirct過的url
        r = requests.get(url, allow_redirects=True).url
        print(urllib.parse.unquote(r).split("stu_files/")[1])
        #getFile
        rr=requests.get(r)
        filename=urllib.parse.unquote(r).split("stu_files/")[1]
        ##print(filename)
        #寫檔
        try:
            open(filename,'wb').write(rr.content)
        except:
            print("檔案未找到!")

    print("done!")
elif craw_mode==2:
    print("==流水號尾:124185,last updated 2020/4/30==")
    serial_start=input("輸入流水號頭:")
    serial_end=input("輸入流水號尾:")
    for i in range(int(serial_start),int(serial_end)):
        url="http://elearning.nuk.edu.tw/m_teacher/m_tea_txbook_files.php?jteabook_sd="+str(i)
        #得到redirct過的url
        r = requests.get(url, allow_redirects=True).url
        print(urllib.parse.unquote(r).split("tea_files/")[1])
        #getFile
        rr=requests.get(r)
        filename=urllib.parse.unquote(r).split("tea_files/")[1]
        try:
            open(filename,'wb').write(rr.content)
        except:
            print("檔案未找到!")
    print("done!")

if craw_mode==3:
    #轉換流水號
    print("==流水號尾:555590,last updated 2020/4/30==")
    serial_start=input("輸入流水號頭:")
    totalMiss=0
    for i in range(int(serial_start),999999):
        b=base64.b64encode(str.encode(str(i)))
        c=bytes.decode(b)
        url="http://elearning.nuk.edu.tw/m_stujobs/p_stujobs_p2_files.php?"+c
        #得到redirct過的url
        Rhead=requests.head(url, allow_redirects=True,headers=headers)
        Rheaders=Rhead.headers
        print ("No.",i,"標頭:",Rhead)
        print ("標頭:",Rheaders)
        # print ("大小:",Rheaders["Content-Length"])
        if Rheaders["Content-Length"]=="218":
            totalMiss+=1
        else:
            totalMiss=0
        if totalMiss==20:
            print("末碼:",i)
            break    
    print("done!")

if craw_mode==4:
    #轉換流水號
    print("==流水號尾:555590,last updated 2020/4/30==")
    serial_start=input("輸入流水號頭:")
    serial_end=input("輸入流水號尾:")
    for i in range(int(serial_start),int(serial_end)):

        b=base64.b64encode(str.encode(str(i)))
        c=bytes.decode(b)
        url="http://elearning.nuk.edu.tw/m_stujobs/p_stujobs_p2_files.php?"+c
        #得到redirct過的url
        Rhead=requests.head(url, allow_redirects=True,headers=headers)
        Rheaders=Rhead.headers
        if Rheaders["Content-Type"]=="image/jpeg" or Rheaders["Content-Type"]=="image/png" \
        or Rheaders["Content-Type"]=="video/mpeg4"or Rheaders["Content-Type"]=="video/mpg" \
        or Rheaders["Content-Type"]=="video/avi":
            #getFile
            r = requests.get(url, allow_redirects=True).url
            rr=requests.get(r)
            print("No.",i,":",urllib.parse.unquote(r).split("stu_files/")[1])
            filename=urllib.parse.unquote(r).split("stu_files/")[1]
            #寫檔
            open(filename,'wb').write(rr.content)

    print("done!")

if craw_mode==5:
    #轉換流水號
    print("==流水號尾:555590,last updated 2020/4/30==")
    serial_start=input("輸入流水號頭:")
    serial_end=input("輸入流水號尾:")
    for i in range(int(serial_start),int(serial_end)):

        b=base64.b64encode(str.encode(str(i)))
        c=bytes.decode(b)
        url="http://elearning.nuk.edu.tw/m_stujobs/p_stujobs_p2_files.php?"+c
        #得到redirct過的url
        Rhead=requests.head(url, allow_redirects=True,headers=headers)
        Rheaders=Rhead.headers
        print ("No.",i,"類型:",Rheaders["Content-Type"],Rhead)
        if Rheaders["Content-Type"]=="text/plain" or Rheaders["Content-Type"]=="video/mpeg4"\
        or Rheaders["Content-Type"]=="video/mpg"  or Rheaders["Content-Type"]=="video/avi" \
        or Rheaders["Content-Type"]=="video/x-msvideo"or Rheaders["Content-Type"]=="video/webm"\
        or Rheaders["Content-Type"]=="application/zip"or Rheaders["Content-Type"]=="application/rar" \
        or Rheaders["Content-Type"]=="application/x-zip-compressed" or Rheaders["Content-Type"]=="image/jpeg" \
        or Rheaders["Content-Type"]=="image/png" :
            #getFile
            r = requests.get(url, allow_redirects=True).url
            rr=requests.get(r)
            #跳過.c/.cpp
            if ".c" in urllib.parse.unquote(r).split("stu_files/")[1]:
                continue
            print("No.",i,":",urllib.parse.unquote(r).split("stu_files/")[1])
            filename=urllib.parse.unquote(r).split("stu_files/")[1]
            #寫檔
            open(filename,'wb').write(rr.content)

    print("done!")
