nombre= input ('introduce tu nonombre: ')
print('Hola, {}!'. format(nombre))

edad = 21
altura = 1.60

#convertir a float
edadString = str(edad)

##print(edad+edad)
##print(edadString + edadString)

##print(type(edadString))

tuedad = input('Introduce tu edad: ')
tuedad = int(tuedad)
if tuedad >= 18 and tuedad < 100:
    print('Eres mayor de edad')
elif tuedad >= 100: 
    print('eres un dios')
else:
    print('Eres menor de edad')

for i in range(0, 10):
    print(i)
# Switch
with switch (dia) as s:
    if s.case(15): 
        print('es quincena 😊')