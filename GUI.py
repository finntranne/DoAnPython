import tkinter as tk
from tkinter import ttk
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from package.chart import *
from package.CRUD import *

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

        tk.Label(self.left_frame, text="Chuc nang", font=("Arial", 20, "bold"), bg="#55B3D9").pack(pady=10)

        self.create_button = tk.Button(self.left_frame, text="Create", command=self.CREATE)
        self.create_button.pack(fill="x", padx=10, pady=5)

        self.read_button = tk.Button(self.left_frame, text="Read", command=self.READ)
        self.read_button.pack(fill="x", padx=10, pady=5)

        self.update_button = tk.Button(self.left_frame, text="Update", command=self.UPDATE)
        self.update_button.pack(fill="x", padx=10, pady=5)

        self.delete_button = tk.Button(self.left_frame, text="Delete", command=self.DELETE)
        self.delete_button.pack(fill="x", padx=10, pady=5)

        self.plot_button = tk.Button(self.left_frame, text="Ve Bieu do", command=self.open_plot_options)
        self.plot_button.pack(fill="x", padx=10, pady=5)

        self.back_button = tk.Button(self.left_frame, text="Back", command=self.show_data)
        self.back_button.pack(fill="x", padx=10, pady=5)
        self.back_button.pack_forget()

        self.top_frame = tk.Frame(self.right_frame)
        self.top_frame.pack(fill="both", expand=True)

        self.tree = ttk.Treeview(self.top_frame, columns=list(df.columns), show="headings")
        for col in df.columns:
            self.tree.heading(col, text=col)
            self.tree.column(col, width=100)

        self.v_scrollbar = ttk.Scrollbar(self.top_frame, orient="vertical", command=self.tree.yview)
        self.tree.configure(yscrollcommand=self.v_scrollbar.set)
        self.tree.grid(row=0, column=0, sticky="nsew")
        self.v_scrollbar.grid(row=0, column=1, sticky="ns")

        self.top_frame.grid_rowconfigure(0, weight=1)
        self.top_frame.grid_columnconfigure(0, weight=1)

        for _, row in df.iterrows():
            self.tree.insert("", "end", values=list(row))

        self.canvas = None

    def save_to_file(self):
        """
        Luu du lieu tu DataFrame vao file CSV.
        """
        global df
        df.to_csv("NewMales.csv", index=False)
        print("Data saved to file.")

    def CREATE(self):
        """
        Goi chuc nang tao ban ghi moi va them vao Treeview.
        """
        def add_to_treeview(new_row):
            self.tree.insert("", "end", values=list(new_row.values()))
        create_row(df, add_to_treeview)
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
        Xoa ban ghi duoc chon tu Treeview va DataFrame.
        """
        global df
        selected_item = self.tree.selection()
        if selected_item:
            item_values = self.tree.item(selected_item, "values")
            if not item_values:
                print("NULL")
                return
            unique_value = item_values[0]
            column_name = df.columns[0]
            df = delete_row(df, column_name, unique_value)
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
        tk.Label(self.plot_options_frame, text="CHON LOAI BIEU DO", font=("Arial", 36)).grid(row=0, column=0, columnspan=3, pady=10)

        buttons = [
            ("Bieu do Wage_Edu", lambda: self.plot_custom(Wage_Edu, df)),
            ("Bieu do Wage_Ind", lambda: self.plot_custom(Wage_Ind, df)),
            ("Bieu do Wage", lambda: self.plot_custom(Wage, df)),
            ("Bieu do Ethnicity", lambda: self.plot_custom(plot_ethn, df)),
            ("Bieu do Marital Status", lambda: self.plot_custom(plot_maried, df)),
            ("Bieu do Health", lambda: self.plot_custom(plot_health, df)),
            ("Bieu do Industry", lambda: self.plot_custom(plot_industry, df)),
            ("Bieu do Occupation", lambda: self.plot_custom(plot_occupation, df)),
            ("Bieu do Residence", lambda: self.plot_custom(plot_residence, df))
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

    def plot_custom(self, plot_function, data, year=None):
        """
        Ve bieu do tuy chinh dua tren chuc nang ve bieu do duoc cung cap.
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
        if year:
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

root = tk.Tk()
app = DataApp(root)
root.mainloop()
