# 导入selenium
from time import sleep

from selenium import webdriver
from datetime import datetime
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
# 输入网址,提前登录且验证，进入项目部角色
driver.get("https://erp.jianwangkeji.cn/#/home/home")

'''
前置：1.确保网页为初始状态
     2.手工审核物资申请单后再执行新增采购计划单
'''
# 点击物资管理
driver.find_element(By.CSS_SELECTOR, '.el-submenu:nth-child(3) > .el-submenu__title').click()

# 点击普通材料采购
driver.find_element(By.CSS_SELECTOR, 'a:nth-child(3) > .el-menu-item').click()
sleep(1)

# 点击新增采购计划单
driver.find_element(By.CSS_SELECTOR, '.add-staff > span').click()
# sleep(0.5)

# 打开下拉选框关联物资申请单
driver.find_element(By.CSS_SELECTOR, ".el-select__input").click()
# sleep(1)

# 默认关联第一个物资申请单
driver.find_element(By.XPATH, "//div[3]/div/div/ul/li/span").click()
# sleep(0.5)

# driver.find_element(By.CSS_SELECTOR, ".wh > .el-input__inner").click()
# 填写收货地址
driver.find_element(By.CSS_SELECTOR, ".wh > .el-input__inner").send_keys("广州市从化区广从南路广州软件学院")
# driver.find_element(By.CSS_SELECTOR, ".el-textarea__inner").click()

# 填写备注
driver.find_element(By.CSS_SELECTOR, ".el-textarea__inner").send_keys("112")

# # 保存草稿
# driver.find_element(By.CSS_SELECTOR, ".certainty:nth-child(1) > span").click()

# 提交单据
driver.find_element(By.CSS_SELECTOR, ".certainty:nth-child(2) > span").click()

sleep(1)
# 返回单据编号
dh = driver.find_element(By.XPATH, '//td[2]/div')
print("本次采购计划单的单据编号为:", dh.text)

# 返回供应商
supplier = driver.find_element(By.XPATH, '//td[3]/div')
print("本次采购计划单供应商为:", supplier.text)

# 返回关联物资申请单
project1 = driver.find_element(By.XPATH, '//td[4]/div')
print("本次采购计划单关联物资申请单为:", project1.text)

# 返回填表人
preparer = driver.find_element(By.XPATH, '//td[5]/div')
print("本次采购计划单的填表人为:", preparer.text)

# 返回单据时间
time = driver.find_element(By.XPATH, '//td[6]/div')
print("本次采购计划单单据时间为:", time.text)

# 返回状态
state = driver.find_element(By.XPATH, '//td[7]/div')
print("本次采购计划单的状态为:", state.text)

# 返回备注
remark = driver.find_element(By.XPATH, '//td[8]/div')
print("本次采购计划单的备注为:", remark.text)

# 记录结束时间
end_time = datetime.now()
execution_time = end_time - start_time
print(f"脚本执行时间: {execution_time.total_seconds():.2f} 秒")




