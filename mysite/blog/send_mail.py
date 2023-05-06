from mysite import settings
from django.core.mail import send_mail

class mailsend:
    @staticmethod
    def sendemail(email,token,id):
        subject = "Your Reset Password Link"  
        msg     = f"Click on the link to change password http://127.0.0.1:8000/changePassword/{token}/{id}" 
        to      = str(email)  
        res     = send_mail(subject, msg, settings.EMAIL_HOST_USER, [to])  
        if(res == 1):  
            msg = "Mail Sent Successfuly"  
        else:  
            msg = "Could not send Mail"  
        return msg 

print("hello anubhav gupta")