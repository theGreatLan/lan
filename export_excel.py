# -*- coding: utf-8 -*-

import xlwt
import logging
import json

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')


def get_str(info):
    return json.dumps(info, encoding='UTF-8', ensure_ascii=False)




response1 = {
        "medical_id": 3,
        "create_time": "2018-11-09",
        "ss_type_name": "中医医院",
        "occur_time": "2018年11月08日",
        "no": "ZGRSBF2017051900017",
        "type_name": "城镇居民",
        "stub": [{
            "status": 0,
            "update_time": "19小时前",
            "stub_id": 5,
            "no": "ZGRSBF2017051900017",
            "mi_type": 3,
            "self_charge_1_max": 0.0,
            "self_charge_1": 202.96,
            "attach_key": "E9C72A9A1B1D46FA92D99F8272E79696.jpg",
            "self_charge": 0.0,
            "self_charge_2": 0.0,
            "attach": "http://zhongkeruijian.oss-cn-beijing.aliyuncs.com/E9C72A9A1B1D46FA92D99F8272E79696.jpg",
            "charge": 247.9,
            "case_id": 1,
            "create_time": "2018-11-08",
            "mi_type_name": "中医医院",
            "status_name": "正常",
            "self_charge_1_min": 158.02,
            "attach_id": 0,
            "total_charge": 739.89,
            "stub_no": "E9C72A9A1B1D46FA92D99F8272E79696",
            "year_total_clinic_charge": 44.95
        },
        {
            "status": 0,
            "update_time": "1天前",
            "stub_id": 4,
            "no": "ZGRSBF2017051900017",
            "mi_type": 3,
            "self_charge_1_max": 0.0,
            "self_charge_1": 220.84,
            "attach_key": "73773CB099AD4860A97F05DC13075EC6.jpg",
            "self_charge": 0.0,
            "self_charge_2": 0.0,
            "attach": "http://zhongkeruijian.oss-cn-beijing.aliyuncs.com/73773CB099AD4860A97F05DC13075EC6.jpg",
            "charge": 220.84,
            "case_id": 1,
            "create_time": "2018-11-08",
            "mi_type_name": "中医医院",
            "status_name": "正常",
            "self_charge_1_min": 220.84,
            "attach_id": 0,
            "total_charge": 491.98,
            "stub_no": "73773CB099AD4860A97F05DC13075EC6",
            "year_total_clinic_charge": 0.0
        },
        {
            "status": 0,
            "update_time": "1天前",
            "stub_id": 2,
            "no": "ZGRSBF2017051900017",
            "mi_type": 3,
            "self_charge_1_max": 0.0,
            "self_charge_1": 26.0,
            "attach_key": "68D4439B6D1141E4BD002B1E47799BD8.jpg",
            "self_charge": 0.0,
            "self_charge_2": 0.0,
            "attach": "http://zhongkeruijian.oss-cn-beijing.aliyuncs.com/68D4439B6D1141E4BD002B1E47799BD8.jpg",
            "charge": 26.0,
            "case_id": 1,
            "create_time": "2018-11-08",
            "mi_type_name": "中医医院",
            "status_name": "正常",
            "self_charge_1_min": 26.0,
            "attach_id": 0,
            "total_charge": 26.0,
            "stub_no": "68D4439B6D1141E4BD002B1E47799BD8",
            "year_total_clinic_charge": 0.0
        }],
        "case_id": 1,
        "mail": "nick_x_wu@163.com",
        "type": 2,
        "bank_no": "600000000000000",
        "status": 0,
        "update_time": "3分钟前",
        "phone": "17621731157",
        "ssn": "11718893500X",
        "bank": "icbc",
        "stub_num": 5,
        "case": {
            "status": 0,
            "update_time": "2018-11-08",
            "user_id": 0,
            "name": "谢悠然",
            "no": "ZGRSBF2017051900017",
            "create_time": "6天前",
            "status_name": "正常",
            "case_id": 1,
            "cate_id": 0,
            "user": {
                "user_id": 0,
                "nickname": "-",
                "avatar": "-"
            },
            "batch_no": "123",
            "cate": {
                "cate_id": 0,
                "name": "-"
            }
        },
        "remark": "remark",
        "name": "谢悠然",
        "status_name": "正常",
        "gender": 1,
        "gender_name": "男",
        "ss_type": 3,
        "batch_no": "B20170101"
    }

