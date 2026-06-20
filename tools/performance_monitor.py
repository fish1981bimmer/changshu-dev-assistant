#!/usr/bin/env python3
"""
性能监控工具
实时监控系统性能并提供优化建议
"""

import psutil
import time
import json
import threading
from datetime import datetime
from typing import Dict, List, Optional
import matplotlib.pyplot as plt
import pandas as pd


class PerformanceMonitor:
    """性能监控器"""
    
    def __init__(self, config: Dict = None):
        self.config = config or {}
        self.monitoring = self.config.get('monitoring', {})
        self.enabled = self.monitoring.get('enabled', False)
        self.interval = self.monitoring.get('interval', 30)
        self.metrics = self.monitoring.get('metrics', ['cpu', 'memory', 'disk', 'network'])
        self.thresholds = self.monitoring.get('thresholds', {})
        self.history = []
        self.is_monitoring = False
        
    def start_monitoring(self):
        """开始监控"""
        if not self.enabled:
            print("性能监控未启用")
            return
            
        self.is_monitoring = True
        print(f"开始性能监控，间隔: {self.interval}秒")
        
        while self.is_monitoring:
            try:
                metrics = self.collect_metrics()
                self.history.append(metrics)
                
                # 检查阈值
                alerts = self.check_thresholds(metrics)
                if alerts:
                    print(f"⚠️  性能警告: {alerts}")
                
                time.sleep(self.interval)
                
            except KeyboardInterrupt:
                print("\n停止性能监控")
                self.is_monitoring = False
                break
            except Exception as e:
                print(f"监控错误: {e}")
                time.sleep(self.interval)
    
    def stop_monitoring(self):
        """停止监控"""
        self.is_monitoring = False
        print("性能监控已停止")
    
    def collect_metrics(self) -> Dict:
        """收集性能指标"""
        metrics = {
            'timestamp': datetime.now().isoformat(),
            'cpu': psutil.cpu_percent(interval=1),
            'memory': psutil.virtual_memory().percent,
            'disk': psutil.disk_usage('/').percent,
            'network': self.get_network_metrics(),
            'processes': len(psutil.pids()),
            'load_average': psutil.getloadavg() if hasattr(psutil, 'getloadavg') else None
        }
        
        # 添加进程信息
        metrics['top_processes'] = self.get_top_processes()
        
        return metrics
    
    def get_network_metrics(self) -> Dict:
        """获取网络指标"""
        net_io = psutil.net_io_counters()
        return {
            'bytes_sent': net_io.bytes_sent,
            'bytes_recv': net_io.bytes_recv,
            'packets_sent': net_io.packets_sent,
            'packets_recv': net_io.packets_recv
        }
    
    def get_top_processes(self) -> List[Dict]:
        """获取top进程"""
        processes = []
        for proc in psutil.process_iter(['pid', 'name', 'cpu_percent', 'memory_percent']):
            try:
                processes.append({
                    'pid': proc.info['pid'],
                    'name': proc.info['name'],
                    'cpu_percent': proc.info['cpu_percent'],
                    'memory_percent': proc.info['memory_percent']
                })
            except (psutil.NoSuchProcess, psutil.AccessDenied):
                continue
        
        # 按CPU使用率排序
        processes.sort(key=lambda x: x['cpu_percent'], reverse=True)
        return processes[:10]
    
    def check_thresholds(self, metrics: Dict) -> List[str]:
        """检查阈值"""
        alerts = []
        
        if 'cpu' in self.thresholds and metrics['cpu'] > self.thresholds['cpu']:
            alerts.append(f"CPU使用率过高: {metrics['cpu']}%")
        
        if 'memory' in self.thresholds and metrics['memory'] > self.thresholds['memory']:
            alerts.append(f"内存使用率过高: {metrics['memory']}%")
        
        if 'disk' in self.thresholds and metrics['disk'] > self.thresholds['disk']:
            alerts.append(f"磁盘使用率过高: {metrics['disk']}%")
        
        return alerts
    
    def generate_report(self, output_file: str = None) -> str:
        """生成性能报告"""
        if not self.history:
            return "没有历史数据"
        
        report = {
            'generated_at': datetime.now().isoformat(),
            'summary': self.generate_summary(),
            'recommendations': self.generate_recommendations(),
            'history': self.history[-100:]  # 最近100条记录
        }
        
        if output_file:
            with open(output_file, 'w', encoding='utf-8') as f:
                json.dump(report, f, indent=2, ensure_ascii=False)
            print(f"性能报告已保存到: {output_file}")
        
        return self.format_report(report)
    
    def generate_summary(self) -> Dict:
        """生成摘要"""
        if not self.history:
            return {}
        
        cpu_values = [m['cpu'] for m in self.history]
        memory_values = [m['memory'] for m in self.history]
        disk_values = [m['disk'] for m in self.history]
        
        return {
            'avg_cpu': sum(cpu_values) / len(cpu_values),
            'max_cpu': max(cpu_values),
            'avg_memory': sum(memory_values) / len(memory_values),
            'max_memory': max(memory_values),
            'avg_disk': sum(disk_values) / len(disk_values),
            'max_disk': max(disk_values),
            'total_samples': len(self.history)
        }
    
    def generate_recommendations(self) -> List[str]:
        """生成优化建议"""
        recommendations = []
        
        if self.history:
            avg_cpu = self.generate_summary()['avg_cpu']
            avg_memory = self.generate_summary()['avg_memory']
            avg_disk = self.generate_summary()['avg_disk']
            
            if avg_cpu > 80:
                recommendations.append("CPU使用率过高，建议优化应用程序性能或增加资源")
            
            if avg_memory > 80:
                recommendations.append("内存使用率过高，建议检查内存泄漏或增加内存")
            
            if avg_disk > 80:
                recommendations.append("磁盘使用率过高，建议清理磁盘或增加存储空间")
            
            # 检查进程异常
            top_processes = self.history[-1]['top_processes'] if self.history else []
            for proc in top_processes:
                if proc['cpu_percent'] > 50:
                    recommendations.append(f"进程 {proc['name']} (PID: {proc['pid']}) CPU使用率过高，建议检查")
        
        return recommendations
    
    def format_report(self, report: Dict) -> str:
        """格式化报告"""
        summary = report['summary']
        recommendations = report['recommendations']
        
        formatted = f"""
性能监控报告
{'='*50}

生成时间: {report['generated_at']}

摘要信息:
- 平均CPU使用率: {summary.get('avg_cpu', 0):.1f}%
- 最大CPU使用率: {summary.get('max_cpu', 0):.1f}%
- 平均内存使用率: {summary.get('avg_memory', 0):.1f}%
- 最大内存使用率: {summary.get('max_memory', 0):.1f}%
- 平均磁盘使用率: {summary.get('avg_disk', 0):.1f}%
- 最大磁盘使用率: {summary.get('max_disk', 0):.1f}%
- 样本数量: {summary.get('total_samples', 0)}

优化建议:
"""
        
        for i, rec in enumerate(recommendations, 1):
            formatted += f"{i}. {rec}\n"
        
        formatted += f"\n历史数据点数: {len(report['history'])}"
        
        return formatted


def main():
    """主函数"""
    import argparse
    
    parser = argparse.ArgumentParser(description='性能监控工具')
    parser.add_argument('--config', help='配置文件路径')
    parser.add_argument('--monitor', action='store_true', help='开始监控')
    parser.add_argument('--report', help='生成报告文件')
    parser.add_argument('--interval', type=int, default=30, help='监控间隔(秒)')
    
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
    
    # 创建监控器
    monitor = PerformanceMonitor(config)
    
    if args.monitor:
        monitor.start_monitoring()
    elif args.report:
        report = monitor.generate_report(args.report)
        print(report)
    else:
        # 显示当前状态
        metrics = monitor.collect_metrics()
        print("当前性能指标:")
        print(f"CPU使用率: {metrics['cpu']}%")
        print(f"内存使用率: {metrics['memory']}%")
        print(f"磁盘使用率: {metrics['disk']}%")
        print(f"网络流量: 发送 {metrics['network']['bytes_sent']} bytes, 接收 {metrics['network']['bytes_recv']} bytes")
        print(f"进程数: {metrics['processes']}")


if __name__ == '__main__':
    main()