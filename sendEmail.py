import smtplib

gmail_user = 'nickvrehoretis@gmail.com'
gmail_password = 'n0turn0nred'

sent_from = gmail_user
to = ['6169165724@vtext.com']#'2483184623@vtext.com', 'npv@umich.edu', 'nickvrahoretis@umich.edu']
subject = ''
body = ''

def sendNickAnEmail(emailBody):
    body = emailBody

    email_text = """\
    From: %s
    To: %s
    Subject: %s

    %s
    """ % (sent_from, ", ".join(to), subject, body)

    try:
        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server.ehlo()
        server.login(gmail_user, gmail_password)
        server.sendmail(sent_from, to, email_text)
        server.close()

        print 'Email sent!'
    except:
        print 'Something went wrong...'
