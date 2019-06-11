from django import template
from blog import models
from django.db.models import Count

register = template.Library()  # 注册一个实例对象


@register.inclusion_tag("left_menu.html")
def get_left_menu(user):
    blog = user.blog
    #  查询文章分类和对应文章数
    category_list = models.Category.objects.filter(blog=blog).annotate(a=Count("article"))
    # 查询标签分和对应文章数
    tag_list = models.Tag.objects.filter(blog=blog).annotate(a=Count("article")).filter(a__gt=0)
    # 按照日期分类并算出规定日期内的文章数
    archive_list = models.Article.objects.filter(user=user).extra(
        select={"archive": "date_format(create_time,'%%Y-%%m')"}
    ).values("archive").annotate(c=Count("nid")).values("archive", 'c')

    # 返回获得的值传给页面left_menu
    return {'category_list': category_list,
            "tag_list": tag_list,
            "archive_list": archive_list}
