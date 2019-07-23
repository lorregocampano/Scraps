from selenium import webdriver
import time
import os
import pyautogui
chrome_path =r"INGRESAR PATH DEL CHROMEDRIVER"
driver = webdriver.Chrome(chrome_path)
driver.get("https://www.boletinconcursal.cl/nomina/liquidadores?fbclid=IwAR3WSpBehEuvia8JrlsRpiTG6nvOjazLup-HzcEBZDGh-FtNkQtMokI1AQc")
driver.implicitly_wait(3)

strnom="Nombre"
strfon="Fono"
strcorreo="Correo"
strsusp="Suspensión"
str1 = ","
print(str1+strnom+str1+strfon+str1+strcorreo+str1+strsusp)
f = open('myoutput.txt', 'wt')
def elementos(): 
#elemento 1
    
    driver.find_element_by_xpath("""//*[@id="tblLiquidadores"]/div[1]/table/tbody/tr[1]/td[1]/i""").click()
    time.sleep(0.5)
    atliq1 = driver.find_element_by_xpath("""//*[@id="tShowLiquidadorIdentificacion"]/tbody/tr[1]/td""")
    atliq2 = driver.find_element_by_xpath("""//*[@id="tShowLiquidadorIdentificacion"]/tbody/tr[4]/td[2]""")
    atliq3 = driver.find_element_by_xpath("""//*[@id="tShowLiquidadorIdentificacion"]/tbody/tr[5]/td""")
    atliqsus1 = driver.find_element_by_xpath("""//*[@id="tShowLiquidadorIdentificacion"]/tbody/tr[7]/td""")
    print(str1+atliq1.text+str1+atliq2.text+str1+atliq3.text+str1+atliqsus1.text)
    driver.find_element_by_xpath("""//*[@id="dlgShowLiquidador"]/div[1]/a""").click()
    time.sleep(0.5)
    
#elemento 2
    driver.find_element_by_xpath("""//*[@id="tblLiquidadores"]/div[1]/table/tbody/tr[2]/td[1]/i""").click()
    time.sleep(0.5)
    atliq4 = driver.find_element_by_xpath("""//*[@id="tShowLiquidadorIdentificacion"]/tbody/tr[1]/td""")
    atliq5 = driver.find_element_by_xpath("""//*[@id="tShowLiquidadorIdentificacion"]/tbody/tr[4]/td[2]""")
    atliq6 = driver.find_element_by_xpath("""//*[@id="tShowLiquidadorIdentificacion"]/tbody/tr[5]/td""")
    atliqsus2 = driver.find_element_by_xpath("""//*[@id="tShowLiquidadorIdentificacion"]/tbody/tr[7]/td""")
    print(str1+atliq4.text+str1+atliq5.text+str1+atliq6.text+str1+atliqsus2.text)
    driver.find_element_by_xpath("""//*[@id="dlgShowLiquidador"]/div[1]/a""").click()
    time.sleep(0.5)
    
#elemento 3
    driver.find_element_by_xpath("""//*[@id="tblLiquidadores"]/div[1]/table/tbody/tr[3]/td[1]/i""").click()
    time.sleep(0.5)
    atliq7 = driver.find_element_by_xpath("""//*[@id="tShowLiquidadorIdentificacion"]/tbody/tr[1]/td""")
    atliq8 = driver.find_element_by_xpath("""//*[@id="tShowLiquidadorIdentificacion"]/tbody/tr[4]/td[2]""")
    atliq9 = driver.find_element_by_xpath("""//*[@id="tShowLiquidadorIdentificacion"]/tbody/tr[5]/td""")
    atliqsus3 = driver.find_element_by_xpath("""//*[@id="tShowLiquidadorIdentificacion"]/tbody/tr[7]/td""")
    print(str1+atliq7.text+str1+atliq8.text+str1+atliq9.text+str1+atliqsus3.text)
    driver.find_element_by_xpath("""//*[@id="dlgShowLiquidador"]/div[1]/a""").click()
    time.sleep(0.5)
