import tkinter as tk
from tkinter import ttk, messagebox
import pandas as pd
import math

df = pd.read_csv('NewMales.csv')

#CREATE
def create_row(df):
  
    root = tk.Tk()
    root.title("Create a new record")
    
    rowname = len(df) + 1 
    def save_record():
        new_row = {
                "rownames": rowname,
                "nr": int(nr_entry.get()),
                "year": int(year_entry.get()),
                "school": int(school_entry.get()),
                "exper": int(exper_entry.get()),
                "union": str(union_var.get()),
                "ethn": str(ethn_var.get()),
                "maried": str(maried_var.get()),
                "health": str(health_var.get()),
                "wage": float(wage_entry.get()),
                "industry": str(industry_entry.get()),
                "occupation": str(occupation_entry.get()),
                "residence": str(residence_var.get())
            }
        global df
        df = pd.concat([df, pd.DataFrame(new_row, index=[0])], ignore_index=True)
        df.to_csv('NewMales.csv', index=False)
        root.destroy()
    

    # Nhập nr
    ttk.Label(root, text="nr:").grid(row=0, column=0, sticky=tk.W, padx=10, pady=5)
    nr_entry = ttk.Entry(root)
    nr_entry.grid(row=0, column=1, sticky=tk.EW, padx=10, pady=5)

    # Nhập year
    ttk.Label(root, text="year:").grid(row=1, column=0, sticky=tk.W, padx=10, pady=5)
    year_var = tk.StringVar()
    year_entry = ttk.Combobox(root, textvariable=year_var, values=[1980, 1981, 1982, 1983, 1984, 1985, 1986, 1987])
    year_entry.grid(row=1, column=1, sticky=tk.EW, padx=10, pady=5)

    # Nhập school
    ttk.Label(root, text="school:").grid(row=2, column=0, sticky=tk.W, padx=10, pady=5)
    school_entry = ttk.Entry(root)
    school_entry.grid(row=2, column=1, sticky=tk.EW, padx=10, pady=5)

    # Nhập exper
    ttk.Label(root, text="exper:").grid(row=3, column=0, sticky=tk.W, padx=10, pady=5)
    exper_entry = ttk.Entry(root)
    exper_entry.grid(row=3, column=1, sticky=tk.EW, padx=10, pady=5)

    # Nhập union
    ttk.Label(root, text="union:").grid(row=4, column=0, sticky=tk.W, padx=10, pady=5)
    union_var = tk.StringVar(root)
    union_entry = ttk.Combobox(root, textvariable=union_var, values=["yes", "no"])
    union_entry.grid(row=4, column=1, sticky=tk.EW, padx=10, pady=5)

    # Nhập ethn
    ttk.Label(root, text="ethn:").grid(row=5, column=0, sticky=tk.W, padx=10, pady=5)
    ethn_var = tk.StringVar(root)
    ethn_entry = ttk.Combobox(root, textvariable=ethn_var, values=["black", "hisp", "other"])
    ethn_entry.grid(row=5, column=1, sticky=tk.EW, padx=10, pady=5)

    # Nhập maried
    ttk.Label(root, text="maried:").grid(row=6, column=0, sticky=tk.W, padx=10, pady=5)
    maried_var = tk.StringVar(root)
    maried_entry = ttk.Combobox(root, textvariable=maried_var, values=["yes", "no"])
    maried_entry.grid(row=6, column=1, sticky=tk.EW, padx=10, pady=5)

    # Nhập health
    ttk.Label(root, text="health:").grid(row=7, column=0, sticky=tk.W, padx=10, pady=5)
    health_var = tk.StringVar(root)
    health_entry = ttk.Combobox(root, textvariable=health_var, values=["yes", "no"])
    health_entry.grid(row=7, column=1, sticky=tk.EW, padx=10, pady=5)

    # Nhập wage
    ttk.Label(root, text="wage:").grid(row=8, column=0, sticky=tk.W, padx=10, pady=5)
    wage_entry = ttk.Entry(root)
    wage_entry.grid(row=8, column=1, sticky=tk.EW, padx=10, pady=5)

    # Nhập industry
    ttk.Label(root, text="industry:").grid(row=9, column=0, sticky=tk.W, padx=10, pady=5)
    industry_entry = ttk.Entry(root)
    industry_entry.grid(row=9, column=1, sticky=tk.EW, padx=10, pady=5)

    # Nhập occupation
    ttk.Label(root, text="occupation:").grid(row=10, column=0, sticky=tk.W, padx=10, pady=5)
    occupation_entry = ttk.Entry(root)
    occupation_entry.grid(row=10, column=1, sticky=tk.EW, padx=10, pady=5)

    # Nhập residence
    ttk.Label(root, text="residence:").grid(row=11, column=0, sticky=tk.W, padx=10, pady=5)
    residence_var = tk.Entry(root)
    residence_var.grid(row=11, column=1, sticky=tk.EW, padx=10, pady=5)
    
    # Nút lưu
    save_button = ttk.Button(root, text="Create", command=save_record)
    save_button.grid(row=12, column=0, columnspan=2, pady=10)

    
