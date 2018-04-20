jinja2模板继承，解决了什么问题？
1. 公共代码只需要写一份，其他html文件只需要extend即可
2. 解决代码冗余的问题

1. 模板: 把公用的布局元素写到一个base.html中，其中需要修改的地方用 {% block blockname %} {% endblock %} 标识
2. 子版: 通过{% extends "base.html" %} 能把母版的所有内容都引入
3. 子版中可以对模板中block的部分进行重写。重写格式为: 
{% block blockname %}
    自定义内容
{% endblock %}
