from django.shortcuts import render, redirect, reverse
import re
from users.models import Passport
from books.models import Books
from books.enums import *
from django.core.paginator import Paginator

# Create your views here.
def index(request):
    '''显示首页'''
    # 查询每个种类的3个新品信息和4个销量最好的商品信息
    python_new = Books.objects.get_books_by_type(PYTHON, limit=3, sort='new')
    python_hot = Books.objects.get_books_by_type(PYTHON, limit=4, sort='hot')
    javascript_new = Books.objects.get_books_by_type(JAVASCRIPT, limit=3, sort='new')
    javascript_hot = Books.objects.get_books_by_type(JAVASCRIPT, limit=4, sort='hot')
    algorithms_new = Books.objects.get_books_by_type(ALGORITHMS, 3, sort='new')
    algorithms_hot = Books.objects.get_books_by_type(ALGORITHMS, 4, sort='hot')
    machinelearning_new = Books.objects.get_books_by_type(MACHINELEARNING, 3, sort='new')
    machinelearning_hot = Books.objects.get_books_by_type(MACHINELEARNING, 4,sort='hot')
    operatingsystem_new = Books.objects.get_books_by_type(OPERATINGSYSTEM, 3, sort='new')
    operatingsystem_hot = Books.objects.get_books_by_type(OPERATINGSYSTEM, 4, sort='hot')
    database_new = Books.objects.get_books_by_type(DATABASE, 3, sort='new')
    database_hot = Books.objects.get_books_by_type(DATABASE, 4, sort='hot')

    # 定义模板上下文
    context = {
        'python_new': python_new,
        'python_hot': python_hot,
        'javascript_new': javascript_new,
        'javascript_hot': javascript_hot,
        'algorithms_new': algorithms_new,
        'algorithms_hot': algorithms_hot,
        'machinelearning_new': machinelearning_new,
        'machinelearning_hot': machinelearning_hot,
        'operatingsystem_new': operatingsystem_new,
        'operatingsystem_hot': operatingsystem_hot,
        'database_new': database_new,
        'database_hot': database_hot,
    }

    return render(request, 'index.html', context)





def user_register(request):
    '''显示用户注册界面'''
    if request.method == 'GET':
        return render(request, 'users/user_register.html')
    else:
        '''进行用户注册处理'''
        # 接收数据
        username = request.POST.get('user_name')
        password = request.POST.get('pwd')
        email = request.POST.get('email')

        # 进行数据校验
        if not all([username, password, email]):
            # 有数据为空
            return render(request, 'users/register.html', {'errmsg': '参数不能为空!'})

        # 判断邮箱是否合法
        if not re.match(r'^[a-z0-9][\w\.\-]*@[a-z0-9\-]+(\.[a-z]{2,5}){1,2}$', email):
            # 邮箱不合法
            return render(request, 'users/register.html', {'errmsg': '邮箱不合法!'})

        # 进行业务处理:注册，向账户系统中添加账户
        # Passport.objects.create(username=username, password=password, email=email)
        try:
            Passport.objects.add_one_passport(username=username, password=password,    email=email)
        except Exception as e:
            print("e: ", e) # 把异常打印出来
            return render(request, 'users/register.html', {'errmsg':'用户名已存在！'})

        # 注册完，还是返回注册页。
        return redirect(reverse('index'))


