import tkinter as tk
from tkinter import ttk, messagebox
import pandas as pd
import math

df = pd.read_csv("NewMales.csv")

#CREATE
def create_row(df, callback):
    """Thêm một bản ghi mới vào DataFrame và lưu vào tệp CSV."""
    # Khởi tạo cửa sổ giao diện để nhập dữ liệu
    root = tk.Tk()
    root.title("Create a new record")

    rowname = len(df) + 1  # Xác định giá trị rowname mới

    def save_record():
        """Lưu bản ghi mới và cập nhật vào DataFrame."""
        # Lấy dữ liệu từ các trường nhập
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

        # Cập nhật DataFrame và lưu vào tệp CSV
        global df
        df = pd.concat([df, pd.DataFrame([new_row])], ignore_index=True)
        df.to_csv('NewMales.csv', index=False)

        # Gọi callback để cập nhật TreeView nếu có
        if callback:
            callback(new_row)
        root.destroy()  # Đóng cửa sổ nhập liệu
        messagebox.showinfo("Success", "Create successfully.")
    # Tạo giao diện nhập liệu
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
    root.mainloop()
    return None

#READ
  
def Record_Details():
    """Hiển thị chi tiết một bản ghi dựa trên giá trị 'rownames'."""
    def show_record_details():
        """Tìm và hiển thị chi tiết bản ghi theo rowname."""
        try:
            # Lấy giá trị rowname người dùng nhập
            rowname_value = int(rowname_entry.get())
        
            # Lọc DataFrame để tìm bản ghi tương ứng
            record = df[df['rownames'] == rowname_value]
        
            if record.empty:
                # Thông báo lỗi nếu không tìm thấy
                messagebox.showerror("Error", "No record found for the given rowname.")
                return

            # Hiển thị chi tiết bản ghi
            details_window = tk.Toplevel(root)
            details_window.title("Record Details")

            # Duyệt qua các cột và giá trị để hiển thị
            row_number = 0
            for col_name, value in record.iloc[0].items():
                ttk.Label(details_window, text=f"{col_name}").grid(row=row_number, column=0, sticky=tk.W, padx=10, pady=5)
                ttk.Label(details_window, text=":").grid(row=row_number, column=1, sticky=tk.W, padx=5, pady=5)
                ttk.Label(details_window, text=f"{value}").grid(row=row_number, column=2, sticky=tk.W, padx=10, pady=5)
                row_number += 1

        except ValueError:
            # Thông báo lỗi nếu nhập giá trị không hợp lệ
            messagebox.showerror("Error", "Please enter a valid integer for rowname.")
    
    # Khởi tạo giao diện nhập liệu rowname
    root = tk.Tk()
    root.title("Record Details by Rowname")

    # Tạo trường nhập liệu và nút bấm
    ttk.Label(root, text="Enter rowname:").grid(row=0, column=0, sticky=tk.W, padx=10, pady=5)
    rowname_entry = ttk.Entry(root)
    rowname_entry.grid(row=0, column=1, sticky=tk.EW, padx=10, pady=5)

    btn_show_details = ttk.Button(root, text="Show Record Details", command=show_record_details)
    btn_show_details.grid(row=1, column=0, columnspan=2, pady=10)

# Variables for pagination
current_page = 0
rows_per_page = 32

