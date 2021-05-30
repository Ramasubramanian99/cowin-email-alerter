
import requests
# if get an error saying 'MODULE NOT FOUND : smtplib -  do pip install smtplib in your command line
import smtplib
import os


#setup
sender_email = os.getenv('SENDER_EMAIL') 
sender_password = os.getenv('SENDER_PASSWORD') 

receiver_email = os.getenv('RECEIVER_EMAIL') 
port = os.getenv('PORT') 
pincode = os.getenv('PINCODE') # this is optional

url = '' # the API endpoint you are going to hit

user = {"vaccine_choice": "COVISHIELD", "fee_type": "Paid"}

def email_client(center_name, center_address, pincode):
    content = 'Hello, \n\n Thanks for being a responsible citizen. Vaccine appointments are now available as per your preference at %(center_name)s located at %(center_address)s %(pincode)s. Please check cowin website to book your appointment. \n\n https://selfregistration.cowin.gov.in/'%{"center_name": center_name, "center_address": center_address, "pincode": pincode}
    subject = 'Vaccine available at your location! Check cowin website now'
    message = """\
    Subject: %(subject)s

    %(content)s"""%{ "subject": subject,"content": content}
    
    with smtplib.SMTP_SSL("smtp.gmail.com", port) as server:
        server.ehlo()  
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, receiver_email, message)


def get_vaccine_details(user):
    header = {'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36'}
    result = requests.get(url, headers=header)
    centers = result.json()['centers']
    flag = 0

    for center in centers:
        if center['fee_type'] == user['fee_type']:
            for session in center['sessions']:
                if session['min_age_limit'] == 18 and session['vaccine'] == user['vaccine_choice']:
                    if session['available_capacity'] > 0 and session['available_capacity_dose1'] > 0:  
                        email_client(center["name"], center['address'], center['pincode'])
                        flag = 1
        
        if flag == 1:    
            break
        

get_vaccine_details(user)
