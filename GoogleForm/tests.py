from selenium import webdriver  
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time   
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from PIL import Image
from Screenshot import Screenshot

import django
from django.conf import settings
from django.core.mail import send_mail,EmailMessage

import os
import django


from django.core.management import call_command


driver_path=Service('.\\chromedriver\\chromedriver.exe')
opt = Options()
driver = webdriver.Chrome(service=driver_path,options=opt)  
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "GoogleForm.settings")
django.setup()
ss = Screenshot.Screenshot()

                
Name_path =     '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input'
Phn_path=       '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input'
Email_path =    '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input'
Address_path=   '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[4]/div/div/div[2]/div/div[1]/div[2]/textarea'
Pincode=        '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[5]/div/div/div[2]/div/div[1]/div/div[1]/input'
Dob_path =      '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[6]/div/div/div[2]/div/div/div[2]/div[1]/div/div[1]/input'
Gender_path =   '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[7]/div/div/div[2]/div/div[1]/div/div[1]/input'
Captcha_path =  '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[8]/div/div/div[2]/div/div[1]/div/div[1]/input'

def send_mails(subject, body , to_mail, cc_mail,attach_file1,attach_file2,attach_file3):
    email =EmailMessage(
        subject=subject,
        body= body,
        from_email=settings.EMAIL_HOST_USER,
        to = to_mail,
        cc=cc_mail
        )
    
    email.attach_file(attach_file1)
    email.attach_file(attach_file2)
    email.attach_file(attach_file3)
    email.send()


def formFill():
    driver.get("https://docs.google.com/forms/d/e/1FAIpQLSdUCd3UWQ3VOgeg0ZzNeT-xzNawU8AJ7Xidml-w1vhfBcvBWQ/viewform")
    time.sleep(10)
    driver.find_element(By.XPATH,Name_path).send_keys("Eswara Mahesh Surisetti")
    driver.find_element(By.XPATH,Phn_path).send_keys("9989848461")
    driver.find_element(By.XPATH,Email_path).send_keys("eswarsurya0@gmail.com")
    driver.find_element(By.XPATH,Address_path).send_keys("5-22/1,Kadali Village,Razole Mandal, East Godavari, Andhra Pradesh")
    driver.find_element(By.XPATH,Pincode).send_keys("533248")
    dobfield = WebDriverWait(driver, 15).until(ec.visibility_of_element_located((By.XPATH,Dob_path)))
    dobfield.send_keys("04/26/1996")
    driver.find_element(By.XPATH,Gender_path).send_keys("Male")
    captcha_text = driver.find_element(By.XPATH,'//*[@id="i30"]/span[1]/b').text
    driver.find_element(By.XPATH,Captcha_path).send_keys(captcha_text)
    driver.find_element(By.XPATH,'//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span/span').click()
    time.sleep(5)
    submit_text = driver.find_element(By.XPATH,"/html/body/div[1]/div[2]/div[1]/div/div[3]").text
    if submit_text =='Your response has been recorded.':
        image = ss.full_screenshot(driver, save_path=r'.' , image_name='Screenshot.png')
    else:
        print("Form Submission Failed !!Check Again")
    

formFill()
subject = 'Python (Selenium) Assignment -Eswara Mahesh Surisetti'
message = 'Hi Team , Good Afternoon Please Find the attached files.'
To_mail_list = ['tech@themedius.ai']
CC_List = ['HR@themedius.ai']
Screenshot_path ='C:\\Users\\esuriset\\Desktop\\FormFill\\GoogleForm\\Screenshot.png'
Resume_path = 'C:\\Users\\esuriset\\Desktop\\FormFill\\Eswar_Resume.pdf'
Document_path = 'C:\\Users\\esuriset\\Desktop\\FormFill\\Code_Documentation.docx'
send_mails(subject,message,To_mail_list,CC_List,Screenshot_path,Resume_path,Document_path)
