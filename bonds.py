from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time
num_bonds = 23 ## change this to # of total bonds in your data file
driver = webdriver.Chrome()
driver.get("https://www.treasurydirect.gov/BC/SBCPrice")
calculate = driver.find_element_by_css_selector('#content > form > div > div.col1 > div > input')


def read_data(file_name, num_bonds, num_features):
    bond_vec = list()
    bond_mat = list()
    file = open(file_name)
    col_num = 0
    for line in file:
        row = line.split(",")
        if (col_num < num_bonds) or (num_bonds == -1):
            if num_features > 0:
                bond_vec = [(row[v]) for v in range(0, num_features)]
            bond_mat.append(bond_vec)
            col_num += 1
    return bond_vec, bond_mat

v,m = read_data("bonds.data", num_bonds, 4) ## change file name here if needed
print(m)

def enter_info(bond_mat):
    for bond_num in range(len(bond_mat)):
        series_drop_down = driver.find_element_by_css_selector('#content > form > div > div.col1 > table > tbody > tr:nth-child(5) > td.ls > select')
        series_drop_down.click()
        series_type_file = bond_mat[bond_num][0]
        if(series_type_file == "I"):   
            series_type_input = driver.find_element_by_css_selector('#content > form > div > div.col1 > table > tbody > tr:nth-child(5) > td.ls > select > option:nth-child(2)')
        else:
            series_type_input = driver.find_element_by_css_selector('#content > form > div > div.col1 > table > tbody > tr:nth-child(5) > td.ls > select > option:nth-child(1)')
        series_type_input.click()
        series_drop_down.click()

        denomination_drop_down = driver.find_element_by_css_selector('#content > form > div > div.col1 > table > tbody > tr:nth-child(5) > td:nth-child(2) > select')
        denomination_drop_down.click()
        denomination_file = bond_mat[bond_num][1]
        print(denomination_file)
        if(denomination_file == "50"):
            denomination_input = driver.find_element_by_xpath('//*[@id="content"]/form/div/div[1]/table/tbody/tr[5]/td[2]/select/option[3]')
        if(denomination_file == "100"):
            denomination_input = driver.find_element_by_xpath('//*[@id="content"]/form/div/div[1]/table/tbody/tr[5]/td[2]/select/option[5]')
        if(denomination_file == "200"):
            denomination_input = driver.find_element_by_xpath('//*[@id="content"]/form/div/div[1]/table/tbody/tr[5]/td[2]/select/option[6]')
        if(denomination_file == "500"):
            denomination_input = driver.find_element_by_xpath('//*[@id="content"]/form/div/div[1]/table/tbody/tr[5]/td[2]/select/option[7]')
        if(denomination_file == "1000"):
            denomination_input = driver.find_element_by_xpath('//*[@id="content"]/form/div/div[1]/table/tbody/tr[5]/td[2]/select/option[8]')
        denomination_input.click()
        serial_num = bond_mat[bond_num][2]
        driver.find_element_by_name("SerialNumber").send_keys(serial_num)
        issue_date = bond_mat[bond_num][3]
        driver.find_element_by_name("IssueDate").send_keys(issue_date)
    calculate_button = driver.find_element_by_css_selector('#content > form > div > div.col1 > div > input')
    calculate_button.click()
enter_info(m)
