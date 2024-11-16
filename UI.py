import tkinter as tk
from tkinter import ttk
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from package.chart import *

# Đọc dữ liệu từ file CSV
file_path = 'NewMales.csv'
df = pd.read_csv(file_path)

class DataApp:
    def __init__(self, root):
        self.root = root
        self.root.title("GIAO DIỆN TƯƠNG TÁC")
        self.root.geometry("1000x600")
        self.root.state("zoomed")
        
        self.left_frame = tk.Frame(root, width=200, bg="#FEAFA1")
        self.left_frame.pack(side="left", fill="y")
        self.right_frame = tk.Frame(root)
        self.right_frame.pack(side="right", fill="both", expand=True)

        tk.Label(self.left_frame, text="Chức năng", font=("Arial", 20, "bold"), bg="#FEAFA1").pack(pady=10)

        self.create_button = tk.Button(self.left_frame, text="Create", command=self.create_data)
        self.create_button.pack(fill="x", padx=10, pady=5)

        self.read_button = tk.Button(self.left_frame, text="Read", command=self.read_data)
        self.read_button.pack(fill="x", padx=10, pady=5)

        self.update_button = tk.Button(self.left_frame, text="Update", command=self.update_data)
        self.update_button.pack(fill="x", padx=10, pady=5)

        self.delete_button = tk.Button(self.left_frame, text="Delete", command=self.delete_data)
        self.delete_button.pack(fill="x", padx=10, pady=5)

        self.plot_button = tk.Button(self.left_frame, text="Vẽ Biểu đồ", command=self.open_plot_options)
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

        self.bottom_frame = tk.Frame(self.right_frame)
        self.bottom_frame.pack(fill="x", padx=10, pady=10)

        self.entry_vars = {}
        for i, col in enumerate(df.columns):
            label = tk.Label(self.bottom_frame, text=col)
            label.grid(row=0, column=i, padx=5, pady=5)
            entry_var = tk.StringVar()
            entry = tk.Entry(self.bottom_frame, textvariable=entry_var, width=15)
            entry.grid(row=1, column=i, padx=5, pady=5)
            self.entry_vars[col] = entry_var

        self.canvas = None

    def create_data(self):
        new_data = [self.entry_vars[col].get() for col in df.columns]
        self.tree.insert("", "end", values=new_data)

    def read_data(self):
        print("Read dữ liệu")

    def update_data(self):
        selected_item = self.tree.selection()
        if selected_item:
            updated_data = [self.entry_vars[col].get() for col in df.columns]
            self.tree.item(selected_item, values=updated_data)

    def delete_data(self):
        selected_item = self.tree.selection()
        if selected_item:
            self.tree.delete(selected_item)

    def open_plot_options(self):
        # Hiển thị các tùy chọn biểu đồ trên giao diện hiện tại
        self.top_frame.pack_forget()
        self.bottom_frame.pack_forget()
        self.back_button.pack(fill="x", padx=10, pady=5)

        # Khung chứa nút tùy chọn biểu đồ
        self.plot_options_frame = tk.Frame(self.right_frame)
        self.plot_options_frame.pack(fill="both", expand=True)

        tk.Label(self.plot_options_frame, text="Chọn loại biểu đồ", font=("Arial", 16)).pack(pady=10)

        # Các nút để chọn loại biểu đồ từ module bieu_do
        tk.Button(self.plot_options_frame, text="Biểu đồ Wage_Edu", 
                  command=lambda: self.plot_custom(Wage_Edu, df)).pack(padx=10, pady=5)
        tk.Button(self.plot_options_frame, text="Biểu đồ Wage_Ind", 
                  command=lambda: self.plot_custom(Wage_Ind, df)).pack(padx=10, pady=5)
        tk.Button(self.plot_options_frame, text="Biểu đồ Wage", 
                  command=lambda: self.plot_custom(Wage, df)).pack(padx=10, pady=5)
        tk.Button(self.plot_options_frame, text="Biểu đồ Ethnicity", 
                  command=lambda: self.plot_custom(plot_ethn, df)).pack(padx=10, pady=5)
        tk.Button(self.plot_options_frame, text="Biểu đồ Marital Status", 
                  command=lambda: self.plot_custom(plot_maried, df)).pack(padx=10, pady=5)
        tk.Button(self.plot_options_frame, text="Biểu đồ Health", 
                  command=lambda: self.plot_custom(plot_health, df)).pack(padx=10, pady=5)
        tk.Button(self.plot_options_frame, text="Biểu đồ Industry", 
                  command=lambda: self.plot_custom(plot_industry, df)).pack(padx=10, pady=5)
        tk.Button(self.plot_options_frame, text="Biểu đồ Occupation", 
                  command=lambda: self.plot_custom(plot_occupation, df)).pack(padx=10, pady=5)
        tk.Button(self.plot_options_frame, text="Biểu đồ Residence", 
                  command=lambda: self.plot_custom(plot_residence, df)).pack(padx=10, pady=5)

    def plot_custom(self, plot_function, data, year=None):
        if hasattr(self, "plot_options_frame"):
            self.plot_options_frame.pack_forget()

        if self.canvas:
            self.canvas.get_tk_widget().destroy()
            self.canvas = None

        fig = plt.Figure(figsize=(6, 4), dpi=100)
        ax = fig.add_subplot(111)

        # Gọi hàm biểu đồ với trục `ax` cụ thể
        if year:
            plot_function(data, year, ax=ax)
        else:
            plot_function(data, ax=ax)

        self.canvas = FigureCanvasTkAgg(fig, master=self.right_frame)
        self.canvas.draw()
        self.canvas.get_tk_widget().pack(fill="both", expand=True)

    def show_data(self):
        # Xóa biểu đồ và hiển thị lại bảng dữ liệu và khung nhập liệu
        if self.canvas:
            self.canvas.get_tk_widget().pack_forget()
            self.canvas = None
        
        self.top_frame.pack(fill="both", expand=True)
        self.bottom_frame.pack(fill="x", padx=10, pady=10)
        self.back_button.pack_forget()

root = tk.Tk()
app = DataApp(root)
root.mainloop()
