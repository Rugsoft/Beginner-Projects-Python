import qrcode  # Importa la librería para generar códigos QR

qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)


print("=== Generador de QR's ===")  # Muestra un título en consola
data = input("Introduce la frase o la URL para generar el QR: ")  # Solicita al usuario la información para el QR

qr.add_data(data)
qr.make(fit=True)
