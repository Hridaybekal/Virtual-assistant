import smtplib
import pyttsx3
import main


def send(to, sub, body):
    conn = smtplib.SMTP('smtp.gmail.com', 587)

    conn.ehlo()

    conn.starttls()

    conn.login('5hd5jin2cx@elatter.com', 'botforminiproject')
    
    
    conn.sendmail('5hd5jin2cx@elatter.com', to, 'Subject : ' + sub + '\n\n' + body)

    conn.quit()

    pyttsx3.speak('mail sent successfully')
