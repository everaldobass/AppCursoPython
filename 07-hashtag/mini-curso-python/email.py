
import smtplib
# e-mail remetente
email_from = "e-mail@gmail.com"
# e-mail de destino
email_to = "e-mail@gmail.com"

smtp = "smtp.gmail.com"

server = smtplib.SMTP(smtp, 587)
server.starttls()
server.login(email_from, open('senha.txt').read().strip())

msg = ''''
      
    e-mail de teste com python3!

'''

server.sendmail(email_from, email_to, msg)
server.quit()

print("Sucesso ao enviar o email")
