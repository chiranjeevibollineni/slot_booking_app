from django.shortcuts import render, redirect

def login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        # For demo purpose — static check (remove later when DB added)
        if username == "admin" and password == "admin":
            return redirect('/slotBook')  # redirect to slot booking page
        else:
            return render(request, 'login_page.html', {"error": "Invalid credentials"})

    return render(request, 'login_page.html')

def home(request):
    return render(request, 'home.html')

#slot book
def slot_book(request):

    return render(request, 'slotbook.html')