def Pagination():
    """Thực hiện phân trang hiển thị dữ liệu từ DataFrame."""
    def display_page(page):
        """Hiển thị dữ liệu của trang hiện tại."""
        global current_page

        # Tính chỉ số bản ghi cần hiển thị
        start_row = page * rows_per_page
        end_row = start_row + rows_per_page
        page_data = df.iloc[start_row:end_row]

        # Xóa dữ liệu cũ trong bảng TreeView
        for item in result_table.get_children():
            result_table.delete(item)

        # Thêm dữ liệu mới vào TreeView
        for _, row in page_data.iterrows():
            result_table.insert("", tk.END, values=list(row))

        # Cập nhật nhãn hiển thị số trang
        page_label.config(text=f"Page {current_page + 1} of {num_pages}")

    def next_page():
        """Chuyển sang trang tiếp theo."""
        global current_page
        if current_page < num_pages - 1:
            current_page += 1
            display_page(current_page)

    def previous_page():
        """Quay lại trang trước đó."""
        global current_page
        if current_page > 0:
            current_page -= 1
            display_page(current_page)

    # Khởi tạo giao diện phân trang
    root = tk.Tk()
    root.title("Pagination")

    # Tạo bảng TreeView để hiển thị dữ liệu
    result_table = ttk.Treeview(root)
    result_table.pack(fill=tk.BOTH, expand=True)

    # Cài đặt các cột cho TreeView
    result_table["columns"] = list(df.columns)
    result_table["show"] = "headings"

    for col_name in df.columns:
        result_table.heading(col_name, text=col_name)
        result_table.column(col_name, width=50, anchor='w')

    # Tính tổng số trang
    num_pages = (len(df) + rows_per_page - 1) // rows_per_page

    # Tạo nhãn và nút điều hướng
    page_label = ttk.Label(root, text=f"Page {current_page + 1} of {num_pages}")
    page_label.pack(side=tk.LEFT, padx=10, pady=10)

    previous_button = ttk.Button(root, text="Previous", command=previous_page)
    previous_button.pack(side=tk.LEFT, padx=10, pady=10)

    next_button = ttk.Button(root, text="Next", command=next_page)
    next_button.pack(side=tk.LEFT, padx=10, pady=10)

    # Hiển thị trang đầu tiên
    display_page(current_page)

def Search_Filter():
    """
    Tạo giao diện tìm kiếm và lọc dữ liệu.
    """
    # Hàm áp dụng phương pháp lọc
    def apply_filter():
        """
        Áp dụng phương pháp lọc dựa trên tùy chọn mà người dùng đã chọn.
        """
        # Lấy giá trị đã chọn từ combobox
        filter_method = filter_var.get()
        # Kiểm tra giá trị đã chọn và thực hiện hành động tương ứng
        if filter_method == 'filter by condition':
            # Gọi hàm lọc dữ liệu theo điều kiện
            filter_by_condition()
        elif filter_method == 'filter by columns':
            # Gọi hàm lọc dữ liệu theo cột
            filter_by_columns()
        elif filter_method == 'filter by rows':
            # Gọi hàm lọc dữ liệu theo hàng
            filter_by_rows()
        elif filter_method == 'sort by column':
            # Gọi hàm sắp xếp dữ liệu theo cột
            sort_by_column()
        else:
            # Hiển thị thông báo lỗi nếu phương pháp lọc không hợp lệ
            tk.messagebox.showerror("Error", "Invalid filter method.")

    # Khởi tạo cửa sổ Tkinter
    root = tk.Tk()
    root.title("Search and Filter")  # Đặt tiêu đề cho cửa sổ

    # Tạo Frame chính để chứa các thành phần giao diện
    main_frame = ttk.Frame(root, padding=10)
    main_frame.grid(row=0, column=0, sticky="NSEW")  # Gán vị trí cho Frame chính

    # Thêm nhãn để hướng dẫn người dùng chọn phương pháp lọc
    ttk.Label(main_frame, text="Select Filter Method:").grid(row=0, column=0, sticky=tk.W, padx=10, pady=10)

    # Tạo combobox để hiển thị danh sách các phương pháp lọc
    filter_var = tk.StringVar(root)  # Biến để lưu giá trị được chọn từ combobox
    filter_dropdown = ttk.Combobox(
        main_frame,
        textvariable=filter_var,
        values=["filter by condition", "filter by columns", "filter by rows", "sort by column"]
    )
    filter_dropdown.grid(row=0, column=1, sticky=tk.EW, padx=10, pady=10)  # Gán vị trí cho combobox

    # Tạo nút để áp dụng bộ lọc
    search_button = ttk.Button(main_frame, text="Search and Filter", command=apply_filter)
    search_button.grid(row=1, column=0, columnspan=2, pady=10)  # Gán vị trí cho nút

    # Chạy vòng lặp chính để hiển thị giao diện
    root.mainloop()



#FILTER

def set_dataframe(dataframe):
    """
    Gán DataFrame toàn cục để sử dụng trong các hàm lọc và hiển thị.
    """
    global df
    df = dataframe

