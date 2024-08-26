import csv

# Datos de ejemplo para los productos
productos = [
    {"Nombre": "Laptop Lenovo", "Marca": "Lenovo", "Precio Lista": 2500, "Precio Online": 2400, "Precio Oh": 2300},
    {"Nombre": "Smartphone Samsung", "Marca": "Samsung", "Precio Lista": 1200, "Precio Online": 1150, "Precio Oh": 1100},
    {"Nombre": "Tablet Apple", "Marca": "Apple", "Precio Lista": 1800, "Precio Online": 1700, "Precio Oh": 1600},
    {"Nombre": "Televisor LG", "Marca": "LG", "Precio Lista": 1500, "Precio Online": 1450, "Precio Oh": 1400},
    {"Nombre": "Monitor Dell", "Marca": "Dell", "Precio Lista": 800, "Precio Online": 750, "Precio Oh": 720},
    {"Nombre": "Impresora HP", "Marca": "HP", "Precio Lista": 500, "Precio Online": 480, "Precio Oh": 450},
    {"Nombre": "Auriculares Sony", "Marca": "Sony", "Precio Lista": 300, "Precio Online": 290, "Precio Oh": 280},
    {"Nombre": "Cámara Canon", "Marca": "Canon", "Precio Lista": 2200, "Precio Online": 2100, "Precio Oh": 2000},
    {"Nombre": "Consola Xbox", "Marca": "Microsoft", "Precio Lista": 1500, "Precio Online": 1450, "Precio Oh": 1400},
    {"Nombre": "Disco Duro WD", "Marca": "Western Digital", "Precio Lista": 400, "Precio Online": 380, "Precio Oh": 360},
    {"Nombre": "Tarjeta Gráfica Nvidia", "Marca": "Nvidia", "Precio Lista": 3000, "Precio Online": 2900, "Precio Oh": 2800},
    {"Nombre": "Teclado Logitech", "Marca": "Logitech", "Precio Lista": 150, "Precio Online": 140, "Precio Oh": 130},
    {"Nombre": "Mouse Razer", "Marca": "Razer", "Precio Lista": 200, "Precio Online": 190, "Precio Oh": 180},
    {"Nombre": "Altavoces Bose", "Marca": "Bose", "Precio Lista": 1200, "Precio Online": 1150, "Precio Oh": 1100},
    {"Nombre": "Proyector Epson", "Marca": "Epson", "Precio Lista": 1800, "Precio Online": 1700, "Precio Oh": 1600},
    {"Nombre": "Refrigerador Samsung", "Marca": "Samsung", "Precio Lista": 5000, "Precio Online": 4800, "Precio Oh": 4700},
    {"Nombre": "Microondas LG", "Marca": "LG", "Precio Lista": 800, "Precio Online": 750, "Precio Oh": 720},
    {"Nombre": "Licuadora Oster", "Marca": "Oster", "Precio Lista": 300, "Precio Online": 280, "Precio Oh": 260},
    {"Nombre": "Horno Bosch", "Marca": "Bosch", "Precio Lista": 1000, "Precio Online": 950, "Precio Oh": 900},
    {"Nombre": "Aspiradora Dyson", "Marca": "Dyson", "Precio Lista": 2000, "Precio Online": 1900, "Precio Oh": 1800}
]

# Crear el archivo CSV
with open('productos.csv', 'w', newline='', encoding='utf-8') as csvfile:
    fieldnames = ['Nombre', 'Marca', 'Precio Lista', 'Precio Online', 'Precio Oh']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()
    for producto in productos:
        writer.writerow(producto)

print("Archivo CSV creado con éxito.")
