from django.contrib import admin
from django.urls import path
from . import views
from .views import PostListView
urlpatterns =[
    path('',views.index),
    path('index.html',views.home),
    path('contact1.html',views.contact1),
    
    path('about.html',views.about),
    #path('Login.html',views.OpenLogin),
    path('review.html',views.review),
    path('Login.html',views.Insertrecord),
    path('contact.html', views.feedback),
    path('Sample.html',views.BookReaderLogin),
    path('profile.html',views.profile1,name="profile1"),
    path('',views.LoginSuccess),
    path('user.html',views.user),
    path('shop.html', views.shop,name="shop"),
    #path('sell.html', views.sell),
    path('buy.html', views.buybook),
    path('mypost.html', views.mypost1,name="mypost1"),
    path('sell.html', views.UploadBook),
    path('message.html', views.message ,name="message"),
    path('compose_message.html', views.compose),
    path('inbox.html', views.inbox,name="inbox"),
    path('more.html', views.more),


    #path('Sample.html',views.login)
    path('library.html', views.pdf,name="library"),
    path('genre/<str:slug>', views.category_detail, name='category_detail'),
    path('book/<str:slug>', views.book_detail, name='book_detail'),

    path('Journal.html', views.journal, name="journal"),
    path('current.html', views.current_book, name="current_book"),
    path('delete/<int:id>', views.delete_book, name="delete_book"),
    # path('current_done.html', views.current_Del, name="done"),edit_wbook
    path('<int:id>/', views.edit_book, name='edit_book'),

    path('want.html', views.want_book, name="want_book"),
    path('delete_wbook/<int:id>', views.delete_wbook, name="delete_wbook"),
    path('edit_wbook/<int:id>/', views.edit_wbook, name="edit_wbook"),

    path('misc.html', views.misc_book, name="misc_book"),
    path('delete_mbook/<int:id>', views.delete_mbook, name="delete_mbook"),

    path('delete/<int:id>', views.pick, name="pick"),
    path('suggetion.html', PostListView.as_view(), name='postlist'),
    
]