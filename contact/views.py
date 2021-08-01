from django.shortcuts import render

# add to the top
from contact.forms import ContactForm

# new imports that go at the top of the file
from django.core.mail import EmailMessage
from django.shortcuts import redirect
from django.template.loader import get_template
from django.core.mail import send_mail

# our view
def contact(request):
    form_class = ContactForm

    # new logic!
    if request.method == "POST":
        form = form_class(data=request.POST)

        if form.is_valid():
            first_name = request.POST.get("first_name", "")
            last_name = request.POST.get("last_name", "")
            phone_number = request.POST.get("phone_number", "")
            contact_email = request.POST.get("contact_email", "")
            form_content = request.POST.get("content", "")

            # Email the profile with the
            # contact information
            template = get_template("contact_template.txt")
            context = {
                "first_name": first_name,
                "last_name": last_name,
                "phone_number": phone_number,
                "contact_email": contact_email,
                "form_content": form_content,
            }

            content = template.render(context)

            email = EmailMessage(
                "New contact form submission",
                content,
                "skatexp.org" +'<info@skatexp.org>',
                ['info@skatexp.org'],
                headers = {'Reply-To': contact_email }
            )
            email.send()
            
            return redirect("contact")

    return render(
        request,
        "contact/contact.html",
        {
            "form": form_class,
        },
    )
