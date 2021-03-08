import pandas as pd
import datetime as dt



def SendMailApp():
    import os
    import smtplib
    from email.message import EmailMessage


    EMAIL_ADRESS = os.environ.get('EM_USER')
    EMAIL_PASSWORD = os.environ.get('EM_PASSWORD')

    contacts = ['danilo.altomar@gmx.de']

    msg = EmailMessage()
    msg['Subject'] = 'Abfuhr Termin'
    msg['From'] = EMAIL_ADRESS
    msg['To'] = contacts
    msg.set_content(data3)


    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(EMAIL_ADRESS, EMAIL_PASSWORD)

        smtp.send_message(msg)


data = pd.read_excel("C:\\Users\\danil\\Desktop\\Python\\Abfall_2020.xlsx", engine = 'xlrd')

today = dt.date.today()
control_date = today + dt.timedelta(7)

data['is_after_control_date'] = [x < control_date for x in data.Datum]


data2 = data.loc[data['is_after_control_date'] == True]

data3 = data2.to_string()




SendMailApp()
