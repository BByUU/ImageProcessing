import os

# 設定 functions 資料夾路徑和 __init__.py 檔案路徑
functions_path = './functions'
init_file_path = os.path.join(functions_path, '__init__.py')

# 檢查並創建 functions 資料夾，如果不存在則創建
if not os.path.exists(functions_path):
    os.makedirs(functions_path)

# 開啟或創建 __init__.py 檔案
with open(init_file_path, 'w') as init_file:
    init_file.write("# __init__.py\n\n")  # 寫入檔案開頭的註解
    all_functions = []  # 用來儲存所有模組名稱的清單
    
    # 遍歷 functions 資料夾中的所有檔案
    for filename in os.listdir(functions_path):
        # 如果是 .py 檔案且不是 __init__.py，則處理該檔案
        if filename.endswith('.py') and filename != '__init__.py':
            module_name = filename[:-3]  # 取得不含副檔名的模組名稱
            init_file.write(f"from .{module_name} import *\n")  # 寫入匯入語句
            all_functions.append(f'"{module_name}"')  # 將模組名稱加入清單

    # 寫入 __all__ 列表，這將定義該模組匯入時的可見函數
    init_file.write("\n__all__ = [")
    init_file.write(", ".join(all_functions))  # 加入所有模組名稱
    init_file.write("]\n")  # 結束 __all__ 列表的定義

# 顯示訊息，告知使用者 __init__.py 已生成
print(f"__init__.py generated with imports for all modules in {functions_path}")
