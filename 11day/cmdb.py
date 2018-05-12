@app.route('/idc')
def idc():
    if not session.get('name',None):
        return redirect('/login')
    name = session['name']
    role = session['role']
    fields = ['id','name','city','address']
    sql = "select %s from idc" % ','.join(fields)
    cur.execute(sql)
    res = cur.fetchall()
    data = [dict((k,row[i]) for i,k in enumerate(fields)) for row in res]
    return render_template('idc.html',data=data,info=session)

@app.route('/cabinet')
def cabinet():
    if not session.get('name',None):
        return redirect('/login')
    name = session['name']
    role = session['role']
    fields = ['id','cicode','location','capacity','idc']
    sql = "select %s from cabinet" % ','.join(fields)
    cur.execute(sql)
    res = cur.fetchall()
    data = [dict((k,row[i]) for i,k in enumerate(fields)) for row in res]
    return render_template('cabinet.html',data=data,info=session)

@app.route('/server')
def server():
    if not session.get('name',None):
        return redirect('/login')
    name = session['name']
    role = session['role']
    fields = ['id','cicode','sn','model','architecture','cpu','memory','disk','cabinet','ip','hostname','os']
    sql = "select %s from server" % ','.join(fields)
    cur.execute(sql)
    res = cur.fetchall()
    data = [dict((k,row[i]) for i,k in enumerate(fields)) for row in res]
    return render_template('server.html',data=data,info=session)

@app.route('/update_server',methods=['GET','POST'])
def update_server():
    if not session.get('name',None):
        return redirect('/login')
    name = session['name']
    role = session['role']
    info = {'name':name,'role':role}
    if request.method == 'GET':
        id = request.args.get('id')
        return render_template('update_server.html',id=id,info=info)
    if request.method == 'POST':
        data = dict((k,v[0]) for k,v in dict(request.form).items())
        if info['role'] == "admin":
            fields = ['id','name','name_cn','password','mobile','email','role','status']
        else:
            fields = ['id','name','name_cn','password','mobile','email']
        data = dict((f,data[f]) for f in fields)
        conditions = ["%s='%s'" % (k,v) for k,v in data.items()]
        try:
            sql = "update users set %s where id=%s" % (','.join(conditions),data['id'])
            cur.execute(sql)
            return json.dumps({"code":0,"errmsg":"update success"})
        except Exception,e:
	    errmsg = e
            return json.dumps({"code":1})