def create_age_col(df):
    df['age'] = 6 + df['school'] + df['exper']  

def create_exper_level_col(df):
   
    df['exper level'] = pd.cut(
        df['exper'],
        bins=[0, 3, 8, 12, 18],
        labels=['beginner', 'intermediate', 'advanced', 'expert'],
        right=True)
    
def create_school_level_col(df):
   
    df['school level'] = pd.cut(
        df['school'],
        bins=[0, 5, 9, 12, 16],
        labels=['very low', 'low', 'intermediate', 'high'],
        right=True)
    
def create_wage_level_col(df):
   
    df['wage level'] = pd.cut(
        df['wage'],
        bins=[-4, -2, 0, 2, 3.5, 4.1],
        labels=['very low', 'low', 'medium', 'high', 'very high'],
        right=True)
    
#READ
  
def Record_Details():
  
    def show_record_details():
        try:
            # Lấy giá trị rownames người dùng nhập
            rowname_value = int(rowname_entry.get())
        
            # Kiểm tra xem rowname_value có tồn tại trong cột 'rownames' không
            record = df[df['rownames'] == rowname_value]
        
            if record.empty:
                messagebox.showerror("Error", "No record found for the given rowname.")
                return
        
            # Tạo cửa sổ chi tiết bản ghi
            details_window = tk.Toplevel(root)
            details_window.title("Record Details")

            row_number = 0
            
            # Hiển thị
            for col_name, value in record.iloc[0].items():
                ttk.Label(details_window, text=f"{col_name}").grid(row=row_number, column=0, sticky=tk.W, padx=10, pady=5)
                ttk.Label(details_window, text=":").grid(row=row_number, column=1, sticky=tk.W, padx=5, pady=5)
                ttk.Label(details_window, text=f"{value}").grid(row=row_number, column=2, sticky=tk.W, padx=10, pady=5)
                row_number += 1

        except ValueError:
            messagebox.showerror("Error", "Please enter a valid integer for rowname.")
        
    # Tkinter setup
    root = tk.Tk()
    root.title("Record Details by Rowname")

    # Nhập rownames
    ttk.Label(root, text="Enter rowname:").grid(row=0, column=0, sticky=tk.W, padx=10, pady=5)
    rowname_entry = ttk.Entry(root)
    rowname_entry.grid(row=0, column=1, sticky=tk.EW, padx=10, pady=5)

    # Button để hiển thị chi tiết bản ghi
    btn_show_details = ttk.Button(root, text="Show Record Details", command=show_record_details)
    btn_show_details.grid(row=1, column=0, columnspan=2, pady=10)

