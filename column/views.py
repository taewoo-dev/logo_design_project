from django.shortcuts import render, redirect

from column.models import Column


# Create your views here.
def column(request):
    column_list = Column.objects.all()
    contents = {"columns": column_list}
    return render(request, "main/column.html", contents)


def column_detail(request, column_id):
    column = Column.objects.get(id=column_id)
    contents = {"column": column}
    return render(request, "main/column_detail.html", contents)


def add_column(request):
    return render(request, "main/add-column.html")


def column_form(request):
    if request.method == "POST":
        print(request.POST)
        title = request.POST["ColumnTitle"]
        content = request.POST["ColumnContents"]
        thumbnail = request.FILES["ColumnThumbnail"]
        Column.objects.create(title=title, content=content, thumbnail=thumbnail)
        print("새로운 칼럼 추가")
    return redirect("column")
