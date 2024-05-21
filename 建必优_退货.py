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
# 隐式等待
driver.implicitly_wait(10)
# 记录开始时间
start_time = datetime.now()
# 输入网址,提前登录且验证，进入分包单位角色
driver.get("https://erp.jianwangkeji.cn/#/home/home")

'''
前置：1.确保打开谷歌浏览器调试并已登录
     2.确保一开始进入分包单位角色
     3.确保网页为初始状态
     4.确保仓库中有相关材料
     5.确保供应商1新增入库单处理无其他原因被置顶的入库单（草稿和退货处理会被置顶）
     6.确保未处理单号不多，未处理单号过多则关联下拉框中不会显示最新单号（容器溢出部分不可见）！！！
'''


# 角色切换
sub = "广州软件学院-分包单位"
project = "广州软件学院-项目部"
supplier = "广州软件学院-供应商1"

# 切换角色
def Switch(name):
    driver.find_element(By.CSS_SELECTOR, '.user-size:nth-child(2)').click()
    driver.find_element(By.XPATH, '//li[text()="切换账号"]').click()
    sleep(0.5)
    switch = driver.find_element(By.XPATH, '//div[text()="%s"]' %name)
    switch.click()
# 分包单位-物资管理
def sub1():
    # 点击项目管理
    # driver.find_element(By.XPATH, '//*[text()="项目管理"]').click()
    xm = WebDriverWait(driver, 10, 2).until(lambda x: x.find_element(By.XPATH, '//*[text()="项目管理"]'))
    xm.click()
    # 点击物资管理
    # driver.find_element(By.XPATH, '//div/span[text()="物资管理"]').click()
    wz = WebDriverWait(driver, 10, 2).until(lambda x: x.find_element(By.CSS_SELECTOR, '.nest-menu .el-submenu__title'))
    wz.click()

def supplier1():
    # 打开项目管理
    driver.find_element(By.CSS_SELECTOR, ".el-submenu:nth-child(3) > .el-submenu__title").click()
    # 打开物资管理
    driver.find_element(By.CSS_SELECTOR, ".el-submenu:nth-child(1) > .el-submenu__title").click()

def project1():
    # 点击物资管理
    sq = WebDriverWait(driver, 10, 2).until(lambda x: x.find_element(By.CSS_SELECTOR, '.el-submenu:nth-child(3) > .el-submenu__title'))
    sq.click()
    # 审核物资申请单/供货单
    driver.find_element(By.CSS_SELECTOR, 'a:nth-child(2) > .el-menu-item').click()

def project2():
    # 点击物资管理
    sq = WebDriverWait(driver, 10, 2).until(lambda x: x.find_element(By.CSS_SELECTOR, '.el-submenu:nth-child(3) > .el-submenu__title'))
    sq.click()
    # 点击库存管理
    driver.find_element(By.CSS_SELECTOR, "a:nth-child(7) span").click()
    # 点击出入库管理
    driver.find_element(By.CSS_SELECTOR, "li:nth-child(4) > div:nth-child(2)").click()
    sleep(0.5)
    # 进入入库界面
    driver.find_element(By.CSS_SELECTOR, '.el-radio-button:nth-child(2) > .el-radio-button__inner').click()
    sleep(0.5)
def supplier2():
    # 打开库存管理
    driver.find_element(By.CSS_SELECTOR, '.el-submenu:nth-child(1) a:nth-child(3) > .el-menu-item').click()
    # 打开出入库管理
    driver.find_element(By.CSS_SELECTOR, "li:nth-child(4) > div:nth-child(2)").click()
    sleep(0.5)
    # 切换到入库界面
    driver.find_element(By.CSS_SELECTOR, ".el-radio-button:nth-child(2) > .el-radio-button__inner").click()