# Variables for pagination
current_page = 0
rows_per_page = 32
def Pagination():
  
    # Hàm để hiển thị các bản ghi cho trang hiện tại
    def display_page(page):
        global current_page
    
        # Tính số lượng bản ghi cần hiển thị
        start_row = page * rows_per_page
        end_row = start_row + rows_per_page
        page_data = df.iloc[start_row:end_row]

        # Cập nhật bảng Treeview
        for item in result_table.get_children():
            result_table.delete(item)

        for _, row in page_data.iterrows():
            result_table.insert("", tk.END, values=list(row))

        # Cập nhật chỉ số trang
        page_label.config(text=f"Page {current_page + 1} of {num_pages}")

    # Hàm chuyển sang trang tiếp theo
    def next_page():
        global current_page
        if current_page < num_pages - 1:
            current_page += 1
            display_page(current_page)

    # Hàm quay lại trang trước đó
    def previous_page():
        global current_page
        if current_page > 0:
            current_page -= 1
            display_page(current_page)

    # Tkinter setup
    root = tk.Tk()
    root.title("Pagination")

    # Tạo bảng Treeview để hiển thị dữ liệu
    result_table = ttk.Treeview(root)
    result_table.pack(fill=tk.BOTH, expand=True)

    # Cài đặt cột cho bảng
    result_table["columns"] = list(df.columns)
    result_table["show"] = "headings"

    # Cài đặt chiều rộng và căn chỉnh các cột
   

    # Điều chỉnh chiều rộng cột và căn chỉnh
    for col_name in df.columns:
        result_table.heading(col_name, text=col_name)
        result_table.column(col_name, width=50, anchor='w')

    # Tính tổng số trang
    num_pages = (len(df) + rows_per_page - 1) // rows_per_page

    # Tạo page_label sau khi tính số trang
    page_label = ttk.Label(root, text=f"Page {current_page + 1} of {num_pages}")
    page_label.pack(side=tk.LEFT, padx=10, pady=10)

    # Hiển thị trang đầu tiên
    display_page(current_page)

    # Các nút điều hướng phân trang
    previous_button = ttk.Button(root, text="Previous", command=previous_page)
    previous_button.pack(side=tk.LEFT, padx=10, pady=10)

    next_button = ttk.Button(root, text="Next", command=next_page)
    next_button.pack(side=tk.LEFT, padx=10, pady=10)
    
def Search_Filter():
    filter.set_dataframe(df)
    # Hàm áp dụng phương pháp tìm kiếm/lọc
    def apply_filter():
        filter_method = filter_var.get()

        if filter_method == 'filter by condition':
            filter.filter_by_condition()
        elif filter_method == 'filter by columns':
            filter.filter_by_columns()
        elif filter_method == 'filter by row':
            filter.filter_by_rows()
        elif filter_method == 'sort by column':
            filter.sort_by_column()
        # else:
        #     tk.messagebox.showerror("Error", "Invalid filter method.")

    # Tkinter setup
    root = tk.Tk()
    root.title("Search and Filter")

    # Frame cho giao diện tìm kiếm
    main_frame = ttk.Frame(root, padding=10)
    main_frame.grid(row=0, column=0, sticky="NSEW")

    # Label và combobox để chọn phương pháp lọc
    ttk.Label(main_frame, text="Select Filter Method:").grid(row=0, column=0, sticky=tk.W, padx=10, pady=10)
    filter_var = tk.StringVar()
    filter_dropdown = ttk.Combobox(main_frame, textvariable=filter_var, values=["filter by condition", "filter by columns", "filter by rows", "sort by column"])
    filter_dropdown.grid(row=0, column=1, sticky=tk.EW, padx=10, pady=10)

    # Nút áp dụng bộ lọc
    search_button = ttk.Button(main_frame, text="Search and Filter", command=apply_filter)
    search_button.grid(row=1, column=0, columnspan=2, pady=10)

    root.mainloop()

#FILTER

def set_dataframe(dataframe):
    global df
    df = dataframe
    
def root(title):
    filter_window = tk.Toplevel()
    filter_window.title(title)
    frame = ttk.Frame(filter_window, padding=10)
    frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
    return frame
    