#elemento 4
    driver.find_element_by_xpath("""//*[@id="tblLiquidadores"]/div[1]/table/tbody/tr[4]/td[1]/i""").click()
    time.sleep(0.5)
    atliq10 = driver.find_element_by_xpath("""//*[@id="tShowLiquidadorIdentificacion"]/tbody/tr[1]/td""")
    atliq11 = driver.find_element_by_xpath("""//*[@id="tShowLiquidadorIdentificacion"]/tbody/tr[4]/td[2]""")
    atliq12 = driver.find_element_by_xpath("""//*[@id="tShowLiquidadorIdentificacion"]/tbody/tr[5]/td""")
    atliqsus4 = driver.find_element_by_xpath("""//*[@id="tShowLiquidadorIdentificacion"]/tbody/tr[7]/td""")
    print(str1+atliq10.text+str1+atliq11.text+str1+atliq12.text+str1+atliqsus4.text)
    driver.find_element_by_xpath("""//*[@id="dlgShowLiquidador"]/div[1]/a""").click()
    time.sleep(0.5)
#elemento 5
    driver.find_element_by_xpath("""//*[@id="tblLiquidadores"]/div[1]/table/tbody/tr[5]/td[1]/i""").click()
    time.sleep(0.5)
    atliq13 = driver.find_element_by_xpath("""//*[@id="tShowLiquidadorIdentificacion"]/tbody/tr[1]/td""")
    atliq14 = driver.find_element_by_xpath("""//*[@id="tShowLiquidadorIdentificacion"]/tbody/tr[4]/td[2]""")
    atliq15 = driver.find_element_by_xpath("""//*[@id="tShowLiquidadorIdentificacion"]/tbody/tr[5]/td""")
    atliqsus5 = driver.find_element_by_xpath("""//*[@id="tShowLiquidadorIdentificacion"]/tbody/tr[7]/td""")
    print(str1+atliq13.text+str1+atliq14.text+str1+atliq15.text+str1+atliqsus5.text)
    driver.find_element_by_xpath("""//*[@id="dlgShowLiquidador"]/div[1]/a""").click()
    time.sleep(0.5)
#elemento 6
    driver.find_element_by_xpath("""//*[@id="tblLiquidadores"]/div[1]/table/tbody/tr[6]/td[1]/i""").click()
    time.sleep(0.5)
    atliq16 = driver.find_element_by_xpath("""//*[@id="tShowLiquidadorIdentificacion"]/tbody/tr[1]/td""")
    atliq17 = driver.find_element_by_xpath("""//*[@id="tShowLiquidadorIdentificacion"]/tbody/tr[4]/td[2]""")
    atliq18 = driver.find_element_by_xpath("""//*[@id="tShowLiquidadorIdentificacion"]/tbody/tr[5]/td""")
    atliqsus6 = driver.find_element_by_xpath("""//*[@id="tShowLiquidadorIdentificacion"]/tbody/tr[7]/td""")
    print(str1+atliq16.text+str1+atliq17.text+str1+atliq18.text+str1+atliqsus6.text)
    driver.find_element_by_xpath("""//*[@id="dlgShowLiquidador"]/div[1]/a""").click()
    time.sleep(0.5)
#elemento 7
    driver.find_element_by_xpath("""//*[@id="tblLiquidadores"]/div[1]/table/tbody/tr[7]/td[1]/i""").click()
    time.sleep(0.5)
    atliq19 = driver.find_element_by_xpath("""//*[@id="tShowLiquidadorIdentificacion"]/tbody/tr[1]/td""")
    atliq20 = driver.find_element_by_xpath("""//*[@id="tShowLiquidadorIdentificacion"]/tbody/tr[4]/td[2]""")
    atliq21 = driver.find_element_by_xpath("""//*[@id="tShowLiquidadorIdentificacion"]/tbody/tr[5]/td""")
    atliqsus7 = driver.find_element_by_xpath("""//*[@id="tShowLiquidadorIdentificacion"]/tbody/tr[7]/td""")
    print(str1+atliq19.text+str1+atliq20.text+str1+atliq21.text+str1+atliqsus7.text)
    driver.find_element_by_xpath("""//*[@id="dlgShowLiquidador"]/div[1]/a""").click()
    time.sleep(0.5)
#elemento 8
    driver.find_element_by_xpath("""//*[@id="tblLiquidadores"]/div[1]/table/tbody/tr[8]/td[1]/i""").click()
    time.sleep(0.5)
    atliq22 = driver.find_element_by_xpath("""//*[@id="tShowLiquidadorIdentificacion"]/tbody/tr[1]/td""")
    atliq23 = driver.find_element_by_xpath("""//*[@id="tShowLiquidadorIdentificacion"]/tbody/tr[4]/td[2]""")
    atliq24 = driver.find_element_by_xpath("""//*[@id="tShowLiquidadorIdentificacion"]/tbody/tr[5]/td""")
    atliqsus8 = driver.find_element_by_xpath("""//*[@id="tShowLiquidadorIdentificacion"]/tbody/tr[7]/td""")
    print(str1+atliq22.text+str1+atliq23.text+str1+atliq24.text+str1+atliqsus8.text)
    driver.find_element_by_xpath("""//*[@id="dlgShowLiquidador"]/div[1]/a""").click()
    time.sleep(0.5)
