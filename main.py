"""我的第一个 Python 项目 —— 简易计算器

运行方式：
    python main.py
"""


def calculate(a, b):
    """返回加减乘除四个结果。"""
    return {
        "加": a + b,
        "减": a - b,
        "乘": a * b,
        "除": a / b if b != 0 else "除数不能为 0",
    }


def main():
    print("=== 简单计算器 ===")
    a = float(input("请输入第一个数: "))
    b = float(input("请输入第二个数: "))

    for name, value in calculate(a, b).items():
        print(f"{name}：{value}")


if __name__ == "__main__":
    main()
