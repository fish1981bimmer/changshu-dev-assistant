#!/usr/bin/env python3
"""
错误分析工具
智能诊断错误并提供解决方案
"""

import re
import json
import traceback
from typing import Dict, List, Optional, Tuple
from datetime import datetime
import os


class ErrorAnalyzer:
    """错误分析器"""
    
    def __init__(self, config: Dict = None):
        self.config = config or {}
        self.patterns = self.config.get('patterns', {})
        self.solutions = self.config.get('solutions', {})
        self.knowledge_base = self.load_knowledge_base()
        
    def load_knowledge_base(self) -> Dict:
        """加载知识库"""
        kb_path = os.path.join(os.path.dirname(__file__), '..', 'data', 'error_patterns.json')
        try:
            with open(kb_path, 'r', encoding='utf-8') as f:
                return json.load(f)
        except FileNotFoundError:
            return self.get_default_patterns()
    
    def get_default_patterns(self) -> Dict:
        """获取默认错误模式"""
        return {
            'database': {
                'ORA-00942': {
                    'description': '表或视图不存在',
                    'solution': '检查表名是否正确，确认表已创建',
                    'example': 'SELECT * FROM existing_table'
                },
                'ORA-00904': {
                    'description': '标识符无效',
                    'solution': '检查列名是否正确',
                    'example': 'SELECT valid_column FROM table'
                },
                'DM-00001': {
                    'description': '违反唯一约束',
                    'solution': '检查重复数据，确保唯一性',
                    'example': 'INSERT INTO table (id, name) VALUES (1, \'test\')'
                }
            },
            'python': {
                'NameError': {
                    'description': '名称未定义',
                    'solution': '检查变量名拼写，确保变量已定义',
                    'example': 'x = 10; print(x)'
                },
                'TypeError': {
                    'description': '类型错误',
                    'solution': '检查数据类型匹配',
                    'example': 'str(123) + "abc"'
                },
                'ImportError': {
                    'description': '导入错误',
                    'solution': '检查模块名，确保已安装',
                    'example': 'import numpy'
                }
            },
            'system': {
                'Segmentation fault': {
                    'description': '段错误',
                    'solution': '检查指针操作，内存访问越界',
                    'example': '避免空指针解引用'
                },
                'Permission denied': {
                    'description': '权限不足',
                    'solution': '检查文件权限，使用sudo或修改权限',
                    'example': 'chmod +x script.sh'
                }
            }
        }
    
    def analyze_error(self, error_message: str, error_type: str = None) -> Dict:
        """分析错误"""
        analysis = {
            'timestamp': datetime.now().isoformat(),
            'error_message': error_message,
            'error_type': error_type,
            'diagnosis': None,
            'solutions': [],
            'similar_errors': [],
            'recommended_actions': []
        }
        
        # 识别错误类型
        if not error_type:
            error_type = self.identify_error_type(error_message)
        
        analysis['error_type'] = error_type
        
        # 诊断错误
        diagnosis = self.diagnose_error(error_message, error_type)
        analysis['diagnosis'] = diagnosis
        
        # 获取解决方案
        solutions = self.get_solutions(error_type, error_message)
        analysis['solutions'] = solutions
        
        # 查找相似错误
        similar_errors = self.find_similar_errors(error_message)
        analysis['similar_errors'] = similar_errors
        
        # 推荐行动
        actions = self.recommend_actions(diagnosis, solutions)
        analysis['recommended_actions'] = actions
        
        return analysis
    
    def identify_error_type(self, error_message: str) -> str:
        """识别错误类型"""
        error_lower = error_message.lower()
        
        # 数据库错误
        if any(pattern in error_message for pattern in ['ORA-', 'DM-', 'SQL', 'ORA']):
            return 'database'
        
        # Python错误
        if any(pattern in error_message for pattern in ['NameError', 'TypeError', 'ImportError', 'AttributeError']):
            return 'python'
        
        # 系统错误
        if any(pattern in error_message for pattern in ['Segmentation fault', 'Permission denied', 'File not found']):
            return 'system'
        
        # 网络错误
        if any(pattern in error_message for pattern in ['Connection', 'Network', 'Timeout', 'HTTP']):
            return 'network'
        
        # 默认返回通用错误
        return 'general'
    
    def diagnose_error(self, error_message: str, error_type: str) -> Dict:
        """诊断错误"""
        diagnosis = {
            'category': error_type,
            'severity': 'medium',
            'description': '',
            'likely_cause': '',
            'affected_components': []
        }
        
        # 根据错误类型进行诊断
        if error_type == 'database':
            diagnosis.update(self.diagnose_database_error(error_message))
        elif error_type == 'python':
            diagnosis.update(self.diagnose_python_error(error_message))
        elif error_type == 'system':
            diagnosis.update(self.diagnose_system_error(error_message))
        elif error_type == 'network':
            diagnosis.update(self.diagnose_network_error(error_message))
        else:
            diagnosis.update(self.diagnose_general_error(error_message))
        
        return diagnosis
    
    def diagnose_database_error(self, error_message: str) -> Dict:
        """诊断数据库错误"""
        diagnosis = {
            'description': '数据库操作错误',
            'likely_cause': '',
            'affected_components': ['database', 'application'],
            'severity': 'high'
        }
        
        if 'ORA-00942' in error_message:
            diagnosis['likely_cause'] = '表不存在或权限不足'
        elif 'ORA-00904' in error_message:
            diagnosis['likely_cause'] = '列名无效或不存在'
        elif 'DM-00001' in error_message:
            diagnosis['likely_cause'] = '违反唯一约束条件'
        elif 'ORA-00001' in error_message:
            diagnosis['likely_cause'] = '违反唯一约束'
        
        return diagnosis
    
    def diagnose_python_error(self, error_message: str) -> Dict:
        """诊断Python错误"""
        diagnosis = {
            'description': 'Python代码错误',
            'likely_cause': '',
            'affected_components': ['python_code', 'dependencies'],
            'severity': 'medium'
        }
        
        if 'NameError' in error_message:
            diagnosis['likely_cause'] = '变量名拼写错误或未定义'
        elif 'TypeError' in error_message:
            diagnosis['likely_cause'] = '数据类型不匹配'
        elif 'ImportError' in error_message:
            diagnosis['likely_cause'] = '模块导入失败或未安装'
        elif 'AttributeError' in error_message:
            diagnosis['likely_cause'] = '对象属性不存在'
        
        return diagnosis
    
    def diagnose_system_error(self, error_message: str) -> Dict:
        """诊断系统错误"""
        diagnosis = {
            'description': '系统级错误',
            'likely_cause': '',
            'affected_components': ['system', 'hardware', 'os'],
            'severity': 'high'
        }
        
        if 'Segmentation fault' in error_message:
            diagnosis['likely_cause'] = '内存访问越界或指针错误'
        elif 'Permission denied' in error_message:
            diagnosis['likely_cause'] = '文件或目录权限不足'
        elif 'File not found' in error_message:
            diagnosis['likely_cause'] = '文件或路径不存在'
        
        return diagnosis
    
    def diagnose_network_error(self, error_message: str) -> Dict:
        """诊断网络错误"""
        diagnosis = {
            'description': '网络连接错误',
            'likely_cause': '',
            'affected_components': ['network', 'connectivity'],
            'severity': 'medium'
        }
        
        if 'Connection refused' in error_message:
            diagnosis['likely_cause'] = '服务未启动或端口被占用'
        elif 'Timeout' in error_message:
            diagnosis['likely_cause'] = '网络超时或服务响应慢'
        elif 'HTTP 404' in error_message:
            diagnosis['likely_cause'] = '资源不存在'
        
        return diagnosis
    
    def diagnose_general_error(self, error_message: str) -> Dict:
        """诊断通用错误"""
        return {
            'description': '通用错误',
            'likely_cause': '未知原因',
            'affected_components': ['general'],
            'severity': 'medium'
        }
    
    def get_solutions(self, error_type: str, error_message: str) -> List[Dict]:
        """获取解决方案"""
        solutions = []
        
        # 从知识库获取解决方案
        if error_type in self.knowledge_base:
            for error_pattern, solution_info in self.knowledge_base[error_type].items():
                if error_pattern in error_message:
                    solutions.append({
                        'title': solution_info['description'],
                        'solution': solution_info['solution'],
                        'example': solution_info['example'],
                        'priority': 'high'
                    })
        
        # 添加通用解决方案
        if error_type == 'database':
            solutions.extend([
                {
                    'title': '检查SQL语法',
                    'solution': '使用SQL格式化工具检查语法',
                    'example': 'SELECT * FROM table WHERE condition',
                    'priority': 'medium'
                },
                {
                    'title': '检查数据库连接',
                    'solution': '验证数据库连接字符串和权限',
                    'example': 'ping database_host',
                    'priority': 'high'
                }
            ])
        elif error_type == 'python':
            solutions.extend([
                {
                    'title': '检查代码语法',
                    'solution': '使用Python语法检查工具',
                    'example': 'python -m py_compile script.py',
                    'priority': 'medium'
                },
                {
                    'title': '检查依赖',
                    'solution': '确保所有依赖已安装',
                    'example': 'pip install -r requirements.txt',
                    'priority': 'high'
                }
            ])
        elif error_type == 'system':
            solutions.extend([
                {
                    'title': '检查系统资源',
                    'solution': '检查CPU、内存使用情况',
                    'example': 'top, htop',
                    'priority': 'medium'
                },
                {
                    'title': '检查日志',
                    'solution': '查看系统日志文件',
                    'example': 'tail -f /var/log/syslog',
                    'priority': 'high'
                }
            ])
        
        return solutions
    
    def find_similar_errors(self, error_message: str) -> List[Dict]:
        """查找相似错误"""
        similar = []
        
        for category, errors in self.knowledge_base.items():
            for error_pattern, error_info in errors.items():
                if error_pattern in error_message:
                    similar.append({
                        'pattern': error_pattern,
                        'description': error_info['description'],
                        'solution': error_info['solution']
                    })
        
        return similar
    
    def recommend_actions(self, diagnosis: Dict, solutions: List[Dict]) -> List[str]:
        """推荐行动步骤"""
        actions = []
        
        # 根据严重程度推荐行动
        if diagnosis['severity'] == 'high':
            actions.append('1. 立即停止相关服务')
            actions.append('2. 检查系统日志')
            actions.append('3. 联系技术支持')
        
        # 添加解决方案相关行动
        for i, solution in enumerate(solutions, len(actions) + 1):
            actions.append(f"{i}. {solution['title']}")
            actions.append(f"   {solution['solution']}")
        
        # 添加预防措施
        actions.append(f"{len(actions) + 1}. 记录错误信息到知识库")
        actions.append(f"{len(actions) + 1}. 设置监控和告警")
        
        return actions
    
    def add_to_knowledge_base(self, error_pattern: str, error_info: Dict):
        """添加错误模式到知识库"""
        error_type = error_info.get('category', 'general')
        
        if error_type not in self.knowledge_base:
            self.knowledge_base[error_type] = {}
        
        self.knowledge_base[error_type][error_pattern] = error_info
        
        # 保存到文件
        self.save_knowledge_base()
    
    def save_knowledge_base(self):
        """保存知识库"""
        kb_path = os.path.join(os.path.dirname(__file__), '..', 'data', 'error_patterns.json')
        
        try:
            os.makedirs(os.path.dirname(kb_path), exist_ok=True)
            with open(kb_path, 'w', encoding='utf-8') as f:
                json.dump(self.knowledge_base, f, indent=2, ensure_ascii=False)
            print("知识库已保存")
        except Exception as e:
            print(f"保存知识库失败: {e}")
    
    def generate_report(self, analysis: Dict) -> str:
        """生成分析报告"""
        report = f"""
错误分析报告
{'='*50}

错误时间: {analysis['timestamp']}
错误类型: {analysis['error_type']}
错误信息: {analysis['error_message']}

诊断结果:
- 类别: {analysis['diagnosis']['category']}
- 严重程度: {analysis['diagnosis']['severity']}
- 描述: {analysis['diagnosis']['description']}
- 可能原因: {analysis['diagnosis']['likely_cause']}
- 影响组件: {', '.join(analysis['diagnosis']['affected_components'])}

解决方案:
"""
        
        for i, solution in enumerate(analysis['solutions'], 1):
            report += f"{i}. {solution['title']}\n"
            report += f"   解决方案: {solution['solution']}\n"
            report += f"   示例: {solution['example']}\n\n"
        
        report += f"相似错误:\n"
        for i, similar in enumerate(analysis['similar_errors'], 1):
            report += f"{i}. {similar['pattern']}: {similar['description']}\n"
        
        report += f"\n推荐行动:\n"
        for action in analysis['recommended_actions']:
            report += f"{action}\n"
        
        return report


