from django.core.mail import send_mail
class UsefullFunction:

    def send_email(message,sender,reciever):
        subject = 'Test Email'
        message = message
        from_email = sender
        recipient_list = [reciever]

        send_mail(subject, message, from_email, recipient_list)