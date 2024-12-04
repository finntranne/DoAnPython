import tkinter as tk
from tkinter import ttk, messagebox
import pandas as pd
import math

df = pd.read_csv("NewMales.csv")

year_list = [1980, 1981, 1982, 1983, 1984, 1985, 1986, 1987]
union_values = ["yes", "no"]
ethn_values = ["black", "hisp", "other"]
maried_values = ["yes", "no"]
health_values = ["yes", "no"]

def validate_input(value, value_type, valid_values=None, non_negative=False, field_name=""):
    """
    Kiem tra tinh hop le cua gia tri dau vao.
    """
    try:
        converted_value = value_type(value)

        if non_negative and converted_value < 0:
            messagebox.showerror("Error", f"{field_name} must be non-negative but got {converted_value}.")
            return False

        if valid_values is not None and converted_value not in valid_values:
            messagebox.showerror("Error", f"{field_name} must be one of {valid_values}, but got {converted_value}.")
            return False

        return True
    except (ValueError, TypeError):
        messagebox.showerror("Error", f"Invalid input for {field_name}. Please enter a valid {value_type.__name__} value.")
        return False
    
def create_row(df, callback):
    """Them mot ban ghi moi vao DataFrame va luu vao tep CSV."""
    root = tk.Tk()
    root.title("Create a new record")
    def save_record():
        """Kiem tra du lieu va luu ban ghi moi."""
        global df
        try:
            if not validate_input(nr_entry.get(), int, non_negative=True, field_name="nr"):
                return
            if not validate_input(year_entry.get(), int, valid_values=year_list, field_name="year"):
                return
            if not validate_input(school_entry.get(), int, non_negative=True, field_name="school"):
                return
            if not validate_input(exper_entry.get(), int, non_negative=True, field_name="exper"):
                return
            if not validate_input(union_var.get(), str, valid_values=union_values, field_name="union"):
                return
            if not validate_input(ethn_var.get(), str, valid_values=ethn_values, field_name="ethn"):
                return
            if not validate_input(maried_var.get(), str, valid_values=maried_values, field_name="maried"):
                return
            if not validate_input(health_var.get(), str, valid_values=health_values, field_name="health"):
                return
            if not validate_input(wage_entry.get(), float, non_negative=True, field_name="wage"):
                return
            if not validate_input(industry_entry.get(), str, field_name="industry"):
                return
            if not validate_input(occupation_entry.get(), str, field_name="occupation"):
                return
            if not validate_input(residence_var.get(), str, field_name="residence"):
                return

            rowname = df['rownames'].max() + 1

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
                "residence": str(residence_var.get()),
                "age": 6 + int(exper_entry.get()) + int(school_entry.get()),
                "exper level": pd.cut([int(exper_entry.get())], bins=[0, 3, 8, 12, 18], labels=['beginner', 'intermediate', 'advanced', 'expert'])[0],
                "school level": pd.cut([int(school_entry.get())], bins=[0, 5, 9, 12, 16], labels=['very low', 'low', 'intermediate', 'high'])[0],
                "wage level": pd.cut([float(wage_entry.get())], bins=[-float('inf'), -2, 0, 2, 3.5, float('inf')], labels=['very low', 'low', 'medium', 'high', 'very high'])[0]
            }

            
            df = pd.concat([df, pd.DataFrame([new_row])], ignore_index=True)
            df.to_csv('NewMales.csv', index=False)
            if callback:
                callback(new_row)
            messagebox.showinfo("Success", "Record created successfully.")
            root.destroy()

        except ValueError as e:
            messagebox.showerror("Error", str(e))


    ttk.Label(root, text="nr:").grid(row=0, column=0, sticky=tk.W, padx=10, pady=5)
    nr_entry = ttk.Entry(root)
    nr_entry.grid(row=0, column=1, sticky=tk.EW, padx=10, pady=5)

    ttk.Label(root, text="year:").grid(row=1, column=0, sticky=tk.W, padx=10, pady=5)
    year_var = tk.StringVar()
    year_entry = ttk.Combobox(root, textvariable=year_var, values=[1980, 1981, 1982, 1983, 1984, 1985, 1986, 1987])
    year_entry.grid(row=1, column=1, sticky=tk.EW, padx=10, pady=5)

    ttk.Label(root, text="school:").grid(row=2, column=0, sticky=tk.W, padx=10, pady=5)
    school_entry = ttk.Entry(root)
    school_entry.grid(row=2, column=1, sticky=tk.EW, padx=10, pady=5)

    ttk.Label(root, text="exper:").grid(row=3, column=0, sticky=tk.W, padx=10, pady=5)
    exper_entry = ttk.Entry(root)
    exper_entry.grid(row=3, column=1, sticky=tk.EW, padx=10, pady=5)

    ttk.Label(root, text="union:").grid(row=4, column=0, sticky=tk.W, padx=10, pady=5)
    union_var = tk.StringVar(root)
    union_entry = ttk.Combobox(root, textvariable=union_var, values=["yes", "no"])
    union_entry.grid(row=4, column=1, sticky=tk.EW, padx=10, pady=5)

    ttk.Label(root, text="ethn:").grid(row=5, column=0, sticky=tk.W, padx=10, pady=5)
    ethn_var = tk.StringVar(root)
    ethn_entry = ttk.Combobox(root, textvariable=ethn_var, values=["black", "hisp", "other"])
    ethn_entry.grid(row=5, column=1, sticky=tk.EW, padx=10, pady=5)

    ttk.Label(root, text="maried:").grid(row=6, column=0, sticky=tk.W, padx=10, pady=5)
    maried_var = tk.StringVar(root)
    maried_entry = ttk.Combobox(root, textvariable=maried_var, values=["yes", "no"])
    maried_entry.grid(row=6, column=1, sticky=tk.EW, padx=10, pady=5)

    ttk.Label(root, text="health:").grid(row=7, column=0, sticky=tk.W, padx=10, pady=5)
    health_var = tk.StringVar(root)
    health_entry = ttk.Combobox(root, textvariable=health_var, values=["yes", "no"])
    health_entry.grid(row=7, column=1, sticky=tk.EW, padx=10, pady=5)

    ttk.Label(root, text="wage:").grid(row=8, column=0, sticky=tk.W, padx=10, pady=5)
    wage_entry = ttk.Entry(root)
    wage_entry.grid(row=8, column=1, sticky=tk.EW, padx=10, pady=5)

    ttk.Label(root, text="industry:").grid(row=9, column=0, sticky=tk.W, padx=10, pady=5)
    industry_entry = ttk.Entry(root)
    industry_entry.grid(row=9, column=1, sticky=tk.EW, padx=10, pady=5)

    ttk.Label(root, text="occupation:").grid(row=10, column=0, sticky=tk.W, padx=10, pady=5)
    occupation_entry = ttk.Entry(root)
    occupation_entry.grid(row=10, column=1, sticky=tk.EW, padx=10, pady=5)

    ttk.Label(root, text="residence:").grid(row=11, column=0, sticky=tk.W, padx=10, pady=5)
    residence_var = tk.Entry(root)
    residence_var.grid(row=11, column=1, sticky=tk.EW, padx=10, pady=5)

    save_button = ttk.Button(root, text="Create", command=save_record)
    save_button.grid(row=12, column=0, columnspan=2, pady=10)
    root.mainloop()
    return None


