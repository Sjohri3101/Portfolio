from django.shortcuts import render
# Create your views here.

# username = portfolio
# password = 12345


def indexpage(request):
    return render(request,'index.html')

def all_portfolio(request):
    return render(request,'all_portfolio.html')

def employee_portfolio(request):
    return render(request,'employee_portfolio.html')

def display_employee_portfolio(request):
    return render(request,'display_employee_portfolio.html')

def create_portfolio(request):
    return render(request,'create_portfolio.html')