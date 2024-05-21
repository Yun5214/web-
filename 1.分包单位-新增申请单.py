# 导入selenium
from time import sleep
import time
from selenium import webdriver
from datetime import datetime

from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

options = Options()
options.add_experimental_option("debuggerAddress", "127.0.0.1:9527")

# 选择谷歌浏览器
driver = webdriver.Chrome(options=options)
driver.implicitly_wait(10)
# 记录开始时间
start_time = datetime.now()
# 输入网址,提前登录且验证，进入分包单位角色
driver.get("https://erp.jianwangkeji.cn/#/home/home")

'''
前置：1.确保网页为初始状态
'''
# 点击项目管理
driver.find_element(By.XPATH, '//*[text()="项目管理"]').click()
# xm = WebDriverWait(driver, 10, 2).until(lambda x: x.find_element(By.XPATH, '//div[@class="el-submenu__title"]//*[text()="项目管理"]'))
# xm.click()

# 点击物资管理
# driver.find_element(By.XPATH, '//div/span[text()="物资管理"]').click()
wz = WebDriverWait(driver, 10, 2).until(lambda x: x.find_element(By.CSS_SELECTOR, '.nest-menu .el-submenu__title'))
wz.click()

# 点击物资申请单
# driver.find_element(By.XPATH, '//a[href="#/supplies/request"]/span[text()="物资申请单"]').click()
sq = WebDriverWait(driver, 10, 2).until(lambda x: x.find_element(By.XPATH, '//li[2]/ul/div/li/ul/a/li'))
sq.click()
sleep(1)

# 点击新增申请单
driver.find_element(By.CSS_SELECTOR, '.add-staff>span').click()

# 选择关联项目
driver.find_element(By.CSS_SELECTOR, '.input>.el-input__inner').click()

# 选择分项工程
element_to_click = driver.find_element(By.CSS_SELECTOR, '.input > .el-input__inner')
# 模拟点击
actions = ActionChains(driver)
actions.move_to_element(element_to_click).click().perform()
# 滚动到底部
list_container = driver.find_element(By.CSS_SELECTOR, '.treeBox')
driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight;", list_container)
# sleep(0.5)
# 点击与材料相关联的工程
driver.find_element(By.XPATH, '/html/body/div[1]/div/section/section/main/section/div/div[3]/div[1]/div[2]/div/div[1]/form/div/div[5]/div/div/div[1]/div[2]/div/div[3]/div[2]/div[2]/div[2]/div[2]/div[1]/label/span/span').click()
# 选择路基工程
# driver.find_element(By.CSS_SELECTOR, '.el-tree > .el-tree-node:nth-child(1)>.el-tree-node__content .el-checkbox__inner').click()
# sleep(1)

# 添加备注
driver.find_element(By.CSS_SELECTOR, '.el-textarea__inner').send_keys("666")
# sleep(1)

# 选择物料
driver.find_element(By.XPATH, '//input[@placeholder="点击选择物料"]').click()
# sleep(0.5)

# 选择片石
driver.find_element(By.XPATH, '(//button[@type="button"])[79]').click()
# sleep(1)

# 添加数量
driver.find_element(By.XPATH, '(//input[@type="text"])[13]').send_keys('100')
# sleep(1)

# # 保存草稿
# driver.find_element(By.XPATH, '//div[2]/button[1]/span').click()

# 提交单据
driver.find_element(By.XPATH, '//div[2]/button[2]/span').click()
sleep(1)

# 返回单据编号
dh = driver.find_element(By.XPATH, '//td[2]/div')
print("本次申请单的单据编号为:", dh.text)

# 返回标段项目
project = driver.find_element(By.XPATH, '//td[3]/div')
print("本次申请单的标段项目为:", project.text)

# 返回关联项目
project1 = driver.find_element(By.XPATH, '//td[4]/div')
print("本次申请单的关联项目为:", project1.text)

# 返回填表人
preparer = driver.find_element(By.XPATH, '//td[5]/div')
print("本次申请单的填表人为:", preparer.text)

# 返回单据时间
time = driver.find_element(By.XPATH, '//td[6]/div')
print("本次申请单的申请时间:", time.text)

# 返回状态
state = driver.find_element(By.XPATH, '//td[7]/div')
print("本次申请单的状态为:", state.text)

# 返回备注
remark = driver.find_element(By.XPATH, '//td[8]/div')
print("本次申请单的备注为:", remark.text)

# 记录结束时间
end_time = datetime.now()
execution_time = end_time - start_time
print(f"脚本执行时间: {execution_time.total_seconds():.2f} 秒")









