from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

from selenium.webdriver.support.select import Select

dr = webdriver.Chrome()
dr.maximize_window()
dr.implicitly_wait(20)


def login(username, password):
    dr.get('http://newecshop.longtest.cn/user.php?act=login')
    dr.find_element(By.ID, 'username').send_keys(username)
    dr.find_element(By.ID, 'password').send_keys(password)
    dr.find_element(By.ID, 'loginsubmit').click()





def search(commodity):
    # 点击首页
    dr.find_element(By.XPATH, "//*[text()='首页']").click()

    # 点击搜索框
    dr.find_element(By.ID, "keyword").send_keys(commodity)
    # 点击搜索
    dr.find_element(By.XPATH, "//*[@id='searchForm']/div/input").click()
    dr.find_elements(By.XPATH, "//li[contains(@id,li_)]")[122].click()
    # 点击商品
    # dr.find_element(By.XPATH,"//*[@id='li_1801']/div").click()
    # 切换窗口

    all_windows = dr.window_handles
    dr.switch_to.window(all_windows[1])
    # 点击立即购买
    dr.find_element(By.XPATH, "//*[@id='choose-btns']/a[1]").click()





# 输入收货地址
def receiver_address(recipients,province,city,town,streets,mobile):
    # 点击提示框确认按钮
    dr.find_element(By.XPATH, "/html/body/div[8]/div[2]/a[1]").click()
    #收货人
    dr.find_element(By.XPATH, "//*[@id='AddressList']/table/tbody/tr[1]/td[2]/input").send_keys(recipients)
    #选择省
    sheng = dr.find_elements(By.ID,"selProvinces")[0]
    Select(sheng).select_by_visible_text(province)
    #选择市
    shi = dr.find_elements(By.ID, "selCities")[0]
    Select(shi).select_by_visible_text(city)
    #选择区
    qu = dr.find_elements(By.ID, "selDistricts")[0]
    Select(qu).select_by_visible_text(town)
    #填写街道
    dr.find_element(By.NAME,"address").send_keys(streets)
    #填写手机号
    dr.find_element(By.NAME, "mobile").send_keys(mobile)
    #点击确定
    dr.find_element(By.XPATH, "//*[@id='AddressList']/table/tbody/tr[8]/td[2]/input[4]").click()
    # 点击收货地址
    dr.find_element(By.XPATH, "//*[@id='AddressList']/ul/li/div[1]").click()


def pay():
    # 支付
    # 点击支付宝/快钱/财付通/其他支付
    dr.find_element(By.XPATH, "//*[@id='payment_tab']/li[3]").click()
    # 点击支付宝
    dr.find_element(By.XPATH, "//*[@id='payment_other1']").click()
    # 点击确认订单
    dr.find_element(By.XPATH, "//*[@id='theForm']/div[6]/div[2]/input[1]").click()




def Delete_the_address():
    all_windows = dr.window_handles
    dr.switch_to.window(all_windows[0])
    dr.find_elements(By.XPATH, "//li[contains(@id,li_)]")[121].click()
    sleep(2)
    all_windows = dr.window_handles
    dr.switch_to.window(all_windows[2])
    print(all_windows)
    # 点击立即购买
    dr.find_element(By.XPATH, "//*[@id='choose-btns']/a[1]").click()
    #删除地址
    dr.find_element(By.XPATH,"//*[@id='address_edit_0']/a[2]").click()
    dr.find_element(By.XPATH,"/html/body/div[8]/div[2]/a[1]").click()
    dr.quit()

login('15836546562@163.com', 'sjx123456')
search("水果")
receiver_address("songjuxiang","北京","北京","海淀区","123123","15836546562")

sleep(2)
pay()
sleep(2)
Delete_the_address()
