import yaml


def read_yaml_data(file_path, key_name):
    # WriteYaml(write_path="../yaml_file/new_write_data.yaml", file_name="file").write_yaml()
    with open(file_path, mode="r", encoding="utf-8") as f:
        read_data = yaml.safe_load(f)  # 安全模式加载yaml文件
        get_data = read_data[key_name]
        return get_data


if __name__ == '__main__':

    print(read_yaml_data(r"../yaml_file/new_write_data.yaml", "csrf_token"))

    # read_yaml("../yaml_file/params_files.yaml","csrf_token")
    # read_yaml("../yaml_file/new_write_data.yaml", "csrf_token")
    # print(read_yaml("../yaml_file/new_write_data.yaml","csrf_token"))
