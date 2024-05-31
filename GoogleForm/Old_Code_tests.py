import undetected_chromedriver as us
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
from pynput.keyboard import Key,Controller
from django.core.mail import EmailMessage
from django.conf import settings



driver_path=Service('C:\\Users\\esuriset\\Desktop\\FormFill\\GoogleForm\\chromedriver\\chromedriver.exe')
opt = Options()
driver = us.Chrome(service=driver_path,options=opt)  

ss = Screenshot.Screenshot()

keyboard = Controller()

Name_path = '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input'
Phn_path='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input'
Email_path = '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input'
Address_path='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[4]/div/div/div[2]/div/div[1]/div[2]/textarea'
Pincode= '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[5]/div/div/div[2]/div/div[1]/div/div[1]/input'
Dob_path = '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[7]/div/div/div[2]/div/div/div[2]/div[1]/div/div[1]/input'
Gender_path = '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[8]/div/div/div[2]/div/div[1]/div/div[1]/input'
Captcha_path = '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[9]/div/div/div[2]/div/div[1]/div/div[1]/input'
File_Upload = '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[6]/div/div/div[2]/div/div[2]/span/span[2]'

def send_mails(subject, body , to_mail, cc_mail,attach_path):
    email =EmailMessage(
        subject=subject,
        body= body,
        from_email=settings.EMAIL_HOST_USER,
        to = to_mail,
        cc=cc_mail
        )
    
    email.attach_file(attach_path)
    email.send()





def formFill():
    driver.get("https://docs.google.com/forms/d/e/1FAIpQLSdUCd3UWQ3VOgeg0ZzNeT-xzNawU8AJ7Xidml-w1vhfBcvBWQ/viewform")
    driver.find_element(By.XPATH,Name_path).send_keys("Mahesh")
    driver.find_element(By.XPATH,Phn_path).send_keys("9989848461")
    driver.find_element(By.XPATH,Email_path).send_keys("eswar@gmail.com")
    driver.find_element(By.XPATH,Address_path).send_keys("5-22/1, kadali , razole")
    driver.find_element(By.XPATH,Pincode).send_keys("533248")
    driver.find_element(By.XPATH,File_Upload).click()
    time.sleep(5)
    main_wind= driver.current_window_handle
    iframe = WebDriverWait(driver, 15).until(ec.visibility_of_element_located((By.XPATH,"/html/body/div[4]/div[2]/div/iframe")))
    driver.switch_to.frame(iframe)
    driver.find_element(By.XPATH,'//*[@id="yDmH0d"]/div[2]/div[3]/div[2]/div[2]/div/div/div/div[1]/div/div[2]/div/button/span').click()
    time.sleep(3)
    keyboard.type("C:\\Users\\esuriset\\Desktop\\FormFill\\Eswar_Resume.pdf")
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
    time.sleep(3)
    driver.switch_to.window(main_wind)
    dobfield = WebDriverWait(driver, 15).until(ec.visibility_of_element_located((By.XPATH,Dob_path)))
    dobfield.send_keys("04/26/1996")
    driver.find_element(By.XPATH,Gender_path).send_keys("Male")
    captcha_text = driver.find_element(By.XPATH,'//*[@id="i35"]/span[1]/b').text
    driver.find_element(By.XPATH,Captcha_path).send_keys(captcha_text)
    time.sleep(10)


 

driver.get("https://docs.google.com/forms/d/e/1FAIpQLSdUCd3UWQ3VOgeg0ZzNeT-xzNawU8AJ7Xidml-w1vhfBcvBWQ/viewform")
    
try:
    driver.find_element(By.XPATH,"/html/body/div[1]/div[2]/div/div[2]/a/span")
    formFill()
except NoSuchElementException:
    print("Needs to be logged in to fill this form")
    mailid = WebDriverWait(driver, 15).until(ec.visibility_of_element_located((By.XPATH,'//*[@id="identifierId"]')))
    #accout details has removed add gmail to  add mail id between ""
    mailid.send_keys(""+Keys.ENTER)
    passwd = WebDriverWait(driver, 15).until(ec.visibility_of_element_located((By.XPATH,'//*[@id="password"]/div[1]/div/div[1]/input')))
    #password has removed 
    passwd.send_keys("pwd"+Keys.ENTER)
    time.sleep(10)
finally:
    formFill()
    image = ss.full_screenshot(driver, save_path=r'.' , image_name='Screenshot.png')
    send_mails('Python (Selenium) Assignment -Eswara Mahesh ', 'body' , 'eswarsurya0@gmail.com', 'eswarsurya0@gmail.com','C:\\Users\\esuriset\\Desktop\\FormFill\\GoogleForm\\name.png')

                  
