
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

dr = webdriver.Chrome()
dr.maximize_window()
dr.implicitly_wait(20)
dr.get('http://newecshop.longtest.cn/user.php')

def login(username,password):
    dr.find_element('id','username').send_keys(username)
    dr.find_element('id','password').send_keys(password)
    dr.find_element('name','submit').click()
    print('登录成功')

def buy(keywords):
    dr.find_element('name','keywords').send_keys(keywords)
    dr.find_element(By.XPATH, '//*[@id="searchForm"]/div/input').click()
    dr.find_element(By.XPATH,'//*[@id="li_1698"]/div/div[2]/a/img').click()
    print('搜索商品')

    t = dr.window_handles
    print(t)
    dr.switch_to.window(t[1])
    print(dr.title)
sleep(3)
def shopping(name,province,city,district,address,mobile):
    dr.find_element(By.XPATH,'//*[@id="choose-btns"]/a[2]').click()
    print('点击加入购物车')
    dr.find_element(By.XPATH,'//*[@id="mc-menu-hd"]').click()
    print('点击购物车，跳转到购物车页面')
    dr.find_element(By.XPATH,'/html/body/div[5]/div[4]/table/tbody/tr/td[4]/a').click()
    print('点击去结算')
    dr.find_element(By.XPATH,'/html/body/div[8]/div[2]/a[1]').click()
    sleep(3)
    print('关闭设置地址的弹窗')
    # dr.find_element(By.XPATH,'//*[@id="address_edit_0"]/a[2]').click()
    # print('点击删除地址')
    # sleep(3)
    # dr.find_element(By.XPATH,'/html/body/div[8]/div[2]/a[1]').click()
    # print('确认删除地址')
    # sleep(2)
    dr.find_element('name','consignee').send_keys(name)
    print('输入收货人姓名')

    # sheng = dr.find_elements_by_name("province")[0]
    # Select(sheng).select_by_visible_text(province)
    # print('选择省份')
    # shi = dr.find_elements_by_name("city")[0]
    # Select(shi).select_by_visible_text(city)
    # print('选择城市')
    # qu = dr.find_elements_by_name("district")[0]
    # Select(qu).select_by_visible_text(district)
    # print('选择地区')

    #选择省
    sheng = dr.find_elements(By.ID,"selProvinces")[0]
    Select(sheng).select_by_visible_text(province)
    #选择市
    shi = dr.find_elements(By.ID, "selCities")[0]
    Select(shi).select_by_visible_text(city)
    #选择区
    qu = dr.find_elements(By.ID, "selDistricts")[0]
    Select(qu).select_by_visible_text(district)

    dr.find_element('name','address').send_keys(address)
    print('输入地址详情')
    dr.find_element('name','mobile').send_keys(mobile)
    print('输入手机号')
    dr.find_element(By.XPATH,'//*[@id="AddressList"]/table/tbody/tr[8]/td[2]/input[4]').click()
    sleep(3)
    print('确定地址')
    dr.find_element(By.XPATH, '//*[@id="payment_tab"]/li[2]/input').click()
    print('选择货到付款')
    dr.find_element(By.XPATH,'//*[@id="theForm"]/div[6]/div[2]/input[1]').click()
    print('确认订单')
login('lilifang','qqqq1111')
buy('lilifang')
shopping('lilifang','北京','北京','海淀区','昌平区立水桥明天生活馆','18310161102')

