from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html')




def user_register(request):
    '''显示用户注册界面'''
    if request.method == 'GET':
        return render(request, 'users/user_register.html')
    else:
        '''进行用户注册处理'''
        # 接收数据
        username = request.POST.get('user_name', '')
        password = request.POST.get('pwd', '')
        email = request.POST.get('email', '')

        # 进行数据校验
        if not all([username, password, email]):
            # 有数据为空
            return render(request, 'users/user_register.html', {
                'errmsg': '参数不能为空!'
                })
        if not re.match(r'^[a-z0-9][\w\.\-]*@[a-z0-9\-]+(\.[a-z]{2,5}){1,2}')

