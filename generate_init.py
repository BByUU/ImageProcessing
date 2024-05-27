import os

functions_path = './functions'
init_file_path = os.path.join(functions_path, '__init__.py')

# 检查并创建 functions 目录
if not os.path.exists(functions_path):
    os.makedirs(functions_path)

with open(init_file_path, 'w') as init_file:
    init_file.write("# __init__.py\n\n")
    all_functions = []
    for filename in os.listdir(functions_path):
        if filename.endswith('.py') and filename != '__init__.py':
            module_name = filename[:-3]
            init_file.write(f"from .{module_name} import *\n")
            all_functions.append(f'"{module_name}"')

    init_file.write("\n__all__ = [")
    init_file.write(", ".join(all_functions))
    init_file.write("]\n")

print(f"__init__.py generated with imports for all modules in {functions_path}")
