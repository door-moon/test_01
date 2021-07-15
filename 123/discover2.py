from HTMLTestRunner import HTMLTestRunner
import unittest
import time
d = './'
diss = unittest.defaultTestLoader.discover(d,pattern='Test自动化测试*.py')
print(diss)

now = time.strftime("%Y-%m-%d-%H-%M-%S")
filename = './' + now + "_result.html"
file = open(filename, "wb")
runner = HTMLTestRunner(stream=file, title="百度搜索测试报告", description="用例执行情况:")
runner.run(diss)

file.close()