from cat.models import Cat
from .models import Main
from subcat.models import SubCat
from news.models import News


def all(request):
    site = Main.objects.get(pk=2)
    news = News.objects.filter(act=1).order_by("-pk")
    cat = Cat.objects.all()
    print(f"****************** Category length{len(cat)}")
    subcat = SubCat.objects.all()
    popnews = News.objects.filter(act=1).order_by("-show")
    popnews2 = News.objects.filter(act=1).order_by("-show")[:3]
    latest_news = News.objects.filter(act=1).order_by("-pk")[:3]
    context = {
        "site": site,
        "news": news,
        "cat": cat,
        "popnews2": popnews2,
        "popnews": popnews,
        "subcat": subcat,
        "latest_news": latest_news,

    }
    return context
