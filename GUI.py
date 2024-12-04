import tkinter as tk
from tkinter import ttk, messagebox, filedialog
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from package.chart import *
from package.CRUD import *
from package.convert_pdf import create_pdf_from_csv

file_path = 'NewMales.csv'
try:
    df = pd.read_csv(file_path)
except FileNotFoundError:
    print(f"File '{file_path}' not found.")
    df = pd.DataFrame()
except pd.errors.EmptyDataError:
    print(f"File '{file_path}' is empty or corrupted.")
    df = pd.DataFrame()

class DataApp:
    """
    Ung dung giao dien tuong tac hien thi, chinh sua, va ve bieu do tu du lieu DataFrame.

    Thuoc tinh:
        df (pd.DataFrame): Du lieu duoc doc tu file CSV.
        root (tk.Tk): Cua so chinh cua ung dung.
        tree (ttk.Treeview): Widget hien thi du lieu DataFrame.
        canvas (FigureCanvasTkAgg): Canvas de ve bieu do matplotlib.
    """
    def __init__(self, root):
        """
        Khoi tao giao dien chinh cua ung dung.
        
        Tham so:
            root (tk.Tk): Cua so chinh.
        """
        self.df = df
        self.root = root
        self.root.title("GIAO DIEN TUONG TAC")
        self.root.geometry("1000x600")
        self.root.state("zoomed")
        
        self.left_frame = tk.Frame(root, width=200, bg="#55B3D9")
        self.left_frame.pack(side="left", fill="y")
        self.right_frame = tk.Frame(root)
        self.right_frame.pack(side="right", fill="both", expand=True)

        tk.Label(self.left_frame, text="Chức năng", font=("Arial", 20, "bold"), bg="#55B3D9").pack(pady=10)

        self.create_button = tk.Button(self.left_frame, text="Create", command=self.CREATE)
        self.create_button.pack(fill="x", padx=10, pady=5)

        self.read_button = tk.Button(self.left_frame, text="Read", command=self.READ)
        self.read_button.pack(fill="x", padx=10, pady=5)

        self.update_button = tk.Button(self.left_frame, text="Update", command=self.UPDATE)
        self.update_button.pack(fill="x", padx=10, pady=5)

        self.delete_button = tk.Button(self.left_frame, text="Delete", command=self.DELETE)
        self.delete_button.pack(fill="x", padx=10, pady=5)

        self.plot_button = tk.Button(self.left_frame, text="Vẽ Biểu đồ", command=self.open_plot_options)
        self.plot_button.pack(fill="x", padx=10, pady=5)
        
        self.plot_button = tk.Button(self.left_frame, text="Generate PDF", command=self.generate_pdf)
        self.plot_button.pack(fill="x", padx=10, pady=5)

        self.back_button = tk.Button(self.left_frame, text="Back", command=self.show_data)
        self.back_button.pack(fill="x", padx=10, pady=5)
        self.back_button.pack_forget()

        self.top_frame = tk.Frame(self.right_frame)
        self.top_frame.pack(fill="both", expand=True)

        self.tree = ttk.Treeview(self.top_frame, columns=list(self.df.columns), show="headings")
        for col in self.df.columns:
            self.tree.heading(col, text=col)
            self.tree.column(col, width=100)

        self.v_scrollbar = ttk.Scrollbar(self.top_frame, orient="vertical", command=self.tree.yview)
        self.tree.configure(yscrollcommand=self.v_scrollbar.set)
        self.h_scrollbar = ttk.Scrollbar(self.top_frame, orient="horizontal", command=self.tree.xview)
        self.tree.configure(xscrollcommand=self.h_scrollbar.set)
        self.tree.grid(row=0, column=0, sticky="nsew")
        self.v_scrollbar.grid(row=0, column=1, sticky="ns")
        self.h_scrollbar.grid(row=1, column=0, sticky="ew")
        self.top_frame.grid_rowconfigure(0, weight=1)
        self.top_frame.grid_columnconfigure(0, weight=1)

        for _, row in self.df.iterrows():
            self.tree.insert("", "end", values=list(row))

        self.canvas = None

    def save_to_file(self):
        """
        Luu du lieu tu DataFrame vao file CSV.
        """
        self.df.to_csv("NewMales.csv", index=False)
        print("Data saved to file.")

    def CREATE(self):
        """
        Goi chuc nang tao ban ghi moi va them vao Treeview.
        """
        def add_to_treeview(new_row):
            self.tree.insert("", "end", values=list(new_row.values()))
        create_row(self.df, add_to_treeview)
        self.df = pd.read_csv(file_path)
        self.save_to_file()

    def READ(self):
        """
        Hien thi cac tuy chon doc du lieu nhu xem chi tiet, phan trang, loc du lieu.
        """
        read_window = tk.Toplevel(root)
        read_window.title("Read Options")
        read_window.geometry("300x300")
        ttk.Button(read_window, text="View Record Details", command=Record_Details).pack(pady=10)
        ttk.Button(read_window, text="Pagination", command=Pagination).pack(pady=10)
        ttk.Button(read_window, text="Search & Filter", command=Search_Filter).pack(pady=10)

    def UPDATE(self):
        """
        Hien thi cac tuy chon cap nhat du lieu.
        """
        self.df = pd.read_csv(file_path)
        update_window = tk.Toplevel(root)
        update_window.title("Update Options")
        update_window.geometry("300x300")
        ttk.Button(update_window, text="Update a Record", command=self.record).pack(pady=10)
        ttk.Button(update_window, text="Update Wage by Experience", command=self.wage_exper).pack(pady=10)
        ttk.Button(update_window, text="Update Wage by School", command=self.wage_school).pack(pady=10)

    def record(self):
        update_record(self.tree, self.df)

    def wage_exper(self):
        update_wage_by_exper(self.tree, self.df)

    def wage_school(self):
        update_wage_by_school(self.tree, self.df)

    def DELETE(self):
        """
        Xoa cac ban ghi duoc chon tu Treeview và DataFrame.
        """
        selected_items = self.tree.selection()
        if not selected_items:
            messagebox.showerror("Error", "Please select the rows you want to delete")
            return
        for selected_item in selected_items:
            item_values = self.tree.item(selected_item, "values")
            if not item_values:
                continue
            unique_value = item_values[0]
            column_name = self.df.columns[0]
            self.df = delete_row(self.df, column_name, unique_value)
            self.tree.delete(selected_item)

        self.save_to_file()


    def open_plot_options(self):
        """
        Tao giao dien lua chon cac loai bieu do de nguoi dung co the chon va ve bieu do du lieu.
        """
        self.top_frame.pack_forget()
        self.back_button.pack(fill="x", padx=10, pady=5)
        self.plot_options_frame = tk.Frame(self.right_frame)
        self.plot_options_frame.pack(fill="both", expand=True)
        tk.Label(self.plot_options_frame, text="CHỌN LOẠI BIỂU ĐỒ", font=("Arial", 36)).grid(row=0, column=0, columnspan=3, pady=10)

        buttons = [
            ("Biểu đồ Wage_Edu", lambda: self.open_year_popup(Wage_Edu)),
            ("Biểu đồ Wage_Ind", lambda: self.open_year_popup(Wage_Ind)),
            ("Biểu đồ Wage", lambda: self.open_year_popup(Wage)),
            ("Biểu đồ Ethnicity", lambda: self.open_year_popup(plot_ethn)),
            ("Biểu đồ Marital Status", lambda: self.open_year_popup(plot_maried)),
            ("Biểu đồ Health", lambda: self.open_year_popup(plot_health)),
            ("Biểu đồ Industry", lambda: self.open_year_popup(plot_industry)),
            ("Biểu đồ Occupation", lambda: self.open_year_popup(plot_occupation)),
            ("Biểu đồ Residence", lambda: self.open_year_popup(plot_residence))
        ]

        for i, (text, command) in enumerate(buttons):
            row = (i // 3) + 1
            col = i % 3
            tk.Button(self.plot_options_frame, text=text, command=command, font=("Arial", 12), width=20, height=2).grid(
                row=row, column=col, padx=10, pady=10, sticky="nsew"
            )

        for r in range(4):
            self.plot_options_frame.rowconfigure(r, weight=1)
        for c in range(3):
            self.plot_options_frame.columnconfigure(c, weight=1)

    def open_year_popup(self, plot_function):
        """
        Mo popup đe chon nam truoc khi ve bieu do.
        """
        popup = tk.Toplevel(self.right_frame)
        popup.title("Chọn Năm")
        tk.Label(popup, text="Chọn năm để vẽ biểu đồ", font=("Arial", 16)).pack(pady=10)
        year_list = [1980, 1981, 1982, 1983, 1984, 1985, 1986, 1987]
        
        def select_year(year):
            popup.destroy()
            self.plot_custom(plot_function, self.df, year)

        for year in year_list + [None]:
            year_text = "Tất cả các năm" if year is None else str(year)
            tk.Button(popup, text=year_text, command=lambda y=year: select_year(y), font=("Arial", 12), width=20).pack(pady=5)

    def plot_custom(self, plot_function, data, year=None):
        """
        Ve bieu do tuy chinh dua tren chuc nang ve bieu do đuoc cung cap.
        """
        if hasattr(self, "plot_options_frame"):
            self.plot_options_frame.pack_forget()
        if self.canvas:
            self.canvas.get_tk_widget().destroy()
            self.canvas = None
        self.plot_frame = tk.Frame(self.right_frame)
        self.plot_frame.pack(fill="both", expand=True)
        fig = plt.Figure(figsize=(14, 8), dpi=100)
        ax = fig.add_subplot(111)
        if year is not None:
            plot_function(data, year, ax=ax)
        else:
            plot_function(data, ax=ax)
        self.canvas = FigureCanvasTkAgg(fig, master=self.right_frame)
        self.canvas.draw()
        self.canvas.get_tk_widget().pack(fill="both", expand=True)


    def show_data(self):
        """
        Hien thi du lieu Treeview.
        """
        if self.canvas:
            self.canvas.get_tk_widget().destroy()
            self.canvas = None
        self.plot_frame.pack_forget()
        self.plot_options_frame.pack_forget()
        self.top_frame.pack(fill="both", expand=True)
        self.back_button.pack_forget()
    
    def generate_pdf(self,event=None):
        """
        Ham goi tu GUI de tao PDF va luu vao tep.
        """
        try:
            self.df = pd.read_csv("NewMales.csv")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to read CSV file: {e}")
            return

        filename = filedialog.asksaveasfilename(
            defaultextension=".pdf",
            filetypes=[("PDF files", "*.pdf"), ("All files", "*.*")],
            title="Save PDF As"
        )

        if filename:
            try:
                create_pdf_from_csv(df, output_filename=filename)
                messagebox.showinfo("Success", f"PDF has been created and saved at {filename}")
            except Exception as e:
                messagebox.showerror("Error", f"An error occurred: {e}")
        else:
            messagebox.showwarning("Warning", "No file selected. PDF was not created.")



root = tk.Tk()
app = DataApp(root)
root.mainloop()
