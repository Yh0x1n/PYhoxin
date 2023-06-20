"""
Programa que simula el sistema de producción y demanda de una panadería,
utilizando el modelo matemático de flujo de producción
"""
#Definimos la clase panadería, y definimos sus respectivas fórmulas.
class Panadería:
    #Tiempo de ciclo
    def form_tc(self, tiempo_total, masa_unidad):
        masa_total = 75000 #gramos
        panes_producidos = masa_total / masa_unidad
        self.tc = tiempo_total / panes_producidos
        return f'El tiempo de ciclo es de {self.tc:.2f} minutos por pan.'

    #Tiempo de ciclo teórico
    def form_tct(self, tiempo_total_disp, panes_necesarios):
        self.tct = tiempo_total_disp / panes_necesarios
        return f'El tiempo de ciclo teórico es de {self.tct:.2f} minutos en condiciones óptimas.'

    #Tiempo de ciclo teórico en la etapa más lenta, se toma el valor más alto
    def form_tctel(self, amasado, fermentado, horneado):
        self.tctel = [amasado, fermentado, horneado]
        if max(self.tctel) == amasado:
            return f'La etapa más lenta es el amasado, tarda {max(self.tctel)} minutos en ser ejecutada.'
        
        elif max(self.tctel) == fermentado:
            return f'La etapa más lenta es el fermentado, tarda {max(self.tctel)} minutos en ser ejecutada.'
        
        elif max(self.tctel) == horneado:
            return f'La etapa más lenta es el horneado, tarda {max(self.tctel)} minutos en ser ejecutada.'

#Se procede a instanciar la clase Panadería y las operaciones principales
panaderia = Panadería()
a = int(input('¿Cuánto tiempo en minutos necesitará la panadería para producir el pan requerido?\n->'))
b = int(input('¿Cuántos panes se deben producir en este tiempo?\n->'))
c = int(input('¿Cuántos gramos de harina debe llevar la masa por cada pan?\n->'))

print("\nRESULTADOS")
print(panaderia.form_tc(300, c))
print(panaderia.form_tct(a, b))
print(panaderia.form_tctel(15, 270, 15))