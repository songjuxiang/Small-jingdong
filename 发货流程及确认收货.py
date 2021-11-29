
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains
dr = webdriver.Chrome()
dr.maximize_window()
dr.implicitly_wait(20)


#登录前台
# def login(username, password):
#     dr.get('http://newecshop.longtest.cn/user.php')
#     dr.find_element('id', 'username').send_keys(username)
#     dr.find_element('id', 'password').send_keys(password)
#     dr.find_element('name', 'submit').click()
#     print('登录成功')
#
#
# def Goods_search(keywords):
#     dr.find_element('name', 'keywords').send_keys(keywords)
#     dr.find_element(By.XPATH, '//*[@id="searchForm"]/div/input').click()
#     dr.find_element(By.XPATH, '//*[@id="li_162"]/div/div[2]/a/img').click()
#     print('搜索商品')
#
#     t = dr.window_handles
#     print(t)
#     dr.switch_to.window(t[1])
#     print(dr.title)
#
#
#
#
# def shopping(name, dizhi, mobile):
#     dr.find_element(By.XPATH, '// *[ @ id = "xuan_a_233"] / div / img').click()
#     dr.find_element(By.XPATH, '//*[@id="choose-btns"]/a[1]').click()
#     print('点击直接购买')
#     dr.find_element(By.XPATH, '/html/body/div[8]/div[2]/a[1]').click()
#     sleep(3)
#     print('关闭设置地址的弹窗')
#     dr.find_element('name', 'consignee').send_keys(name)
#     print('输入收货人姓名')
#     dr.find_element(By.XPATH, '//*[@id="selProvinces"]/option[1]').click()
#     dr.find_element(By.XPATH, '//*[@id="selProvinces"]/option[2]').click()
#     print('选择北京市')
#     dr.find_element(By.XPATH, '//*[@id="selCities"]/option').click()
#     dr.find_element(By.XPATH, '//*[@id="selCities"]/option[2]').click()
#     print('选择北京市')
#     sleep(3)
#     dr.find_element(By.XPATH, '//*//*[@id="selDistricts"]/option[1]').click()
#     dr.find_element(By.XPATH, '//*[@id="selDistricts"]/option[14]').click()
#     print('选择昌平区')
#     dr.find_element('name', 'address').send_keys(dizhi)
#     print('输入地址详情')
#     dr.find_element('name', 'mobile').send_keys(mobile)
#     print('输入手机号')
#     dr.find_element(By.XPATH, '//*[@id="AddressList"]/table/tbody/tr[8]/td[2]/input[4]').click()
#     sleep(3)
#     print('确定地址')
#
# def pay():
#     dr.find_element(By.XPATH, '//*[@id="alipay_bank_input"]').click()
#     dr.find_element(By.XPATH, '//*[@id="payment_tab"]/li[1]/div/ul/li[1]/label/img').click()
#     print('选择支付宝和银行卡')
#     dr.find_element(By.XPATH, '//*[@id="theForm"]/div[6]/div[2]/input[1]').click()
#     print('支付弹框点击确定')
#
#     # dr.find_element(By.XPATH, '//*[@id="payment_tab"]/li[2]/input').click()
    # print('点击货到付款')
    # dr.find_element(By.XPATH, '//*[@id="theForm"]/div[6]/div[2]/input[1]').click()
    # print('确认订单')



#登录后台
def Login(username,password):
    dr.get('http://newecshop.longtest.cn/admin/privilege.php?act=login')
    username=dr.find_element(By.NAME,'username').send_keys(username)
    password=dr.find_element(By.NAME,'password').send_keys(password)
    login_btn=dr.find_element(By.CLASS_NAME,'button2').click()
    sleep(3)


def Fahuo(ordernum):
    dr.switch_to.frame('menu_frame')  # 切入菜单框架
    dr.find_element(By.XPATH, '//*[@id="menu-ul"]/li/ul/li[7]/a').click()
    print('点击订单管理')
    dr.find_element(By.XPATH, '//*[@id="04_order"]/ul/li[1]/a').click()
    print('点击订单列表')
    dr.switch_to.parent_frame()  # 切出框架
    dr.switch_to.frame('main-frame')  # 切入main框架
    dr.find_element(By.XPATH, '//*[@id="order_sn"]').send_keys(ordernum)
    print('订单号搜索')
    dr.find_element(By.XPATH, '//*[@id="listDiv"]/table[1]/tbody/tr[3]/td[9]/a').click()
    print('点击查看')
    dr.find_element(By.XPATH, '/html/body/form/div[4]/table/tbody/tr[3]/td[2]/input[1]').click()
    print('点击确认')
    sleep(4)
    dr.find_element(By.XPATH, '/html/body/form/div[4]/table/tbody/tr[3]/td[2]/input[1]').click()
    print('点击付款')
    sleep(4)
    dr.find_element(By.XPATH, '/html/body/form/div[1]/table/tbody/tr[5]/td[2]/a').click()
    print('点击编辑')
    sleep(3)
    dr.find_element(By.XPATH, '/html/body/form/p/input[1]').click()
    print('点击确定')
    sleep(3)
    dr.find_element(By.XPATH, '/html/body/form/div[4]/table/tbody/tr[3]/td[2]/input[2]').click()
    print('点击一键发货')

#登录前台
def login(username, password):
    dr.get('http://newecshop.longtest.cn/user.php')
    dr.find_element('id', 'username').send_keys(username)
    dr.find_element('id', 'password').send_keys(password)
    dr.find_element('name', 'submit').click()
    print('登录成功')



def shouhuo():
    mouse = ActionChains(dr)  # 生成一个鼠标生成的对象
    mouse.move_to_element(dr.find_element('xpath', '//*[@id="site-nav"]/div/ul/li[1]/div/a')).perform()
    sleep(2)
    dr.find_element('link text', '已买到的宝贝').click()
    print('点击我的信息-已买到的宝贝')
    dr.find_element(By.XPATH, '/html/body/div[6]/div[4]/div/table/tbody[1]/tr[3]/td[8]/font/a').click()
    print('点击确认收货')
    alert=dr.switch_to.alert
    alert.accept()
    sleep(3)
    print('关闭提醒收货的弹窗')

# login('hs01', '123456')
# Goods_search('HTC One M9w 联通4G手机')
# shopping('hs', '北京昌平区沙河', '18888888888')
# pay()
Login('test01','test888')
Fahuo('2021110591904')
login('hs01', '123456')
shouhuo()