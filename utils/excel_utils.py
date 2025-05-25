class Excelutill :
    def __init__(self,path,sheet_name) :
        self.path = path
        self.workbook = Load_workbook(path)
        self.sheet = self.workbook[sheet_name]

    def read_data(self,row_no, col_no) :
        return self.sheet.cell(row_no,col_no).value

    def write_data(self,row_no, col_no) :
        self.sheet.cell(row_no,col_no).value = data

    def row_count(slef) :
        return self.sheet.max_row