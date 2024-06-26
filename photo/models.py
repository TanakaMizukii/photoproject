from django.db import models

# Create your models here.
from accounts.models import CustomUser

class Category(models.Model):
    '''投稿する写真のカテゴリを管理するモデル'''

    # カテゴリ名のフィールド
    title = models.CharField(
        verbose_name='カテゴリ', # フィールドのタイトル
        max_length=20)
    
    def __str__(self):
        '''オブジェクトを文字列に変換して返す
           Returns(str):カテゴリ名'''
        return self.title
    
class PhotoPost(models.Model):
    '''投稿されたデータを管理するモデル'''

    # CustomUserモデルの(user_id)とPhotoPostモデルを
    # １対多の関係で結びつける
    # CustomUserが親でPhotoPostが子の関係となる
    user = models.ForeignKey(
        CustomUser,
        # フィールドのタイトル
        verbose_name='ユーザー',
        # ユーザーを削除する場合はそのユーザーの投稿データもすべて削除する
        on_delete=models.CASCADE
    )
    # Categoryモデルの(title)とPhotoPostモデルを
    # １対多の関係で結びつける
    # Categoryが親でPhotoPostが子の関係となる
    category = models.ForeignKey(
        Category,
        verbose_name='カテゴリ',
        #カテゴリに関連付けられた投稿データが存在する場合は
        #そのカテゴリを削除できないようにする
        on_delete=models.PROTECT
        )
    # タイトル用のフィールド
    title = models.CharField(
        verbose_name='タイトル',
        max_length=200
        )
    # コメント用フィールド
    comment = models.TextField(
        verbose_name='コメント',
        )
    # イメージのフィールド１
    image1 = models.ImageField(
        verbose_name='イメージ１',
        upload_to='photos'  # MEDIA_ROOT以下のphotosにファイルを保存
        )
    # イメージのフィールド２
    image2 = models.ImageField(
        verbose_name='イメージ２',
        upload_to='photos',
        blank=True,   # フィールド値の設定は必須ではない
        null=True     # データベースにnullが保存されることを許容
        )
    # 投稿日時のフィールド
    posted_at = models.DateTimeField(
        verbose_name='投稿日時',
        auto_now_add=True   # 日時を自動追加
        )
    
    def __str__(self):
        '''オブジェクトを文字列に変換して返す
           Returns(str):投稿記事のタイトル'''
        
        return self.title