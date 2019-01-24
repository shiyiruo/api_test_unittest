import unittest
from lib.HTMLTestReportCN import HTMLTestRunner
from lib.send_email import *
from config.config import *
from test.suite.test_suites import *
import time
import pickle
import sys


def discover():
    return unittest.defaultTestLoader.discover(test_case_path)

def save_failures(result, file):
    suite = unittest.TestSuite()
    for case_result in result.failures:
        suite.addTest(case_result[0])

    with open(file, 'wb') as f:
        pickle.dump(suite, f)

def collect():
    suite = unittest.TestSuite()

    def _collect(tests):
        if isinstance(tests, unittest.TestSuite):
            if tests.countTestCases() != 0:
                for i in tests:
                    _collect(i)
        else:
            suite.addTest(tests)

    _collect(discover())
    return suite

def makesuite_by_testlist(testlist_file):

    with open(testlist_file) as f:
        testlist = f.readlines()

    testlist = [i.strip() for i in testlist if not i.startswith("#")]

    suite = unittest.TestSuite()
    all_cases = collect()
    for case in all_cases:
        if case._testMethodName in testlist:
            suite.addTest(case)
    return suite

def makesuite_by_tag(tag):
    suite = unittest.TestSuite()
    for case in collect():
        if case._testMethodDoc and tag in case._testMethodDoc: #用例方法存在docstring，并且docstring包含本标签
            suite.addTest(case)
    return suite

def run(suite):
    logging.info("================================== 测试开始 ==================================")
    with open(report_file, 'wb') as f:
        result = HTMLTestRunner(stream=f, title='API Test', description='发券接口测试', tester='syr').run(suite)

    if result.failures:   # 保存失败用例的序列化文件
        save_failures(result, last_fails_file)

    if send_email_after_run:   # 是否发送邮件
        send_email(report_file)
    logging.info("================================== 测试结束 ==================================")

def collect_only():   #仅列出所有用例
    t0 = time.time()
    i = 0
    for case in collect():
        i += 1
        print("{}.{}".format(str(i), case.id()))
    print("----------------------------------------------------------------------")
    print("Collect {} tests is {:.3f}s".format(str(i), time.time() - t0))

def run_all():   #运行所有用例
    run(discover())

def run_suite(suite_name):
    suite = get_suite(suite_name)
    if isinstance(suite, unittest.TestSuite):
        run(suite)
    else:
        print('TestSuite不存在')

def run_by_testlist():
    run(makesuite_by_testlist(testlist_file))

def run_by_tag(tag):
    run(makesuite_by_tag(tag))

def rerun_fails():   # 重跑失败的用例
    sys.path.append(test_case_path)   # 需要将用例路径添加到包搜索路径中，不然反序列化TestSuite会找不到用例
    with open(last_fails_file, 'rb') as f:
        suite = pickle.load(f)   # 反序列化得到TestSuite
    run(suite)


def main():
    if options.collect_only:
        collect_only()
    elif options.rerun_fails:
        rerun_fails()
    elif options.testlist:
        run(makesuite_by_testlist(testlist_file))
    elif options.testsuite:
        run_suite(options.testsuite)
    elif options.tag:
        run(makesuite_by_tag(options.tag))
    else:
        run_all()

if __name__ == '__main__':
    main()