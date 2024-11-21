import pandas as pd
import csv
import numpy as np


def lapDayORong(data, fill_value='south'):
    """Dien gia tri N/A cho cac o thieu trong cot 'residence'."""
    data['residence'].replace('', np.nan, inplace=True)
    data['residence'].replace(' ', np.nan, inplace=True)
    data['residence'].fillna(fill_value, inplace=True)
    return data

def chuanHoaDuLieuPhanLoai(data, categorical_columns):
    """Chuan hoa cac cot dang phan loai thanh chu thuong."""
    for col in categorical_columns:
        data[col] = data[col].str.lower()
    return data

def thayDauGachDuoiThanhKhoangTrang(data):
    """Thay doi dau gach duoi thanh khoang trang"""
    data = data.applymap(lambda x: x.replace('_', ' ') if isinstance(x, str) else x)
    return data

def cleanData(data):
    """Chay tat ca cac ham lam sach tren tap du lieu."""
    data = lapDayORong(data)
    categorical_columns = ['union', 'ethn', 'maried', 'health', 'industry', 'occupation', 'residence']
    data = chuanHoaDuLieuPhanLoai(data, categorical_columns)
    data = thayDauGachDuoiThanhKhoangTrang(data)
    return data

def loadAndCleanCSV(filePath, outPath, cols = 13):
    """Tach du lieu cac hang chua hop le va lam sach """
    all_rows = []
    with open(filePath, "r") as file:
        reader = csv.reader(file, skipinitialspace=True)
        for row in reader:
            if len(row) == cols:
                all_rows.append(row)
            else:
                split_row = []
                for element in row:
                    split_element = list(csv.reader([element], delimiter=','))
                    split_row.extend(split_element[0])
                if len(split_row) < cols:
                    split_row.extend([None] * (cols - len(split_row)))
                all_rows.append(split_row)
    df_all = pd.DataFrame(all_rows, columns=["rownames", "nr", "year", "school", "exper", "union", "ethn", 
                                            "maried", "health", "wage", "industry", "occupation", "residence"])
    df_all = cleanData(df_all)
    df_all.to_csv(outPath, index=False, header=False)
    return df_all
