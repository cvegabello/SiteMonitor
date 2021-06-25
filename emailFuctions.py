# modules
from email import message
import smtplib
from email.message import EmailMessage

# def send_email_bodyHtml_externalHTMLFile(host, sender, receiver, subject, body_html, attachedsFileName) -> None:
#     msg = EmailMessage()
#     msg['from'] = sender
#     msg['to'] = receiver
#     msg['subject'] = subject
#     html_body = open(body_html).read()
#     msg.add_alternative(html_body, subtype='html')
#     for attachedFileName in attachedsFileName:
#         with open(attachedFileName, 'rb') as content_file:
#             content = content_file.read()
#             msg.add_attachment(content, maintype='application', subtype='html', filename = attachedFileName)
#     with smtplib.SMTP(host)as smtp:
#         smtp.send_message(msg)
#         smtp.quit
    
def send_email_bodyHtml_externalHTMLFile(host, sender, receiver, subject, body_html, attachedsFileName) -> None:
    try:
        msg = EmailMessage()
        msg['from'] = sender
        msg['to'] = receiver
        msg['subject'] = subject
        html_body = open(body_html).read()
        msg.add_alternative(html_body, subtype='html')
        for attachedFileName in attachedsFileName:
            with open(attachedFileName, 'rb') as content_file:
                content = content_file.read()
                msg.add_attachment(content, maintype='application', subtype='html', filename = attachedFileName)
        if host != '156.24.14.132':
            with smtplib.SMTP(host, 587) as smtp:
                smtp.starttls()
                smtp.login(sender, 'Alej@ndr01234') #my gmail account
                smtp.send_message(msg)
                smtp.quit
        else:
            with smtplib.SMTP(host) as smtp:
                smtp.send_message(msg)
                smtp.quit

    except Exception as e:
        print("Error: {}".format(e.args))



def send_email_bodyHtml(host, sender, receiver, subject, body_html, attachedsFileName) -> None:
    msg = EmailMessage()
    msg['from'] = sender
    msg['to'] = receiver
    msg['subject'] = subject
    msg.add_alternative(body_html, subtype='html')
    for attachedFileName in attachedsFileName:
        with open(attachedFileName, 'rb') as content_file:
            content = content_file.read()
            msg.add_attachment(content, maintype='application', subtype='', filename = attachedFileName)
    with smtplib.SMTP(host)as smtp:
        smtp.send_message(msg)
        smtp.quit


def send_email_bodyText(host, sender, receiver, subject, bodyText, attachedsFileName) -> None:
    msg = EmailMessage()
    msg['from'] = sender
    msg['to'] = receiver
    msg['subject'] = subject
    msg.set_content(bodyText)
    for attachedFileName in attachedsFileName:
        with open(attachedFileName, 'rb') as content_file:
            content = content_file.read()
            msg.add_attachment(content, maintype='application', subtype='', filename = attachedFileName)
    with smtplib.SMTP(host)as smtp:
        smtp.send_message(msg)
        smtp.quit

def send_email_fromGmail(host, sender, receiver, subject, bodyText) -> None:

    try:
        messageStr = bodyText
        subjectStr = subject
        messageStr = 'Subject: {}\n\n{}'.format(subjectStr, messageStr)
        server = smtplib.SMTP(host, 587)
        server.starttls()
        server.login(sender, 'Alej@ndr01234')
        server.sendmail(sender, receiver, messageStr)
    except Exception as e:
        print("Error: {}".format(e.args))
    finally:
        server.quit()

def send_email_fromGmail2(host, sender, receiver, subject, body_html, attachedsFileName) -> None:
    try:
        msg = EmailMessage()
        msg['from'] = sender
        msg['to'] = receiver
        msg['subject'] = subject
        html_body = open(body_html).read()
        msg.add_alternative(html_body, subtype='html')
        for attachedFileName in attachedsFileName:
            with open(attachedFileName, 'rb') as content_file:
                content = content_file.read()
                msg.add_attachment(content, maintype='application', subtype='html', filename = attachedFileName)
        with smtplib.SMTP(host, 587) as smtp:
            smtp.starttls()
            smtp.login(sender, 'Alej@ndr01234')
            smtp.send_message(msg)
            smtp.quit
    except Exception as e:
        print("Error: {}".format(e.args))
    
    





# # content
# sender = "do.not.reply@igt-noreply.com"
# reciever = "carlos.vegabello@igt.com"
# #msg_body = "You are Fired!!"


# # action
# msg = EmailMessage()
# msg['subject'] = 'Email using Python'   
# msg['from'] = sender
# msg['to'] = reciever
# #msg.set_content(html_body)
# html_message = open("test_email_html.html").read()
# msg.add_alternative(html_message, subtype='html')

# attachedsFileName = ["pexels-pixabay-270360.jpg"]

# for attachedFileName in attachedsFileName:
#     with open(attachedFileName, 'rb') as content_file:
#         content = content_file.read()
#         msg.add_attachment(content, maintype='application', subtype='', filename = attachedFileName)


# with smtplib.SMTP("156.24.14.132")as smtp:
#     smtp.send_message(msg)
#     smtp.quit