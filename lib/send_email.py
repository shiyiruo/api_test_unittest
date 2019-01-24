import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart   # 混合MIME格式，支持上传附件
from email.header import Header   # 用于使用中文邮件主题
from config.config import *

def send_email(report_file):
    msg = MIMEMultipart()
    msg.attach(MIMEText(open(report_file, encoding='utf-8').read(), 'html', 'utf-8'))   # 添加html格式邮件正文（会丢失css格式）

    msg['From'] = sender
    msg['To'] = receiver
    msg['Subject'] = Header(subject, 'utf-8')   # 中文邮件主题，指定utf-8编码

    att1 = MIMEText(open(report_file, 'rb').read(), 'base64', 'utf-8')  # 二进制格式打开
    att1["Content-Type"] = 'application/octet-stream'
    att1["Content-Disposition"] = 'attachment; filename="report.html"'
    msg.attach(att1)

    try:
        smtp = smtplib.SMTP_SSL(smtp_sever)   # smtp服务器地址 使用SSL模式
        smtp.login(smtp_user, smtp_password)
        smtp.sendmail(sender, receiver, msg.as_string())
        logging.info('邮件发送完成！')
    except Exception as e:
        logging.error(str(e))
    finally:
        smtp.quit()

if __name__ == "__main__":
    send_email(report_file)