import smtplib
import pandas as pd
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import data

email_list = pd.read_csv("emails.csv")

count=0
subject = 'Huge Discounts on Amazon Act Now!'

server = smtplib.SMTP("smtp.gmail.com", 587)
server.starttls()
server.login(data.your_email, data.your_password)
file = open('content.txt', 'r')
file2 = open('used.txt', 'a')

content = file.read()

for index, row in email_list.iterrows():
    msg = MIMEMultipart()
    msg["From"] = data.your_email
    msg["To"] = row["email"]
    msg["Subject"] = subject
    msg.attach(MIMEText(content, "plain"))
    
    server.sendmail(data.your_email, row["email"], msg.as_string())
    count=count+1
    print(count)
    email_list = email_list.drop(index)
    file2.write(row["email"] + '\n')
    email_list.to_csv("emails.csv", index=False)

server.quit()
file.close()
file2.close()

print("finish")