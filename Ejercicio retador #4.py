numero_cajas=int(input("Ingresa el numero de cajas: "))
ID=int(input("Ingrese el ID del producto: "))
precio_caja_maiz_grano=285.55
precio_caja_pepino=334.72
precio_caja_tomate_verde=129.0
costo_total=0
if 0<ID<4:
  if ID==1:
    print("El producto es: Maiz grano")
    print("El costo por caja es:$",precio_caja_maiz_grano)
    costo_total=precio_caja_maiz_grano*numero_cajas
    if numero_cajas<=100:
      costo_total+=1500
      print("El costo total con envio incluido es de:$",costo_total)
    else:
      print("El costo total con envio gratuito es de:$",costo_total)
      
  elif ID==2:
    print("El producto es: Pepino")
    print("El costo por caja es:$",precio_caja_pepino)
    costo_total=precio_caja_pepino*numero_cajas
    if numero_cajas<=100:
      costo_total+=1500
      print("El costo total con envio incluido es de:$",costo_total)
    else:
      print("El costo total con envio gratuito es de:$",costo_total)  
  else:
    print("El producto es: Tomate verde")
    print("El costo por caja es:$",precio_caja_tomate_verde)
    costo_total=precio_caja_tomate_verde*numero_cajas
    if numero_cajas<=100:
      costo_total+=1500
      print("El costo total con envio incluido es de:$",costo_total)
    else:
      print("El costo total con envio gratuito es de:$",costo_total)  
else:
  print("Este ID no se encontro en el sistema. Favor de intentar con otro")
    
      
    
  