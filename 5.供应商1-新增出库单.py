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
前置：
      1.确保网页为初始状态
      2.打开项目部新增采购计划单中关联的供应商
      3.确定有被项目部审批通过的相对应材料的供货申请单（一个供货申请单只能关联一次）
      4.确保仓库材料充足
'''

# 打开项目管理
driver.find_element(By.CSS_SELECTOR, ".el-submenu:nth-child(3) > .el-submenu__title").click()

# 打开物资管理
driver.find_element(By.CSS_SELECTOR, ".el-submenu:nth-child(1) > .el-submenu__title").click()

# 打开库存管理
driver.find_element(By.CSS_SELECTOR, ".el-submenu:nth-child(1) a:nth-child(3) > .el-menu-item").click()

# 打开出入库管理
driver.find_element(By.CSS_SELECTOR, "li:nth-child(4) > div:nth-child(2)").click()
sleep(0.5)

# 点击新增出库单
driver.find_element(By.CSS_SELECTOR, ".right span").click()
# sleep(1)

# 选择出库对象
driver.find_element(By.CSS_SELECTOR, ".dialog-form-item:nth-child(2) .el-select .el-input__inner").click()
driver.find_element(By.XPATH, "/html/body/div[3]/div[1]/div[1]/ul/li[2]").click()

# 选择供货申请单
driver.find_element(By.XPATH, "//div[3]/div[2]/div/div/input").click()
driver.find_element(By.XPATH, "/html/body/div[3]/div[1]/div[1]/ul/li[2]/span").click()
# sleep(1)

# 选择出库仓库
driver.find_element(By.CSS_SELECTOR, ".dialog-form-item:nth-child(5) .el-input__inner").click()
driver.find_element(By.XPATH, "/html/body/div[3]/div[1]/div[1]/ul/li[1]/span").click()

# 填写收获地址
driver.find_element(By.CSS_SELECTOR, ".el-col-24 .el-input__inner").send_keys("广州市从化区广从南路")

# 填写备注
driver.find_element(By.CSS_SELECTOR, ".el-textarea__inner").send_keys("112")

# 填写运输信息
# 车牌号
driver.find_element(By.CSS_SELECTOR, ".dialog-form-item:nth-child(2) > .content > .el-input > .el-input__inner").send_keys("粤V·zwb66")
# 运输司机
driver.find_element(By.CSS_SELECTOR, ".dialog-form-item:nth-child(3) > .content > .el-input > .el-input__inner").send_keys("周某人")
# 联系方式
driver.find_element(By.CSS_SELECTOR, ".dashedDiv > .dialog-form-item:nth-child(4) .el-input__inner").send_keys("13421195888")

# 填写物料单价（有默认值）
clear = driver.find_element(By.XPATH, "(//input[@type='text'])[19]")
clear.clear()
clear.send_keys('30')

# 本次出库数量
driver.find_element(By.XPATH, "(//input[@type='text'])[20]").send_keys('100')

# 保存草稿
# driver.find_element(By.CSS_SELECTOR, '.el-dialog__footer:nth-child(3) .el-button:nth-child(1)')
# sleep(1)

# 确定出库
driver.find_element(By.CSS_SELECTOR, '.el-dialog__footer:nth-child(3) .el-button:nth-child(2)').click()
# WebDriverWait(driver, 10, 0.5).until(lambda x: x.find_element(By.CSS_SELECTOR, '.el-dialog__footer:nth-child(3) .el-button:nth-child(2)')).click()
sleep(3)

# 返回单据编号
dh = driver.find_element(By.XPATH, '//td[2]/div')
print("本次出库单据编号为:", dh.text)

# 返回关联单据
relevance = driver.find_element(By.XPATH, '//td[3]/div')
print("本次出库的关联单据为：", relevance.text)

# 返回出库时间
time = driver.find_element(By.XPATH, '//td[4]/div')
print("本次出库的单据时间为:", time.text)

# 返回填表人
preparer = driver.find_element(By.XPATH, '//td[5]/div')
print("本次出库的填表人为:", preparer.text)

# 返回单据时间
time1 = driver.find_element(By.XPATH, '//td[6]/div')
print("本次出库的单据时间为:", time1.text)

# 返回出库对象
project1 = driver.find_element(By.XPATH, '//td[7]/div')
print("本次出库对象为:", project1.text)

# 返回状态
state = driver.find_element(By.XPATH, '//td[8]/div')
print("本次出库的状态为:", state.text)

# 记录结束时间
end_time = datetime.now()
execution_time = end_time - start_time
print(f"脚本执行时间: {execution_time.total_seconds():.2f} 秒")