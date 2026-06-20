#!/usr/bin/env python3
"""
示例应用程序
用于测试测试自动化工具
"""

def add(a, b):
    """加法函数"""
    return a + b

def subtract(a, b):
    """减法函数"""
    return a - b

def multiply(a, b):
    """乘法函数"""
    return a * b

def divide(a, b):
    """除法函数"""
    if b == 0:
        raise ValueError("除数不能为零")
    return a / b

class Calculator:
    """计算器类"""
    
    def __init__(self):
        self.history = []
    
    def calculate(self, operation, a, b):
        """执行计算操作"""
        if operation == 'add':
            result = a + b
        elif operation == 'subtract':
            result = a - b
        elif operation == 'multiply':
            result = a * b
        elif operation == 'divide':
            if b == 0:
                raise ValueError("除数不能为零")
            result = a / b
        else:
            raise ValueError("不支持的操作")
        
        self.history.append((operation, a, b, result))
        return result
    
    def get_history(self):
        """获取计算历史"""
        return self.history
    
    def clear_history(self):
        """清空计算历史"""
        self.history.clear()

def is_even(number):
    """判断数字是否为偶数"""
    return number % 2 == 0

def is_odd(number):
    """判断数字是否为奇数"""
    return number % 2 != 0

def factorial(n):
    """计算阶乘"""
    if n < 0:
        raise ValueError("阶乘不能为负数")
    if n == 0 or n == 1:
        return 1
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

def fibonacci(n):
    """计算斐波那契数列第n项"""
    if n < 0:
        raise ValueError("斐波那契数列索引不能为负数")
    if n == 0:
        return 0
    if n == 1:
        return 1
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b

# 私有函数，不应生成测试用例
def _private_helper():
    """私有辅助函数"""
    pass

# 特殊方法，不应生成测试用例
def __special_method__():
    """特殊方法"""
    pass