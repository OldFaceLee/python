# -*- encoding= utf-8 -*-

"""
@Author lixuejun
@Time 2020/5/18
"""

import xlrd


class ExcelUtil:

    def read_excel(self, file_path, sheet_name, row_no, column_no):
        workbook = xlrd.open_workbook(file_path)
        sheet = workbook.sheet_by_name(sheet_name)
        cell_data = sheet.cell(row_no, column_no)
        if cell_data.ctype == 1:
            print("返回的cell内的数据格式为 %d, 是str类型, 值为:%s" % (cell_data.ctype, cell_data))
        elif cell_data.ctype == 2:
            print("返回的cell内的数据格式为 %d, 是number类型, 值为:%s" % (cell_data.ctype, cell_data))
        return cell_data


instance_excel = ExcelUtil()
path = "/Users/macos/Desktop/testParam.xlsx"
cell = instance_excel.read_excel(path, "tc01", 0, 0)

