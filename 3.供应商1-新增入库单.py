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
前置: 1.确保网页为初始状态
     2.打开项目部新增采购计划单中关联的供应商
     3.手工审核供应商对采购计划单进行确认
     4.打印单据前确保无单据被置顶，新入库单能正常输出在第一行(草稿和退货处理会被置顶)
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
# 切换到入库界面
driver.find_element(By.CSS_SELECTOR, ".el-radio-button:nth-child(2) > .el-radio-button__inner").click()

# 点击新增入库单
driver.find_element(By.CSS_SELECTOR, ".right > .el-button:nth-child(2)").click()
# sleep(0.5)

# 默认仓库为：首个仓库
driver.find_element(By.XPATH, '//*[@id="app"]/div/section/section/main/section/div/div[6]/div[3]/div/div[2]/div/div[1]/div[1]/div[3]/div[2]/div/div/input').click()
# sleep(2)
driver.find_element(By.XPATH, '/html/body/div[3]/div[1]/div[1]/ul/li[1]').click()

# 填写签收人
driver.find_element(By.CSS_SELECTOR, ".dialog-form-item:nth-child(7) .el-input__inner").send_keys("周蔚彬")

# 填写备注
driver.find_element(By.CSS_SELECTOR, ".el-textarea__inner").send_keys("112")

# 点击选择物料
driver.find_element(By.CSS_SELECTOR, ".selectFac > .el-input__inner").click()
# 查询物料
driver.find_element(By.CSS_SELECTOR, ".el-form-item:nth-child(2) .wh-140 > .el-input__inner").send_keys("片石")
# 点击查询
driver.find_element(By.CSS_SELECTOR, ".ml-20:nth-child(3) > span").click()
sleep(0.5)

# 选择物料
driver.find_element(By.XPATH, "//button[contains(.,'选择')]").click()


# 输入单价
driver.find_element(By.XPATH, "(//input[@type='text'])[17]").send_keys("20")

# 输入数量
driver.find_element(By.XPATH, "(//input[@type='text'])[18]").send_keys("100")
# sleep(1)

# 保存草稿
# driver.find_element(By.CSS_SELECTOR, ".el-dialog__footer:nth-child(3) .el-button:nth-child(1) > span").click()
# sleep(2)

# 确认提交
driver.find_element(By.CSS_SELECTOR, ".el-dialog__footer:nth-child(3) .el-button:nth-child(2) > span").click()
sleep(1)

# 返回单据编号
dh = driver.find_element(By.XPATH, '//td[2]/div')
print("本次入库单据编号为:", dh.text)

# 返回入库仓库
warehouse = driver.find_element(By.XPATH, '//td[3]/div')
print("本次入库仓库为:", warehouse.text)

# 返回单据对象
project1 = driver.find_element(By.XPATH, '//td[4]/div')
print("本次入库的单据对象为:", project1.text)

# 返回关联单据
relevance = driver.find_element(By.XPATH, '//td[5]/div')
print("本次入库的关联单据为：", relevance.text)

# 返回填表人
preparer = driver.find_element(By.XPATH, '//td[6]/div')
print("本次入库的填表人为:", preparer.text)

# 返回单据时间
time = driver.find_element(By.XPATH, '//td[7]/div')
print("本次入库的单据时间为:", time.text)

# 返回单据类型
type1 = driver.find_element(By.XPATH, '//td[8]/div')
print("本次入库的单据类型为:", type1.text)

# 返回状态
state = driver.find_element(By.XPATH, '//td[9]/div')
print("本次入库的状态为:", state.text)

# 记录结束时间
end_time = datetime.now()
execution_time = end_time - start_time
print(f"脚本执行时间: {execution_time.total_seconds():.2f} 秒")

