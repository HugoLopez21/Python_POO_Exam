# Hugo López Valladares 20/10/2025


from abc import abstractmethod
import random
class Animal:
    def __init__(self, vivo=None, peso=None, especie=None, piel=None):
        self.vivo = vivo
        self.__peso = peso # USO DE Encapsulamiento
        self.especie = especie
        self._piel = piel # USO DE Encapsulamiento

    @abstractmethod # uso de abstraccion
    def hablar(self):
        pass

    @abstractmethod
    def reproducirse(self):
        pass


    #Getter, setters y deleters de PESO USO DE Encapsulamiento
    @property
    def peso(self):
        return self.__peso
    
    @peso.setter
    def peso(self, valor):
        if valor > 0:
            self.__peso = valor
        else:
            raise ValueError('No se puede poner peso negativo')

    @peso.deleter
    def peso(self):
        del self.__peso

    #clase creada por mi para mostrar la informacion del animal
    def animal_info(self):
        if self.vivo:
            self.hablar()
            print(f'''
            - especie: {self.especie}
            - estado: {self.vivo}
            - peso: {self.peso}
            ''')
        else:
            print(f'''
            - especie: {self.especie}
            - estado: {self.vivo}
            - peso: {self.peso}
            ''')

class Mamifero(Animal):
    def __init__(self, vivo=None, peso=None, especie=None, piel='Pelo'):
        super().__init__(vivo, peso, especie, piel)

    def hablar(self):
        pass

    def reproducirse(self):
        return 'Tengo crías!'



class Reptil(Animal):
    def __init__(self, vivo=None, peso=None, especie=None, piel='Escamas'):
        super().__init__(vivo, peso, especie, piel)

    def hablar(self):
        pass
    def reproducirse(self):
        return 'Pongo huevos!'

class Depredador:
    def __init__(self):
        pass
    #Sonido al atacar
    def hablar(self):
        return 'ÑAM ÑAM ÑAM'

class Presa:
    def __init__(self):
        pass

    #Sonido al ser atacado
    def hablar(self):
        return 'NO PORFAVOR!'

class Leon(Mamifero, Depredador):
    def __init__(self, vivo=None, peso=None, especie=None, piel='Pelo'):
        super().__init__(vivo, peso, especie, piel)

    def hablar(self):
        print('*Rugido de León*')

    # Si el animal es presa o depredador tendra un metodo 
    # que devuelve la manera de hablar de la clase padre
    def hablar_depredador(self):
        return Depredador().hablar()

    

class Bufalo(Mamifero,Presa):
    def __init__(self, vivo=None, peso=None, especie=None, piel='Pelo'):
        super().__init__(vivo, peso, especie, piel)
    
    def hablar(self):
        print('*Sonido de bufalo*')

    def hablar_presa(self):
        return Presa().hablar()

class Cocodrilo(Reptil,Depredador):
    def __init__(self, vivo=None, peso=None, especie=None, piel='Escamas'):
        super().__init__(vivo, peso, especie, piel)

    def hablar(self):
        print('*Bufido de reptil*')
    
    def hablar_depredador(self):
        return Depredador().hablar()

class Manada:
    def __init__(self, grupo=None):
        self.grupo = grupo
        self.manada = []
    
    def reproduccion(self, especie=None):
        ''' Recibe la especie como str y según cual sea, genera un animal de esa especie tantas veces como la cantidad (random) se 
            haya decidido
            Despues se añade el animal a la lista manada
        '''
        print('------------ REPRODUCCIÓN MANADA ------------')
        cantidad=random.randint(4,15)
        for i in range(cantidad):
            if especie == 'Leones':
                self.manada.append(Leon(vivo=True, peso=random.randint(1,250), especie='Leon', piel='Pelo'))
            elif especie == 'Bufalos':
                self.manada.append(Bufalo(vivo=True, peso=random.randint(1,400), especie='Bufalo', piel='Pelo'))
            # Polimorfismo una misma funcion imprime de manera distinta
            elif especie == 'Cocodrilos':
                self.manada.append(Cocodrilo(vivo=True, peso=random.randint(1,500), especie='Cocodrilo', piel='Escamas'))
        
        print(self.manada[0].reproducirse())
        print(f'La manada es de {especie} y hay {cantidad} animales')

    def ordena_manada(self):
        #Funcion lambda con sorted para ordenar la manada por el peso (De menor a mayor)
        self.manada = sorted( self.manada, key=lambda x: x.peso)