def filter_by_condition():
    
    def apply_condition():
        col = col_var.get()
        if col not in df.columns:
            messagebox.showerror("Error", "The selected column does not exist in the dataset.")
            return

        if col in ['rownames', 'nr', 'year', 'school', 'exper', 'wage']:
            try:
                choice = comp_type_var.get()
                val = float(value_entry.get())
                if choice == "greater than":
                    result = df[df[col] > val]
                elif choice == "greater than or equal to":
                    result = df[df[col] >= val]
                elif choice == "less than":
                    result = df[df[col] < val]
                elif choice == "less than or equal to":
                    result = df[df[col] <= val]
                elif choice == "equal to":
                    result = df[df[col] == val]
                elif choice == "different from":
                    result = df[df[col] != val]
                else:
                    messagebox.showerror("Error", "Invalid comparison type.")
                    return
            except ValueError:
                 messagebox.showerror("Error", "Please enter a valid numeric value.")
                 return
        else:
            cond = value_entry.get()
            result = df[df[col] == cond]

        # Hiển thị kết quả
        display_dataframe(result, "Filtered by Condition")
        
    frame = root("Filter by condition")
       
    # Column Selection for Apply Condition
    ttk.Label(frame, text="Select Column for Condition:").grid(row=0, column=0, sticky=tk.W)
    col_var = tk.StringVar()
    col_dropdown = ttk.Combobox(frame, textvariable=col_var, values=df.columns.tolist())
    col_dropdown.grid(row=0, column=1, sticky=tk.EW)

    # Comparison Type for Apply Condition
    ttk.Label(frame, text="Comparison Type:").grid(row=1, column=0, sticky=tk.W)
    comp_type_var = tk.StringVar()
    comp_dropdown = ttk.Combobox(frame, textvariable=comp_type_var, values=["greater than", "greater than or equal to", "less than", "less than or equal to", "equal to", "different from"])
    comp_dropdown.grid(row=1, column=1, sticky=tk.EW)


    # Value Entry for Apply Condition
    ttk.Label(frame, text="Enter Value/Condition:").grid(row=2, column=0, sticky=tk.W)
    value_entry = ttk.Entry(frame)
    value_entry.grid(row=2, column=1, sticky=tk.EW)


    # Button to Apply Condition
    filter_condition_button = ttk.Button(frame, text="Filter by Condition", command=apply_condition)
    filter_condition_button.grid(row=3, column=0, columnspan=2, pady=10)
    
# Hàm lọc theo cột
def filter_by_columns():
    def apply_columns():
        selected_cols = [listbox.get(i) for i in listbox.curselection()]
        if not selected_cols:
            messagebox.showwarning("Warning", "No columns selected. Displaying all columns.")
            selected_cols = list(df.columns)

        result = df[selected_cols]

        # Hiển thị kết quả
        display_dataframe(result, "Filtered by Columns")
        
    frame = root("Filter by columns")
    
    # Column Selection for Apply Columns
    ttk.Label(frame, text="Select Columns to Display:").grid(row=0, column=0, sticky=tk.W)
    listbox = tk.Listbox(frame, selectmode="multiple", exportselection=False, height=6)
    for col_name in df.columns:
        listbox.insert(tk.END, col_name)
    listbox.grid(row=0, column=1, sticky=tk.EW)

    # Button to Apply Columns
    filter_columns_button = ttk.Button(frame, text="Filter by Columns", command=apply_columns)
    filter_columns_button.grid(row=1, column=0, columnspan=2, pady=10)
        
