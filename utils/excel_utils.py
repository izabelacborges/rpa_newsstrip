from RPA.Excel.Files import Files
from RPA.Tables import Tables


excel = Files()
table = Tables()


def setup_file(filename):
    excel.create_workbook()
    excel.save_workbook(filename)


def articles_to_table(articles):
    columns = list(articles[0].keys())
    return table.create_table(articles, columns=columns)


def save_results(articles, filename):
    articles_tb = articles_to_table(articles)
    excel.set_cell_values("A1", articles_tb, table_heading=True)
    excel.save_workbook(filename)


def teardown():
    excel.close_workbook()
