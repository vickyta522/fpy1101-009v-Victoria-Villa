especialistas = 0
residentes = 0

cantidad = int(input("Ingrese la cantidad de medicos:"))

for i in range(cantidad):
    print("\nRegistro medico",i + 1)

    nombre = input("Ingrese nombre profesional:")
    experiencia = int (input("Ingrese años de experiencia clinica:"))

if experiencia > 5:
    print(nombre," Fue clasificado como especialista senior")
    especialistas = especialistas + 1

else:
    print(nombre, "Fue clasificado como residente junior")
    residentes = residentes + 1

print("\n===== Resumen Final =====")
print("Total especialistas senior", especialistas)
print("Total residentes junior:",residentes)
print("Sistema listo para operar.")