def main():
    """主函数"""
    import argparse
    
    parser = argparse.ArgumentParser(description='错误分析工具')
    parser.add_argument('--error', required=True, help='错误信息')
    parser.add_argument('--type', help='错误类型')
    parser.add_argument('--config', help='配置文件路径')
    parser.add_argument('--report', help='输出报告文件')
    parser.add_argument('--add-to-kb', action='store_true', help='添加到知识库')
    
    args = parser.parse_args()
    
    # 加载配置
    config = {}
    if args.config:
        try:
            with open(args.config, 'r', encoding='utf-8') as f:
                import yaml
                config = yaml.safe_load(f)
        except Exception as e:
            print(f"加载配置失败: {e}")
    
    # 创建分析器
    analyzer = ErrorAnalyzer(config)
    
    # 分析错误
    analysis = analyzer.analyze_error(args.error, args.type)
    
    # 生成报告
    report = analyzer.generate_report(analysis)
    print(report)
    
    # 保存到文件
    if args.report:
        with open(args.report, 'w', encoding='utf-8') as f:
            f.write(report)
        print(f"报告已保存到: {args.report}")
    
    # 添加到知识库
    if args.add_to_kb:
        error_pattern = analysis['error_type']
        error_info = {
            'category': analysis['error_type'],
            'description': analysis['diagnosis']['description'],
            'solution': analysis['solutions'][0]['solution'] if analysis['solutions'] else '',
            'example': analysis['solutions'][0]['example'] if analysis['solutions'] else ''
        }
        analyzer.add_to_knowledge_base(error_pattern, error_info)
        print("错误已添加到知识库")


if __name__ == '__main__':
    main()