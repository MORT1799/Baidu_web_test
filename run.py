import os
import time
import unittest
from HTMLTestRunner import HTMLTestRunner


# 测试用例所在文件夹
test_dir = './testcase'
# 将【testcase】里的.py文件作为Testsuite
# 批量执行
discover = unittest.defaultTestLoader.discover(start_dir='./testcase', pattern="test*.py")


if __name__ == "__main__":
    # 新建目录名
    report_dir = './test_report'
    # 在当前目录【.】，创建【test_report】文件夹
    os.makedirs(report_dir, exist_ok=True)
    # 获得字符串格式的时间
    now = time.strftime("%Y-%m-%d %H-%M-%S")
    # format 字符串格式化函数
    report_name = '{0}/{1}.html'.format(report_dir, now)

    with open(report_name, 'wb')as f:
        runner = HTMLTestRunner(stream=f, title="测试报告", description="本测试报告内容包含超级计算器的简单测试")
        runner.run(discover)