#READ
  
def Record_Details():
    """Hien thi chi tiet mot ban ghi dua tren gia tri 'rownames'."""
    def show_record_details():
        """Tim va hien thi chi tiet ban ghi theo rowname."""
        try:
            rowname_value = int(rowname_entry.get())
            if not validate_input(rowname_value, int, non_negative=True, field_name="Rowname"):
                return
            record = df[df['rownames'] == rowname_value]
            if record.empty:
                messagebox.showerror("Error", "No record found for the given rowname.")
                return
            details_window = tk.Toplevel(root)
            details_window.title("Record Details")
            row_number = 0
            for col_name, value in record.iloc[0].items():
                ttk.Label(details_window, text=f"{col_name}").grid(row=row_number, column=0, sticky=tk.W, padx=10, pady=5)
                ttk.Label(details_window, text=":").grid(row=row_number, column=1, sticky=tk.W, padx=5, pady=5)
                ttk.Label(details_window, text=f"{value}").grid(row=row_number, column=2, sticky=tk.W, padx=10, pady=5)
                row_number += 1
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid integer for rowname.")
    
    root = tk.Tk()
    root.title("Record Details by Rowname")
    ttk.Label(root, text="Enter rowname:").grid(row=0, column=0, sticky=tk.W, padx=10, pady=5)
    rowname_entry = ttk.Entry(root)
    rowname_entry.grid(row=0, column=1, sticky=tk.EW, padx=10, pady=5)
    btn_show_details = ttk.Button(root, text="Show Record Details", command=show_record_details)
    btn_show_details.grid(row=1, column=0, columnspan=2, pady=10)

