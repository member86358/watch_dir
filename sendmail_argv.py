import os
import smtplib
import sys
import bcrypt

realpw = sys.argv[4]
hashpw = b'$2b$12$CEzvwiZ.2OqVa7bOfBEIFuL4hrRpYNZ//z4zpqI003xC1o.165OS.'
def Auth():

    if bcrypt.checkpw(realpw.encode('UTF-8'), hashpw):
        print(True)
        return True
    else:
        print(False)
        return False

if Auth():
    EMAIL_PASSWORD = realpw
    EMAIL_ADDRESS = 'ragnarssondavid@gmail.com'

    def sendmail(subject, body):
        with smtplib.SMTP('smtp.gmail.com',587) as smtp:
            smtp.ehlo()
            smtp.starttls()
            smtp.ehlo()
            smtp.login(EMAIL_ADDRESS,EMAIL_PASSWORD)
            msg = f'subject: {subject}\n\n{body}'
            smtp.sendmail(EMAIL_ADDRESS, 'ragnarssondavid@gmail.com', msg)

    message = '{0}, {1}, {2}'.format(sys.argv[1], sys.argv[2], sys.argv[3])
    sendmail('Watch Dir',message)