def filter_by_rows():
    def apply_rows():
        try:
            from_row = int(from_entry.get())
            to_row = int(to_entry.get())

            if from_row < 0 or to_row >= len(df):
                messagebox.showerror("Error", "Invalid row range. Please enter valid row indices.")
                return

            result = df.iloc[from_row:to_row + 1]  # Lọc các hàng từ `from_row` đến `to_row`
            display_dataframe(result, "Filtered by Rows")
        except ValueError:
            messagebox.showerror("Error", "Please enter valid integers for row indices.")
            return
        
    frame = root("Filter by rows")
        
    # Row Selection for Filtering by Rows
    ttk.Label(frame, text="From Row:").grid(row=0, column=0, sticky=tk.W)
    from_entry = ttk.Entry(frame)
    from_entry.grid(row=0, column=1, sticky=tk.EW)

    ttk.Label(frame, text="To Row:").grid(row=1, column=0, sticky=tk.W)
    to_entry = ttk.Entry(frame)
    to_entry.grid(row=1, column=1, sticky=tk.EW)

    # Button to Filter by Rows
    filter_rows_button = ttk.Button(frame, text="Filter by Rows", command=apply_rows)
    filter_rows_button.grid(row=2, column=0, columnspan=2, pady=10)
 
def sort_by_column():
    def sort():
        col = sort_col_var.get()
        if col not in df.columns:
            messagebox.showerror("Error", "The selected column does not exist in the dataset.")
            return
    
        # Kiểm tra hướng sắp xếp
        ascending = sort_order_var.get() == "Ascending"
    
        # Sắp xếp theo cột đã chọn và hướng đã chọn
        result = df.sort_values(by=col, ascending=ascending)

        # Hiển thị kết quả
        display_dataframe(result, f"Sorted by {col} ({'Ascending' if ascending else 'Descending'})")
        
    frame = root("Sort by column")
    
    # Cột để sắp xếp
    sort_col_var = tk.StringVar()
    ttk.Label(frame, text="Select Column to Sort By:").grid(row=10, column=0, sticky=tk.W)
    sort_col_dropdown = ttk.Combobox(frame, textvariable=sort_col_var, values=df.columns.tolist())
    sort_col_dropdown.grid(row=10, column=1, sticky=tk.EW)

    # Hướng sắp xếp
    sort_order_var = tk.StringVar(value="Ascending")
    ttk.Label(frame, text="Sort Order:").grid(row=11, column=0, sticky=tk.W)
    sort_order_dropdown = ttk.Combobox(frame, textvariable=sort_order_var, values=["Ascending", "Descending"])
    sort_order_dropdown.grid(row=11, column=1, sticky=tk.EW)

    # Button để sắp xếp theo cột
    sort_button = ttk.Button(frame, text="Sort Data", command=sort)
    sort_button.grid(row=12, column=0, columnspan=2, pady=10)

# Hàm hiển thị DataFrame
def display_dataframe(dataframe, title):
    # Tạo cửa sổ mới để hiển thị dữ liệu
    display_window = tk.Toplevel()
    display_window.title(title)

    tree = ttk.Treeview(display_window)
    tree["columns"] = list(dataframe.columns)
    tree["show"] = "headings"
 
    
    for col in dataframe.columns:
        tree.heading(col, text=col)
        tree.column(col, width=50, anchor="w")

    for _, row in dataframe.iterrows():
        tree.insert("", tk.END, values=list(row))

    tree.pack(fill=tk.BOTH, expand=True)

#UPDATE

def set_dataframe(dataframe):
    global df
    df = dataframe

