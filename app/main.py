from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import os
import time
import re

print("Test Execution Started")
options = webdriver.ChromeOptions()
options.add_argument('--ignore-ssl-errors=yes')
options.add_argument('--ignore-certificate-errors')
driver = webdriver.Remote(
        command_executor="http://" +  os.environ.get('SELENIUM_HOST', "localhost") + ":4444/wd/hub",
        options=options
        )
driver.maximize_window()
time.sleep(1)
#navigate to browserstack.com
driver.get("https://www.imprensaoficial.com.br/DO/BuscaDO2001Resultado_11_3.aspx?filtropalavraschave=CPF&f=xhitlist&xhitlist_vpc=next&xhitlist_x=Advanced&xhitlist_q=%5bfield+%27dc%3adatapubl%27%3a%3e%3d01.01.2023%3c%3d13.09.2023%5d(CPF)&filtrogrupos=Todos%2c+Cidade+de+SP%2c+Editais+e+Leil%c3%b5es%2c+Empresarial%2c+Executivo%2c+Junta+Comercial%2c+DOU-Justi%c3%a7a%2c+Judici%c3%a1rio%2c+DJE%2c+Legislativo%2c+Municipios%2c+OAB%2c+Suplemento%2c+TRT+&xhitlist_mh=9999&filtrodatafimsalvar=20230913&filtroperiodo=01%2f01%2f2023+a+13%2f09%2f2023&filtrodatainiciosalvar=20230101&filtrogrupossalvar=Todos%2c+Cidade+de+SP%2c+Editais+e+Leil%c3%b5es%2c+Empresarial%2c+Executivo%2c+Junta+Comercial%2c+DOU-Justi%c3%a7a%2c+Judici%c3%a1rio%2c+DJE%2c+Legislativo%2c+Municipios%2c+OAB%2c+Suplemento%2c+TRT+&xhitlist_hc=%5bXML%5d%5bKwic%2c3%5d&xhitlist_vps=15&filtrotodosgrupos=True&xhitlist_d=Todos%2c+Cidade+de+SP%2c+Editais+e+Leil%c3%b5es%2c+Empresarial%2c+Executivo%2c+Junta+Comercial%2c+DOU-Justi%c3%a7a%2c+Judici%c3%a1rio%2c+DJE%2c+Legislativo%2c+Municipios%2c+OAB%2c+Suplemento%2c+TRT+&filtrotipopalavraschavesalvar=UP&xhitlist_s=&xhitlist_sel=title%3bField%3adc%3atamanho%3bField%3adc%3adatapubl%3bField%3adc%3acaderno%3bitem-bookmark%3bhit-context&xhitlist_xsl=xhitlist.xsl&navigators=")
next = 3
#WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'a.joyride-close-tip')))
try:
    driver.find_element(By.CSS_SELECTOR, 'a.joyride-close-tip').click()
except:
    print ('skip tutorial')

filecsv = open("output.txt", "w")

while next:
    table_data = driver.find_elements(By.XPATH, '/html/body/form/div[3]/div/div[2]') #/div[2]/div[1]/div[2]')
    for row in table_data:
        columns = row.find_elements(By.XPATH,"./div/div") #/d/a # Use dot in the xpath to find elements with in element.
        for column in columns:
            textline = column.text
            if len(re.findall('[0-9]', textline )) > 11:
                filecsv.writelines(textline) #(table_row)
                filecsv.flush()
    try:
        driver.find_element(By.CSS_SELECTOR, 'a#content_hplProximaFooter.page-link').click()
        next = 1
        print ("next page")
        WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'a#content_hplProximaFooter.page-link')))
    except:
        print ('no link')
        next = 0
    #next = driver.find_element(By.XPATH, '//a[@id="content_hplProximaFooter"]')
    #next = driver.find_element(By.ID, 'content_hplProximaFooter').click()
    #WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH,  '//span[@id="content_hplProximaFooter"]'))).click()
filecsv.close()
#close the browser
driver.close()
driver.quit()

print("Test Execution Successfully Completed!")