def root(title):
    """
    Tạo cửa sổ giao diện phụ với tiêu đề được chỉ định.
    """
    # Tạo cửa sổ con (Toplevel) để hiển thị các lựa chọn và thao tác
    filter_window = tk.Toplevel()
    filter_window.title(title)

    # Tạo Frame chính để chứa giao diện
    frame = ttk.Frame(filter_window, padding=10)
    frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
    return frame

def filter_by_condition():
    """
    Lọc dữ liệu dựa trên điều kiện (so sánh hoặc giá trị cụ thể).
    """
    def apply_condition():
        """
        Áp dụng điều kiện lọc dữ liệu và hiển thị kết quả.
        """
        # Lấy cột được chọn từ combobox
        col = col_var.get()
        if col not in df.columns:
            messagebox.showerror("Error", "The selected column does not exist in the dataset.")
            return

        # Kiểm tra nếu cột là số thì thực hiện so sánh, nếu không thì lọc bằng giá trị
        if col in ['rownames', 'nr', 'year', 'school', 'exper', 'wage']:
            try:
                choice = comp_type_var.get()  # Lấy kiểu so sánh từ combobox
                val = float(value_entry.get())  # Lấy giá trị nhập vào
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
            cond = value_entry.get()  # Lấy giá trị nhập vào để lọc bằng giá trị
            result = df[df[col] == cond]

        # Hiển thị kết quả lọc
        display_dataframe(result, "Filtered by Condition")

    # Tạo cửa sổ giao diện lọc theo điều kiện
    frame = root("Filter by condition")

    # Tùy chọn cột để lọc
    ttk.Label(frame, text="Select Column for Condition:").grid(row=0, column=0, sticky=tk.W)
    col_var = tk.StringVar()
    col_dropdown = ttk.Combobox(frame, textvariable=col_var, values=df.columns.tolist())
    col_dropdown.grid(row=0, column=1, sticky=tk.EW)

    # Tùy chọn kiểu so sánh
    ttk.Label(frame, text="Comparison Type:").grid(row=1, column=0, sticky=tk.W)
    comp_type_var = tk.StringVar()
    comp_dropdown = ttk.Combobox(frame, textvariable=comp_type_var, values=["greater than", "greater than or equal to", "less than", "less than or equal to", "equal to", "different from"])
    comp_dropdown.grid(row=1, column=1, sticky=tk.EW)

    # Nhập giá trị để lọc
    ttk.Label(frame, text="Enter Value/Condition:").grid(row=2, column=0, sticky=tk.W)
    value_entry = ttk.Entry(frame)
    value_entry.grid(row=2, column=1, sticky=tk.EW)

    # Nút áp dụng điều kiện lọc
    filter_condition_button = ttk.Button(frame, text="Filter by Condition", command=apply_condition)
    filter_condition_button.grid(row=3, column=0, columnspan=2, pady=10)

def filter_by_columns():
    """
    Lọc dữ liệu dựa trên các cột được chọn.
    """
    def apply_columns():
        """
        Áp dụng lựa chọn cột để hiển thị dữ liệu.
        """
        # Lấy danh sách các cột được chọn từ listbox
        selected_cols = [listbox.get(i) for i in listbox.curselection()]
        if not selected_cols:
            messagebox.showwarning("Warning", "No columns selected. Displaying all columns.")
            selected_cols = list(df.columns)  # Hiển thị toàn bộ cột nếu không chọn gì

        result = df[selected_cols]

        # Hiển thị kết quả lọc
        display_dataframe(result, "Filtered by Columns")

    # Tạo cửa sổ giao diện lọc theo cột
    frame = root("Filter by columns")

    # Listbox để chọn các cột
    ttk.Label(frame, text="Select Columns to Display:").grid(row=0, column=0, sticky=tk.W)
    listbox = tk.Listbox(frame, selectmode="multiple", exportselection=False, height=6)
    for col_name in df.columns:
        listbox.insert(tk.END, col_name)
    listbox.grid(row=0, column=1, sticky=tk.EW)

    # Nút áp dụng lọc theo cột
    filter_columns_button = ttk.Button(frame, text="Filter by Columns", command=apply_columns)
    filter_columns_button.grid(row=1, column=0, columnspan=2, pady=10)