# 分包单位-物资申请单
sub1()
# 点击物资申请单
# driver.find_element(By.XPATH, '//a[href="#/supplies/request"]/span[text()="物资申请单"]').click()
sq = WebDriverWait(driver, 10, 2).until(lambda x: x.find_element(By.CSS_SELECTOR, '#app > div > section > section > aside > ul > div > li:nth-child(3) > ul > div > li > ul > a:nth-child(1) > li'))
sq.click()
sleep(1)
# 点击新增申请单
driver.find_element(By.CSS_SELECTOR, '.add-staff>span').click()
sleep(1)
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
sleep(0.5)
# 点击与材料相关联的工程
driver.find_element(By.XPATH, '/html/body/div[1]/div/section/section/main/section/div/div[3]/div[1]/div[2]/div/div[1]/form/div/div[5]/div/div/div[1]/div[2]/div/div[3]/div[2]/div[2]/div[2]/div[2]/div[1]/label/span/span').click()
# driver.find_element(By.CSS_SELECTOR, '.input > .el-input__inner').click()
# sleep(0.5)
# driver.find_element(By.XPATH, '//*[@id="app"]/div/section/section/main/section/div/div[3]/div/div[2]/div/div[1]/form/div/div[5]/div/div/div[1]/div[2]/div/div[1]/div[2]/div/div[2]/div[4]/div[1]/label/span/span').click()
# 添加备注
driver.find_element(By.CSS_SELECTOR, ".el-textarea__inner").send_keys("112")
# 选择物料
driver.find_element(By.XPATH, '//input[@placeholder="点击选择物料"]').click()
sleep(0.5)
# 选择片石
driver.find_element(By.XPATH, '(//button[@type="button"])[79]').click()
# 添加数量
driver.find_element(By.XPATH, '(//input[@type="text"])[13]').send_keys('100')
# # 保存草稿
# driver.find_element(By.XPATH, '//div[2]/button[1]/span').click()
sleep(1)
# 提交单据
driver.find_element(By.XPATH, '//div[2]/button[2]/span').click()
sleep(1)
print("………………………………………………………………分包单位物资申请单…………………………………………………………………………")
# 返回单据编号
SQ_dh = driver.find_element(By.XPATH, '//td[2]/div')
print("本次申请单的单据编号为:", SQ_dh.text)
# 返回标段项目
SQ_project = driver.find_element(By.XPATH, '//td[3]/div')
print("本次申请单的标段项目为:", SQ_project.text)
# 返回关联项目
SQ_project1 = driver.find_element(By.XPATH, '//td[4]/div')
print("本次申请单的关联项目为:", SQ_project1.text)
# 返回填表人
SQ_preparer = driver.find_element(By.XPATH, '//td[5]/div')
print("本次申请单的填表人为:", SQ_preparer.text)
# 返回单据时间
SQ_time = driver.find_element(By.XPATH, '//td[6]/div')
print("本次申请单的申请时间:", SQ_time.text)
# 返回状态
SQ_state = driver.find_element(By.XPATH, '//td[7]/div')
print("本次申请单的状态为:", SQ_state.text)
# 返回备注
SQ_remark = driver.find_element(By.XPATH, '//td[8]/div')
print("本次申请单的备注为:", SQ_remark.text)
# 记录单据编号
sub_sq = SQ_dh.text

