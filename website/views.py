from django.shortcuts import render 

def home(request):
    return render(request, 'website/home.html')

def contact(request):
    return render(request, 'website/contact.html')

def about(request):
    return render(request, 'website/about.html')


from django.core.mail import send_mail
from django.conf import settings

def career(request):
    if request.method == "POST":
        data = request.POST

        message = f"""
Name: {data['name']}
Position: {data['role']}
Expected Salary: {data['expected_salary']}
Email: {data['email']}
Contact: {data['contact']}
Age: {data['age']}
Qualification: {data['qualification']}

Experience:
{data['experience']}
"""

        send_mail(
            subject="New Career Application",
            message=message,
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=["tanaji.screens@gmail.com"],
        )

        return render(request, "website/career.html", {"success": True})

    return render(request, "website/career.html")
