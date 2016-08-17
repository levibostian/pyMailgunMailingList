import requests

configFileLine = 0

apiKey = ""
emailFrom = ""
emailTo = ""

for line in open("config.txt", 'r'):
    line = line.split(":")

    if configFileLine == 0:
        apiKey = line[1].strip()
    elif configFileLine == 1:
        emailFrom += line[1].strip() + " "
    elif configFileLine == 2:
        emailFrom += line[1].strip() + " "
    elif configFileLine == 3:
        emailFrom += "<" + line[1].strip() + ">"
    elif configFileLine == 4:
        emailTo = line[1].strip()

    configFileLine += 1

emailTextLine = 0

subject = ""
body = ""

for line in open("email_text.txt", "r"):
    if emailTextLine == 0:
        line = line.split(":")
        subject = line[1].strip()
    elif emailTextLine == 4:
        body += line

    emailTextLine += 1

data = {"from": emailFrom, "to": emailTo, "subject": subject, "text": body}

requests.post("https://api.mailgun.net/v3/curiosityio.com/messages", auth=("api", apiKey), data=data)
