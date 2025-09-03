from django.shortcuts import render, get_object_or_404, redirect
from .models import Cat
from news.models import News
from main.models import Main
import csv
from django.http import HttpResponse
import xlwt

# Create your views here.


def cat_list(request):

    # login check start
    if not request.user.is_authenticated:
        return redirect("mylogin")
    # login check end

    cat = Cat.objects.all()

    return render(request, "back/cat_list.html", {"cat": cat})


def cat_add(request):

    # login check start
    if not request.user.is_authenticated:
        return redirect("mylogin")
    # login check end

    if request.method == "POST":

        name = request.POST.get("name")

        if name == "":

            error = "All Fields Requirded"
            return render(request, "back/error.html", {"error": error})

        if len(Cat.objects.filter(name=name)) != 0:

            error = "This Name Used Before"
            return render(request, "back/error.html", {"error": error})

        b = Cat(name=name)
        b.save()
        return redirect("cat_list")

    return render(request, "back/cat_add.html")


def export_cat_csv(request):

    response = HttpResponse(content_type="text/csv")
    response["Content-Disposition"] = 'attachment; filename="cat.csv"'

    writer = csv.writer(response)
    writer.writerow(["Title", "Counter"])
    for i in Cat.objects.all():
        writer.writerow([i.name, i.count])

    return response


def import_cat_csv(request):

    if request.method == "POST":

        csv_file = request.FILES["csv_file"]

        if not csv_file.name.endswith(".csv"):
            error = "Please Input Csv File"
            return render(request, "back/error.html", {"error": error})

        if csv_file.multiple_chunks():
            error = "File Too Large"
            return render(request, "back/error.html", {"error": error})

        file_data = csv_file.read().decode("utf-8")

        lines = file_data.split("\n")

        for line in lines:

            fields = line.split(",")

            try:

                if (
                    len(Cat.objects.filter(name=fields[0])) == 0
                    and fields[0] != "Title"
                    and fields[0] != ""
                ):
                    b = Cat(name=fields[0])
                    b.save()

            except:
                print("finish")

    return redirect("cat_list")


from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def category_page(request, category):
    # You can also fetch category-specific news here
    site = Main.objects.get(pk=2)
    print(f"****************** {category} **********************")
    popular_news = News.objects.filter(catname=category).order_by("-id")[:5]
    all_news = News.objects.filter(catname=category).order_by("-id")
    print(f"****************** {len(popular_news)} **********************")
    # Pagination
    paginator = Paginator(all_news, 4)  # 5 news items per page
    page = request.GET.get("page")

    try:
        news_list = paginator.page(page)
    except PageNotAnInteger:
        news_list = paginator.page(1)
    except EmptyPage:
        news_list = paginator.page(paginator.num_pages)
    context = {
        "site": site,
        "category": category,
        "news_list": news_list,  # example if you have a News model
        "popular_news": popular_news,
        "page_obj": news_list,
        "paginator": paginator,
        "is_paginated": news_list.has_other_pages(),
    }
    return render(request, "front/category.html", context)
