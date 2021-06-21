import emailFuctions
import requests
import csv
from datetime import datetime
from datetime import date


def get_status_website(webSitesInfoList):
    for info in webSitesInfoList:
        if info[4] == "Active":
            try: 
                r = requests.get(info[0], timeout=8)
            except Exception as e:
                print("Exception: {}".format(e.args))
                emailFuctions.send_email_bodyHtml_externalHTMLFile("156.24.14.132","do.not.reply@igt-noreply.com",info[1], info[2], info[3], [])
                writeLog("Exception: {}".format(e.args)) 
            else:
                if r.status_code != 200:
                    print("{}. Response code: {}".format (info[2], r.status_code))
                    emailFuctions.send_email_bodyHtml_externalHTMLFile("156.24.14.132", "do.not.reply@igt-noreply.com", info[1], "{}. Response code: {}".format (info[2], r.status_code), info[3], [])
                    writeLog("{}. Response code: {}".format (info[2], r.status_code))
                else:
                    print("{} is UP. Response code: {}".format (info[0], r.status_code))
                    #emailFuctions.send_email_bodyHtml_externalHTMLFile("156.24.14.132", "do.not.reply@igt-noreply.com", info[1], "NY Subscription portal is UP", info[3], [])
                    writeLog("{} is UP. Response code: {}".format (info[0], r.status_code))
      
def readCSV(pathFile):
    infoList = []
    try:
        with open(pathFile, encoding="UTF-8") as f:
            reader = csv.reader(f)
            for row in reader:
                infoList.append(row)
            f.close
    except Exception as e:
        print("Something wrong opening the CSV file: {}".format(pathFile))
        writeLog("Something wrong opening the CSV file: {}. Exception:{}".format(pathFile, e.args))
        emailFuctions.send_email_bodyText("156.24.14.132", "do.not.reply@igt-noreply.com", "carlos.vegabello@igt.com", "Something wrong opening the CSV file.", "Something wrong opening the CSV file: {}. Exception:{}".format(pathFile, e.args), [])

    return infoList
    

def writeLog(message):
    today = datetime.now()
    date_now_dt= today.strftime("%m_%d_%Y")
    try:
        with open("./LOGS/log_{}.txt".format(date_now_dt), "a", encoding="utf-8") as f:
            time_now_dt = today.strftime("%H:%M:%S")
            f.write("{}: {}".format(time_now_dt, message))
            f.write("\n")
            f.close
    except Exception as e:
        emailFuctions.send_email_bodyText("156.24.14.132", "do.not.reply@igt-noreply.com", "carlos.vegabello@igt.com", "Something wrong opening the LOG file of the Websites Monitoring.", "Something wrong opening the LOG file: {}. Exception:{}".format("./LOGS/log_{}.txt".format(date_now_dt), e.args), [])

    

def run():
    website_infoList = readCSV("./websiteInfo.csv")
    if len(website_infoList) > 0:
        get_status_website(website_infoList)
    

if __name__== '__main__':
    run()