response = {
        "medical_id": 8,
        "create_time": "2018-11-09",
        "ss_type_name": "非营利性医疗机构",
        "occur_time": "2018年11月08日",
        "no": "ZGRSBF2017051000308",
        "type_name": "城镇职工",
        "stub": [{
            "create_time": "2018-11-08",
            "stub_no": "D17D825104274C5B8925121BA3B8FDE0",
            "staff_charge": 0.0,
            "no": "ZGRSBF2017051000308",
            "person_balance": 0.0,
            "clinic_charge": 0.0,
            "self_charge_1": 265.26,
            "self_charge_2": 13.99,
            "retire_charge": 0.0,
            "charge": 265.26,
            "case_id": 8,
            "mi_type_name": "非营利性医疗机构",
            "attach": "http://zhongkeruijian.oss-cn-beijing.aliyuncs.com/D17D825104274C5B8925121BA3B8FDE0.jpg",
            "year_total_clinic_charge": 0.0,
            "status": 0,
            "update_time": "2018-11-08",
            "stub_id": 23,
            "mi_type": 5,
            "attach_key": "D17D825104274C5B8925121BA3B8FDE0.jpg",
            "self_charge_1_max": 0.0,
            "self_charge_1_min": 265.26,
            "army_charge": 0.0,
            "status_name": "正常",
            "self_charge": 0.0,
            "attach_id": 0,
            "total_charge": 265.26
        },
        {
            "create_time": "2018-11-08",
            "stub_no": "24383558B7A04F82892F717F28BB948A",
            "staff_charge": 0.0,
            "no": "ZGRSBF2017051000308",
            "person_balance": 0.0,
            "clinic_charge": 2.0,
            "self_charge_1": 0.0,
            "self_charge_2": 2.0,
            "retire_charge": 0.0,
            "charge": 2.0,
            "case_id": 8,
            "mi_type_name": "非营利性医疗机构",
            "attach": "http://zhongkeruijian.oss-cn-beijing.aliyuncs.com/24383558B7A04F82892F717F28BB948A.jpg",
            "year_total_clinic_charge": 0.0,
            "status": 0,
            "update_time": "2018-11-08",
            "stub_id": 22,
            "mi_type": 5,
            "attach_key": "24383558B7A04F82892F717F28BB948A.jpg",
            "self_charge_1_max": 0.0,
            "self_charge_1_min": 0.0,
            "army_charge": 0.0,
            "status_name": "正常",
            "self_charge": 1.0,
            "attach_id": 0,
            "total_charge": 0.0
        },
        {
            "create_time": "2018-11-08",
            "stub_no": "640B0640A50D4923A26CEDD381FE60F5",
            "staff_charge": 0.0,
            "no": "ZGRSBF2017051000308",
            "person_balance": 0.0,
            "clinic_charge": 0.0,
            "self_charge_1": 768.94,
            "self_charge_2": 52.0,
            "retire_charge": 0.0,
            "charge": 768.94,
            "case_id": 8,
            "mi_type_name": "综合医院",
            "attach": "http://zhongkeruijian.oss-cn-beijing.aliyuncs.com/640B0640A50D4923A26CEDD381FE60F5.jpg",
            "year_total_clinic_charge": 0.0,
            "status": 0,
            "update_time": "2018-11-08",
            "stub_id": 21,
            "mi_type": 1,
            "attach_key": "640B0640A50D4923A26CEDD381FE60F5.jpg",
            "self_charge_1_max": 0.0,
            "self_charge_1_min": 768.94,
            "army_charge": 0.0,
            "status_name": "正常",
            "self_charge": 0.0,
            "attach_id": 0,
            "total_charge": 1034.3
        },
        {
            "create_time": "2018-11-08",
            "stub_no": "31A5AE55CFB6479B8EB517449D10C978",
            "staff_charge": 0.0,
            "no": "ZGRSBF2017051000308",
            "person_balance": 0.0,
            "clinic_charge": 40.0,
            "self_charge_1": 0.0,
            "self_charge_2": 10.0,
            "retire_charge": 0.0,
            "charge": 40.0,
            "case_id": 8,
            "mi_type_name": "综合医院",
            "attach": "http://zhongkeruijian.oss-cn-beijing.aliyuncs.com/31A5AE55CFB6479B8EB517449D10C978.jpg",
            "year_total_clinic_charge": 0.0,
            "status": 0,
            "update_time": "2018-11-08",
            "stub_id": 20,
            "mi_type": 1,
            "attach_key": "31A5AE55CFB6479B8EB517449D10C978.jpg",
            "self_charge_1_max": 0.0,
            "self_charge_1_min": 0.0,
            "army_charge": 0.0,
            "status_name": "正常",
            "self_charge": 0.0,
            "attach_id": 0,
            "total_charge": 265.26
        },
        {
            "create_time": "2018-11-08",
            "stub_no": "6BE39003B85E442894A12DEFA3069AF2",
            "staff_charge": 0.0,
            "no": "ZGRSBF2017051000308",
            "person_balance": 0.0,
            "clinic_charge": 2.0,
            "self_charge_1": 0.0,
            "self_charge_2": 2.0,
            "retire_charge": 0.0,
            "charge": 2.0,
            "case_id": 8,
            "mi_type_name": "非营利性医疗机构",
            "attach": "http://zhongkeruijian.oss-cn-beijing.aliyuncs.com/6BE39003B85E442894A12DEFA3069AF2.jpg",
            "year_total_clinic_charge": 0.0,
            "status": 0,
            "update_time": "2018-11-08",
            "stub_id": 19,
            "mi_type": 5,
            "attach_key": "6BE39003B85E442894A12DEFA3069AF2.jpg",
            "self_charge_1_max": 0.0,
            "self_charge_1_min": 0.0,
            "army_charge": 0.0,
            "status_name": "正常",
            "self_charge": 1.0,
            "attach_id": 0,
            "total_charge": 0.0
        }],
        "case_id": 8,
        "mail": "",
        "type": 1,
        "bank_no": "",
        "status": 0,
        "update_time": "2018-11-08",
        "phone": "",
        "ssn": "11076572800X",
        "bank": "",
        "stub_num": 5,
        "case": {
            "status": 0,
            "update_time": "2018-11-08",
            "user_id": 0,
            "name": "张弛",
            "no": "ZGRSBF2017051000308",
            "create_time": "6天前",
            "status_name": "正常",
            "case_id": 8,
            "cate_id": 0,
            "user": {
                "user_id": 0,
                "nickname": "-",
                "avatar": "-"
            },
            "batch_no": "123",
            "cate": {
                "cate_id": 0,
                "name": "-"
            }
        },
        "remark": "",
        "name": "张弛",
        "status_name": "正常",
        "gender": 1,
        "gender_name": "男",
        "ss_type": 5,
        "batch_no": "B20170101"
    }

