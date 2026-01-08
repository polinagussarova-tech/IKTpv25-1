import smtplib, ssl
from email.message import EmailMessage

def saada_email(saaja_email):
    teema = "Test kiri Pythonist"
    saatja_email = "polina.gussarova@gmail.com"
    parool = input("Sisesta rakenduse parool: ")

    smtp_server = "smtp.gmail.com"
    port = 587
    context = ssl.create_default_context()

    msg = EmailMessage()
    msg["Subject"] = teema
    msg["From"] = saatja_email
    msg["To"] = saaja_email

    with open(r"C:\Users\opilane\source\repos\penguiiin.jpg", "rb") as f:
        image_data=f.read()
    msg.add_attachment(image_data, maintype="image", subtype="jpg")

    try:
        with smtplib.SMTP(smtp_server, port) as server:
            server.starttls(context=context)
            server.login(saatja_email, parool)
            server.send_message(msg)
        print("E-kiri saadetud!")
    except Exception as e:
        print(f"Midagi läks valesti... {e}")

kellele = input("Sisesta saaja e-posti aadress: ")
saada_email(kellele)

