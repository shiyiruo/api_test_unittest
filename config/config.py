import logging
import os
from optparse import OptionParser
import time

today = time.strftime('%Y%m%d', time.localtime())
now = time.strftime('%Y%m%d_%H%M%S', time.localtime())

#项目路径
prj_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

test_case_path = os.path.join(prj_path, 'test', 'case')   #用例目录

data_path = os.path.join(prj_path, 'data')   #数据目录

log_file = os.path.join(prj_path, 'log', 'log_{}.txt'.format(today))

report_file = os.path.join(prj_path, 'report', 'report_{}.html'.format(now))

testlist_file = os.path.join(prj_path, 'test', 'testlist.txt')

last_fails_file = os.path.join(prj_path, 'last_failures.pickle')

logging.basicConfig(level=logging.INFO,
                    format='[%(asctime)s] %(levelname)s [%(funcName)s: %(filename)s, %(lineno)d] %(message)s',  # log格式
                    datefmt='%Y-%m-%d %H:%M:%S',  # 日期格式
                    filename=log_file,   # 日志输出文件
                    filemode='a')   # 追加模式

# 邮件配置
smtp_sever = 'smtp.qq.com'
smtp_user = '2553417094@qq.com'
smtp_password = 'gendngxrhbrmdibe'

sender = '2553417094@qq.com'   # 发件人
receiver = 'shiyiruo@chexiang.com'   # 收件人
subject = '接口测试报告'   # 邮件主题

send_email_after_run = True   # send email开关


# 命令行选项
parser = OptionParser()
parser.add_option('--collect-only', action='store_true', dest='collect_only', help='仅列出所有用例')
parser.add_option('--rerun-fails', action='store_true', dest='rerun_fails', help='运行上次失败的用例')
parser.add_option('--testlist', action='store_true', dest='testlist', help='运行test/testlist.txt列表指定用例')
parser.add_option('--testsuite', action='store', dest='testsuite', help='运行指定的TestSuite')
parser.add_option('--tag', action='store', dest='tag', help='运行指定tag的用例')

(options, args) = parser.parse_args()

if __name__ == '__main__':
    logging.info('hello')