base_info = [
    ['姓名', '性别', '社保号', '医保类型', '电话', '邮箱', '银行名称', '银行账号', '备注'],
    []
]

stub = []

stub_info = [
    ['票据号', '医疗机构类型', '本次医保范围内金额', '年度累计医保范围内金额', '年度门诊大额累计支付', '自付一', '起付金额',
        '超封顶金额', '自付二', '自费']
]

stub_staff_info = [
    ['票据号', '医疗机构类型', '门诊大额支付', '退休补充支付', '残军补助支付', '单位补充险支付', '本次医保范围金额',
              '年度累计医保金额', '年度门诊大额累计支付', '本次支付后个人账户余额', '自付一', '起付金额', '超封顶金额', '自付二',
              '自费']
]

for item in base_info[0]:
    if item == '姓名':
        base_info[1].append(response['name'])
    if item == '性别':
        base_info[1].append(response['gender_name'])
    if item == '社保号':
        base_info[1].append(response['ssn'])
    if item == '医保类型':
        base_info[1].append(response['type_name'])
    if item == '电话':
        base_info[1].append(response['phone'])
    if item == '邮箱':
        base_info[1].append(response['mail'])
    if item == '银行名称':
        base_info[1].append(response['bank'])
    if item == '银行账号':
        base_info[1].append(response['bank_no'])
    if item == '备注':
        base_info[1].append(response['remark'])


if response['type'] == 1:
    for i in response['stub']:
        ary = []
        for j in stub_staff_info[0]:
            if j == '票据号':
                ary.append(i['stub_no'])
            if j == '医疗机构类型':
                ary.append(i['mi_type_name'])
            if j == '门诊大额支付':
                ary.append(i['clinic_charge'])
            if j == '退休补充支付':
                ary.append(i['retire_charge'])
            if j == '残军补助支付':
                ary.append(i['army_charge'])
            if j == '单位补充险支付':
                ary.append(i['staff_charge'])
            if j == '本次医保范围金额':
                ary.append(i['charge'])
            if j == '年度累计医保金额':
                ary.append(i['total_charge'])
            if j == '年度门诊大额累计支付':
                ary.append(i['year_total_clinic_charge'])
            if j == '本次支付后个人账户余额':
                ary.append(i['person_balance'])
            if j == '自付一':
                ary.append(i['self_charge_1'])
            if j == '起付金额':
                ary.append(i['self_charge_1_min'])
            if j == '超封顶金额':
                ary.append(i['self_charge_1_max'])
            if j == '自付二':
                ary.append(i['self_charge_2'])
            if j == '自费':
                ary.append(i['self_charge'])
        stub_staff_info.append(ary)
    stub = stub_staff_info
    logging.info(1111)


