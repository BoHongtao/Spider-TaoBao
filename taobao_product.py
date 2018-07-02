from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from urllib.parse import quote
from pyquery import PyQuery
import pymysql

browser = webdriver.Chrome()
wait = WebDriverWait(browser, 10)
KEYWORD = ''
global count
count = 0

# 用selenium打开指定的商品页
def index_page(page):
    print('正在爬取第', page, '页')
    try:
        url = 'https://s.taobao.com/search?q=' + quote(KEYWORD)
        browser.get(url)
        if page > 1:
            input = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#mainsrp-pager div.form > input')))
            submit = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#mainsrp-pager div.form > span.btn.J_Submit')))
            input.clear()
            input.send_keys(page)
            submit.click()
        wait.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, '#mainsrp-pager li.item.active > span'), str(page)))
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '.m-itemlist .items .item')))
        get_products()
    except TimeoutException:
        print("抓取失败")
        return

# 使用PyQuery解析每一页的商品信息
def get_products():
    html = browser.page_source
    doc = PyQuery(html)
    items = doc('#mainsrp-itemlist .items .item').items()
    for item in items:
        product = {
            'image': item.find('.pic .img').attr('data-src').replace('\n',''),
            'price': item.find('.price').text().replace('\n',''),
            'deal': item.find('.deal-cnt').text().replace('\n',''),
            'title': item.find('.title').text().replace('\n',''),
            'shop': item.find('.shop').text().replace('\n',''),
            'location': item.find('.location').text().replace('\n','')
        }
        save_db(product)

# 保存数据到mysql
def save_db(product):
    try:
        global count
        # 获取游标
        connect = pymysql.Connect(user='root', password='', host='127.0.0.1', database='spider',charset='utf8')
        cur = connect.cursor()
        sql = "INSERT INTO tmall (id,image_url,price,deal,title,shop,location) VALUES ( '%s', '%s', '%s' ,'%s', '%s', '%s', '%s')"
        value = ('0',product['image'],product['price'],product['deal'],product['title'],product['shop'],product['location'])
        cur.execute(sql % value)
        connect.commit()
        count = count + 1
        print("保存数据成功,当前以保存"+str(count))
    except pymysql.Error as why:
        print("保存失败，原因是"+str(why))

if __name__ == '__main__':
    print("请输入你想要爬取的商品")
    KEYWORD = input()
    for i in range(1,100):
        index_page(i)
