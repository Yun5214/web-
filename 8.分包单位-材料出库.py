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
     2.确保材料已签收入库
'''

# 点击项目管理
driver.find_element(By.CSS_SELECTOR, ".el-submenu:nth-child(3) > .el-submenu__title").click()

# 点击物资管理
driver.find_element(By.CSS_SELECTOR, ".el-submenu:nth-child(1) > .el-submenu__title").click()

# 点击库存管理
driver.find_element(By.CSS_SELECTOR, ".el-submenu:nth-child(1) a:nth-child(2) span").click()

# 点击出入库管理
driver.find_element(By.CSS_SELECTOR, "li:nth-child(5) > div:nth-child(2)").click()
sleep(0.5)

# 点击新增出库单
driver.find_element(By.CSS_SELECTOR, ".right span").click()

# 选择出库对象，选择施工单位
driver.find_element(By.CSS_SELECTOR, ".dialog-form-item:nth-child(2) .el-select .el-input__inner").click()

driver.find_element(By.XPATH, "/html/body/div[3]/div[1]/div[1]/ul/li[1]").click()
sleep(0.5)

# 选择标段项目
driver.find_element(By.CSS_SELECTOR, ".dialog-form-item:nth-child(3) .el-select .el-input__inner").click()
driver.find_element(By.CSS_SELECTOR, "div:nth-child(7) > div.el-scrollbar > div.el-select-dropdown__wrap.el-scrollbar__wrap > ul > li").click()

# 选择出库仓库
driver.find_element(By.CSS_SELECTOR, ".dialog-form-item:nth-child(4) .el-select .el-input__inner").click()
driver.find_element(By.CSS_SELECTOR, "div:nth-child(8) > div.el-scrollbar > div.el-select-dropdown__wrap.el-scrollbar__wrap > ul > li").click()

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
driver.find_element(By.XPATH, '/html/body/div[1]/div/section/section/main/section/div/div[6]/div[2]/div/div[2]/div/div[1]/div[5]/div[2]/div/div[2]/div/div[3]/div[2]/div[2]/div[2]/div[2]/div[1]/label/span/span').click()

# 选择关联入库单
element_to_click1 = driver.find_element(By.CSS_SELECTOR, '.el-select__input')
# 模拟点击
actions = ActionChains(driver)
actions.move_to_element(element_to_click1).click().perform()
# 滚动到底部
list_container = driver.find_element(By.CSS_SELECTOR, 'body > div.el-select-dropdown.el-popper.is-multiple > div.el-scrollbar > div.el-select-dropdown__wrap.el-scrollbar__wrap')
driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight;", list_container)
# sleep(0.5)
# 选择最后一个元素（最新关联入库单）
driver.find_element(By.XPATH, '/html/body/div[6]/div[1]/div[1]/ul/li[last()]/span').click()

# 填写收货地址
driver.find_element(By.CSS_SELECTOR, ".el-col-24 .el-input__inner").send_keys("广州市从化区太平镇广从南路")

# 填写备注
driver.find_element(By.CSS_SELECTOR, ".el-textarea__inner").send_keys("112")

# 运输信息
# 车牌号
driver.find_element(By.CSS_SELECTOR, ".dialog-form-item:nth-child(2) > .content > .el-input > .el-input__inner").send_keys("粤A·zwb66")

# 运输司机
driver.find_element(By.CSS_SELECTOR, ".dialog-form-item:nth-child(3) > .content > .el-input > .el-input__inner").send_keys("周某人")

# 联系方式
driver.find_element(By.CSS_SELECTOR, ".dialog-form-item:nth-child(4) > .content > .el-input > .el-input__inner").send_keys("13421195888")

# 选择签收状态（已签收）
driver.find_element(By.CSS_SELECTOR, ".el-radio:nth-child(2) .el-radio__inner").click()
# 填写签收人
driver.find_element(By.CSS_SELECTOR, ".dialog-form-item:nth-child(6) > .content > .el-input > .el-input__inner").send_keys("周人某")
# 选择签收时间
driver.find_element(By.CSS_SELECTOR, ".dialog-form-item:nth-child(7) .el-date-editor > .el-input__inner").click()
sleep(0.5)
# 选择此刻
driver.find_element(By.CSS_SELECTOR, ".el-button--text > span").click()

# 填写单价（默认是与关联入库单一致）
dj = driver.find_element(By.XPATH, "//td[8]/div/div/input")
dj.clear()
dj.send_keys('40')

# 填写出库数量（默认是与关联入库单一致）
much = driver.find_element(By.XPATH, "//td[9]/div/div/input")
much.clear()
much.send_keys('40')

# # 点击保存草稿
# driver.find_element(By.CSS_SELECTOR, ".el-dialog__footer:nth-child(3) .el-button:nth-child(1) > span").click()
# sleep(2)

# 点击确定出库
driver.find_element(By.CSS_SELECTOR, ".el-dialog__footer:nth-child(3) .el-button:nth-child(2) > span").click()
sleep(2.5)

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