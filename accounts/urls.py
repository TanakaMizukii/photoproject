from django.urls import path 
from . import views

from django.contrib.auth import views as auth_viws
# URLパターンを逆引きできるように名前をつける
app_name = 'accounts'

# URLパターンを登録する変数
urlpatterns = [
    # http(s)://<ホスト名>/signup_success/へのアクセスはviewsモジュールのSignUpViweを実行
    path('signup/', views.SignUpView.as_view(), name='signup'),

    # サインアップ完了ページのビューの呼び出し
    path('signup_success/', views.SignUpSuccessView.as_view(), name='signup_success'),

    # ログインページの表示
    path('login/', auth_viws.LoginView.as_view(template_name='login.html'), name='login'),

    # ログアウトを実行
    path('logout/', auth_viws.LogoutView.as_view(template_name='logout.html'), name='logout'),

]