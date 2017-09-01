# -*- coding: UTF-8 -*-
from django.http import StreamingHttpResponse
from pyhtmlex.base.root import *
from body import *


EXP = [
    "负责ThinkCloud（基于OpenStack）计算组件Nova的开发。已完成新特性Enable/Disable KSM 和 Hot Extand vDisk的开发。涉及WSGI（PasteDeploy/Django），RPC（RabbitMQ），eventlet，stevedore，SqlAlchemy等",
    "用shell脚本完成HA controller nodes（3个控制节点）关键数据备份，并用scp上传至远程主机，可设置定期备份（crontab），查看版本，删除版本，选择版本进行恢复，进行相关配置（使用awk读取配置文件、使用sed修改配置文件），自动配置RSA public key",
    "参与SDS（软件定义存储）开发。参与horizon开发与调试，负责host模块。用python封装expect命令，进行远程server的添加部署（安装并启动agent服务，与controller上的服务通信），并对文件读写加锁以支持多线程并发；用SqlAlchemy访问MySql。",
    "负责Ceph参数调优测试系统后端搭建（设置一系列相近的参数，测试Ceph的性能指标，并将结果记入数据库，前端可以查询这些结果进行图形化展示）。使用Django为前端提供RestAPI，使用blocking方式的RPC server（oslo_messagimg）为多组测试提供队列，用Django自带的ORM工具访问数据库。",
    "自编UI库，完成“固态存储检测软件”的开发，主要功能为查看磁盘SMART信息，IO速率测试等。",
    "使用多线程、信号量、异步IO，完成数据转储设备的软件部分。将公司原有的因为没有采用线程同步互斥机制而无法同时转储4块SSD的软件加入同步互斥，跑出1GB/s的速度，并且在之后又重新设计转储的业务逻辑，将峰值速度提高到1.4GB/s，平均1.3GB/s",
    "开发了串口调试工具。windows命令行工具，可以和单片机（51，STM32等）串口进行交互，接收串口信息并打印，可发送任意数据，也可编辑配置文件，使用快捷键发送指定数据，方便嵌入式工程师调试。",
    "负责百度壁纸（3.0～4.0）的开发；参与百度卫士抢票插件开发。	",
    "使用ATL自绘控件开发图形界面。	",
    "使用STL和引用计数来处理控件、图片等资源的刷新和内存驻留等问题。	",
    "使用观察者模式处理网络资源（文案、图片）的异步加载问题。	",
    "跨进程在界面嵌入IE浏览器，解决IE容易卡死、崩溃的问题，增强鲁棒性。",
    "了解和使用智能指针和COM。",
    "在导师的指导下进行OpenStack中Neutron网络模块的开发。	",
    "在Subnet表中添加qos字段，当该子网中的Port没有配置qos时，将其qos配置成其所在的子网的qos。",
    "调用接口为隧道口配置默认路由，解决了跨三层不通的问题。	",
    "使用python -mpdb进行调试。学会了tail -f | grep -E过滤日志。	",
    "",
]


class Resume(object):
    def __init__(self):
        self.row = 0
        self.exp_index = 0
        self.title_style = 'font-weight: bold; font-size: 20px'
        self.company_style = 'font-weight: bold'
        self.form = ColorTable(27, 3, [150, 300, 300])
        self.create()

    def create(self):
        self.form(0, 0).inner_html = "周宁"
        self.form(0, 1).inner_html = "18116119117"
        self.form(0, 2).inner_html = "icemanzhouning@yeah.net"
        self.row += 1

        self.add_title("教育背景")
        self.add_edu("中南大学", "软件工程（硕士）", "2013.09~2016.06")
        self.add_edu("江苏警官学院", "行政管理（本科）", "2008.09~2012.06")

        self.add_title("工作经验")

        self.add_company("2016.12~至今", "联想（上海）计算机科技有限公司", "云计算工程师")
        for i in range(4):
            self.add_exp()

        self.add_company("2016.07~2016.12", "湖南博匠信息科技有限公司", "C++软件开发工程师")
        for i in range(3):
            self.add_exp()

        self.add_title("实习经验")

        self.add_company("2014.05~2015.02", "百度", "C++软件开发工程师")
        for i in range(6):
            self.add_exp()

        self.add_company("2015.11-2016.02", "深圳市深信服电子科技有限公司", "云计算工程师")
        for i in range(4):
            self.add_exp()

    def add_title(self, title):
        self.form(self.row, 0).inner_html = title
        self.form(self.row, 0).set_attributes(style=self.title_style)
        self.form(self.row).combine_col(0, 2)
        self.row += 1

    def add_edu(self, school, institute, time):
        self.form(self.row, 0).inner_html = school
        self.form(self.row, 1).inner_html = institute
        self.form(self.row, 2).inner_html = time
        self.row += 1

    def add_company(self, time, name, job):
        self.form(self.row, 0).inner_html = time
        self.form(self.row, 1).inner_html = name
        self.form(self.row, 1).set_attributes(style=self.company_style)
        self.form(self.row, 2).inner_html = job
        self.row += 1

    def add_exp(self):
        self.form(self.row, 0).inner_html = ""
        self.form(self.row, 1).inner_html = EXP[self.exp_index]
        self.form(self.row, 1).set_attributes(align="left")
        self.form(self.row).combine_col(1, 2)
        self.row += 1
        self.exp_index += 1


def body_main():
    body, style, left, right = body_factory([("/", "首页")])

    # img = Img("/static/img/baidu.png")
    # a.push_back(img)
    # left.push_back(a)
    # a = A("/blog/python")
    # a.inner_html = 'python'
    # left.push_back(a)

    right_style = md_parser(right, os.path.join(os.path.dirname(__file__)), 'readme')
    style.extend(right_style)
    # right.push_back(Resume().form)

    style.append(Resume().form.style)
    return body, style


def main(request):
    body, styles = body_main()
    head = lazy_head("my PyHtmlEx", styles)
    response = StreamingHttpResponse(Html(head, body).generate())

    # response = HttpResponse(main())
    # print type(response)
    # print dir(response)
    # print response
    # print response._headers
    return response
