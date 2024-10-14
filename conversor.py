def convertir_longitud(valor, unidad_origen, unidad_destino):
    conversiones = {
        'metros': 1,
        'kilómetros': 1000,
        'millas': 1609.34,
        'pies': 0.3048
    }
    valor_en_metros = valor * conversiones[unidad_origen]
    return valor_en_metros / conversiones[unidad_destino]


def convertir_masa(valor, unidad_origen, unidad_destino):
    conversiones = {
        'kilogramos': 1,
        'gramos': 0.001,
        'libras': 0.453592,
        'onzas': 0.0283495
    }
    valor_en_kilogramos = valor * conversiones[unidad_origen]
    return valor_en_kilogramos / conversiones[unidad_destino]


def convertir_tiempo(valor, unidad_origen, unidad_destino):
    conversiones = {
        'segundos': 1,
        'minutos': 60,
        'horas': 3600,
        'días': 86400
    }
    valor_en_segundos = valor * conversiones[unidad_origen]
    return valor_en_segundos / conversiones[unidad_destino]


def convertir_intensidad_corriente(valor, unidad_origen, unidad_destino):
    conversiones = {
        'amperios': 1,
        'miliamperios': 0.001,
        'microamperios': 0.000001
    }
    valor_en_amperios = valor * conversiones[unidad_origen]
    return valor_en_amperios / conversiones[unidad_destino]


def convertir_temperatura(valor, unidad_origen, unidad_destino):
    if unidad_origen == 'celsius':
        if unidad_destino == 'kelvin':
            return valor + 273.15
        elif unidad_destino == 'fahrenheit':
            return (valor * 9/5) + 32
        return valor
    elif unidad_origen == 'kelvin':
        if unidad_destino == 'celsius':
            return valor - 273.15
        elif unidad_destino == 'fahrenheit':
            return (valor - 273.15) * 9/5 + 32
        return valor
    elif unidad_origen == 'fahrenheit':
        if unidad_destino == 'celsius':
            return (valor - 32) * 5/9
        elif unidad_destino == 'kelvin':
            return (valor - 32) * 5/9 + 273.15
        return valor


def convertir_cantidad_sustancia(valor, unidad_origen, unidad_destino):
    conversiones = {
        'moles': 1,
        'gramos': 1/0.001  #gramos por mole
    }
    valor_en_moles = valor * conversiones[unidad_origen]
    return valor_en_moles / conversiones[unidad_destino]


def convertir_intensidad_luminosa(valor, unidad_origen, unidad_destino):
    conversiones = {
        'lumens': 1,
        'candelas': 1/4 * 3.14159  #candelas por lumen
    }
    valor_en_lumens = valor * conversiones[unidad_origen]
    return valor_en_lumens / conversiones[unidad_destino]
def main():
    print("Conversor de Magnitudes Físicas")
   
    print("1. Longitud")
    print("2. Masa")
    print("3. Tiempo")
    print("4. Intensidad de Corriente Eléctrica")
    print("5. Temperatura")
    print("6. Cantidad de Sustancia")
    print("7. Intensidad Luminosa")
   
    opcion = int(input("Selecciona la magnitud a convertir (1-7): "))
   
    valor = float(input("Introduce el valor a convertir: "))
   
    if opcion == 1:  # Longitud
        unidad_origen = input("Introduce la unidad de origen (metros, kilómetros, millas, pies): ").strip().lower()
        unidad_destino = input("Introduce la unidad de destino (metros, kilómetros, millas, pies): ").strip().lower()
        resultado = convertir_longitud(valor, unidad_origen, unidad_destino)
   
    elif opcion == 2:  # Masa
        unidad_origen = input("Introduce la unidad de origen (kilogramos, gramos, libras, onzas): ").strip().lower()
        unidad_destino = input("Introduce la unidad de destino (kilogramos, gramos, libras, onzas): ").strip().lower()
        resultado = convertir_masa(valor, unidad_origen, unidad_destino)
   
    elif opcion == 3:  # Tiempo
        unidad_origen = input("Introduce la unidad de origen (segundos, minutos, horas, días): ").strip().lower()
        unidad_destino = input("Introduce la unidad de destino (segundos, minutos, horas, días): ").strip().lower()
        resultado = convertir_tiempo(valor, unidad_origen, unidad_destino)
   
    elif opcion == 4:  # Intensidad de Corriente Eléctrica
        unidad_origen = input("Introduce la unidad de origen (amperios, miliamperios, microamperios): ").strip().lower()
        unidad_destino = input("Introduce la unidad de destino (amperios, miliamperios, microamperios): ").strip().lower()
        resultado = convertir_intensidad_corriente(valor, unidad_origen, unidad_destino)
   
    elif opcion == 5:  # Temperatura
        unidad_origen = input("Introduce la unidad de origen (celsius, kelvin, fh): ").strip().lower()
        unidad_destino = input("Introduce la unidad de destino (celsius, kelvin, fh): ").strip().lower()
        resultado = convertir_temperatura(valor, unidad_origen, unidad_destino)
   
    elif opcion == 6:  # Cantidad de Sustancia
        unidad_origen = input("Introduce la unidad de origen (moles, gramos): ").strip().lower()
        unidad_destino = input("Introduce la unidad de destino (moles, gramos): ").strip().lower()
        resultado = convertir_cantidad_sustancia(valor, unidad_origen, unidad_destino)
   
    elif opcion == 7:  # Intensidad Luminosa
        unidad_origen = input("Introduce la unidad de origen (candelas, lumens): ").strip().lower()
        unidad_destino = input("Introduce la unidad de destino (candelas, lumens): ").strip().lower()
        resultado = convertir_intensidad_luminosa(valor, unidad_origen, unidad_destino)


    else:
        print("Opción no válida.")
        return


    print(f"{valor} en {unidad_origen} son {resultado} en {unidad_destino}.")


if __name__ == "__main__":
    main()


