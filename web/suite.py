import os
import unittest

from HTMLTestRunner import HTMLTestRunner

suite  = unittest.TestSuite()
# suite.addTest(Skip('test_3'))
# suite.addTest(Skip('test_1'))
# suite.addTest(Skip('test_2'))
# case  = [Skip('test_3'),Skip('test_2'),Skip('test_1')]
# suite.addTests(case)
# test_dir = './'
# discover = unittest.defaultTestLoader.discover(start_dir=test_dir,pattern='sk*.py')
report_path = './report/'
report_file=report_path+'report.html'
report_name='测试报告'
report_desc='测试报告描述'
report_title='测试报告标题'
if not os.path.exists(report_path):
    os.mkdir(report_path)
else:
    pass
with open(report_file,'wb') as report:
    suite.addTests(unittest.TestLoader().loadTestsFromName('skip.Skip.test_2'))
    runner = HTMLTestRunner(stream=report,title=report_title,description=report_desc)
    runner.run(suite)
report.close()
# suite.addTests(unittest.TestLoader().loadTestsFromName('skip.Skip.test_2'))
# suite.addTests(unittest.TestLoader.loadTestsFromTestCase(Skip.test_3(2)))
# suite.addTests(unittest.TestLoader.loadTestsFromModule('PyCode.base.demo.skip.Skip'))
# runner.run(discover)
