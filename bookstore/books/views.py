from django.shortcuts import render
from books.models import Books
from books.enums import *
from django.core.urlresolvers import reverse
from django.core.paginator import Paginator

# Create your views here.
def book_detail(request, books_id):
    '''显示商品的详情页面'''
    # 获取商品的详情信息
    books = Books.objects.get_books_by_id(books_id=books_id)

    if books is None:
        # 商品不存在，跳转到首页
        return redirect(reverse('index'))

    # 新品推荐
    books_li = Books.objects.get_books_by_type(type_id=books.type_id, limit=2, sort='new')

    # 当前商品类型
    type_title = BOOKS_TYPE[books.type_id]

    # 定义上下文
    context = {'books': books, 'books_li': books_li, 'type_title': type_title}

    # 使用模板
    return render(request, 'books/book_detail.html', context)


