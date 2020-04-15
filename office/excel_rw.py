import xlrd
import xlwt


class excel:
    def _read_(self,open_file_abspath,row,col):
        #1. 读取Excel
        # 选择文件路径，打开Excel文件
        xlsx = xlrd.open_workbook(open_file_abspath)
        # 选择工作表
        table = xlsx.sheet_by_index(1)
        # table = xlsx.sheet_by_name("购物车")
        # 通过下标取值——三种方式
        print(table.cell_value(row,col))
        # print(table.cell(0, 1).value)
        # print(table.row(0)[1].value)
        pass

    def __write__(self,sheet_name,new_excel_name,save_path):
        # 2. 写入Excel
        # 新建工作簿
        new_excel = xlwt.Workbook()
        # 添加工作表
        worksheet = new_excel.add_sheet(sheet_name)
        # 写入数据到新的Excel文件中
        worksheet.write(0,0,new_excel_name)
        # 保存到路径
        new_excel.save(save_path)
        pass