current_page = 0
rows_per_page = 32

def Pagination():
    """Thuc hien phan trang hien thi du lieu tu DataFrame."""
    def display_page(page):
        """Hien thi du lieu cua trang hien tai."""
        global current_page
        start_row = page * rows_per_page
        end_row = start_row + rows_per_page
        page_data = df.iloc[start_row:end_row]
        for item in result_table.get_children():
            result_table.delete(item)
        for _, row in page_data.iterrows():
            result_table.insert("", tk.END, values=list(row))
        page_label.config(text=f"Page {current_page + 1} of {num_pages}")

    def next_page():
        """Chuyen sang trang tiep theo."""
        global current_page
        if current_page < num_pages - 1:
            current_page += 1
            display_page(current_page)

    def previous_page():
        """Quay lai trang truoc do."""
        global current_page
        if current_page > 0:
            current_page -= 1
            display_page(current_page)

    root = tk.Tk()
    root.title("Pagination")
    result_table = ttk.Treeview(root)
    result_table.pack(fill=tk.BOTH, expand=True)
    result_table["columns"] = list(df.columns)
    result_table["show"] = "headings"

    for col_name in df.columns:
        result_table.heading(col_name, text=col_name)
        result_table.column(col_name, width=50, anchor='w')

    num_pages = (len(df) + rows_per_page - 1) // rows_per_page
    page_label = ttk.Label(root, text=f"Page {current_page + 1} of {num_pages}")
    page_label.pack(side=tk.LEFT, padx=10, pady=10)
    previous_button = ttk.Button(root, text="Previous", command=previous_page)
    previous_button.pack(side=tk.LEFT, padx=10, pady=10)
    next_button = ttk.Button(root, text="Next", command=next_page)
    next_button.pack(side=tk.LEFT, padx=10, pady=10)
    display_page(current_page)


def Search_Filter():
    """Tao giao dien tim kiem va loc du lieu."""
    def apply_filter():
        """Ap dung phuong phap loc du lieu."""
        filter_method = filter_var.get()
        if filter_method == 'filter by condition':
            filter_by_condition()
        elif filter_method == 'filter by columns':
            filter_by_columns()
        elif filter_method == 'filter by rows':
            filter_by_rows()
        elif filter_method == 'sort by column':
            sort_by_column()
        else:
            tk.messagebox.showerror("Error", "Invalid filter method.")

    root = tk.Tk()
    root.title("Search and Filter")
    main_frame = ttk.Frame(root, padding=10)
    main_frame.grid(row=0, column=0, sticky="NSEW")
    ttk.Label(main_frame, text="Select Filter Method:").grid(row=0, column=0, sticky=tk.W, padx=10, pady=10)
    filter_var = tk.StringVar(root)
    filter_dropdown = ttk.Combobox(
        main_frame,
        textvariable=filter_var,
        values=["filter by condition", "filter by columns", "filter by rows", "sort by column"]
    )
    filter_dropdown.grid(row=0, column=1, sticky=tk.EW, padx=10, pady=10)
    search_button = ttk.Button(main_frame, text="Search and Filter", command=apply_filter)
    search_button.grid(row=1, column=0, columnspan=2, pady=10)
    root.mainloop()