# 切换到项目部
Switch(project)
sleep(3)
# project1()
# 点击物资管理
# driver.find_element(By.CSS_SELECTOR, '.el-submenu:nth-child(3) > .el-submenu__title').click()
# sq = WebDriverWait(driver, 10, 2).until(lambda x: x.find_element(By.CSS_SELECTOR, '.el-submenu:nth-child(3) > .el-submenu__title'))
# sq.click()
# # 审核分包单位的物资申请单
# driver.find_element(By.CSS_SELECTOR, 'a:nth-child(2) > .el-menu-item').click()
project1()
driver.find_element(By.CSS_SELECTOR, '.el-form-item:nth-child(4) .el-input__inner').send_keys(sub_sq)
driver.find_element(By.CSS_SELECTOR, '.seek').click()
sleep(0.5)
driver.find_element(By.CSS_SELECTOR, '.el-button--success > span').click()
sleep(0.5)
driver.find_element(By.CSS_SELECTOR, '.dialog-footer > .certainty:nth-child(1)').click()
# 点击普通材料采购
driver.find_element(By.CSS_SELECTOR, 'a:nth-child(3) > .el-menu-item').click()
sleep(1)
# 点击新增采购计划单
driver.find_element(By.CSS_SELECTOR, '.add-staff > span').click()
sleep(1)
# 打开下拉选框关联物资申请单
driver.find_element(By.CSS_SELECTOR, ".el-select__input").click()
sleep(0.5)
xpath_1 = '//span[text()="%s"]' % sub_sq
element1 = driver.find_element(By.XPATH, xpath_1)
element1.click()
# 关联记录的申请单号
# driver.find_element(By.CSS_SELECTOR, ".el-select__input").send_keys(sub_sq)
# 填写收货地址
driver.find_element(By.CSS_SELECTOR, ".wh > .el-input__inner").send_keys("广州市从化区广从南路广州软件学院")
# driver.find_element(By.CSS_SELECTOR, ".el-textarea__inner").click()
# 填写备注
driver.find_element(By.CSS_SELECTOR, ".el-textarea__inner").send_keys("112")
# # 保存草稿
# driver.find_element(By.CSS_SELECTOR, ".certainty:nth-child(1) > span").click()
# sleep(1)
# 提交单据
driver.find_element(By.CSS_SELECTOR, ".certainty:nth-child(2) > span").click()
sleep(1)
print("………………………………………………………………项目部新增采购计划单…………………………………………………………………………")
# 返回单据编号
JH_dh = driver.find_element(By.XPATH, '//td[2]/div')
print("本次采购计划单的单据编号为:", JH_dh.text)
# 返回供应商
JH_supplier = driver.find_element(By.XPATH, '//td[3]/div')
print("本次采购计划单供应商为:", JH_supplier.text)
# 返回关联物资申请单
JH_project1 = driver.find_element(By.XPATH, '//td[4]/div')
print("本次采购计划单关联物资申请单为:", JH_project1.text)
# 返回填表人
JH_preparer = driver.find_element(By.XPATH, '//td[5]/div')
print("本次采购计划单的填表人为:", JH_preparer.text)
# 返回单据时间
JH_time = driver.find_element(By.XPATH, '//td[6]/div')
print("本次采购计划单单据时间为:", JH_time.text)
# 返回状态
JH_state = driver.find_element(By.XPATH, '//td[7]/div')
print("本次采购计划单的状态为:", JH_state.text)
# 返回备注
JH_remark = driver.find_element(By.XPATH, '//td[8]/div')
print("本次采购计划单的备注为:", JH_remark.text)
# 记录采购计划单单号
project_jh = JH_dh.text
sleep(1)

# 切换到供应商1
Switch(supplier)
# 无选中"广州软件学院-供应商1"
# driver.find_element(By.CSS_SELECTOR, '.user-size:nth-child(2)').click()
# driver.find_element(By.XPATH, '//li[text()="切换账号"]').click()
# driver.find_element(By.XPATH, '/html/body/div[1]/div/section/header/div/div[8]/div/div[2]/div[4]/div[2]/div/div[2]/div[1]').click()
sleep(3)
supplier1()
sleep(1)
# 处理采购计划单
driver.find_element(By.CSS_SELECTOR, '.el-submenu:nth-child(1) a:nth-child(2) > .el-menu-item').click()
driver.find_element(By.CSS_SELECTOR, '.el-form-item:nth-child(4) .el-input__inner').send_keys(project_jh)
driver.find_element(By.CSS_SELECTOR, '.seek').click()
sleep(0.5)
driver.find_element(By.CSS_SELECTOR, '.el-button--success > span').click()
sleep(0.5)
driver.find_element(By.CSS_SELECTOR, '.dialog-footer > .certainty:nth-child(1)').click()