def filter_by_rows():
    """
    Lọc dữ liệu dựa trên chỉ số hàng.
    """
    def apply_rows():
        """
        Áp dụng giới hạn hàng để hiển thị dữ liệu.
        """
        try:
            from_row = int(from_entry.get())  # Lấy chỉ số hàng bắt đầu
            to_row = int(to_entry.get())  # Lấy chỉ số hàng kết thúc

            if from_row < 0 or to_row >= len(df):
                messagebox.showerror("Error", "Invalid row range. Please enter valid row indices.")
                return

            # Lọc các hàng trong khoảng từ `from_row` đến `to_row`
            result = df.iloc[from_row:to_row + 1]
            display_dataframe(result, "Filtered by Rows")
        except ValueError:
            messagebox.showerror("Error", "Please enter valid integers for row indices.")
            return

    # Tạo giao diện lọc theo hàng
    frame = root("Filter by rows")

    # Nhập chỉ số hàng bắt đầu
    ttk.Label(frame, text="From Row:").grid(row=0, column=0, sticky=tk.W)
    from_entry = ttk.Entry(frame)
    from_entry.grid(row=0, column=1, sticky=tk.EW)

    # Nhập chỉ số hàng kết thúc
    ttk.Label(frame, text="To Row:").grid(row=1, column=0, sticky=tk.W)
    to_entry = ttk.Entry(frame)
    to_entry.grid(row=1, column=1, sticky=tk.EW)

    # Nút áp dụng lọc theo hàng
    filter_rows_button = ttk.Button(frame, text="Filter by Rows", command=apply_rows)
    filter_rows_button.grid(row=2, column=0, columnspan=2, pady=10)

def sort_by_column():
    """
    Sắp xếp dữ liệu theo một cột đã chọn với thứ tự tăng hoặc giảm dần.
    """
    def sort():
        """
        Áp dụng sắp xếp dữ liệu theo cột và thứ tự được chỉ định.
        """
        # Lấy cột được chọn để sắp xếp
        col = sort_col_var.get()
        if col not in df.columns:
            messagebox.showerror("Error", "The selected column does not exist in the dataset.")
            return

        # Kiểm tra hướng sắp xếp (tăng dần hoặc giảm dần)
        ascending = sort_order_var.get() == "Ascending"

        # Thực hiện sắp xếp
        result = df.sort_values(by=col, ascending=ascending)

        # Hiển thị kết quả sắp xếp
        display_dataframe(result, f"Sorted by {col} ({'Ascending' if ascending else 'Descending'})")

    # Tạo giao diện sắp xếp theo cột
    frame = root("Sort by column")

    # Chọn cột để sắp xếp
    sort_col_var = tk.StringVar()
    ttk.Label(frame, text="Select Column to Sort By:").grid(row=10, column=0, sticky=tk.W)
    sort_col_dropdown = ttk.Combobox(frame, textvariable=sort_col_var, values=df.columns.tolist())
    sort_col_dropdown.grid(row=10, column=1, sticky=tk.EW)

    # Chọn hướng sắp xếp
    sort_order_var = tk.StringVar(value="Ascending")
    ttk.Label(frame, text="Sort Order:").grid(row=11, column=0, sticky=tk.W)
    sort_order_dropdown = ttk.Combobox(frame, textvariable=sort_order_var, values=["Ascending", "Descending"])
    sort_order_dropdown.grid(row=11, column=1, sticky=tk.EW)

    # Nút để sắp xếp
    sort_button = ttk.Button(frame, text="Sort Data", command=sort)
    sort_button.grid(row=12, column=0, columnspan=2, pady=10)


def display_dataframe(dataframe, title):
    """
    Hiển thị DataFrame trong một cửa sổ mới với định dạng bảng.
    """
    # Tạo cửa sổ mới để hiển thị dữ liệu
    display_window = tk.Toplevel()
    display_window.title(title)

    # Sử dụng Treeview để hiển thị dữ liệu dạng bảng
    tree = ttk.Treeview(display_window)
    tree["columns"] = list(dataframe.columns)  # Thiết lập cột theo DataFrame
    tree["show"] = "headings"  # Ẩn cột mặc định của Treeview

    # Cấu hình từng cột với tên và độ rộng
    for col in dataframe.columns:
        tree.heading(col, text=col)  # Đặt tiêu đề cho mỗi cột
        tree.column(col, width=50, anchor="w")  # Căn chỉnh nội dung cột

    # Thêm dữ liệu vào Treeview
    for _, row in dataframe.iterrows():
        tree.insert("", tk.END, values=list(row))

    # Hiển thị bảng dữ liệu trong cửa sổ
    tree.pack(fill=tk.BOTH, expand=True)