def set_dataframe(dataframe):
    """Gan DataFrame toan cuc de su dung trong cac ham loc va hien thi."""
    global df
    df = dataframe

def root(title):
    """Tao cua so giao dien phu voi tieu de duoc chi dinh."""
    filter_window = tk.Toplevel()
    filter_window.title(title)
    frame = ttk.Frame(filter_window, padding=10)
    frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
    return frame

def filter_by_condition():
    """Loc du lieu dua tren dieu kien."""
    def apply_condition():
        """Ap dung dieu kien loc du lieu va hien thi ket qua."""
        col = col_var.get()
        if col not in df.columns:
            messagebox.showerror("Error", "The selected column does not exist in the dataset.")
            return
        if col in ['rownames', 'nr', 'year', 'school', 'exper', 'wage', 'age']:
            try:
                choice = comp_type_var.get()
                val = value_entry.get()
                if not validate_input(val, float, non_negative=True, field_name="Value"):
                    return
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
            if comp_type_var.get() in ["greater than", "greater than or equal to", "less than", "less than or equal to"]:
                messagebox.showerror("Error", "Invalid comparison type")
                return
            else:
                choice = value_entry.get()
                if choice == "equal to":
                    result = df[df[col] == val]
                elif choice == "different from":
                    result = df[df[col] != val]
        display_dataframe(result, "Filtered by Condition")

    frame = root("Filter by condition")
    ttk.Label(frame, text="Select Column for Condition:").grid(row=0, column=0, sticky=tk.W)
    col_var = tk.StringVar()
    col_dropdown = ttk.Combobox(frame, textvariable=col_var, values=df.columns.tolist())
    col_dropdown.grid(row=0, column=1, sticky=tk.EW)
    ttk.Label(frame, text="Comparison Type:").grid(row=1, column=0, sticky=tk.W)
    comp_type_var = tk.StringVar()
    comp_dropdown = ttk.Combobox(frame, textvariable=comp_type_var, values=[
        "greater than", "greater than or equal to", "less than", "less than or equal to", 
        "equal to", "different from"])
    comp_dropdown.grid(row=1, column=1, sticky=tk.EW)
    ttk.Label(frame, text="Enter Value/Condition:").grid(row=2, column=0, sticky=tk.W)
    value_entry = ttk.Entry(frame)
    value_entry.grid(row=2, column=1, sticky=tk.EW)
    filter_condition_button = ttk.Button(frame, text="Filter by Condition", command=apply_condition)
    filter_condition_button.grid(row=3, column=0, columnspan=2, pady=10)

def filter_by_columns():
    """Loc du lieu dua tren cac cot duoc chon."""
    def apply_columns():
        """Ap dung lua chon cot de hien thi du lieu."""
        selected_cols = [listbox.get(i) for i in listbox.curselection()]
        if not selected_cols:
            messagebox.showwarning("Warning", "No columns selected. Displaying all columns.")
            selected_cols = list(df.columns)
        result = df[selected_cols]
        display_dataframe(result, "Filtered by Columns")

    frame = root("Filter by columns")
    ttk.Label(frame, text="Select Columns to Display:").grid(row=0, column=0, sticky=tk.W)
    listbox = tk.Listbox(frame, selectmode="multiple", exportselection=False, height=6)
    for col_name in df.columns:
        listbox.insert(tk.END, col_name)
    listbox.grid(row=0, column=1, sticky=tk.EW)
    filter_columns_button = ttk.Button(frame, text="Filter by Columns", command=apply_columns)
    filter_columns_button.grid(row=1, column=0, columnspan=2, pady=10)