# # 打开库存管理
# driver.find_element(By.CSS_SELECTOR, '.el-submenu:nth-child(1) a:nth-child(3) > .el-menu-item').click()
# # 打开出入库管理
# driver.find_element(By.CSS_SELECTOR, "li:nth-child(4) > div:nth-child(2)").click()
# sleep(0.5)
# # 切换到入库界面
# driver.find_element(By.CSS_SELECTOR, ".el-radio-button:nth-child(2) > .el-radio-button__inner").click()
supplier2()
# 点击新增入库单
driver.find_element(By.CSS_SELECTOR, ".right > .el-button:nth-child(2)").click()
# sleep(0.5)
# 默认仓库为：首个仓库
# driver.find_element(By.XPATH, '//*[@id="app"]/div/section/section/main/section/div/div[6]/div[3]/div/div[2]/div/div[1]/div[1]/div[3]/div[2]/div/div/input').click()
# sleep(1)
# driver.find_element(By.XPATH, '//*[text()="建优组专用库"]').click()
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
XZ_dh = driver.find_element(By.XPATH, '//td[2]/div')
# 记录入库单单号
supplier_xz = XZ_dh.text
# 材料入库
driver.find_element(By.CSS_SELECTOR, '.el-form-item:nth-child(4) .el-input__inner').send_keys(supplier_xz)
driver.find_element(By.CSS_SELECTOR, '.ml-20 > span').click()
sleep(0.5)
driver.find_element(By.CSS_SELECTOR, '.el-button:nth-child(4)').click()
sleep(0.5)
driver.find_element(By.CSS_SELECTOR, '.el-dialog__footer:nth-child(3) .el-button-primary > span').click()
sleep(1.5)
print("………………………………………………………………供应商1新增入库单…………………………………………………………………………")
# 返回单据编号
print("本次入库单据编号为:", XZ_dh.text)
# 返回入库仓库
XZ_warehouse = driver.find_element(By.XPATH, '//td[3]/div')
print("本次入库仓库为:", XZ_warehouse.text)
# 返回单据对象
XZ_project1 = driver.find_element(By.XPATH, '//td[4]/div')
print("本次入库的单据对象为:", XZ_project1.text)
# 返回关联单据
XZ_relevance = driver.find_element(By.XPATH, '//td[5]/div')
print("本次入库的关联单据为：", XZ_relevance.text)
# 返回填表人
XZ_preparer = driver.find_element(By.XPATH, '//td[6]/div')
print("本次入库的填表人为:", XZ_preparer.text)
# 返回单据时间
XZ_time = driver.find_element(By.XPATH, '//td[7]/div')
print("本次入库的单据时间为:", XZ_time.text)
# 返回单据类型
XZ_type1 = driver.find_element(By.XPATH, '//td[8]/div')
print("本次入库的单据类型为:", XZ_type1.text)
# 返回状态
XZ_state = driver.find_element(By.XPATH, '//td[9]/div')
print("本次入库的状态为:", XZ_state.text)
driver.find_element(By.XPATH, '//div[@id="app"]/div/section/section/main/section/div/div[6]/div/div/div/button/i')
driver.back()

# 发起供货申请单
# 打开供货申请单
driver.find_element(By.CSS_SELECTOR, ".el-submenu:nth-child(1) a:nth-child(1) > .el-menu-item").click()
sleep(1)
# 点击新增物资申请单
driver.find_element(By.CSS_SELECTOR, ".add-staff > span").click()
sleep(1)
# 选择标段项目 非select下拉框
driver.find_element(By.CSS_SELECTOR, ".is-required .el-select .el-input__inner").click()
sleep(1)
driver.find_element(By.CSS_SELECTOR, 'body > div.el-select-dropdown.el-popper > div.el-scrollbar > div.el-select-dropdown__wrap.el-scrollbar__wrap > ul > li').click()
# 选择关联采购计划单,默认选择第一个 非select下拉框
driver.find_element(By.XPATH, "//div[4]/div/div/div/div/input").click()
sleep(0.5)
xpath_2 = '//span[text()="%s"]' % project_jh
element2 = driver.find_element(By.XPATH, xpath_2)
element2.click()
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
sleep(2)
print("………………………………………………………………供应商1供货申请单…………………………………………………………………………")
# 返回供货申请单号
GSQ_dh = driver.find_element(By.XPATH, '//td[2]/div')
print("本次供货申请单号为:", GSQ_dh.text)
# 返回供货对象
GSQ_supplier = driver.find_element(By.XPATH, '//td[3]/div')
print("本次供货对象为:", GSQ_supplier.text)
# 返回关联采购计划单
GSQ_relevance = driver.find_element(By.XPATH, '//td[4]/div')
print("本次关联采购计划单：", GSQ_relevance.text)
# 返回填表人
GSQ_preparer = driver.find_element(By.XPATH, '//td[5]/div')
print("本次供货申请的填表人为:", GSQ_preparer.text)
# 返回单据时间
GSQ_time = driver.find_element(By.XPATH, '//td[6]/div')
print("本次供货申请的单据时间为:", GSQ_time.text)
# 返回状态
GSQ_state = driver.find_element(By.XPATH, '//td[7]/div')
print("本次供货申请的状态为:", GSQ_state.text)
# 返回备注
GSQ_remark = driver.find_element(By.XPATH, '//td[8]/div')
print("本次供货申请的备注为:", GSQ_remark.text)
# 记录供货申请单号
gh_dh = GSQ_dh.text

