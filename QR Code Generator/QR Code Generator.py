import qrcode  # Importa la librería para generar códigos QR

print("=== Generador de QR's ===")  # Muestra un título en consola
data = input("Introduce la frase o la URL para generar el QR: ")  # Solicita al usuario la información para el QR

imagen = qrcode.make(data)  # Genera el código QR con la información proporcionada
imagen.save("QR Code Generator/QR Generados/qr_generado.png")  # Guarda la imagen del QR en la ruta especificada

print("QR generado")  # Informa al usuario que el QR ha sido generado
