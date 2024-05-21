# 导入selenium
from time import sleep
from datetime import datetime
from selenium import webdriver

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
# 输入网址,提前登录且验证，进入相对应的供应商角色
driver.get("https://erp.jianwangkeji.cn/#/home/home")


'''
前置：1.确保网页为初始状态
     2.打开项目部新增采购计划单中关联的供应商
'''
# 打开项目管理
driver.find_element(By.CSS_SELECTOR, ".el-submenu:nth-child(3) > .el-submenu__title").click()

# 打开物资管理
driver.find_element(By.CSS_SELECTOR, ".el-submenu:nth-child(1) > .el-submenu__title").click()

# 打开供货申请单
driver.find_element(By.CSS_SELECTOR, ".el-submenu:nth-child(1) a:nth-child(1) > .el-menu-item").click()
sleep(1)

# 点击新增物资申请单
driver.find_element(By.CSS_SELECTOR, ".add-staff > span").click()
sleep(1)

# 选择标段项目 非select下拉框
driver.find_element(By.CSS_SELECTOR, ".is-required .el-select .el-input__inner").click()
sleep(0.5)
driver.find_element(By.XPATH, '/html/body/div[3]/div[1]/div[1]/ul/li/span').click()

# 选择关联采购计划单,默认选择第一个 非select下拉框
driver.find_element(By.XPATH, "//div[4]/div/div/div/div/input").click()
sleep(0.5)
driver.find_element(By.XPATH, "/html/body/div[4]/div[1]/div[1]/ul/li[1]/span").click()

# 填写备注
driver.find_element(By.CSS_SELECTOR, ".el-textarea__inner").send_keys("112")

# 填写物料单价
clear = driver.find_element(By.XPATH, "//td[7]/div/div/input")
clear.clear()
clear.send_keys('40')

# 填写供货数量
driver.find_element(By.XPATH, "//td[8]/div/div/input").send_keys("100")

# 保存草稿
# driver.find_element(By.CSS_SELECTOR, ".certainty:nth-child(1) > span").click()
# sleep(1)

# 申请供货
driver.find_element(By.CSS_SELECTOR, ".certainty:nth-child(2) > span").click()
sleep(1)

# 返回供货申请单号
dh = driver.find_element(By.XPATH, '//td[2]/div')
print("本次供货申请单号为:", dh.text)

# 返回供货对象
supplier = driver.find_element(By.XPATH, '//td[3]/div')
print("本次供货对象为:", supplier.text)

# 返回关联采购计划单
relevance = driver.find_element(By.XPATH, '//td[4]/div')
print("本次关联采购计划单：", relevance.text)

# 返回填表人
preparer = driver.find_element(By.XPATH, '//td[5]/div')
print("本次供货申请的填表人为:", preparer.text)

# 返回单据时间
time = driver.find_element(By.XPATH, '//td[6]/div')
print("本次供货申请的单据时间为:", time.text)

# 返回状态
state = driver.find_element(By.XPATH, '//td[7]/div')
print("本次供货申请的状态为:", state.text)

# 返回备注
remark = driver.find_element(By.XPATH, '//td[8]/div')
print("本次供货申请的备注为:", remark.text)

# 记录结束时间
end_time = datetime.now()
execution_time = end_time - start_time
print(f"脚本执行时间: {execution_time.total_seconds():.2f} 秒")
