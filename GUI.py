import tkinter as tk
from tkinter import ttk
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from package.chart import *
from package.CRUD import *

# Đọc dữ liệu từ file CSV
file_path = 'NewMales.csv'
try:
    df = pd.read_csv(file_path)
except FileNotFoundError:
    print(f"File '{file_path}' not found.")
    df = pd.DataFrame()  # Nếu file không tồn tại, tạo DataFrame trống
except pd.errors.EmptyDataError:
    print(f"File '{file_path}' is empty or corrupted.")
    df = pd.DataFrame()  # Nếu file bị lỗi hoặc trống, tạo DataFrame trống

class DataApp:
    """
    Ứng dụng giao diện tương tác hiển thị, chỉnh sửa, và vẽ biểu đồ từ dữ liệu DataFrame.

    Attributes:
        df (pd.DataFrame): Dữ liệu được đọc từ file CSV.
        root (tk.Tk): Cửa sổ chính của ứng dụng.
        tree (ttk.Treeview): Widget hiển thị dữ liệu DataFrame.
        canvas (FigureCanvasTkAgg): Canvas để vẽ biểu đồ matplotlib.
    """
    def __init__(self, root):
        """
        Khởi tạo giao diện chính của ứng dụng.
        
        Args:
            root (tk.Tk): Cửa sổ chính.
        """
        self.df = df
        self.root = root
        self.root.title("GIAO DIỆN TƯƠNG TÁC")
        self.root.geometry("1000x600")
        self.root.state("zoomed")  # Phóng to giao diện khi khởi động
        
        # Tạo giao diện chia thành 2 khung: trái và phải
        self.left_frame = tk.Frame(root, width=200, bg="#55B3D9")
        self.left_frame.pack(side="left", fill="y")
        self.right_frame = tk.Frame(root)
        self.right_frame.pack(side="right", fill="both", expand=True)

        # Thêm các nút chức năng vào khung bên trái
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

        self.back_button = tk.Button(self.left_frame, text="Back", command=self.show_data)
        self.back_button.pack(fill="x", padx=10, pady=5)
        self.back_button.pack_forget()  # Ẩn nút "Back" khi chưa cần thiết

        # Tạo khung hiển thị dữ liệu bên phải
        self.top_frame = tk.Frame(self.right_frame)
        self.top_frame.pack(fill="both", expand=True)

        # Treeview để hiển thị DataFrame
        self.tree = ttk.Treeview(self.top_frame, columns=list(df.columns), show="headings")
        for col in df.columns:
            self.tree.heading(col, text=col)
            self.tree.column(col, width=100)

        # Thanh cuộn dọc cho Treeview
        self.v_scrollbar = ttk.Scrollbar(self.top_frame, orient="vertical", command=self.tree.yview)
        self.tree.configure(yscrollcommand=self.v_scrollbar.set)
        self.tree.grid(row=0, column=0, sticky="nsew")
        self.v_scrollbar.grid(row=0, column=1, sticky="ns")

        self.top_frame.grid_rowconfigure(0, weight=1)
        self.top_frame.grid_columnconfigure(0, weight=1)

        # Hiển thị dữ liệu từ DataFrame vào Treeview
        for _, row in df.iterrows():
            self.tree.insert("", "end", values=list(row))

        self.canvas = None  # Canvas để vẽ biểu đồ

    def save_to_file(self):
        """
        Lưu dữ liệu từ DataFrame vào file CSV.
        """
        global df
        df.to_csv("NewMales.csv", index=False)
        print("Data saved to file.")

    def CREATE(self):
        """
        Gọi chức năng tạo bản ghi mới và thêm vào Treeview.
        """
        def add_to_treeview(new_row):
            self.tree.insert("", "end", values=list(new_row.values()))
        create_row(df, add_to_treeview)  # Hàm `create_row` nằm trong module `CRUD`
        self.save_to_file()

    def READ(self):
        """
        Hiển thị các tùy chọn đọc dữ liệu như xem chi tiết, phân trang, lọc dữ liệu.
        """
        read_window = tk.Toplevel(root)
        read_window.title("Read Options")
        read_window.geometry("300x300")
        ttk.Button(read_window, text="View Record Details", command=Record_Details).pack(pady=10)
        ttk.Button(read_window, text="Pagination", command=Pagination).pack(pady=10)
        ttk.Button(read_window, text="Search & Filter", command=Search_Filter).pack(pady=10)

    def UPDATE(self):
        """
        Hiển thị các tùy chọn cập nhật dữ liệu.
        """
        update_window = tk.Toplevel(root)
        update_window.title("Update Options")
        update_window.geometry("300x300")
        ttk.Button(update_window, text="Update a Record", command=self.record).pack(pady=10)
        ttk.Button(update_window, text="Update Wage by Experience", command=self.wage_exper).pack(pady=10)
        ttk.Button(update_window, text="Update Wage by School", command=self.wage_school).pack(pady=10)

    def record(self):
        """
        Cập nhật một bản ghi cụ thể.
        """
        update_record(self.tree, self.df)  # Hàm `update_record` trong module `CRUD`

    def wage_exper(self):
        """
        Cập nhật lương theo kinh nghiệm.
        """
        update_wage_by_exper(self.tree, self.df)  # Hàm `update_wage_by_exper` trong module `CRUD`

    def wage_school(self):
        """
        Cập nhật lương theo cấp độ học vấn.
        """
        update_wage_by_school(self.tree, self.df)  # Hàm `update_wage_by_school` trong module `CRUD`

    def DELETE(self):
        """
        Xóa bản ghi được chọn từ Treeview và DataFrame.
        """
        global df
        selected_item = self.tree.selection()  # Lấy bản ghi được chọn
        if selected_item:
            item_values = self.tree.item(selected_item, "values")
            if not item_values:
                print("NULL")
                return

            unique_value = item_values[0]  # Xác định giá trị khóa duy nhất
            column_name = df.columns[0]  # Giả sử cột đầu tiên là khóa chính
            df = delete_row(df, column_name, unique_value)  # Hàm `delete_row` trong module `CRUD`
            self.tree.delete(selected_item)  # Xóa khỏi Treeview
            self.save_to_file()

    def open_plot_options(self):
        """
        Tạo giao diện lựa chọn các loại biểu đồ để người dùng có thể chọn và vẽ biểu đồ dữ liệu.
        Phương thức này ẩn phần hiển thị bảng dữ liệu và tạo giao diện chứa các nút để chọn loại biểu đồ.
        """
        # Ẩn phần hiển thị bảng dữ liệu (top_frame)
        self.top_frame.pack_forget()
        
        # Hiển thị lại nút "Back" để người dùng có thể quay lại giao diện dữ liệu
        self.back_button.pack(fill="x", padx=10, pady=5)

        # Tạo frame mới để chứa các lựa chọn biểu đồ
        self.plot_options_frame = tk.Frame(self.right_frame)
        self.plot_options_frame.pack(fill="both", expand=True)

        # Tiêu đề cho phần lựa chọn biểu đồ
        tk.Label(self.plot_options_frame, text="CHỌN LOẠI BIỂU ĐỒ", font=("Arial", 36)).grid(row=0, column=0, columnspan=3, pady=10)

        # Danh sách các nút lựa chọn loại biểu đồ và hành động đi kèm khi nhấn
        buttons = [
            ("Biểu đồ Wage_Edu", lambda: self.plot_custom(Wage_Edu, df)),
            ("Biểu đồ Wage_Ind", lambda: self.plot_custom(Wage_Ind, df)),
            ("Biểu đồ Wage", lambda: self.plot_custom(Wage, df)),
            ("Biểu đồ Ethnicity", lambda: self.plot_custom(plot_ethn, df)),
            ("Biểu đồ Marital Status", lambda: self.plot_custom(plot_maried, df)),
            ("Biểu đồ Health", lambda: self.plot_custom(plot_health, df)),
            ("Biểu đồ Industry", lambda: self.plot_custom(plot_industry, df)),
            ("Biểu đồ Occupation", lambda: self.plot_custom(plot_occupation, df)),
            ("Biểu đồ Residence", lambda: self.plot_custom(plot_residence, df))
        ]

        # Tạo các nút lựa chọn biểu đồ và sắp xếp chúng trong giao diện
        for i, (text, command) in enumerate(buttons):
            row = (i // 3) + 1  # Xác định hàng
            col = i % 3  # Xác định cột
            tk.Button(self.plot_options_frame, text=text, command=command, font=("Arial", 12), width=20, height=2).grid(
                row=row, column=col, padx=10, pady=10, sticky="nsew"
            )
        
        # Cấu hình các hàng và cột trong frame để tự động điều chỉnh kích thước
        for r in range(4):
            self.plot_options_frame.rowconfigure(r, weight=1)
        for c in range(3):
            self.plot_options_frame.columnconfigure(c, weight=1)

    def plot_custom(self, plot_function, data, year=None):
        """
        Vẽ biểu đồ tùy chỉnh dựa trên chức năng vẽ biểu đồ được cung cấp.
        Phương thức này sẽ tạo và hiển thị một biểu đồ từ dữ liệu, 
        sử dụng một hàm vẽ biểu đồ tương ứng và hiển thị trên giao diện Tkinter.
        """
        # Ẩn phần lựa chọn biểu đồ (plot_options_frame)
        if hasattr(self, "plot_options_frame"):
            self.plot_options_frame.pack_forget()

        # Nếu đã có biểu đồ hiển thị trước đó, hủy nó đi
        if self.canvas:
            self.canvas.get_tk_widget().destroy()
            self.canvas = None

        # Tạo một frame mới để chứa biểu đồ
        self.plot_frame = tk.Frame(self.right_frame)
        self.plot_frame.pack(fill="both", expand=True)

        # Tạo một figure để vẽ biểu đồ
        fig = plt.Figure(figsize=(14, 8), dpi=100)
        ax = fig.add_subplot(111)

        # Vẽ biểu đồ bằng hàm được truyền vào (nếu có năm, truyền thêm năm)
        if year:
            plot_function(data, year, ax=ax)
        else:
            plot_function(data, ax=ax)

        # Tạo canvas để hiển thị biểu đồ và thêm vào giao diện
        self.canvas = FigureCanvasTkAgg(fig, master=self.right_frame)
        self.canvas.draw()
        self.canvas.get_tk_widget().pack(fill="both", expand=True)

    def show_data(self):
        """
        Hiển thị lại bảng dữ liệu trong giao diện Tkinter sau khi người dùng quay lại.
        Phương thức này sẽ tái tạo bảng dữ liệu từ DataFrame và hiển thị trong giao diện.
        """
        # Xóa tất cả các widget hiện tại trong phần giao diện hiển thị dữ liệu
        for widget in self.right_frame.winfo_children():
            widget.destroy()

        # Tạo lại frame chứa bảng dữ liệu
        self.top_frame = tk.Frame(self.right_frame)
        self.top_frame.pack(fill="both", expand=True)

        # Tạo Treeview để hiển thị dữ liệu dưới dạng bảng
        self.tree = ttk.Treeview(self.top_frame, columns=list(df.columns), show="headings")
        
        # Cấu hình các cột trong bảng
        for col in df.columns:
            self.tree.heading(col, text=col)
            self.tree.column(col, width=100)

        # Chèn từng dòng dữ liệu từ DataFrame vào bảng
        for _, row in df.iterrows():
            self.tree.insert("", "end", values=list(row))

        # Tạo thanh cuộn dọc cho bảng
        self.v_scrollbar = ttk.Scrollbar(self.top_frame, orient="vertical", command=self.tree.yview)
        self.tree.configure(yscrollcommand=self.v_scrollbar.set)

        # Đặt bảng vào giao diện
        self.tree.grid(row=0, column=0, sticky="nsew")
        self.v_scrollbar.grid(row=0, column=1, sticky="ns")

        # Cấu hình giao diện để tự động điều chỉnh kích thước
        self.top_frame.grid_rowconfigure(0, weight=1)
        self.top_frame.grid_columnconfigure(0, weight=1)

        # Ẩn nút "Back" sau khi quay lại dữ liệu
        self.back_button.pack_forget()

root = tk.Tk()
app = DataApp(root)
root.mainloop()
