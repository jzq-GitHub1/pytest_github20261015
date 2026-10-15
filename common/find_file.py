import os


def find_path(dir_name,file_name):
    root_directory = os.path.dirname(os.path.abspath(os.path.dirname(os.path.abspath(__file__))))
    # file_path = os.path.join(root_directory, "yaml_file", "new_write_data.yaml")
    file_path = os.path.join(root_directory,dir_name,file_name)
    return file_path

# print(find_path("yaml_file","new_write_data.yaml"))


# root_directory = os.path.dirname(os.path.abspath(os.path.dirname(os.path.abspath(__file__))))
# join_path = os.path.join(root_directory, "yaml_file", "new_write_data.yaml")
# with open(join_path,mode="r") as f:
#     data = yaml.safe_load(f)
#     print(data)
# dir_path = '../yaml_file/new_write_data.yaml'
# # if not os.path.exists(dir_path):
# #     os.makedirs(dir_path)  # 创建目录
# file_path = os.path.join(dir_path)
# with open(file_path, 'a+') as file:
#     file.write("Hello")

# # 获取当前脚本所在的绝对目录
# script_dir = Path(__file__).resolve().parent
#
# # 构建目标文件的绝对路径 (假设文件在脚本同级目录的 data 文件夹下)
# file_path = script_dir / "../yaml_file" / "new_write_data.yaml"
#
# # 检查文件是否存在
# if file_path.exists():
#     with open(file_path, 'r', encoding='utf-8') as f:
#         content = f.read()
#         print(content)
# else:
#     print(f"文件未找到: {file_path}")
#     # 调试用：打印当前工作目录和预期路径
#     print(f"当前工作目录: {os.getcwd()}")


# if os.path.exists(file_path2):
#     with open(file_path2, 'r') as f:
#         content = f.read()
#         print(content)
# else:
#     print("文件不存在!")
