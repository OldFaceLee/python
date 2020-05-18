# -*- encoding= utf-8 -*-

"""
@Author lixuejun
@Time 2020/5/18
"""

import xlrd


class ExcelUtil:

    def read(self, file_path, sheet_name):
        workbook = xlrd.open_workbook(file_path)
        sheet = workbook.sheet_by_name(sheet_name)
        