class Sabana:
    def __init__(self,manadas=None):
        self.manadas = manadas
        
        # Genero dos listas que van a almacenar los animales vivos y muertos
        self.animales_muertos = []
        self.animales_vivos = []

    def caceria(self, despiadada):

        
        manada_presa = None
        manada_depredador = None
        
        #Este bucle recorre la lista de  las 2 manadas de la sabana y separa
        # a los depredadores de las presas 
        for manada in self.manadas:
            # Accedo al primer anima de la manada y se comprueba de que tipo es
            if isinstance(manada.manada[0], Depredador):
                manada_depredador = manada
                
            elif isinstance(manada.manada[0], Presa):
                manada_presa = manada
        

        
        #1. Comprueba si la caceria es despiadada, si lo es, pone a los depredadores mas pesados primero
        #   y ordeno a los depredadores de mayor a menor dando la vuelta a la lista
        #2. Con zip creamos una lista donde estarán todos los animales que pelan emparejados los demas no participan
        ganadores = []
    
        if despiadada:
            print('----------- CACERÍA DESPIADADA -----------')
            #ordena cada manada de menor a mayor
            manada_presa.ordena_manada()
            manada_depredador.ordena_manada()
            manada_depredador.manada.reverse()
            batalla = list(zip(manada_depredador.manada, manada_presa.manada))
        else:
            print('----------------- CACERÍA ------------------')
            #La batalla se organiza tal y como se han creado las mandas
            batalla = list(zip(manada_depredador.manada, manada_presa.manada))
        
        print('----------- COMIENZA LA BATALLA -----------')
    
        #3. Bucle que recorre el zip y comprueba que animal es mas pesado
        
        i = 1 #Contador de cada pelea
        for x,y in batalla:
            # x es depredador
            # y es presa
            n_pelea = f'Pelea nº {i}:'
            info_x = f'{type(x).__name__}, peso: {x.peso}'
            info_y = f'{type(y).__name__}, peso: {y.peso}'
            if x.peso > y.peso:
                print(n_pelea)
                print(f'{info_x}, dice: {x.hablar_depredador()}. VS {info_y} dice: {y.hablar_presa()}.')
                print(f'Gana el {info_x}')
                print()

                ganadores.append(x)
                y.vivo = False
            elif x.peso < y.peso:
                print(n_pelea)
                print(f'{info_x}, dice: {x.hablar_depredador()}. VS {info_y} dice: {y.hablar_presa()}.')
                print(f'Gana el {info_y}')
                print()

                ganadores.append(y)
                x.vivo = False
            
            # En caso de empate
            else:
                print(n_pelea)
                print(f'{info_x}, dice: {x.hablar_depredador()}. VS {info_y} dice: {y.hablar_presa()}.')
                aleatorio = random.randint(0,1)
                if aleatorio == 0: 
                    print(f'Gana el {info_x}')
                    ganadores.append(x)
                    y.vivo = False
                else:
                    print(f'Gana el {info_y}')
                    ganadores.append(y)
                    x.vivo = False
                print()
            i +=1
       
            

        

    
    def mostrar_animales(self):
        ''' 
            Recorremos las mandas, dentro de cada manda recorre cada animal y
              comprueba su atributo vivo para añadirlo a su lista correspondiente
        '''
        for manada in self.manadas:
            for animal in manada.manada:
                if animal.vivo :
                    self.animales_vivos.append(animal)
                else: 
                    self.animales_muertos.append(animal)

        #Bucles que muestran la informacion de los animales tanto vivos como muertos
        # Si están vivos vana a halbar
        print('-----------ANIMALES VIVOS----------------')
        for a_vivo in self.animales_vivos:
            a_vivo.animal_info()

        print('-----------ANIMALES MUERTOS----------------')
        for a_muerto in self.animales_muertos:
            a_muerto.animal_info()

                

grupo_leones = Manada('Manada de Leones')
grupo_leones.reproduccion('Leones')




grupo_bufalos = Manada('Manada de bufalos')
grupo_bufalos.reproduccion('Bufalos')


sabana1 = Sabana([grupo_bufalos, grupo_leones])
 


sabana1.caceria(True)
sabana1.mostrar_animales()



