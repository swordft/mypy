1. 导入db.sql数据库文件
2. 安装程序所需要的依赖包  pip install  -r requirement.txt
3. 运行run.py文集爱你
4. 默认管理员帐号：fangtao:xiaofang

jquery三步走
1. 选择器--选择要操作的元素
    id: <div id='idname'> --> $("#idname")
    class: <div class="classname"> --> $(".classname")
    元素: <div><p>你好</p></div> --> $("p")
2. 动作--选择的元素该怎么操作
    $("选择器").html() --> $("选择器").html("内容")
    $("选择器").val() --> $("选择器").val("内容")
    $("选择器").attr('data-id') --> $("选择器").attr('data-id'=1)
    $("选择器").css() --> $("选择器").css("color":red)
3. 事件--在什么情况下执行上面的动作
    onclick     

渲染的两种方式：
1. jinja2
逻辑端：
idcs = [{'id':7,'name':'hp'},{'id':8,'name','syq'}]
return render_template("cabinetlist.html",idcs=idcs)

前端渲染：
<select id='idc_id' name='idc_id'>
    {% for idc in idcs %}
        <option value="{{ idc.id }}">{{ idc.name }}</option>
    {% endfor %}
</select>

2. jquery
逻辑端：
idcs = [{'id':7,'name':'hp'},{'id':8,'name','syq'}]
return json.dump('code':0,idcs=idcs)

前端：
<select id='idc_id' name='idc_id'>
</select>

jquery:
    for idc in idcs:
        str += '<option values="idc.id">'+idc.name+'</option>'
    $('#idc_id').html(str)


app.config: flask内置全局字典
