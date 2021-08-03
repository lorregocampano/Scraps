from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException

chrome_path= ".\\chromedriver.exe"
options = Options()
options.add_argument("--headless") 
options.add_argument('--no-sandbox') 
options.add_argument('--disable-gpu')  
options.add_argument('start-maximized')  
options.add_argument('disable-infobars')
options.add_argument("--disable-extensions")
driver = webdriver.Chrome(chrome_options=options, executable_path=r'.\\chromedriver.exe')
text_file = open("OutputIPC 1975-2006.txt", "a")
text_file2 = open("OutputIPC 2007-2021.txt", "a")
for x in range (1975,1979):
    print ("https://www.sii.cl/pagina/valores/utm/utm"+str(x)+".htm")
    driver.get("https://www.sii.cl/pagina/valores/utm/utm"+str(x)+".htm")
    table_elements = WebDriverWait(driver, 0.3).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "#contenido > table.tabla")))
    for table_element in table_elements:
        for row in table_element.find_elements_by_css_selector("#contenido > table.tabla > tbody > tr"):
            text_file.write(str(x)+";"+str(row.text)+'\n')
            print(str(row.text))

for x in range (1979,1986):
    print ("https://www.sii.cl/pagina/valores/utm/utm"+str(x)+".htm")
    driver.get("https://www.sii.cl/pagina/valores/utm/utm"+str(x)+".htm")
    table_elements = WebDriverWait(driver, 0.3).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "#contenido > table.tabla")))
    for table_element in table_elements:
        for row in table_element.find_elements_by_css_selector("#contenido > table.tabla > tbody > tr"):
            text_file.write(str(x)+str(";")+str(" ")+str(";")+str(row.text)+'\n')
            print(str(row.text))

for x in range (1986,1987):
    print ("https://www.sii.cl/pagina/valores/utm/utm"+str(x)+".htm")
    driver.get("https://www.sii.cl/pagina/valores/utm/utm"+str(x)+".htm")
    table_elements = WebDriverWait(driver, 0.3).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "#contenido > center:nth-child(1) > table")))
    for table_element in table_elements:
        for row in table_element.find_elements_by_css_selector("#contenido > center:nth-child(1) > table > tbody > tr"):
            text_file.write(str(x)+str(";")+str(" ")+str(";")+str(row.text)+'\n')
            print(str(row.text))

for x in range (1987,2002):
    print ("https://www.sii.cl/pagina/valores/utm/utm"+str(x)+".htm")
    driver.get("https://www.sii.cl/pagina/valores/utm/utm"+str(x)+".htm")
    table_elements = WebDriverWait(driver, 0.3).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "#contenido > table.tabla")))
    for table_element in table_elements:
        for row in table_element.find_elements_by_css_selector("#contenido > table.tabla > tbody > tr"):
            text_file.write(str(x)+str(";")+str(" ")+str(";")+str(row.text)+'\n')
            print(str(row.text))

for x in range (2002,2007):
    print ("https://www.sii.cl/pagina/valores/utm/utm"+str(x)+".htm")
    driver.get("https://www.sii.cl/pagina/valores/utm/utm"+str(x)+".htm")
    table_elements = WebDriverWait(driver, 0.3).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "#contenido > table.tabla")))
    for table_element in table_elements:
        for row in table_element.find_elements_by_css_selector("#contenido > table.tabla > tbody > tr"):
            text_file.write(str(x)+";"+str(row.text)+'\n')
            print(str(row.text))

for x in range (2007,2013):
    print ("https://www.sii.cl/pagina/valores/utm/utm"+str(x)+".htm")
    driver.get("https://www.sii.cl/pagina/valores/utm/utm"+str(x)+".htm")
    table_elements = WebDriverWait(driver, 0.3).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "#contenido > table.tabla")))
    for table_element in table_elements:
        for row in table_element.find_elements_by_css_selector("#contenido > table.tabla > tbody > tr"):
            text_file2.write(str(x)+";"+str(row.text)+'\n')
            print(str(row.text))

for x in range (2013,2022):
   
    print ("https://www.sii.cl/valores_y_fechas/utm/utm"+str(x)+".htm")
    driver.get("https://www.sii.cl/valores_y_fechas/utm/utm"+str(x)+".htm")
    table_elements = WebDriverWait(driver, 0.3).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "#table_export")))
    for table_element in table_elements:
        for row in table_element.find_elements_by_css_selector("#table_export > tbody > tr"):
            text_file2.write(str(x)+";"+str(row.text)+'\n')
            print(str(row.text))

print("Extracción terminada...")