def update_record():
    filter.set_dataframe(df)
    def search_record():
        try:
            rowname = int(rowname_entry.get())
            record = df[df['rownames'] == rowname]
            if record.empty:
                messagebox.showerror("Error", "Rowname not found!")
                return

            # Nếu tìm thấy bản ghi, mở cửa sổ chỉnh sửa
            edit_record(record.iloc[0])

        except ValueError:
            messagebox.showerror("Error", "Please enter a valid rowname.")

    def edit_record(record):
        edit_window = tk.Toplevel(root)
        edit_window.title(f"Edit Record - Rowname: {record['rownames']}")

        # Các trường sẽ hiển thị và chỉnh sửa
        def save_changes():
            try:
                # Lấy giá trị mới từ các ô nhập liệu
                updated_row = {
                    "rownames": record['rownames'],
                    "nr": int(nr_entry.get()) if nr_entry.get() else record["nr"],
                    "year": int(year_entry.get()) if year_entry.get() else record["year"],
                    "school": int(school_entry.get()) if school_entry.get() else record["school"],
                    "exper": int(exper_entry.get()) if exper_entry.get() else record["exper"],
                    "union": union_var.get() if union_var.get() else record["union"],
                    "ethn": ethn_var.get() if ethn_var.get() else record["ethn"],
                    "maried": maried_var.get() if maried_var.get() else record["maried"],
                    "health": health_var.get() if health_var.get() else record["health"],
                    "wage": float(wage_entry.get()) if wage_entry.get() else record["wage"],
                    "industry": industry_entry.get() if industry_entry.get() else record["industry"],
                    "occupation": occupation_entry.get() if occupation_entry.get() else record["occupation"],
                    "residence": residence_var.get() if residence_var.get() else record["residence"]
                }

                # Cập nhật dữ liệu từng cột
                for col, value in updated_row.items():
                    df.loc[df['rownames'] == record['rownames'], col] = value

                # Lưu vào CSV
          #      df.to_csv(file_path, index=False)

                messagebox.showinfo("Success", "Record updated successfully.")
                edit_window.destroy()
            except ValueError:
                messagebox.showerror("Error", "Please enter valid values.")
            

        # Hiển thị các trường và giá trị cũ
        ttk.Label(edit_window, text="nr:").grid(row=0, column=0, sticky=tk.W, padx=10, pady=5)
        nr_entry = ttk.Entry(edit_window)
        nr_entry.insert(0, record["nr"])
        nr_entry.grid(row=0, column=1, sticky=tk.EW, padx=10, pady=5)

        ttk.Label(edit_window, text="year:").grid(row=1, column=0, sticky=tk.W, padx=10, pady=5)
        year_entry = ttk.Entry(edit_window)
        year_entry.insert(0, record["year"])
        year_entry.grid(row=1, column=1, sticky=tk.EW, padx=10, pady=5)

        ttk.Label(edit_window, text="school:").grid(row=2, column=0, sticky=tk.W, padx=10, pady=5)
        school_entry = ttk.Entry(edit_window)
        school_entry.insert(0, record["school"])
        school_entry.grid(row=2, column=1, sticky=tk.EW, padx=10, pady=5)

        ttk.Label(edit_window, text="exper:").grid(row=3, column=0, sticky=tk.W, padx=10, pady=5)
        exper_entry = ttk.Entry(edit_window)
        exper_entry.insert(0, record["exper"])
        exper_entry.grid(row=3, column=1, sticky=tk.EW, padx=10, pady=5)

        ttk.Label(edit_window, text="union:").grid(row=4, column=0, sticky=tk.W, padx=10, pady=5)
        union_var = tk.StringVar(value=record["union"])
        union_entry = ttk.Combobox(edit_window, textvariable=union_var, values=["yes", "no"])
        union_entry.grid(row=4, column=1, sticky=tk.EW, padx=10, pady=5)

        ttk.Label(edit_window, text="ethn:").grid(row=5, column=0, sticky=tk.W, padx=10, pady=5)
        ethn_var = tk.StringVar(value=record["ethn"])
        ethn_entry = ttk.Combobox(edit_window, textvariable=ethn_var, values=["black", "hisp", "other"])
        ethn_entry.grid(row=5, column=1, sticky=tk.EW, padx=10, pady=5)

        ttk.Label(edit_window, text="maried:").grid(row=6, column=0, sticky=tk.W, padx=10, pady=5)
        maried_var = tk.StringVar(value=record["maried"])
        maried_entry = ttk.Combobox(edit_window, textvariable=maried_var, values=["yes", "no"])
        maried_entry.grid(row=6, column=1, sticky=tk.EW, padx=10, pady=5)

        ttk.Label(edit_window, text="health:").grid(row=7, column=0, sticky=tk.W, padx=10, pady=5)
        health_var = tk.StringVar(value=record["health"])
        health_entry = ttk.Combobox(edit_window, textvariable=health_var, values=["yes", "no"])
        health_entry.grid(row=7, column=1, sticky=tk.EW, padx=10, pady=5)

        ttk.Label(edit_window, text="wage:").grid(row=8, column=0, sticky=tk.W, padx=10, pady=5)
        wage_entry = ttk.Entry(edit_window)
        wage_entry.insert(0, record["wage"])
        wage_entry.grid(row=8, column=1, sticky=tk.EW, padx=10, pady=5)

        ttk.Label(edit_window, text="industry:").grid(row=9, column=0, sticky=tk.W, padx=10, pady=5)
        industry_entry = ttk.Entry(edit_window)
        industry_entry.insert(0, record["industry"])
        industry_entry.grid(row=9, column=1, sticky=tk.EW, padx=10, pady=5)

        ttk.Label(edit_window, text="occupation:").grid(row=10, column=0, sticky=tk.W, padx=10, pady=5)
        occupation_entry = ttk.Entry(edit_window)
        occupation_entry.insert(0, record["occupation"])
        occupation_entry.grid(row=10, column=1, sticky=tk.EW, padx=20, pady=5)

        ttk.Label(edit_window, text="residence:").grid(row=11, column=0, sticky=tk.W, padx=10, pady=5)
        residence_var = tk.StringVar(value=record["residence"])
        residence_entry = ttk.Entry(edit_window, textvariable=residence_var)
        residence_entry.grid(row=11, column=1, sticky=tk.EW, padx=10, pady=5)

        # Nút Lưu thay đổi
        save_button = ttk.Button(edit_window, text="Save Changes", command=save_changes)
        save_button.grid(row=12, column=0, columnspan=2, pady=10)
        
    

    # Cửa sổ nhập rowname
    root = tk.Tk()
    root.title("Update Record")

    ttk.Label(root, text="Enter rowname to update:").grid(row=0, column=0, padx=10, pady=10)
    rowname_entry = ttk.Entry(root)
    rowname_entry.grid(row=0, column=1, padx=10, pady=10)

    search_button = ttk.Button(root, text="Search", command=search_record)
    search_button.grid(row=1, column=0, columnspan=2, pady=10)

    
    # update_button = ttk.Button(root, text="Update Record", command=search_record)
    # update_button.pack(pady=20)

    root.mainloop()

