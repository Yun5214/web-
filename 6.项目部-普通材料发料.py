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
前置:    1.确保网页为初始状态
        2.确保材料已经签收入库
        3.普通发料前需手工对产品进行试验检测
'''

# 点击物资管理
driver.find_element(By.CSS_SELECTOR, ".el-submenu:nth-child(3) > .el-submenu__title").click()

# 点击普通材料发料
driver.find_element(By.CSS_SELECTOR, "a:nth-child(4) > .el-menu-item").click()

# 点击新增发料单
driver.find_element(By.CSS_SELECTOR, ".add-staff > span").click()
sleep(1)

# 选择出库对象
driver.find_element(By.CSS_SELECTOR, ".el-col:nth-child(2) .el-input__inner").click()
sleep(1)
driver.find_element(By.XPATH, "/html/body/div[3]/div[1]/div[1]/ul/li[3]").click()

# 选择分包单位
driver.find_element(By.CSS_SELECTOR, ".el-col:nth-child(3) .el-input__inner").click()
driver.find_element(By.XPATH, "/html/body/div[4]/div[1]/div[1]/ul/li").click()

# 选择出库仓库
driver.find_element(By.CSS_SELECTOR, ".el-col:nth-child(4) .el-input__inner").click()
driver.find_element(By.XPATH, "/html/body/div[5]/div[1]/div[1]/ul/li[1]/span").click()

# 关联入库单
element_to_click = driver.find_element(By.CSS_SELECTOR, 'div:nth-child(1) > .el-select .el-select__input')
# 模拟点击
actions = ActionChains(driver)
actions.move_to_element(element_to_click).click().perform()
# 滚动到底部
list_container = driver.find_element(By.CSS_SELECTOR, 'body > div.el-select-dropdown.el-popper.is-multiple > div.el-scrollbar > div.el-select-dropdown__wrap.el-scrollbar__wrap')
driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight;", list_container)
# sleep(0.5)
# 点击最后一个元素(最新的入库单)
driver.find_element(By.XPATH, '/html/body/div[6]/div[1]/div[1]/ul/li[last()]/span').click()

# 关联申请单（第一个；最新的申请单）
driver.find_element(By.CSS_SELECTOR, ".el-select__input:nth-child(1)").click()
# sleep(0.5)
driver.find_element(By.XPATH, "/html/body/div[7]/div[1]/div[1]/ul/li[1]/span").click()

# 添加收获地址
driver.find_element(By.CSS_SELECTOR, ".el-col-24 .el-input__inner").send_keys("广州市从化区广从南路")

# 添加备注
driver.find_element(By.CSS_SELECTOR, ".el-textarea__inner").send_keys("112")

# # 保存草稿
# driver.find_element(By.XPATH, '//*[@id="app"]/div/section/section/main/section/div/div[3]/div[1]/div[3]/div/button[1]').click()

# 确认单据
driver.find_element(By.CSS_SELECTOR, ".certainty").click()


sleep(1)
# 返回单据编号
dh = driver.find_element(By.XPATH, '//td[2]/div')
print("本次普通材料发料的单据编号为:", dh.text)

# 返回出库对象
project1 = driver.find_element(By.XPATH, '//td[3]/div')
print("本次普通材料发料出库对象为:", project1.text)

# 返回关联入库单
project1 = driver.find_element(By.XPATH, '//td[4]/div')
print("本次普通材料发料关联入库单为:", project1.text)

# 返回关联物资申请单
relevance = driver.find_element(By.XPATH, '//td[5]/div')
print("本次普通材料发料关联物资申请单为：", relevance.text)

# 返回填表人
preparer = driver.find_element(By.XPATH, '//td[6]/div')
print("本次普通材料发料的填表人为:", preparer.text)

# 返回单据时间
time = driver.find_element(By.XPATH, '//td[7]/div')
print("本次普通材料发料单据时间为:", time.text)

# 返回状态
state = driver.find_element(By.XPATH, '//td[8]/div')
print("本次普通材料发料的状态为:", state.text)

# 记录结束时间
end_time = datetime.now()
execution_time = end_time - start_time
print(f"脚本执行时间: {execution_time.total_seconds():.2f} 秒")
