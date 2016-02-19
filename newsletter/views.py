from django.shortcuts import render
from .forms import SignUpForm, ContactForm
from django.core.mail import send_mail
from django.conf import settings
from .models import SignUp

# Create your views here.
def home(request):
    title = "Sign-Up Now"
    form = SignUpForm(request.POST or None)

    context = {
        "title": title,
        "form": form
    }

    if form.is_valid():
        instance = form.save(commit=False)
        full_name = form.cleaned_data.get("full_name")

        if not full_name:
            full_name = "new full name"
            instance.full_name = full_name

        instance.save()  # if not instance.full_name:
        # instance.full_name = 'Dummy'
        context = {
            "title": "Thank you"
        }


    if request.user.is_authenticated() and request.user.is_staff:
        # i = 1
        # for instance in SignUp.objects.all():
        #     print i, instance, instance.full_name
        #     i += 1

        queryset = SignUp.objects.all().order_by('-timestamp').filter(full_name__icontains='r')
        context = {

            "queryset": queryset
        }

    return (render(request, "home.html", context))


def contact(request):
    title = 'Contact Us'
    title_align_center = True
    form = ContactForm(request.POST or None)
    if form.is_valid():
        # for key, value in form.cleaned_data.iteritems():
        # 		print key, value
        form_email = form.cleaned_data.get("email")
        form_message = form.cleaned_data.get("message")
        form_full_name = form.cleaned_data.get("full_name")
        # print email, message, full_name

        subject = 'Site contact form'
        from_email = settings.EMAIL_HOST_USER
        to_email = [from_email, 'ros@ncryptedcloud.com']

        contact_message = "%s: %s via %s" % (
            form_full_name,
            form_message,
            to_email)

        send_mail(subject,
                  contact_message,
                  from_email,
                  to_email,
                  fail_silently=False)

    context = {
        "form": form,
        "title": title,
        "title_align_center": title_align_center,

    }

    return render(request, "forms.html", context)









	