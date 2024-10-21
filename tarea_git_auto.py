import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Configuración del servidor SMTP
smtp_server = "amgmetalmecanica-com.correoseguro.dinaserver.com"
smtp_port = 465  # Puerto para SSL
smtp_user = "n.perez@amgmetalmecanica.com"
smtp_password = "$amgMECNO3"

# Configuración del correo
from_email = smtp_user
to_email = "n.perez@amgmetalmecanica.com"
subject = "Prueba tarea automatizada Git"
body = "Este es un correo enviado desde un script de Python como parte de una tarea automatizada."

# Crear el mensaje
msg = MIMEMultipart()
msg["From"] = from_email
msg["To"] = to_email
msg["Subject"] = subject
msg.attach(MIMEText(body, "plain"))

try:
    # Conectar al servidor SMTP usando SSL
    server = smtplib.SMTP_SSL(smtp_server, smtp_port)  # Usar SMTP_SSL para SSL directo
    server.login(smtp_user, smtp_password)  # Iniciar sesión

    # Enviar el correo
    server.sendmail(from_email, to_email, msg.as_string())
    print(f"Correo enviado a {to_email}")

    # Cerrar la conexión
    server.quit()

except Exception as e:
    print(f"Error al enviar el correo: {e}")
