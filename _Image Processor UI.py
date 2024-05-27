import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk, ImageEnhance, ImageFilter
import random
import os

# 打印当前工作目录
print("Current working directory:", os.getcwd())

# 创建主窗口
root = tk.Tk()
root.title("Image Processor")

# 原图与处理后图
original_image = None
processed_image = None

# 上传图片函数
def upload_image():
    global original_image, processed_image
    file_path = filedialog.askopenfilename()
    if file_path:
        original_image = Image.open(file_path)
        processed_image = original_image.copy()
        display_image(original_image, original_label)
        display_image(processed_image, processed_label)

# 显示图片函数
def display_image(image, label):
    # 设置缩放比例
    max_width, max_height = 300, 300  # 最大显示尺寸
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
    label.config(width=max_width, height=max_height)  # 设置标签尺寸

# 获取所有函数名
def get_function_names():
    functions_path = './functions'
    init_file_path = os.path.join(functions_path, '__init__.py')
    
    
    function_names = []
    if os.path.exists(init_file_path):
        with open(init_file_path, 'r') as file:
            lines = file.readlines()
            for line in lines:
                if line.startswith('from .'):
                    parts = line.split()
                    if len(parts) > 2:
                        module_name = parts[1].split('.')[1]
                        function_names.append(module_name)
    else:
        print(f"__init__.py not found in {functions_path}")
    
    print(f"Function names found: {function_names}")  # 调试信息
    return function_names

# 创建上传图片按钮
upload_button = tk.Button(root, text="Upload Image", command=upload_image)
upload_button.pack()

# 创建一个框架来放置图像和按钮
frame = tk.Frame(root)
frame.pack()

# 创建显示图片的标签，设置尺寸和占位符
original_label = tk.Label(frame, text="Original Image", width=40, height=20, bg='lightgrey')
original_label.grid(row=0, column=0, padx=10, pady=10)
processed_label = tk.Label(frame, text="Processed Image", width=40, height=20, bg='lightgrey')
processed_label.grid(row=0, column=1, padx=10, pady=10)

# 创建效果按钮
buttons_frame = tk.Frame(root)
buttons_frame.pack()
button_names = get_function_names()
# effect_labels = [f"Effect {i}" for i in range(1, 11)]
if button_names:
        for i in range(len(button_names)):
            button = tk.Button(buttons_frame, text=button_names[i], command=lambda i=i+1: apply_effect(i))
            button.grid(row=i//5, column=i%5, padx=2, pady=2)
else:
    print("No function names found.")


# 运行主循环
root.mainloop()