#elemento 9
    driver.find_element_by_xpath("""//*[@id="tblLiquidadores"]/div[1]/table/tbody/tr[9]/td[1]/i""").click()
    time.sleep(0.5)
    atliq25 = driver.find_element_by_xpath("""//*[@id="tShowLiquidadorIdentificacion"]/tbody/tr[1]/td""")
    atliq26 = driver.find_element_by_xpath("""//*[@id="tShowLiquidadorIdentificacion"]/tbody/tr[4]/td[2]""")
    atliq27 = driver.find_element_by_xpath("""//*[@id="tShowLiquidadorIdentificacion"]/tbody/tr[5]/td""")
    atliqsus9 = driver.find_element_by_xpath("""//*[@id="tShowLiquidadorIdentificacion"]/tbody/tr[7]/td""")
    print(str1+atliq25.text+str1+atliq26.text+str1+atliq27.text+str1+atliqsus9.text)
    driver.find_element_by_xpath("""//*[@id="dlgShowLiquidador"]/div[1]/a""").click()
    time.sleep(0.5)
#elemento 10
    driver.find_element_by_xpath("""//*[@id="tblLiquidadores"]/div[1]/table/tbody/tr[10]/td[1]/i""").click()
    time.sleep(0.5)
    atliq28 = driver.find_element_by_xpath("""//*[@id="tShowLiquidadorIdentificacion"]/tbody/tr[1]/td""")
    atliq29 = driver.find_element_by_xpath("""//*[@id="tShowLiquidadorIdentificacion"]/tbody/tr[4]/td[2]""")
    atliq30 = driver.find_element_by_xpath("""//*[@id="tShowLiquidadorIdentificacion"]/tbody/tr[5]/td""")
    atliqsus10 = driver.find_element_by_xpath("""//*[@id="tShowLiquidadorIdentificacion"]/tbody/tr[7]/td""")
    print(str1+atliq28.text+str1+atliq29.text+str1+atliq30.text+str1+atliqsus10.text)
    driver.find_element_by_xpath("""//*[@id="dlgShowLiquidador"]/div[1]/a""").click()
    time.sleep(0.5)
#elemento 11
    driver.find_element_by_xpath("""//*[@id="tblLiquidadores"]/div[1]/table/tbody/tr[11]/td[1]/i""").click()
    time.sleep(0.5)
    atliq31 = driver.find_element_by_xpath("""//*[@id="tShowLiquidadorIdentificacion"]/tbody/tr[1]/td""")
    atliq32 = driver.find_element_by_xpath("""//*[@id="tShowLiquidadorIdentificacion"]/tbody/tr[4]/td[2]""")
    atliq33 = driver.find_element_by_xpath("""//*[@id="tShowLiquidadorIdentificacion"]/tbody/tr[5]/td""")
    atliqsus11 = driver.find_element_by_xpath("""//*[@id="tShowLiquidadorIdentificacion"]/tbody/tr[7]/td""")
    print(str1+atliq31.text+str1+atliq32.text+str1+atliq33.text+str1+atliqsus11.text)
    driver.find_element_by_xpath("""//*[@id="dlgShowLiquidador"]/div[1]/a""").click()
    time.sleep(0.5)
#elemento 12
    driver.find_element_by_xpath("""//*[@id="tblLiquidadores"]/div[1]/table/tbody/tr[12]/td[1]/i""").click()
    time.sleep(0.5)
    atliq34 = driver.find_element_by_xpath("""//*[@id="tShowLiquidadorIdentificacion"]/tbody/tr[1]/td""")
    atliq35 = driver.find_element_by_xpath("""//*[@id="tShowLiquidadorIdentificacion"]/tbody/tr[4]/td[2]""")
    atliq36 = driver.find_element_by_xpath("""//*[@id="tShowLiquidadorIdentificacion"]/tbody/tr[5]/td""")
    atliqsus12 = driver.find_element_by_xpath("""//*[@id="tShowLiquidadorIdentificacion"]/tbody/tr[7]/td""")
    print(str1+atliq34.text+str1+atliq35.text+str1+atliq36.text+str1+atliqsus12.text)
    driver.find_element_by_xpath("""//*[@id="dlgShowLiquidador"]/div[1]/a""").click()
    time.sleep(0.5)