#UPDATE

def update_tree(tree, df):
    """
    Cập nhật Treeview để hiển thị dữ liệu từ DataFrame.
    """
    # Xóa tất cả các dòng hiện tại trong Treeview
    for item in tree.get_children():
        tree.delete(item)

    # Thêm lại dữ liệu từ DataFrame vào Treeview
    for _, row in df.iterrows():
        tree.insert("", "end", values=list(row))


def update_record(tree, df):
    """
    Cho phép người dùng tìm kiếm và chỉnh sửa một bản ghi trong DataFrame.
    """
    def search_record():
        """
        Tìm kiếm bản ghi trong DataFrame dựa trên giá trị 'rownames'.
        """
        try:
            rowname = int(rowname_entry.get())  # Lấy rowname từ người dùng
            record = df[df['rownames'] == rowname]  # Tìm bản ghi theo rowname
            if record.empty:
                messagebox.showerror("Error", "Rowname not found!")
                return
            # Nếu tìm thấy bản ghi, mở cửa sổ chỉnh sửa
            edit_record(record.iloc[0])
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid rowname.")

    def edit_record(record):
        """
        Hiển thị giao diện chỉnh sửa bản ghi được tìm thấy.
        """
        edit_window = tk.Toplevel(root)
        edit_window.title(f"Edit Record - Rowname: {record['rownames']}")

        def save_changes():
            """
            Lưu thay đổi vào DataFrame và cập nhật Treeview.
            """
            try:
                # Lấy giá trị mới từ các ô nhập liệu
                updated_row = {
                    "rownames": record['rownames'],
                    "nr": int(nr_entry.get()) if nr_entry.get().isdigit() else record["nr"],
                    # Tiếp tục lấy dữ liệu cho các cột khác...
                }

                # Cập nhật DataFrame với dữ liệu mới
                for col, value in updated_row.items():
                    df.loc[df['rownames'] == record['rownames'], col] = value

                # Lưu thay đổi vào file CSV và cập nhật Treeview
                df.to_csv("NewMales.csv", index=False)
                update_tree(tree, df)

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
        year_var = tk.StringVar(value=str(record["year"]))
        year_entry = ttk.Combobox(edit_window, textvariable=year_var, values=[1980, 1981, 1982, 1983, 1984, 1985, 1986, 1987])
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
        union_var = tk.StringVar(value=record["union"] if record["union"] else "no")
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
        occupation_entry.grid(row=10, column=1, sticky=tk.EW, padx=10, pady=5)


        ttk.Label(edit_window, text="residence:").grid(row=11, column=0, sticky=tk.W, padx=10, pady=5)
        residence_entry = ttk.Entry(edit_window)
        residence_entry.insert(0, record["residence"])
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
    root.mainloop()
    