def update_wage_by_exper():
    filter.set_dataframe(df)
    root = tk.Tk()
    root.title("Update wage with raise by exper level")
    
    # Nhập phần trăm tăng lương với trình độ beginner
    ttk.Label(root, text="Beginner:").grid(row=0, column=0, sticky=tk.W, padx=10, pady=5)
    beginner_entry = ttk.Entry(root)
    beginner_entry.grid(row=0, column=1, sticky=tk.EW, padx=10, pady=5)

    # Nhập phần trăm tăng lương với trình độ intermediate
    ttk.Label(root, text="Intermediate:").grid(row=1, column=0, sticky=tk.W, padx=10, pady=5)
    intermediate_entry = ttk.Entry(root)
    intermediate_entry.grid(row=1, column=1, sticky=tk.EW, padx=10, pady=5)

    # Nhập phần trăm tăng lương với trình độ advanced
    ttk.Label(root, text="Advanced:").grid(row=2, column=0, sticky=tk.W, padx=10, pady=5)
    advanced_entry = ttk.Entry(root)
    advanced_entry.grid(row=2, column=1, sticky=tk.EW, padx=10, pady=5)

    # Nhập phần trăm tăng lương với trình độ expert
    ttk.Label(root, text="Expert:").grid(row=3, column=0, sticky=tk.W, padx=10, pady=5)
    expert_entry = ttk.Entry(root)
    expert_entry.grid(row=3, column=1, sticky=tk.EW, padx=10, pady=5)
    
    raise_map = {
        "beginner" : beginner_entry,
        "intermediate" : intermediate_entry,
        "advanced" : advanced_entry,
        "expert" : expert_entry
        }

    df["wage"] = df.apply(
        lambda row: row["wage"] + math.log(1 + raise_map.get(row["exper_level"], 0)),
        axis = 1                            
    )
    
