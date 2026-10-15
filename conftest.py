import os
import subprocess
import time


def pytest_sessionfinish(session, exitstatus):
    """
    测试会话结束后，自动生成Allure报告并尝试在默认浏览器打开
    """
    # 定义结果目录和报告输出目录
    results_dir = r"./report"
    report_dir = r"./report/html"

    # 确保结果目录存在（虽然pytest通常会创建，但防御性编程）
    # if not os.path.exists(results_dir):
    #     return

    print("\n正在生成 Allure 报告...")

    # 执行 allure generate 命令
    # --clean: 清空输出目录后再生成，避免旧报告残留
    # -o: 指定输出目录
    cmd_generate = f"allure generate {results_dir} -o {report_dir} --clean"
    # os.system(cmd_generate) os.system() 被划线提醒：这个函数‌已过时，不推荐继续使用‌，建议改用更安全的 subprocess 模块
    subprocess.run(cmd_generate, shell=True)
    print(f"Allure 报告已生成至: {os.path.abspath(report_dir)}")

    # 可选：自动生成后直接在默认浏览器打开
    # 注意：os.system 在某些CI环境中可能无法打开浏览器，本地开发非常有用
    cmd_open = f"allure open {report_dir}"
    print("Allure 报告正在打开...")
    subprocess.run(cmd_open, shell=True)

