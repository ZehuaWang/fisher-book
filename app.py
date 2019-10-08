# 主文件 - 入口文件 web服务器的启动和初始化核心对象 业务应该放到其他的文件中
from flask import Flask, make_response, jsonify
# 如果当前文件是主动执行的，__name__ 变量的值就是：__main__，
# 如果是被导入执行的，则是被导入的文件名
from app import create_app
# 请求上下文对象 Request
# 应用上下文对象 Flask
# Flask核心对象  存储在AppContext中
# Request 存储在 RequestContext中
app = create_app()


# 主执行文件 - 入口文件
if __name__ == '__main__':
    # 生产环境 nginx + uwsgi
    print(id(app))
    app.run(host='0.0.0.0', debug=app.config['DEBUG'])  # host 可以接受外网的访问
