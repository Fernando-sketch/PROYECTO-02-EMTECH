import csv

datos = []


# Extraer los datos del archivo synergy_logistics_database.csv

with open('./synergy_logistics_database.csv', 'r') as archivo:
    lector = csv.DictReader(archivo)
    
    for registro in lector:
        datos.append(registro)


##### Opción 1. Rutas de importación y exportación #####

def contar_direccion_rutas(direccion):
    rutas_contadas = []
    
    for registro in datos:
        if registro['direction'] == direccion:
            ruta_actual = [registro['origin'], registro['destination']]
            
            existe = False
            for ruta_contada in rutas_contadas:
                if ruta_contada[0] == ruta_actual[0] and ruta_contada[1] == ruta_actual[1]:
                    ruta_contada[2] += 1
                    existe = True
                    break
            
            if not existe:
                rutas_contadas.append([ruta_actual[0], ruta_actual[1], 1])

    return rutas_contadas

def mostrar_rutas_mas_demandadas(rutas, cantidad, direccion):
    enum = 0
    
    print(f'\n>>>> LAS {cantidad} RUTAS DE {direccion.upper()} MÁS DEMANDADAS <<<<\n')
    
    for ruta in rutas:
        enum += 1
        print(f'{enum}. origen:{ruta[0]} | destino:{ruta[1]} | operaciones:{ruta[2]}')
        
        if enum >= cantidad:
            break

# rutas_exportaciones = contar_direccion_rutas('Exports')
# rutas_exportaciones.sort(key = lambda x:x[2], reverse = True)
# mostrar_rutas_mas_demandadas(rutas_exportaciones, 10, 'Exportación')

# rutas_importaciones = contar_direccion_rutas('Imports')
# rutas_importaciones.sort(key = lambda x:x[2], reverse = True)
# mostrar_rutas_mas_demandadas(rutas_importaciones, 10, 'Importación')


##### Opción 2. Medio de transporte utilizado #####

def calcular_valor_medios_transporte():
    valor_medios_transporte = []
    
    for registro in datos:
        medio_transporte_actual = registro['transport_mode']
        
        existe = False
        for medio in valor_medios_transporte:
            if medio[0] == medio_transporte_actual:
                medio[1] += int(registro['total_value'])
                existe = True
                break
            
        if not existe:
            valor_medios_transporte.append([medio_transporte_actual, int(registro['total_value'])])
    
    return valor_medios_transporte

def mostrar_medios_transporte(medios_transporte):
    enum = 0
    
    print('\n>>>> MEDIOS DE TRANSPORTE UTILIZADOS <<<<\n')
    
    for medio in medios_transporte:
        enum += 1
        print(f'{enum}. {medio[0]} | Valor Total: {medio[1]}')
    
# medios_transporte = calcular_valor_medios_transporte()
# medios_transporte.sort(key = lambda x:x[1], reverse = True)
# mostrar_medios_transporte(medios_transporte)


##### Opción 3. Valor total de importaciones y exportaciones #####

def calcular_valor_total_paises(direccion):
    valor_total_paises = []
    valor_total = 0
    
    for registro in datos:
        if registro['direction'] == direccion:
            pais_actual = registro['origin']
            valor_actual = int(registro['total_value'])
            
            existe = False
            for pais in valor_total_paises:
                if pais[0] == pais_actual:
                    pais[1] += valor_actual
                    valor_total += valor_actual
                    existe = True
                    break
                
            if not existe:
                valor_total_paises.append([pais_actual, valor_actual])
    
    return valor_total_paises, valor_total

def calcular_porcentaje_paises(valor_total_paises, valor_total):
    porcentaje_paises = []
    
    for pais in valor_total_paises:
        porcentaje = round((pais[1] / valor_total) * 100, 2)
        porcentaje_paises.append([pais[0], porcentaje, pais[1]])
        
    return porcentaje_paises

def mostrar_paises_generan_porcentaje(porcentaje_paises, porcentaje, direccion):
    porcentaje_acumulado = 0
    enum = 0
    
    print(f'\n>>>> PAÍSES QUE GENERAN EL {porcentaje}% DE LAS {direccion.upper()} <<<<\n')
    
    for pais in porcentaje_paises:
        porcentaje_acumulado += pais[1]
        
        enum += 1
        print(f'{enum}. {pais[0]} | Porcentaje: {pais[1]} | Valor Total: {pais[2]}')
        
        if porcentaje_acumulado >= porcentaje:
            break

# valor_total_paises_exportaciones, valor_total_exportaciones = calcular_valor_total_paises('Exports')
# porcentaje_paises_exportaciones = calcular_porcentaje_paises(valor_total_paises_exportaciones, valor_total_exportaciones)
# porcentaje_paises_exportaciones.sort(key = lambda x:x[1], reverse = True)
# mostrar_paises_generan_porcentaje(porcentaje_paises_exportaciones, 80, 'Exportaciones')

# valor_total_paises_importaciones, valor_total_importaciones = calcular_valor_total_paises('Imports')
# porcentaje_paises_importaciones = calcular_porcentaje_paises(valor_total_paises_importaciones, valor_total_importaciones)
# porcentaje_paises_importaciones.sort(key = lambda x:x[1], reverse = True)
# mostrar_paises_generan_porcentaje(porcentaje_paises_importaciones, 80, 'Importaciones')
