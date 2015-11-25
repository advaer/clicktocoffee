from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import TemplateView, View

# Create your views here.
from django.core.mail import EmailMultiAlternatives
from django.template.loader import get_template
from django.template import Context


class Index(TemplateView):
    template_name = 'main/index.html'


class SendMail(View):
    template_name = 'main/index.html'

    @staticmethod
    def get():
        return HttpResponseRedirect('/')

    @staticmethod
    def post(request):
        subject = "[feedback] Click to Coffee"
        email = request.POST.get('email')
        name = request.POST.get('name')
        form_message = request.POST.get('message')
        text_content = "Email: "+email+" Name: "+name+" Message: "+form_message
        html_content = get_template('main/email/feedback.html').render(
            Context(
                {
                    'email': email,
                    'name': name,
                    'message': form_message
                }
            )
        )
        from_email = "noreply@clicktocoffee.com"
        to_email = "rinat.advaer@gmail.com"
        headers = {
            'Reply-To': email
        }
        msg = EmailMultiAlternatives(
            subject,
            text_content,
            from_email,
            [to_email],
            headers=headers
        )
        msg.attach_alternative(html_content, "text/html")
        msg.send()
        return HttpResponse(status=200)



