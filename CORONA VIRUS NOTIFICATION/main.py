from plyer import notification
import requests
from bs4 import BeautifulSoup
import time

def notifyMe(title,message):
    notification.notify(
        title=title,
        message=message,
        app_icon="C:\\Users\\soham\\OneDrive\\Documents\\PYTHON PROJECTS\\CORONA VIRUS NOTIFICATION\\icon.ico",
        timeout=10
    )
def getData(url):
    r=requests.get(url)
    return r.text

if __name__=="__main__":
    while True:
        # notifyMe("Soham","Hi! Wan'na have some fun !")
        myHTMLData=getData("https://www.hhs.gov/")
        
        soup=BeautifulSoup(myHTMLData,"html.parser")
        myDataStr=""

        for tr in soup.findAll('table')[-1].findAll('tr'):
            myDataStr+=tr.get_text()
        myDataStr=myDataStr[1:]
        itemList=myDataStr.split("\n\n")
        states=['West Bengal',"Maharashtra","Kerala"]
        for item in itemList[0:22]:
            
            dataList=item.split("\n")
            if dataList[1] in states:
                print(dataList)
                nTitle="Cases of Covid-19"
                nText=f"STATE {dataList[1]}\nIndian : {dataList[2]}& Foreign : {dataList[3]}\nCured : {dataList[4]}\nDeaths:{dataList[5]}"
                notifyMe(nTitle,nText)
                time.sleep(4)
        time.sleep(10)
