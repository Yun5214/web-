# 导入selenium
from time import sleep

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
# 输入网址,提前登录且验证，进入项目部角色
driver.get("https://erp.jianwangkeji.cn/#/home/home")

'''
前置：1.确保网页为初始状态
     2.确保材料已签收入库
     3.材料试验检测为合格发货分包单位
'''

# 点击物资管理
driver.find_element(By.CSS_SELECTOR, ".el-submenu:nth-child(3) > .el-submenu__title").click()

# 点击库存管理
driver.find_element(By.CSS_SELECTOR, "a:nth-child(7) span").click()

# 点击出入库管理
driver.find_element(By.CSS_SELECTOR, "li:nth-child(4) > div:nth-child(2)").click()
sleep(0.5)

# 新增出库单
driver.find_element(By.CSS_SELECTOR, ".right > .el-button").click()

# 选择出库对象（分包单位）
driver.find_element(By.CSS_SELECTOR, ".dialog-form-item:nth-child(2) .el-select .el-input__inner").click()
# sleep(1)
driver.find_element(By.XPATH, "/html/body/div[3]/div[1]/div[1]/ul/li[3]").click()

# 选择出库仓库
driver.find_element(By.CSS_SELECTOR, ".dialog-form-item:nth-child(3) .el-select .el-input__inner").click()

driver.find_element(By.XPATH, "/html/body/div[4]/div[1]/div[1]/ul/li").click()

# 选择分包单位
driver.find_element(By.CSS_SELECTOR, ".dialog-form-item:nth-child(4) .el-select .el-input__inner").click()
# sleep(1)
driver.find_element(By.CSS_SELECTOR, "body > div:nth-child(8) > div.el-scrollbar > div.el-select-dropdown__wrap.el-scrollbar__wrap > ul > li").click()

# 选择关联发料单
driver.find_element(By.CSS_SELECTOR, ".dialog-form-item:nth-child(5) .el-select .el-input__inner").click()
driver.find_element(By.XPATH, "/html/body/div[6]/div[1]/div[1]/ul/li[2]/span").click()

# 添加备注
driver.find_element(By.CSS_SELECTOR, ".el-textarea__inner").send_keys("112")

# 运输信息
# 车牌号
driver.find_element(By.CSS_SELECTOR, ".dialog-form-item:nth-child(2) > .content > .el-input > .el-input__inner").send_keys("粤A·zwb66")
# 运输司机
driver.find_element(By.CSS_SELECTOR, ".dialog-form-item:nth-child(3) > .content > .el-input > .el-input__inner").send_keys("周某人")
# 联系方式
driver.find_element(By.CSS_SELECTOR, ".dialog-form-item:nth-child(4) > .content > .el-input > .el-input__inner").send_keys("13421195888")


# # 填写单价(默认价格是供应商提供的价格)
# dj = driver.find_element(By.XPATH, '//td[8]/div/div/input')
# dj.clear()
# dj.send_keys('50')
#
# # 填写本次出库数量
# much = driver.find_element(By.XPATH, '//td[9]/div/div/input')
# much.clear()
# much.send_keys('50')

# 保存草稿
# driver.find_element(By.XPATH, "//div[3]/div/button[1]/span").click()
# sleep(1)

# # 确定出库
driver.find_element(By.XPATH, "//div[3]/div/button[2]/span").click()
sleep(3.5)

# 返回单据编号
dh = driver.find_element(By.XPATH, '//td[2]/div')
print("本次出库单据编号为:", dh.text)

# 返回关联单据
relevance = driver.find_element(By.XPATH, '//td[3]/div')
print("本次出库的关联单据为：", relevance.text)

# 返回出库时间
time = driver.find_element(By.XPATH, '//td[4]/div')
print("本次出库时间为:", time.text)

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