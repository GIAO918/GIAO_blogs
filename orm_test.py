import os

if __name__ == "__main__":
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'GIAO_blogs.settings')  # 加载当前的django配置，在manage.py里
    import django

    django.setup()  # 导入django模块并启动
    from blog import models
    from django.db.models import Count
    print(models.Article.objects.values("category"))