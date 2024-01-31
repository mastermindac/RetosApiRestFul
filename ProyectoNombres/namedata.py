import json
from models import Persona
# Clase que nos permite trabajar con los datos de prueba
class NameData:

    #Propiedades que almacenarán todos los datos
    personas=[]
    filePersonas = None

    def __init__(self):
        #Carga de los ficheros de datos de prueba
        self.filePersonas=open('personas.json')
        self.personas = json.load(self.filePersonas)
        self.filePersonas.close()

#PERSONAS


        # Recibimos y guardamos una nueva persona
    async def write_persona(self, persona: Persona):
        self.filePersonas=open('personas.json','w')
        #Conseguimos el último id de la lista
        ultima_persona=self.alimentos['personas'][-1]['id']
        #Añadimos un nuevo id a la persona
        personaDict=persona.model_dump()
        personaDict['id']=ultima_persona+1
        self.personas['personas'].append(personaDict)
        json.dump(self.personas,self.filePersonas,indent=2)
        self.filePersonas.close()
        return personaDict

    

    # Recibimos y actualizamos una nueva persona
    async def update_persona(self, persona_id: int, persona: Persona):
        self.filePersonas=open('personas.json','w')
        self.personas = json.load(self.filePersonas)
        #Buscamos la persona
        personaEncontrado=None
        personaPos=0
        #Recorremos todos los datos JSON
        for item in self.personas['personas']:
            #Comparamos el id que es int
            if item['id']==persona_id:
                personaEncontrado=item
                break
            personaPos=personaPos+1
        #Si se ha encontrado
        if(personaEncontrado):
            #Realizamos la actualization
            personaDict = persona.model_dump()
            for elem in personaDict:
                #cambiamos el valor
                self.personas['personas'][personaPos][elem]=personaDict[elem]
            json.dump(self.personas,self.filePersonas,indent=2)
            self.filePersonas.close()
            return self.personas['personas'][personaPos]
        else:
            return None
