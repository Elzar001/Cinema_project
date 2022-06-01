from django.core.mail import send_mail

from cinema_project.celery import app


@app.task
def send_activation_code(to_email, code):
    full_link = f'http://localhost:8000/api/v1/account/activate/{code}/'
    send_mail('Здравствуйте, активируйте Ваш аккаунт!',
              f'Чтобы активировать Ваш аккаунт'f'нужно перейти по ссылке: {full_link}',
              'example@gmail.com', [to_email], fail_silently=False)