# 切换到项目部
Switch(project)
sleep(3)
# 处理供货申请单
project1()
sleep(0.5)
driver.find_element(By.CSS_SELECTOR, '#tab-2').click()
sleep(0.5)
driver.find_element(By.CSS_SELECTOR, '.el-form-item:nth-child(4) .el-input__inner').send_keys(gh_dh)
driver.find_element(By.CSS_SELECTOR, '.seek').click()
sleep(0.5)
driver.find_element(By.CSS_SELECTOR, '.el-button--success > span').click()
sleep(0.5)
driver.find_element(By.CSS_SELECTOR, ' .certainty:nth-child(1)').click()

# 切换到供应商1
Switch(supplier)
# 无选中"广州软件学院-供应商1"
# driver.find_element(By.CSS_SELECTOR, '.user-size:nth-child(2)').click()
# driver.find_element(By.XPATH, '//li[text()="切换账号"]').click()
# driver.find_element(By.XPATH, '/html/body/div[1]/div/section/header/div/div[8]/div/div[2]/div[4]/div[1]/div/div[2]/div[1]').click()
sleep(3)
supplier1()
driver.find_element(By.CSS_SELECTOR, '.el-submenu:nth-child(1) a:nth-child(3) > .el-menu-item').click()
# 打开出入库管理
driver.find_element(By.CSS_SELECTOR, "li:nth-child(4) > div:nth-child(2)").click()
sleep(0.5)
# 点击新增出库单
driver.find_element(By.CSS_SELECTOR, ".right span").click()
# 选择出库对象
driver.find_element(By.CSS_SELECTOR, ".dialog-form-item:nth-child(2) .el-select .el-input__inner").click()
driver.find_element(By.XPATH, "/html/body/div[3]/div[1]/div[1]/ul/li[2]").click()
# 选择供货申请单
# 打开下拉选框选择供货申请单
driver.find_element(By.XPATH, "//div[3]/div[2]/div/div/input").click()
sleep(1)
xpath_3 = '//span[text()="%s"]' % gh_dh
element3 = driver.find_element(By.XPATH, xpath_3)
element3.click()
# driver.find_element(By.XPATH, "//div[3]/div[2]/div/div/input").click()
# driver.find_element(By.XPATH, "/html/body/div[3]/div[1]/div[1]/ul/li[2]/span").click()
# 选择出库仓库
driver.find_element(By.CSS_SELECTOR, ".dialog-form-item:nth-child(5) .el-input__inner").click()
driver.find_element(By.XPATH, "//span[text()='建优组专用库']").click()
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
print("………………………………………………………………供应商1新增出库单…………………………………………………………………………")
# 返回单据编号
CK_dh = driver.find_element(By.XPATH, '//td[2]/div')
print("本次出库单据编号为:", CK_dh.text)
# 返回关联单据
CK_relevance = driver.find_element(By.XPATH, '//td[3]/div')
print("本次出库的关联单据为：", CK_relevance.text)
# 返回出库时间
CK_time = driver.find_element(By.XPATH, '//td[4]/div')
print("本次出库的单据时间为:", CK_time.text)
# 返回填表人
CK_preparer = driver.find_element(By.XPATH, '//td[5]/div')
print("本次出库的填表人为:", CK_preparer.text)
# 返回单据时间
CK_time1 = driver.find_element(By.XPATH, '//td[6]/div')
print("本次出库的单据时间为:", CK_time1.text)
# 返回出库对象
CK_project1 = driver.find_element(By.XPATH, '//td[7]/div')
print("本次出库对象为:", CK_project1.text)
# 返回状态
CK_state = driver.find_element(By.XPATH, '//td[8]/div')
print("本次出库的状态为:", CK_state.text)
# 记录出库单单号
supplier_ck = CK_dh.text
driver.back()
sleep(1)


