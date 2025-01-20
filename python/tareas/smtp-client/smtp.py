import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders


def enviarCorreo(nombreDestinatario:str,emailDestinatario:str) -> None:

    textoPlano = f"""Hola {nombreDestinatario}, te adjunto el archivo solicitado. Saludos PGV.s.l."""
    textoHtml = f"""
    <html>
        <body>
            <h2>Hola {nombreDestinatario}, te adjunto el archivo solicitado. Saludos PGV.s.l.</h2>        
        </body>
    </html>"""

    enviado_por = 'josefbueno@gmx.es'
    password = 'Jose987456.'
    to = emailDestinatario

    mensaje = MIMEMultipart()
    mensaje['From'] = enviado_por
    mensaje['To'] = to
    mensaje['Subject'] = f'Correo para {nombreDestinatario}'  

    mensaje.attach(MIMEText(textoPlano,'plain'))
    mensaje.attach(MIMEText(textoHtml,'html'))

    archivos = ["documento.pdf","foto.png"]

    for archivo in archivos:
        with open(archivo,'rb') as fichero:
            mime_base = MIMEBase('application','octet-stream')
            mime_base.set_payload(fichero.read())
            encoders.encode_base64(mime_base)
            mime_base.add_header('Content-Disposition',f'attachment; filename={archivo}')
            mensaje.attach(mime_base)

    try:
        servidor = smtplib.SMTP('mail.gmx.es',587)
        servidor.starttls()
        servidor.login(enviado_por,password)
        servidor.sendmail(enviado_por,to,mensaje.as_string())
        servidor.quit()
        print("Correo enviado con exito!")
    except Exception as error:
        print(f"Error al enviar el corre: {error}")

enviarCorreo("Angel","alice8@gmx.es")