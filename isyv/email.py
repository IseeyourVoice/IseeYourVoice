from django.core.mail import send_mail

import config.settings


def email(request):
    subject = 'AI 보이스 학습 완료'
    message = '학습이 완료되었습니다.'
    email_from = config.settings.EMAIL_HOST_USER
    recipient_list = '받는 사람 이메일'
    send_mail(subject, message, email_from, recipient_list)