# 切换到项目部
Switch(project)
sleep(3)
project2()
# 记录入库单号
rk_dh = driver.find_element(By.XPATH, '//td[2]/div')
project_RK = rk_dh.text
driver.find_element(By.XPATH, '//button[3]').click()
# 选择入库仓库
driver.find_element(By.XPATH, '/html/body/div[1]/div/section/section/main/section/div/div[7]/div[3]/div/div[2]/div/div[1]/div[1]/div[3]/div[2]/div/div/input').click()
sleep(0.5)
driver.find_element(By.XPATH, '/html/body/div[3]/div[1]/div[1]/ul/li[2]').click()
driver.find_element(By.CSS_SELECTOR, ' .el-button-primary:nth-child(3)').click()
driver.back()

# 点击生产管理
driver.find_element(By.CSS_SELECTOR, '.el-submenu:nth-child(2) > .el-submenu__title').click()
# 点击试验检测
driver.find_element(By.CSS_SELECTOR, ".is-opened .el-menu-item").click()
sleep(0.5)
# 查询
driver.find_element(By.CSS_SELECTOR, '.el-form-item:nth-child(4) .el-input__inner').send_keys(project_RK)
driver.find_element(By.CSS_SELECTOR, '.el-icon-search').click()
sleep(0.5)
# 检测
driver.find_element(By.CSS_SELECTOR, '.is-plain:nth-child(1)').click()
sleep(0.5)
# 填写检测人
driver.find_element(By.CSS_SELECTOR, '.el-col:nth-child(4) .el-input__inner').send_keys("周某人")
# 填写检测报告
driver.find_element(By.CSS_SELECTOR, '.el-textarea__inner').send_keys("112")
# 选择合格
driver.find_element(By.CSS_SELECTOR, '.cell .el-input__inner').click()
driver.find_element(By.XPATH, '/html/body/div[3]/div[1]/div[1]/ul/li[2]').click()
sleep(0.5)
# 点击保存
driver.find_element(By.CSS_SELECTOR, '.el-button-primary:nth-child(1) > span').click()
sleep(1)

# 项目部材料退货
project2()
driver.find_element(By.CSS_SELECTOR, '.el-form-item:nth-child(4) .el-input__inner').send_keys(project_RK)
driver.find_element(By.CSS_SELECTOR, '.ml-20 > span').click()
sleep(0.5)
# 点击退货
driver.find_element(By.CSS_SELECTOR, '.el-table__row:nth-child(1) .el-button:nth-child(6)').click()
# 填写退回地址
driver.find_element(By.CSS_SELECTOR, '.dialog-form-item:nth-child(9) .el-input__inner').send_keys("广州市从化区太平镇广从南路")
# 填写备注
driver.find_element(By.CSS_SELECTOR, '.el-col-24:nth-child(5) .el-input__inner').send_keys("材料试验检测不合格！")
# 运输信息
driver.find_element(By.CSS_SELECTOR, '.dashedDiv:nth-child(6) > .dialog-form-item:nth-child(2) .el-input__inner').send_keys("粤A·zwb66")
driver.find_element(By.CSS_SELECTOR, '.dashedDiv:nth-child(6) > .dialog-form-item:nth-child(3) .el-input__inner').send_keys("周某人")
driver.find_element(By.CSS_SELECTOR, '.dashedDiv:nth-child(6) > .dialog-form-item:nth-child(4) .el-input__inner').send_keys("13421195888")
# 确认退货
driver.find_element(By.CSS_SELECTOR, '.el-dialog__footer:nth-child(3) .el-button-primary > span').click()
driver.back()
sleep(2)

Switch(supplier)
sleep(3)
supplier1()
supplier2()
# 点击处理
driver.find_element(By.CSS_SELECTOR, '.el-table__row:nth-child(1) .el-button:nth-child(3) > span').click()
sleep(0.5)
# 填写备注
driver.find_element(By.CSS_SELECTOR, '.el-textarea__inner').send_keys('检测不合格')
# 确认签收入库
driver.find_element(By.CSS_SELECTOR, '.el-dialog__footer:nth-child(3) .el-button:nth-child(2) > span').click()
print("………………………………………………………………项目部退货成功…………………………………………………………………………")


# 记录结束时间
end_time = datetime.now()
execution_time = end_time - start_time
print(f"脚本执行时间: {execution_time.total_seconds():.2f} 秒")





























