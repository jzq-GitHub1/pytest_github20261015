import yaml


class WriteYaml:
    def __init__(self,write_path,write_data):
        self.write_path = write_path
        self.write_data = write_data


    def write_yaml_w(self):
        with open(self.write_path, "w",encoding="utf-8") as f:
            # safe_dump避免特殊字符导致的解析异常，allow_unicode=True保证中文正常显示
            yaml.safe_dump(self.write_data, f,allow_unicode=True)

    def write_yaml_a(self):
        with open(self.write_path, mode='a+') as f:
            yaml.safe_dump(self.write_data, f)

# class WriteYaml:
#     def __init__(self):
#         with open("../yaml_file/new_write_data.yaml", "w") as f:
#             pass
#
#     def write_yaml(self):
#         with open("../yaml_file/new_write_data.yaml", mode='a+') as file:
#             yaml.dump(write_data, file)


if __name__ == '__main__':

    # read_yaml.read_yaml("../yaml_file/new_write_data.yaml","csrf_token")
    WY = WriteYaml("../yaml_file/new_write_data.yaml")
    WY.write_yaml()