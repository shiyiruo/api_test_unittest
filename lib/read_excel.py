import xlrd

def excel_to_list(data_file, sheet):
    data_list = []
    wb = xlrd.open_workbook(data_file)   # 打开excel
    sh = wb.sheet_by_name(sheet)   # 获取工作簿
    header = sh.row_values(0)
    for i in range(1, sh.nrows):
        d = dict(zip(header, sh.row_values(i)))   # 将标题和每行数据组装成字典
        data_list.append(d)
    return data_list

def get_test_data(data_list, case_name):
    for case_data in data_list:
        if case_name == case_data['case_name']:
            return case_data
            # 如果查询不到会返回None

if __name__ == '__main__':
    data_list = excel_to_list('test_user_data.xlsx', 'TestGrantCouponToUser')
    case_data = get_test_data(data_list, 'test_grant_coupon_to_user_normal')
    print(case_data)
