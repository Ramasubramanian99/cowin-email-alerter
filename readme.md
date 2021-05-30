# Cowin - E-mail Alerter

This script will help you to book your covid-19 vaccine in India.

## Setup

#### To setup the environment

To run the script we should set some environment variables. They are explained below.

```python

    # An sender email - the email from which you will be sending the alerts
    SENDER_EMAIL

    # You can use ur senders emails password but make sure you are not sharing it in public or running the script in a public scheduler. alternatively if you are gmail user u can use an app password for better security - more on that : https://support.google.com/accounts/answer/185833?hl=en
    SENDER_PASSWORD

    # An receiver email -  the email id in which you will be reveiving the alerts. 
    RECEIVER_EMAIL

    # This is port is for gmail to find the port for your mailing service google <email serrrvice name> port number
    PORT

    # The pincode in which you want to search for vaccine
    PINCODE
```

#### To setup the URL

To search via pincode copy this and paste it in url variable in line 16 -

'https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByPin?pincode='+pincode+'&date='+date.today().strftime("%d-%m-%Y")

To search in your whole district - 

- Go to https://www.cowin.gov.in/home, right click on the webpage and click on inspect
- In the side panel that opens click on the network which is one of the tab in the top of the side panel
- Now search for the district you will see the requests that are being sent.
- Click on the request titled - calendarByDistrict, copy the request url and paste it in the url variable.
- Please note that you have to change the date to the current date everyday

#### To setup user object
In line 18 the user object, you can edit it as per your choice:
- vaccine choice - COVISHIELD or COVAXIN
- fee type - Paid or Free ( for 18+ its mostly its Paid service only )

#### To run this in a script

You can run this is script in any scheduler. For example the script in **crontab** scheduler for script every minute.

```shell

* * * * *  cd <path to script> && <path to python> python cron_ash.py

```
