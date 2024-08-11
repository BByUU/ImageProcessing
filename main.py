import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
import cv2
import numpy as np
import importlib.util
import os

# 創建主窗口
root = tk.Tk()
root.title("Image Processor")

# 原圖與處理後圖
original_image = None
processed_image = None

# 存儲函數的全局字典
function_dict = {}

# 上傳圖片函數
def upload_image():
    global original_image, processed_image
    # 定義允許的檔案類型
    filetypes = [        
        ('image files', '*.png;*.jpg;*.jpeg'),  # 允許的圖片類型
        ('All files', '*.*')             # 允許所有檔案類型
    ]
    # 獲取當前腳本的目錄
    current_directory = os.path.dirname(__file__)
    
    # 彈出檔案選擇對話框，並指定允許的檔案類型
    file_path = filedialog.askopenfilename(
        title='Open a file',
        initialdir=current_directory,  # 設置初始目錄為程式碼所在資料夾
        filetypes=filetypes
    )

    if file_path:
        original_image = Image.open(file_path)
        processed_image = original_image.copy()
        display_image(original_image, original_label)
        display_image(processed_image, processed_label)

# 顯示圖片函數
def display_image(image, label):
    # 設置縮放比例
    max_width, max_height = 300, 300  # 最大顯示尺寸
    image_ratio = image.width / image.height
    label_ratio = max_width / max_height

    if label_ratio > image_ratio:
        new_height = max_height
        new_width = int(new_height * image_ratio)
    else:
        new_width = max_width
        new_height = int(new_width / image_ratio)

    resized_image = image.resize((new_width, new_height), Image.LANCZOS)
    photo = ImageTk.PhotoImage(resized_image)
    label.config(image=photo)
    label.image = photo
    label.config(width=max_width, height=max_height)  # 設置標籤尺寸

# 獲取所有函數名
def get_function_names():
    functions_path = './functions'
    init_file_path = os.path.join(functions_path, '__init__.py')
    
    function_names = []
    if os.path.exists(init_file_path):
        with open(init_file_path, 'r') as file:
            lines = file.readlines()
            for line in lines:
                if line.startswith('__all__'):
                    # 獲取 __all__ 列表中的函數名
                    start = line.find('[') + 1
                    end = line.find(']')
                    function_names = line[start:end].replace('"', '').replace("'", "").split(', ')
    else:
        print(f"__init__.py not found in {functions_path}")
    
    print(f"Function names found: {function_names}")  # 調試信息
    return function_names

# 動態導入函數
def load_function(function_name):
    module_name = f"functions.{function_name}"
    spec = importlib.util.find_spec(module_name)
    if spec:
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        return getattr(module, function_name)
    return None

# 初始化加載所有函數
def initialize_functions():
    global function_dict
    function_names = get_function_names()
    for name in function_names:
        func = load_function(name)
        if func and callable(func):
            function_dict[name] = func
        else:
            print(f"Function {name} is not callable or not found.")

# 創建處理圖片的函數
def apply_effect(n):
    global original_image, processed_image
    if original_image:
        function_names = list(function_dict.keys())
        if 0 <= n < len(function_names):
            function_name = function_names[n]
            func = function_dict[function_name]
            if func:
                # 將 PIL 圖像轉換為 NumPy 數組
                original_np = np.array(original_image)
                # 調用處理函數
                processed_np = func(original_np)
                # 將處理後的 NumPy 數組轉換回 PIL 圖像
                processed_image = Image.fromarray(processed_np)
                display_image(processed_image, processed_label)
            else:
                print(f"Function {function_name} is not callable or not found.")
        else:
            print(f"Invalid function index: {n}")

# 創建上傳圖片按鈕
upload_button = tk.Button(root, text="Upload Image", command=upload_image)
upload_button.pack()

# 創建一個框架來放置圖像和按鈕
frame = tk.Frame(root)
frame.pack()

# 創建顯示圖片的標籤，設置尺寸和佔位符
original_label = tk.Label(frame, text="Original Image", width=40, height=20, bg='lightgrey')
original_label.grid(row=0, column=0, padx=10, pady=10)
processed_label = tk.Label(frame, text="Processed Image", width=40, height=20, bg='lightgrey')
processed_label.grid(row=0, column=1, padx=10, pady=10)

# 創建效果按鈕
buttons_frame = tk.Frame(root)
buttons_frame.pack()
initialize_functions()
button_names = list(function_dict.keys())
if button_names:
    for i in range(len(button_names)):
        button = tk.Button(buttons_frame, text=button_names[i], command=lambda i=i: apply_effect(i))
        button.grid(row=i//5, column=i%5, padx=2, pady=2)
else:
    print("No function names found.")

# 運行主循環
root.mainloop()