def filter_by_rows():
    """Loc du lieu dua tren chi so hang."""
    def apply_rows():
        """Ap dung gioi han hang de hien thi du lieu."""
        try:
            from_row = from_entry.get()
            to_row = to_entry.get()
            if not validate_input(from_row, int, non_negative=True, field_name="From Row"):
                return
            if not validate_input(to_row, int, non_negative=True, field_name="To Row"):
                return
            from_row = int(from_row)
            to_row = int(to_row)
            if to_row > len(df) or from_row > to_row:
                messagebox.showerror("Error", "Invalid row range. Please enter valid row indices.")
                return
            result = df.iloc[from_row-1:to_row]
            display_dataframe(result, "Filtered by Rows")
        except ValueError:
            messagebox.showerror("Error", "Please enter valid integers for row indices.")

    frame = root("Filter by rows")
    ttk.Label(frame, text="From Row:").grid(row=0, column=0, sticky=tk.W)
    from_entry = ttk.Entry(frame)
    from_entry.grid(row=0, column=1, sticky=tk.EW)
    ttk.Label(frame, text="To Row:").grid(row=1, column=0, sticky=tk.W)
    to_entry = ttk.Entry(frame)
    to_entry.grid(row=1, column=1, sticky=tk.EW)
    filter_rows_button = ttk.Button(frame, text="Filter by Rows", command=apply_rows)
    filter_rows_button.grid(row=2, column=0, columnspan=2, pady=10)

def sort_by_column():
    """Sap xep du lieu theo mot cot da chon voi thu tu tang hoac giam dan."""
    def sort():
        """Ap dung sap xep du lieu theo cot va thu tu duoc chi dinh."""
        col = sort_col_var.get()
        if col not in df.columns:
            messagebox.showerror("Error", "The selected column does not exist in the dataset.")
            return
        
        sort_order = sort_order_var.get()
        if sort_order not in ["Ascending", "Descending"]:
            messagebox.showerror("Error", "Invalid sort order. Please select 'Ascending' or 'Descending'.")
            return
        ascending = sort_order_var.get() == "Ascending"
        result = df.sort_values(by=col, ascending=ascending)
        display_dataframe(result, f"Sorted by {col} ({'Ascending' if ascending else 'Descending'})")

    frame = root("Sort by column")
    sort_col_var = tk.StringVar()
    ttk.Label(frame, text="Select Column to Sort By:").grid(row=10, column=0, sticky=tk.W)
    sort_col_dropdown = ttk.Combobox(frame, textvariable=sort_col_var, values=df.columns.tolist())
    sort_col_dropdown.grid(row=10, column=1, sticky=tk.EW)
    sort_order_var = tk.StringVar(value="Ascending")
    ttk.Label(frame, text="Sort Order:").grid(row=11, column=0, sticky=tk.W)
    sort_order_dropdown = ttk.Combobox(frame, textvariable=sort_order_var, values=["Ascending", "Descending"])
    sort_order_dropdown.grid(row=11, column=1, sticky=tk.EW)
    sort_button = ttk.Button(frame, text="Sort Data", command=sort)
    sort_button.grid(row=12, column=0, columnspan=2, pady=10)
    
def display_dataframe(dataframe, title):
    """Hien thi DataFrame trong mot cua so moi voi dinh dang bang."""
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

def update_tree(tree, df):
    """Cap nhat Treeview de hien thi du lieu tu DataFrame."""
    for item in tree.get_children():
        tree.delete(item)
    for _, row in df.iterrows():
        tree.insert("", "end", values=list(row))

