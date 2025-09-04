
# Quiz Cálculo del consumo y almacenamiento de agua en un edificio


# Datos a solicitar al usuario:
print("Cálcular el consumo y almacenamiento de agua de un edificio")

cons_persona = float(input("Ingrese el consumo promedio por persona (Litros/día): "))
personas = int(input("Ingrese la cantidad de personas que hay en el edificio: "))
cap_tanque = float(input("Ingrese la capacidad de cada tanque (En litros): "))
eficiencia = float(input("Ingrese la eficiencia del tanque en porcentaje (90% = 0.90): "))
dias_sin_inactividad = int(input("Ingrese los de días de inactividad en el año: "))
area_por_cada_tanque = float(input("Ingrese el área de cada tanque (mt^2) : "))
area_total = float(input("Ingrese el área destinada para los tanques (mt^2) : "))
# Cálculos:
dias_del_año = 365
dias_planificados = dias_del_año + dias_sin_inactividad

# Consumo  diario
cons_total_dia = cons_persona * personas

# Consumo anual
cons_total_anual = cons_total_dia * dias_planificados

# Capacidad efectiva de cada tanque dependiendo de  la eficiencia
cap_efectiva_tanque = cap_tanque * eficiencia

# Cantidad de tanques que se pueden colocar en el área disponible
tanques_por_el_area = area_total / area_por_cada_tanque

# Consumo necesario durante los días sin recolección
consumo_de_las_reservas = cons_total_dia * dias_sin_inactividad


# Capacidad total de los tanque en el área disponible
capacidad_total_del_area = tanques_por_el_area * cap_efectiva_tanque

# Días que se pueden cubrir con las reservas de agua
cobertura_de_dias = capacidad_total_del_area / cons_total_dia

#Resultados obtenidos
print(f" Los calculos son los siguientes: ")
print(f"Consumo total diario es de :", cons_total_dia, "litros")
print(f"Consumo total anual es de:", cons_total_anual, "litros")
print(f"Capacidad efectiva que tiene un  tanque:", cap_efectiva_tanque, "litros")
print(f"Tanques por area:", tanques_por_el_area)
print(f"Capacidad de todos los tanques:", capacidad_total_del_area, "litros")
print(f"Consumo necesario durante", dias_sin_inactividad, "días sin recolección:", consumo_de_las_reservas, "litros")
print(f"Con el área disponible, los tanques pueden cubrir aproximadamente", cobertura_de_dias, "días de consumo.")