def update_wage_by_school():
    filter.set_dataframe(df)
    root = tk.Tk()
    root.title("Update wage with raise by school level")
    
    # Nhập phần trăm tăng lương với trình độ very low
    ttk.Label(root, text="Very low:").grid(row=0, column=0, sticky=tk.W, padx=10, pady=5)
    vlow_entry = ttk.Entry(root)
    vlow_entry.grid(row=0, column=1, sticky=tk.EW, padx=10, pady=5)

    # Nhập phần trăm tăng lương với trình độ low
    ttk.Label(root, text="Low:").grid(row=1, column=0, sticky=tk.W, padx=10, pady=5)
    low_entry = ttk.Entry(root)
    low_entry.grid(row=1, column=1, sticky=tk.EW, padx=10, pady=5)

    # Nhập phần trăm tăng lương với trình độ intermediate
    ttk.Label(root, text="Intermediate:").grid(row=2, column=0, sticky=tk.W, padx=10, pady=5)
    intermediate_entry = ttk.Entry(root)
    intermediate_entry.grid(row=2, column=1, sticky=tk.EW, padx=10, pady=5)

    # Nhập phần trăm tăng lương với trình độ high
    ttk.Label(root, text="High:").grid(row=3, column=0, sticky=tk.W, padx=10, pady=5)
    high_entry = ttk.Entry(root)
    high_entry.grid(row=3, column=1, sticky=tk.EW, padx=10, pady=5)

    raise_map = {
        "very low" : vlow_entry,
        "low" : low_entry,
        "intermediate" : intermediate_entry,
        "high" : high_entry
        }

    df["wage"] = df.apply(
        lambda row: row["wage"] + math.log(1 + raise_map.get(row["school_level"], 0)),
        axis = 1                            
    )

#DELETE

def delete_row():
    def del_row():
        global df
        try:
            # Lấy giá trị rownames người dùng nhập
            rowname_value = int(rowname_entry.get())
        
            # Kiểm tra xem rowname_value có tồn tại trong cột 'rownames' không
            record = df[df['rownames'] == rowname_value]
        
            if record.empty:
                messagebox.showerror("Error", "No record found for the given rowname.")
                return
        
            df = df[df['rownames'] != rowname_value]
            messagebox.showinfo("Success", f"Row with rowname {rowname_value} deleted.")
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid integer for rowname.")
    # Tkinter setup
    root = tk.Tk()
    root.title("Delete row")

    # Nhập rownames
    ttk.Label(root, text="Enter rowname:").grid(row=0, column=0, sticky=tk.W, padx=10, pady=5)
    rowname_entry = ttk.Entry(root)
    rowname_entry.grid(row=0, column=1, sticky=tk.EW, padx=10, pady=5)

    # Button để hiển thị chi tiết bản ghi
    btn_del = ttk.Button(root, text="Delete", command=del_row)
    btn_del.grid(row=1, column=0, columnspan=2, pady=10)
    
def delete_column():
    def del_col():
        global df
        try:
            
            colname_value = colname_entry.get()
            
          
            if colname_value not in df.columns:
                messagebox.showerror("Error", "No column found with the given name.")
                return
            
            # Delete the column
            df = df.drop(columns=[colname_value])
            messagebox.showinfo("Success", f"Column '{colname_value}' deleted.")
        except Exception as e:
            messagebox.showerror("Error", str(e))

    # Tkinter setup
    root = tk.Tk()
    root.title("Delete Column")

   
    ttk.Label(root, text="Enter column name:").grid(row=0, column=0, sticky=tk.W, padx=10, pady=5)
    colname_entry = ttk.Entry(root)
    colname_entry.grid(row=0, column=1, sticky=tk.EW, padx=10, pady=5)

   
    btn_del = ttk.Button(root, text="Delete", command=del_col)
    btn_del.grid(row=1, column=0, columnspan=2, pady=10)
    
    

    
    



    

