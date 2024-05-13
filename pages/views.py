from django.shortcuts import render
from pages.models import Entry
from pages.process_functions import convert_text_to_link


def home(request):
    return render(request, "pages/home.html", {})


def text_entry(request):
    return render(request, "pages/text_entry.html", {})


def get_link(request):
    link = ''
    if request.method == 'POST':
        link = convert_text_to_link(request.POST['data'], request.environ['HTTP_HOST'])
        print("link = ", link)
    return render(request, "pages/get_link.html", {'link': link})


def get_text(request):
    db_id = '0_0'
    text_display = ''
    if request.method == "GET":
        db_id = request.GET['db_id']
        text = [e.text for e in Entry.objects.raw(f"SELECT * FROM pages_entry WHERE db_id = '{db_id}'")]
        if len(text) != 0:
            text_display = text[0]

    args = {'text_display': text_display, 'db_id': db_id}
    return render(request, "pages/get_text.html", args)


def delete_link(request):
    print(request)