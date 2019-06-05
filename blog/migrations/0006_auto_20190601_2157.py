# Generated by Django 2.1.3 on 2019-06-01 13:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_article_tags'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='article',
            options={'verbose_name': '文章', 'verbose_name_plural': '文章'},
        ),
        migrations.AlterModelOptions(
            name='article2tag',
            options={'verbose_name': '文章-标签', 'verbose_name_plural': '文章-标签'},
        ),
        migrations.AlterModelOptions(
            name='articledetail',
            options={'verbose_name': '文章详情', 'verbose_name_plural': '文章详情'},
        ),
        migrations.AlterModelOptions(
            name='articleupdown',
            options={'verbose_name': '文章点赞', 'verbose_name_plural': '文章点赞'},
        ),
        migrations.AlterModelOptions(
            name='blog',
            options={'verbose_name': 'Blog站点', 'verbose_name_plural': 'Blog站点'},
        ),
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': '文章分类', 'verbose_name_plural': '文章分类'},
        ),
        migrations.AlterModelOptions(
            name='comment',
            options={'verbose_name': '文章评论', 'verbose_name_plural': '文章评论'},
        ),
        migrations.AlterModelOptions(
            name='tag',
            options={'verbose_name': '文章标签', 'verbose_name_plural': '文章标签'},
        ),
        migrations.AlterModelOptions(
            name='userinfo',
            options={'verbose_name': '用户', 'verbose_name_plural': '用户'},
        ),
        migrations.AlterField(
            model_name='article',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='blog.Category', verbose_name='所属分类'),
        ),
        migrations.AlterField(
            model_name='article',
            name='desc',
            field=models.CharField(max_length=255, verbose_name='文章描述'),
        ),
        migrations.AlterField(
            model_name='article',
            name='title',
            field=models.CharField(max_length=50, verbose_name='文章标题'),
        ),
        migrations.AlterField(
            model_name='article',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='用户'),
        ),
        migrations.AlterField(
            model_name='blog',
            name='site',
            field=models.CharField(max_length=32, unique=True, verbose_name='个人博客后缀'),
        ),
        migrations.AlterField(
            model_name='blog',
            name='theme',
            field=models.CharField(max_length=32, verbose_name='博客主题'),
        ),
        migrations.AlterField(
            model_name='blog',
            name='title',
            field=models.CharField(max_length=64, verbose_name='个人博客标题'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='parent_comment',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='blog.Comment'),
        ),
    ]