def update_record(tree, df):
    """Cho phep nguoi dung tim kiem va chinh sua mot ban ghi trong DataFrame."""
    def search_record():
        """Tim kiem ban ghi trong DataFrame dua tren gia tri 'rownames'."""
        try:
            rowname = int(rowname_entry.get())
            record = df[df['rownames'] == rowname]
            if record.empty:
                messagebox.showerror("Error", "Rowname not found!")
                return
            edit_record(record.iloc[0])
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid rowname.")

    def edit_record(record):
        """Hien thi giao dien chinh sua ban ghi duoc tim thay."""
        edit_window = tk.Toplevel(root)
        edit_window.title(f"Edit Record - Rowname: {record['rownames']}")
        def save_changes():
            """Luu thay doi vao DataFrame va cap nhat Treeview."""
            try:
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
                    "residence": residence_entry.get() if residence_entry.get() else record["residence"],
                    "age": 6 + int(exper_entry.get()) + int(school_entry.get()),
                    "exper level": pd.cut([int(exper_entry.get())], bins=[0, 3, 8, 12, 18], labels=['beginner', 'intermediate', 'advanced', 'expert'])[0],
                    "school level": pd.cut([int(school_entry.get())], bins=[0, 5, 9, 12, 16], labels=['very low', 'low', 'intermediate', 'high'])[0],
                    "wage level": pd.cut([float(wage_entry.get())], bins=[-float('inf'), -2, 0, 2, 3.5, float('inf')], labels=['very low', 'low', 'medium', 'high', 'very high'])[0]
                }

                if not validate_input(nr_entry.get(), int, non_negative=True, field_name="nr"):
                    return
                if not validate_input(year_entry.get(), int, valid_values=year_list, field_name="year"):
                    return
                if not validate_input(school_entry.get(), int, non_negative=True, field_name="school"):
                    return
                if not validate_input(exper_entry.get(), int, non_negative=True, field_name="exper"):
                    return
                if not validate_input(union_var.get(), str, valid_values=union_values, field_name="union"):
                    return
                if not validate_input(ethn_var.get(), str, valid_values=ethn_values, field_name="ethn"):
                    return
                if not validate_input(maried_var.get(), str, valid_values=maried_values, field_name="maried"):
                    return
                if not validate_input(health_var.get(), str, valid_values=health_values, field_name="health"):
                    return
                if not validate_input(wage_entry.get(), float, non_negative=True, field_name="wage"):
                    return
                if not validate_input(industry_entry.get(), str, field_name="industry"):
                    return
                if not validate_input(occupation_entry.get(), str, field_name="occupation"):
                    return
                if not validate_input(residence_entry.get(), str, field_name="residence"):
                    return

                for col, value in updated_row.items():
                    df.loc[df['rownames'] == record['rownames'], col] = value

                df.to_csv("NewMales.csv", index=False)
                update_tree(tree, df)
                messagebox.showinfo("Success", "Record updated successfully.")
                edit_window.destroy()

            except ValueError:
                messagebox.showerror("Error", "Please enter valid values.")

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
        union_var = tk.StringVar(edit_window)
        union_var.set(record["union"])
        union_entry = ttk.Combobox(edit_window, textvariable=union_var, values=["yes", "no"])
        union_entry.grid(row=4, column=1, sticky=tk.EW, padx=10, pady=5)

        ttk.Label(edit_window, text="ethn:").grid(row=5, column=0, sticky=tk.W, padx=10, pady=5)
        ethn_var = tk.StringVar(edit_window)
        ethn_var.set(record["ethn"])
        ethn_entry = ttk.Combobox(edit_window, textvariable=ethn_var, values=["black", "hisp", "other"])
        ethn_entry.grid(row=5, column=1, sticky=tk.EW, padx=10, pady=5)

        ttk.Label(edit_window, text="maried:").grid(row=6, column=0, sticky=tk.W, padx=10, pady=5)
        maried_var = tk.StringVar(edit_window)
        maried_var.set(record["maried"]) 
        maried_entry = ttk.Combobox(edit_window, textvariable=maried_var, values=["yes", "no"])
        maried_entry.grid(row=6, column=1, sticky=tk.EW, padx=10, pady=5)

        ttk.Label(edit_window, text="health:").grid(row=7, column=0, sticky=tk.W, padx=10, pady=5)
        health_var = tk.StringVar(edit_window)
        health_var.set(record["health"])
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
        
        save_button = ttk.Button(edit_window, text="Save Changes", command=save_changes)
        save_button.grid(row=12, column=0, columnspan=2, pady=10)

    root = tk.Tk()
    root.title("Update Record")
    ttk.Label(root, text="Enter rowname to update:").grid(row=0, column=0, padx=10, pady=10)
    rowname_entry = ttk.Entry(root)
    rowname_entry.grid(row=0, column=1, padx=10, pady=10)
    search_button = ttk.Button(root, text="Search", command=search_record)
    search_button.grid(row=1, column=0, columnspan=2, pady=10)
    root.mainloop()

