# ****** codigo principal ******
from RegistroVehiculos import RegistroVehiculos

objRegistro = RegistroVehiculos()
auxRegistro = objRegistro.iniciar_ventana()
objRegistro.iniciar_preguntas()

auxRegistro.mainloop()
