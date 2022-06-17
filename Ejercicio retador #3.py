sacos_cemento=int(input("Numero de sacos de cemento:"))
sacos_yeso=int(input("Numero de sacos de yeso:"))
maximo=3254
peso_cemento_kg=sacos_cemento*40
peso_yeso_kg=sacos_yeso*30
peso_total=peso_cemento_kg+peso_yeso_kg
comparador1=peso_total<maximo
comparador2=peso_total>maximo/2
envio=comparador1 and comparador2
print("El peso total en kilogramos es: ",peso_total)
print("El envio se puede ejecutar: ",envio)

if envio==True:
  print("El envio se puede ejecutar sin problemas")
else:
  print("Lamentablemente el envio no se puede llevar a cabo")
  