if response['type'] == 2:
    for i in response['stub']:
        ary = []
        for j in stub_info[0]:
            if j == '票据号':
                ary.append(i['stub_no'])
            if j == '医疗机构类型':
                ary.append(i['mi_type_name'])
            if j == '本次医保范围内金额':
                ary.append(i['charge'])
            if j == '年度累计医保范围内金额':
                ary.append(i['total_charge'])
            if j == '年度门诊大额累计支付':
                ary.append(i['year_total_clinic_charge'])
            if j == '自付一':
                ary.append(i['self_charge_1'])
            if j == '起付金额':
                ary.append(i['self_charge_1_min'])
            if j == '超封顶金额':
                ary.append(i['self_charge_1_max'])
            if j == '自付二':
                ary.append(i['self_charge_2'])
            if j == '自费':
                ary.append(i['self_charge'])
        stub_info.append(ary)
    stub = stub_info
    logging.info(2222)







logging.info(get_str(stub))

#


# 获取字符串长度，一个中文的长度为2
def len_byte(value):
    length = len(value)
    utf8_length = len(value.decode('utf-8'))
    length = (utf8_length - length) / 2 + length
    return int(length)


# 设置字体
font = xlwt.Font()
font.bold = True

# 设置边框
borders = xlwt.Borders()
borders.left = xlwt.Borders.THIN
borders.right = xlwt.Borders.THIN
borders.top = xlwt.Borders.THIN
borders.bottom = xlwt.Borders.THIN

# 设置居中
alignment = xlwt.Alignment()
alignment.horz = xlwt.Alignment.HORZ_CENTER  # 水平方向
alignment.vert = xlwt.Alignment.VERT_TOP  # 垂直方向

# 设置背景颜色
pattern = xlwt.Pattern()
pattern.pattern = xlwt.Pattern.SOLID_PATTERN
pattern.pattern_fore_colour = 3  # 背景颜色

# 定义不同的excel style
style1 = xlwt.XFStyle()
style1.font = font
style1.borders = borders
style1.alignment = alignment
style2 = xlwt.XFStyle()
style2.borders = borders
style2.alignment = alignment
style3 = xlwt.XFStyle()
style3.borders = borders
style3.alignment = alignment
style4 = xlwt.XFStyle()
style4.borders = borders
style4.font = font
style4.pattern = pattern
style4.alignment = alignment
workbook = xlwt.Workbook(encoding='utf-8')
worksheet = workbook.add_sheet('My Worksheet')

# 确定栏位宽度
col_width = []
for i in range(len(stub)):
    for j in range(len(stub[i])):
        if i == 0:
            col_width.append(len_byte(stub[i][j]))
        else:
            if col_width[j] < len_byte(str(stub[i][j])):
                col_width[j] = len_byte(stub[i][j])

print col_width

# 设置栏位宽度，栏位宽度小于10时候采用默认宽度
for i in range(len(col_width)):
    if col_width[i] > 10:
        worksheet.col(i).width = 256 * (col_width[i] + 1)

# 设置栏位高度
# tall_style = xlwt.easyxf('font:height 720;') #设置字体高度
# row0 = worksheet.row(0)
# row0.set_style(tall_style)


# excel内容写入
for i in range(len(base_info)):
    for j in range(len(base_info[i])):
        if i == 0:
            worksheet.write(i, j, label=base_info[i][j], style=style1)
        else:
            worksheet.write(i, j, label=base_info[i][j], style=style2)


for i in range(len(stub)):
    for j in range(len(stub[i])):
        if i == 0:
            worksheet.write(i+3, j, label=stub[i][j], style=style1)
        else:
            worksheet.write(i+3, j, label=stub[i][j], style=style2)

# excel统计结果写入
# for m in range(len(total)):
#     for n in range(len(total[m])):
#         if m == 0:
#             worksheet.write(m + i + 3, n + 2, label=total[m][n], style=style4)
#         else:
#             worksheet.write(m + i + 3, n + 2, label=total[m][n], style=style2)
#
# # 合并单元格
# worksheet.write_merge(m + i + 4, m + i + 6, 2, 4, label='统计:       签名：', style=style3)
workbook.save('../aa/Excel_Workbook.xls')