#elemento 13
    driver.find_element_by_xpath("""//*[@id="tblLiquidadores"]/div[1]/table/tbody/tr[13]/td[1]/i""").click()
    time.sleep(0.5)
    atliq37 = driver.find_element_by_xpath("""//*[@id="tShowLiquidadorIdentificacion"]/tbody/tr[1]/td""")
    atliq38 = driver.find_element_by_xpath("""//*[@id="tShowLiquidadorIdentificacion"]/tbody/tr[4]/td[2]""")
    atliq39 = driver.find_element_by_xpath("""//*[@id="tShowLiquidadorIdentificacion"]/tbody/tr[5]/td""")
    atliqsus13 = driver.find_element_by_xpath("""//*[@id="tShowLiquidadorIdentificacion"]/tbody/tr[7]/td""")
    print(str1+atliq37.text+str1+atliq38.text+str1+atliq39.text+str1+atliqsus13.text)
    driver.find_element_by_xpath("""//*[@id="dlgShowLiquidador"]/div[1]/a""").click()
    time.sleep(0.5)
#elemento 14
    driver.find_element_by_xpath("""//*[@id="tblLiquidadores"]/div[1]/table/tbody/tr[14]/td[1]/i""").click()
    time.sleep(0.5)
    atliq40 = driver.find_element_by_xpath("""//*[@id="tShowLiquidadorIdentificacion"]/tbody/tr[1]/td""")
    atliq41 = driver.find_element_by_xpath("""//*[@id="tShowLiquidadorIdentificacion"]/tbody/tr[4]/td[2]""")
    atliq42 = driver.find_element_by_xpath("""//*[@id="tShowLiquidadorIdentificacion"]/tbody/tr[5]/td""")
    atliqsus14 = driver.find_element_by_xpath("""//*[@id="tShowLiquidadorIdentificacion"]/tbody/tr[7]/td""")
    print(str1+atliq40.text+str1+atliq41.text+str1+atliq42.text+str1+atliqsus14.text)
    driver.find_element_by_xpath("""//*[@id="dlgShowLiquidador"]/div[1]/a""").click()
    time.sleep(0.5)
#elemento 15
    driver.find_element_by_xpath("""//*[@id="tblLiquidadores"]/div[1]/table/tbody/tr[15]/td[1]/i""").click()
    time.sleep(0.5)
    atliq43 = driver.find_element_by_xpath("""//*[@id="tShowLiquidadorIdentificacion"]/tbody/tr[1]/td""")
    atliq44 = driver.find_element_by_xpath("""//*[@id="tShowLiquidadorIdentificacion"]/tbody/tr[4]/td[2]""")
    atliq45 = driver.find_element_by_xpath("""//*[@id="tShowLiquidadorIdentificacion"]/tbody/tr[5]/td""")
    atliqsus15 = driver.find_element_by_xpath("""//*[@id="tShowLiquidadorIdentificacion"]/tbody/tr[7]/td""")
    print(str1+atliq43.text+str1+atliq44.text+str1+atliq45.text+str1+atliqsus15.text)
    driver.find_element_by_xpath("""//*[@id="dlgShowLiquidador"]/div[1]/a""").click()
    time.sleep(0.5)

elementos()

def cambio_pag():
    driver.find_element_by_xpath("""//*[@id="tblLiquidadores"]/div[2]/span[3]/span[2]""").click()
    time.sleep(0.5)
    elementos()
    time.sleep(0.5)
    driver.find_element_by_xpath("""//*[@id="tblLiquidadores"]/div[2]/span[3]/span[3]""").click()
    time.sleep(0.5)
    elementos()
    time.sleep(0.5)
    driver.find_element_by_xpath("""//*[@id="tblLiquidadores"]/div[2]/span[3]/span[4]""").click()
    time.sleep(0.5)
    elementos()
    time.sleep(0.5)
    driver.find_element_by_xpath("""//*[@id="tblLiquidadores"]/div[2]/span[3]/span[5]""").click()
    time.sleep(0.5)
    elementos()
    time.sleep(0.5)
    driver.find_element_by_xpath("""//*[@id="tblLiquidadores"]/div[2]/span[3]/span[6]""").click()
    time.sleep(0.5)
    elementos()
    time.sleep(0.5)

cambio_pag()

os.system("taskkill /im chromedriver.exe")

  






