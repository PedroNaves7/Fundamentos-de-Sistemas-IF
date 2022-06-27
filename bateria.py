import psutil

#acesso o sensor da bateria
bateria = psutil.sensors_battery()

#captura/solicito o percentual da bateria
percentual = str(bateria.percent)

#apresenta o nivel
print(f'No momento você tem {percentual}% de bateria')
