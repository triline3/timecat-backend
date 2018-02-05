# timecat-backend
timecat-backend

# 本地部署
## 安装virtualenv
clone仓库，用virtualenv创建虚拟环境venv35，并激活venv35
```bash
virtualenv venv35 --python=python3.5
source venv35/bin/activate
```
## 安装依赖
```bash
pip install -r requirements.txt
```
## 初始化数据库，并创建超级用户
```bash
python manage.py makemigrations tasks
python manage.py migrate
python manage.py createsuperuser
```
## 启动服务器
```bash
python manage.py runserver
```
用浏览器打开http://localhost:8000/

## 安装提示
在Windows下安装依赖时可能会报错(出错的包是markupsafe), 如果报错，先用
```python
pip uninstall makrupsafe
```
卸载markupsafe。
然后参考[makrupsafe-issues-67 @alorence](https://github.com/pallets/markupsafe/issues/67)