def update_wage_by_exper(tree, df):
    """
    Cập nhật mức lương theo mức độ kinh nghiệm của nhân viên.
    """
    def apply():
        """
        Áp dụng thay đổi mức lương dựa trên phần trăm tăng.
        """
        try:
            # Lấy giá trị phần trăm tăng từ các ô nhập liệu
            beginner_raise = float(beginner_entry.get()) / 100
            intermediate_raise = float(intermediate_entry.get()) / 100
            advanced_raise = float(advanced_entry.get()) / 100
            expert_raise = float(expert_entry.get()) / 100

            # Cập nhật mức lương
            raise_map = {
                "beginner": beginner_raise,
                "intermediate": intermediate_raise,
                "advanced": advanced_raise,
                "expert": expert_raise,
            }

            df["wage"] = df.apply(
                lambda row: row["wage"] * (1 + raise_map.get(row["exper level"], 0)), axis=1
            )

            # Lưu thay đổi và cập nhật giao diện
            df.to_csv("NewMales.csv", index=False)
            update_tree(tree, df)
            messagebox.showinfo("Success", "Wage updated successfully.")
            root.destroy()
        except ValueError:
            messagebox.showerror("Error", "Please enter valid numbers for the raise percentages.")

    # Giao diện nhập phần trăm tăng lương
    root = tk.Tk()
    root.title("Update Wage by Experience Level")
    labels = ["Beginner", "Intermediate", "Advanced", "Expert"]
    entries = {}
    for i, label in enumerate(labels):
        ttk.Label(root, text=f"{label}:").grid(row=i, column=0, padx=10, pady=5, sticky=tk.W)
        entries[label] = ttk.Entry(root)
        entries[label].grid(row=i, column=1, padx=10, pady=5, sticky=tk.EW)

    beginner_entry, intermediate_entry, advanced_entry, expert_entry = (
        entries["Beginner"],
        entries["Intermediate"],
        entries["Advanced"],
        entries["Expert"],
    )

    apply_button = ttk.Button(root, text="Apply", command=apply)
    apply_button.grid(row=4, column=0, columnspan=2, pady=10)
    root.mainloop()

    
def update_wage_by_school(tree, df):
    """
    Cập nhật mức lương theo cấp độ học vấn của nhân viên.
    """
    def apply():
        """
        Áp dụng thay đổi mức lương dựa trên phần trăm tăng lương theo cấp độ học vấn.
        """
        try:
            # Lấy giá trị phần trăm tăng từ các ô nhập liệu
            vlow_raise = float(vlow_entry.get()) / 100
            low_raise = float(low_entry.get()) / 100
            intermediate_raise = float(intermediate_entry.get()) / 100
            high_raise = float(high_entry.get()) / 100

            # Tạo bản đồ phần trăm tăng lương theo cấp độ học vấn
            raise_map = {
                "very low": vlow_raise,
                "low": low_raise,
                "intermediate": intermediate_raise,
                "high": high_raise,
            }

            # Cập nhật mức lương trong DataFrame
            df["wage"] = df.apply(
                lambda row: row["wage"] * (1 + raise_map.get(row["school level"], 0)), axis=1
            )

            # Xóa dữ liệu hiện tại trong Treeview và thêm dữ liệu đã cập nhật
            for item in tree.get_children():
                tree.delete(item)
            for _, row in df.iterrows():
                tree.insert("", "end", values=(row["rownames"], row["school level"], row['wage']))

            # Lưu thay đổi vào file CSV và hiển thị thông báo thành công
            df.to_csv("NewMales.csv", index=False)
            update_tree(tree, df)
            messagebox.showinfo("Success", "Wage updated successfully.")
            root.destroy()
        except ValueError:
            messagebox.showerror("Error", "Please enter valid numbers for the raise percentages.")

    # Tạo giao diện người dùng để nhập phần trăm tăng lương
    root = tk.Tk()
    root.title("Update Wage by School Level")
    
    labels = ["Very Low", "Low", "Intermediate", "High"]
    entries = {}
    for i, label in enumerate(labels):
        ttk.Label(root, text=f"{label}:").grid(row=i, column=0, padx=10, pady=5, sticky=tk.W)
        entries[label] = ttk.Entry(root)
        entries[label].grid(row=i, column=1, padx=10, pady=5, sticky=tk.EW)

    vlow_entry, low_entry, intermediate_entry, high_entry = (
        entries["Very Low"],
        entries["Low"],
        entries["Intermediate"],
        entries["High"],
    )

    apply_button = ttk.Button(root, text="Apply", command=apply)
    apply_button.grid(row=4, column=0, columnspan=2, pady=10)
    root.mainloop()


#DELETE

def delete_row(df, column_name, unique_value):
    """
    Xóa một hàng trong DataFrame dựa trên giá trị duy nhất của một cột cụ thể.
    """
    # Kiểm tra nếu cột là kiểu dữ liệu số, chuyển unique_value sang kiểu tương ứng
    if pd.api.types.is_numeric_dtype(df[column_name]):
        unique_value = float(unique_value) if "." in str(unique_value) else int(unique_value)

    # Trả về DataFrame đã xóa hàng
    updated_df = df[df[column_name] != unique_value]
    return updated_df

    

    
    



    