def update_wage_by_exper(tree, df):
    """Cap nhat muc luong theo muc do kinh nghiem cua nhan vien."""
    def apply():
        """Ap dung thay doi muc luong dua tren phan tram tang."""
        try:
            beginner_raise = float(beginner_entry.get()) / 100
            intermediate_raise = float(intermediate_entry.get()) / 100
            advanced_raise = float(advanced_entry.get()) / 100
            expert_raise = float(expert_entry.get()) / 100
            raise_map = {
                "beginner": beginner_raise,
                "intermediate": intermediate_raise,
                "advanced": advanced_raise,
                "expert": expert_raise,
            }
            df["wage"] = df.apply(
                lambda row: row["wage"] + math.log(1 + raise_map.get(row["exper level"], 0)), axis=1
            )
            df['wage level'] = pd.cut(df['wage'], bins=[-float('inf'), -2, 0, 2, 3.5, float('inf')], labels=['very low', 'low', 'medium', 'high', 'very high'], right=True)

            df.to_csv("NewMales.csv", index=False)
            update_tree(tree, df)
            messagebox.showinfo("Success", "Wage updated successfully.")
            root.destroy()
        except ValueError:
            messagebox.showerror("Error", "Please enter valid numbers for the raise percentages.")

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
    """Cap nhat muc luong theo cap do hoc van cua nhan vien."""
    def apply():
        """Ap dung thay doi muc luong dua tren phan tram tang luong theo cap do hoc van."""
        try:
            vlow_raise = float(vlow_entry.get()) / 100
            low_raise = float(low_entry.get()) / 100
            intermediate_raise = float(intermediate_entry.get()) / 100
            high_raise = float(high_entry.get()) / 100
            raise_map = {
                "very low": vlow_raise,
                "low": low_raise,
                "intermediate": intermediate_raise,
                "high": high_raise,
            }
            df["wage"] = df.apply(
                lambda row: row["wage"] + math.log(1 + raise_map.get(row["school level"], 0)), axis=1
            )

            df['wage level'] = pd.cut(df['wage'], bins=[-float('inf'), -2, 0, 2, 3.5, float('inf')], labels=['very low', 'low', 'medium', 'high', 'very high'], right=True)

            for item in tree.get_children():
                tree.delete(item)
            for _, row in df.iterrows():
                tree.insert("", "end", values=(row["rownames"], row["school level"], row['wage']))
            df.to_csv("NewMales.csv", index=False)
            update_tree(tree, df)
            messagebox.showinfo("Success", "Wage updated successfully.")
            root.destroy()
        except ValueError:
            messagebox.showerror("Error", "Please enter valid numbers for the raise percentages.")

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
    """Xoa mot hang trong DataFrame dua tren gia tri duy nhat cua mot cot cu the."""
    if pd.api.types.is_numeric_dtype(df[column_name]):
        unique_value = float(unique_value) if "." in str(unique_value) else int(unique_value)
    updated_df = df[df[column_name] != unique_value]
    return updated_df
