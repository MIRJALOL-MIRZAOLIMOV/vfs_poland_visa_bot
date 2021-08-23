from selenium import webdriver
from time import sleep
import smtplib

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import os
from selenium.webdriver.common.action_chains import ActionChains



print("bu app vize almakta zorluk yaşayan öğrenciler için yazılmıştır")
print("önce şehir seçip tarayıcı acıldıktan sonra kendi bilgilerinizle vfsye giriş için 30 saniyeniz var")
print("appi kullanmadan önce firefox tarayıcısını bilgisayarınıza yükleyin")
print("app polonya vizesi için sürekli randevu almayı dener, boş buldugu anda alarm çalar")
print("bu yüzden bilgisayarınızın sesini açık tutun")
print("alarm çaldıktan sonra app durur ve kişisel bilgilerinizi kendiniz girmeniz gerekmektedir")



print("1- altunizade")
print("2- ankara")
print("3- antalya")
print("4- beyoglu")
print("5- gaziantep")
print("6- izmir")
print("7- trabzon")

merkez = 0

try:
    while merkez < 1 or merkez > 7 :
        print("başvuru yapılacak şehir? sadece rakam giriniz ")
        merkez = int(input())
except:
    print("başvuru yapılacak şehir? sadece rakam giriniz ")
    merkez = int(input())


if merkez > 0 or merkez < 8:
    print("tarayıcı açılıyor. vfs giriş bilgilerini girmek için 30 saniyen var")
    sleep(3)

driver = webdriver.Firefox(executable_path="geckodriver.exe")

driver.get("https://online.vfsglobal.com/global-appointment/Account/RegisteredLogin?q=shSA0YnE4pLF9Xzwon/x/ASnHZRMROGDyz5YljrTPrnvkCGRs++Pfo4IkOWvgfeQYBAkmBryQbZleBk4vbrGBA==")

driver.maximize_window()

sleep(30)

randevu_var = 0
sayac = 0




while randevu_var == 0:
    randevu = driver.find_element_by_xpath('/html/body/div[2]/div[1]/div[2]/div/div/div[2]/div/ul/li[1]/a').click()

    sleep(2)

    lokasyon = driver.find_element_by_xpath('//*[@id="LocationId"]')
    dropdown = Select(lokasyon)
    dropdown.select_by_index(merkez)

    sleep(2)

    kategori = driver.find_element_by_xpath('//*[@id="VisaCategoryId"]')

    if kategori.is_enabled():
        os.system("alarm.mp3")
        randevu_var = 1
        # dropdown2 = Select(kategori)
        # dropdown2.select_by_value('4843')
        #
        # sleep(1)
        #
        # next = driver.find_element_by_xpath('//*[@id="btnContinue"]').click()
        # print("randevu var")
        #
        # sleep(1)
        #
        # musteri_add = driver.find_element_by_xpath('/html/body/div[2]/div[1]/div[3]/div[3]/a').click()
        #
        # sleep(1)
        #
        # passport_number = driver.find_element_by_xpath('//*[@id="PassportNumber"]')
        # passport_number.send_keys("123123123")
        #
        # sleep(1)
        #
        # date_birth = driver.find_element_by_xpath('//*[@id="DateOfBirth"]')
        # date_birth.send_keys("01011990")
        #
        # sleep(1)
        #
        # pass_expire_date = driver.find_element_by_xpath('//*[@id="PassportExpiryDate"]')
        # pass_expire_date.send_keys("01012031")
        #
        # sleep(1)
        #
        # nationality = driver.find_element_by_xpath('//*[@id="NationalityId"]')
        # dropdown3 = Select(nationality)
        # dropdown3.select_by_value("160")
        #
        # sleep(1)
        #
        # first_name = driver.find_element_by_xpath('//*[@id="FirstName"]')
        # first_name.send_keys("OMER FARUK")
        #
        # sleep(1)
        #
        # last_name = driver.find_element_by_xpath('//*[@id="LastName"]')
        # last_name.send_keys("NAZLI")
        #
        # sleep(1)
        #
        # gender = driver.find_element_by_xpath('//*[@id="GenderId"]')
        # dropdown4 = Select(gender)
        # dropdown4.select_by_value("1")
        #
        # sleep(1)
        #
        # submit_btn = driver.find_element_by_xpath('//*[@id="submitbuttonId"]').click()
        #
        # sleep(1)
        #
        # actions = ActionChains(driver)
        # actions.send_keys(Keys.ENTER)
        # actions.perform()
        #
        # sleep(1)
        #
        # devam = driver.find_element_by_xpath('/html/body/div[2]/div[1]/div[3]/div[4]/form/div[2]/input').click()







    else:
        print("randevu yok")
        sayac += 1
        print(str(sayac) + " kez denendi")



    sleep(1)









