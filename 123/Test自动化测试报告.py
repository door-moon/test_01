from selenium import webdriver
import unittest
from HTMLTestRunner import HTMLTestRunner
#HTMLTestRunner用来生成HTML格式的测试报告
import time
class TestBaidu(unittest.TestCase):
    '''这是在对搜索功能进行测试'''
    def setUp(self) -> None:
        self.driver=webdriver.Chrome()
        self.driver.implicitly_wait(10)
        self.base_url='https://www.baidu.com'

    def test_search(self):
        ''' 测试内容：HTMLTR猪猪侠'''
        pic_path = './' + '55' + '.png'
        driver=self.driver
        driver.get(self.base_url)
        time.sleep(1)
        driver.find_element_by_id("kw").send_keys("HTMLTestRunner")
        time.sleep(1)
        driver.find_element_by_id("su").click()
        time.sleep(1)
        driver.save_screenshot(pic_path)
        print(pic_path)
        print('小朋友')


    def test_search2(self):
        ''' 测试内容：HTMLTR'''
        pic_path = './' + '55' + '.png'
        driver=self.driver
        driver.get(self.base_url)
        time.sleep(1)
        driver.find_element_by_id("kw").send_keys("猪猪侠")
        time.sleep(1)
        driver.find_element_by_id("su").click()
        time.sleep(1)
        driver.save_screenshot(pic_path)
        print(pic_path)
        print('aa')

    def tearDown(self) -> None:
        self.driver.quit()



if __name__ == '__main__':
    time.sleep(2)
    # unittest.main()
    # 测试套件，构建测试集
    # suite=unittest.TestSuite()
    # suite.addTest(TestBaidu('test_search'))
    # # suite.addTest(TestBaidu('test_search2'))
    #
    # # 我们要新建一个用于保存我们测试结果的文件，html
    # now=time.strftime("%Y-%m-%d-%H-%M-%S")
    # print(now)
    # # 定义文件的名字
    # filename='./'+now+"_result.html"
    # print(filename)
    # file = open(filename, "wb")
    # # 执行我们的报告写入
    #
    # runner=HTMLTestRunner(stream=file,title="百度搜索测试报告",description="用例执行情况:")
    # # stream：是指定测试报告文件
    # # title：指定报告的标题
    # # description:指定报告的副标题
    # # 执行我们测试用例
    #
    # runner.run(suite)
    #
    # time.sleep(3)
    # print(file.closed)
    # # 要进行关闭
    # file.close()
    # print(file.closed)
   # 执行测试用例
   #  runner=unittest.TextTestRunner()
   #  runner.run(suite)
