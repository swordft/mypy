1. 如何引入模块（py结尾的文件）
import 模块名

2. 什么是包？
一个目录里面如果有__init__.py文件，那么这个目录就可以称之为包

3. 如何调用包里面的模块？
from 包名 import 模块名


机房表
id 自增id
name 机房英文简写
name_cn	机房中文名
address	地址
admin 联系人
phone 联系电话
num 机柜数量int

机柜表：
id 自增id
name 机柜名
idc_id 所在机房
u_num U位
power 电量

服务器表
id 自增id
hostname 主机名，主键不允许为空
inter_ip 内部ip
outer_ip 外部ip
canbinet_id 机柜id
op 负责人
phone 联系电话

