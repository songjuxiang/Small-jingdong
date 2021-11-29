from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

dr = webdriver.Chrome()
dr.maximize_window()
dr.implicitly_wait(20)
def main ():
    login('test01', 'test888')
    click_menu('商品管理', '商品列表')
    goods_list('iPhone', '商品名称-lyq')
    member_login('lyq', 'l2377552729')
    menu('商品与描述不符','F:\\python\\day2\\退货图片.jpg')

def login(username,pw):
    dr.get('http://newecshop.longtest.cn/admin/privilege.php?act=login')
    dr.find_element('name','username').send_keys(username)
    dr.find_element('name', 'password').send_keys(pw)
    dr.find_element('class name', 'button2').click()
    sleep(1)

def click_menu(menu,sub_menu):
    dr.switch_to.frame('menu_frame')  # 切换到左侧操作栏的网页
    dr.find_element('link text',menu).click()
    dr.find_element('link text',sub_menu ).click()
    dr.switch_to.default_content()
    sleep(2)

def goods_list(cat_name,keyword):     #商品列表
    dr.switch_to.frame('main-frame')
    dr.find_element('id','cat_name').send_keys(cat_name)
    dr.find_element('name', 'keyword').send_keys(keyword)
    dr.find_element(By.XPATH,'/html/body/div[2]/form/input[4]').click()
    sleep(2)
    dr.find_element('id','listDiv').\
        find_elements('tag name','tr')[2].\
        find_elements('tag name','td')[12].\
        find_elements('tag name','a')[0].click()
    sleep(1)

def member_login(username,pw):      #前台用户登录
    all_windows = dr.window_handles  # 所有窗口的句柄，列表格式，先打开的在前面
    dr.switch_to_window(all_windows[-1])
    l1 = dr.find_element('xpath','//a[text()="请登录"]').get_attribute('text')
    try:
        if l1 =='请登录':
            print("用户未登录")
            dr.find_element('xpath', '//a[text()="请登录"]').click()
            dr.find_element('name', 'username').send_keys(username)
            dr.find_element('name', 'password').send_keys(pw)
            dr.find_element('id', 'loginsubmit').click()
            sleep(1)

        else:
            print('用户已登录')
    except Exception as e:
        print(e)


def menu(reason,img):   #我的订单页面
    dr.find_element('xpath','//*[@id="site-nav"]/div/ul/li[1]/div/a').click()
    dr.find_element('xpath','//*[text()="我的订单"]').click()
    dr.find_element('xpath','//*[text()="退货"]').click()
    dr.find_element('xpath','//*[@id = "back_reason"]').send_keys(reason)
    dr.find_element('xpath', '//*[@id = "back_order_img"]').click()
    dr.find_element('name','imgFile').send_keys(img)
    dr.find_element('xpath','//span[@title="确定"]/input').click()
    sleep(2)
    dr.find_element('xpath','//input[@name = "submit"]').click()
    sleep(1)
    dr.find_element('xpath','//input[@value="确定"]').click()



main()