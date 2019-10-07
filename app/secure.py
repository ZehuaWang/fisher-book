# 数据库 密码 账号配置文件 -> 不应上传到git
# 生产环境与开发环境采取不同设置
DEBUG = True
SQLALCHEMY_DATABASE_URI = 'mysql+cymysql://root:CA123456ca@@localhost:3306/fisher'
