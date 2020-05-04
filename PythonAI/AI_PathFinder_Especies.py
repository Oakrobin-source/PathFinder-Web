import sys
import organismo
from pymongo import MongoClient

colores = ["Rojo", "Naranja", "Verde_Oscuro", "Verde_Claro", "Amarillo",
          "Azul_Marino", "Cian", "Violeta", "Marron"]
numero_especies: int = 0

# Step 1: Connect to MongoDB - Note: Change connection string as needed
client = MongoClient('localhost', 27017)
db = client.PathFinder

for x in range(sys.argv.__len__()-1):
    numero_especies = x + 1

    # Step 2: Create sample data
    especieMongoDB = {
        'numeroEspecie': x+1,
        'ratioMutacion': float(sys.argv[x+1]),
        'color': colores[x]
    }
    # Step 3: Insert business object directly into MongoDB via isnert_one
    result = db.especies.insert_one(especieMongoDB)

    # Step 4: Print to the console the ObjectID of the new document
    print('Creada especie {0} de {1} as {2}'.format(x, numero_especies, result.inserted_id))

    for i in range(50):
        # Step 2: Create sample data
        organismoMongoDB = {
            'coordX': 0,
            'coordY': 0,
            'angulo': 0,
            'especie': x+1
        }
        # Step 3: Insert business object directly into MongoDB via isnert_one
        result = db.organismos.insert_one(organismoMongoDB)

        # Step 4: Print to the console the ObjectID of the new document
        print('Creado organismo {0} de 50 de la especie {1} as {2}'.format(i+1, numero_especies, result.inserted_id))



#resultado_turno:[int][int] = [range(50) for i in range(numero_especies)]
#resultado_cercano:[float][float] = [range(50) for i in range(numero_especies)]
#resultado_turno2:[float][float] = [range(50) for i in range(numero_especies)]
#top1:[float][float] = [range(numero_especies) for i in range(1000)]
#top2:[float][float] = [range(numero_especies) for i in range(1000)]

#//IntList line[] = new IntList(); //graph line
#ArrayList<IntList> line = new ArrayList<IntList>();
#team leaderboard = new team();
#float top_fitness[] = {0, 0, 0, 0, 0, 0};

#turno: int = 1
#generacion: int = 1;
#muertes: int = 0;
#int div = 0;



