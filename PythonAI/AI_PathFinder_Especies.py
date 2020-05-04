import math
import sys
import organismo
from pymongo import MongoClient

def copiar_genoma(genoma_antiguo: float):
    genoma_nuevo: [float] = [float] * 1000

    for i in range(1000):
        genoma_nuevo[i] = genoma_antiguo[i]

    return genoma_nuevo

def move():
    global turno
    global generacion
    global muertes

    if turno == 1:
        print("-----Generation: " + generacion + "-----")

    if turno == 200:
        # leaderboard.reset_new_score()

    # POSITION UPDATES
    for t in range(numero_especies): # Numero de especies
        especieResult = especieMongoDB.find_one({"numeroEspecie": t + 1})
        for g in range(50): # Numero de organismos
            organismoResult = organismoMongoDB.find_one({"especie": t+1,"numero_miembro": g+1})

            organismoAux: organismo = organismo(organismoResult["coordX"],
                                                organismoResult["coordY"],
                                                organismoResult["angulo"],
                                                organismoResult["genoma"],
                                                organismoResult["estado"],
                                                organismoResult["especie"],
                                                organismoResult["numero_miembro"],
                                                especieResult["ratioMutacion"],
                                                especieResult["color"])

            if organismoAux.estado == 0:
                organismoAux.mover(turno-1)

                posXMeta: int = 0
                posYMeta: int = 0

                distancia:float = 0
                distancia = math.hypot(posXMeta - organismoAux.posX, posYMeta - organismoAux.posY)
                if distancia < resultado_cercano[g][t]:
                    resultado_cercano[g][t]=distancia

                if organismoAux.posX > 800 or organismoAux.posY < 3 or organismoAux.posY > 494 or organismoAux.posY < 3 or esObstaculo(organismoAux.posX, organismoAux.posY):
                    organismoAux.set_state(-1)
                    muertes = muertes + 1
                    resultado_turno[g][t] = turno
                else:
                    if esMeta(organismoAux.posX, organismoAux.posY):
                        organismoAux.set_state(1)
                        resultado_turno[g][t] = turno
                        muertes = muertes + 1
                        print("goal in turn: " + turno)

    # DRAW ORGANISMS - SE HACE EN ANGULAR

    # draw - LEADERBOARD
    # data
    # fill(0);
    # noStroke();
    # textSize(22);
    # text("Generation: " + gen, 810, 30);
    # // text("Fitness: " + top_fitness, 810, 60);
    # text("Time Left: " + (1000 - turn), 810, 60);
    # text("Alive: " + (300 - deads), 810, 90);
    # text("--Leaderboard--", 810, 140);
    # for (int t=0; t < 6; t++)
    # {
    #     fill(0);
    # text("#" + (t + 1), 810, (180 + t * 30));
    # switch(t)
    # {
    # case
    # 0:
    # fill(  # CBCBCB); stroke(#CBCBCB); break;
    #     case
    # 1:
    # fill(  # FFEB08); stroke(#FFEB08); break;
    #     case
    # 2:
    # fill(  # 0DD300); stroke(#0DD300); break;
    #     case
    # 3:
    # fill(  # 0060E3); stroke(#0060E3);break;
    #     case
    # 4:
    # fill(  # C100ED); stroke(#C100ED); break;
    #     case
    # 5:
    # fill(
    # # FF0808); stroke(#FF0808); break;
    # }
    # text(leaderboard.get_name(t), 850, (180 + leaderboard.get_position(t) * 30));
    # noFill();
    # // draw
    # graph
    # beginShape();
    # if (gen > 3)
    # {
    #     div = 1000 / (line.get(t).size() - 1);
    # curveVertex(-div, 650 - ((line.get(t).get(0) - 1600) / 5));
    # for (int j = 0; j < line.get(t).size();
    # j + +)
    # {
    #     curveVertex(div * (j), 650 - ((line.get(t).get(j) - 1600) / 5));
    # }
    # curveVertex(1000 + div, 650 - ((line.get(t).get(line.get(t).size() - 1) - 1600) / 5));
    # endShape();
    # }
    #
    # if (leaderboard.get_new_state(t))
    # fill(  # FA0000);
    # else
    # fill(0);
    # text(int(top2_score[0][t]), 930, (180+leaderboard.get_position(t) * 30));
    # }
    #
    # stroke(0);

    # check if last turn
    if turno == 999 or muertes == 300:
        for t in range(numero_especies):  # Numero de especies
            for j in range(50):  # Numero de organismos

                organismoResult = organismoMongoDB.find_one({"especie": t + 1, "numero_miembro": j + 1})

                organismoAux: organismo = organismo(organismoResult["coordX"],
                                                    organismoResult["coordY"],
                                                    organismoResult["angulo"],
                                                    organismoResult["genoma"],
                                                    organismoResult["estado"],
                                                    organismoResult["especie"],
                                                    organismoResult["numero_miembro"],
                                                    especieResult["ratioMutacion"],
                                                    especieResult["color"])

                resultado: float
                distancia_final = math.hypot(posXMeta - organismoAux.posX, posYMeta - organismoAux.posY)
                if organismoAux.estado == 1:
                    resultado = 1 * (1500-distancia_final)+0.5 * (1500-distancia_final)+1 * (1000-resultado_turno[j][t])+0.3 * (1000-resultado_turno[j][t])
                else:
                    resultado = 1 * (1500-distancia_final)+0.5 * (1500-resultado_cercano[j][t])+1 * (1000-1000)+0.3 * (1000-resultado_turno[j][t])

                print(j + "-" + resultado + " (best:" + resultado_turno2[0][t])

                if resultado > resultado_turno2[0][t]: # 1st
                    resultado_turno2[1][t]=resultado_turno2[0][t];
                    top2[t]=copiar_genoma(top1[t])
                    resultado_turno2[0][t]=resultado
                    top1[t]=copiar_genoma(organismoAux.genoma)
                    # leaderboard.set_new_true(t);
                else:
                    if resultado > resultado_turno2[1][t] and j != 0: # 2nd
                        resultado_turno2[1][t]=resultado
                        top2[t]=copiar_genoma(organismoAux.genoma)

            # update graph
            # line.get(t).append((int(top2_score[0][t])));
            #
            # top_fitness=top2_score[0];
            # leaderboard.reset();
            # for (int x=0; x < 6; x++)
            # leaderboard.update(top2_score[0][x], x);

            # nuevo genoma
            for j in range(50):

                organismoResult = organismoMongoDB.find_one({"especie": t + 1, "numero_miembro": j + 1})

                organismoAux: organismo = organismo(organismoResult["coordX"],
                                                    organismoResult["coordY"],
                                                    organismoResult["angulo"],
                                                    organismoResult["genoma"],
                                                    organismoResult["estado"],
                                                    organismoResult["especie"],
                                                    organismoResult["numero_miembro"],
                                                    especieResult["ratioMutacion"],
                                                    especieResult["color"])

                organismoAux.hijo(top1[t], top2[t])

                #Guardar todos los hijos modificados

                # top2_score[0]=0;
                # top2_score[1]=0;
                organismoAux.reset();
                resultado_turno[j][t]=1000;
                resultado_cercano[j][t]=1500;

        # reset things
        turno=0
        muertes = 0
        generacion = generacion + 1


        #Evennto de refresco para Angular

    print("top1 score: " + resultado_turno2[0])
    print("top2 score: " + resultado_turno2[1])

    turno = turno + 1



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
    # print('Creada especie {0} de {1} as {2}'.format(x, numero_especies, result.inserted_id))

    for i in range(50):
        # Step 2: Create sample data
        organismoMongoDB = {
            'coordX': 0,
            'coordY': 0,
            'angulo': 0,
            'especie': x+1,
            'numero_miembro': i+1,
            'estado': 0
        }
        # Step 3: Insert business object directly into MongoDB via isnert_one
        result = db.organismos.insert_one(organismoMongoDB)

        # Step 4: Print to the console the ObjectID of the new document
        # print('Creado organismo {0} de 50 de la especie {1} as {2}'.format(i+1, numero_especies, result.inserted_id))

# Proceso finalizado OK
print('Proceso finalizado OK')

resultado_turno: [int][int] = [range(50) for i in range(numero_especies)]
resultado_cercano: [float][float] = [range(50) for i in range(numero_especies)]
resultado_turno2: [float][float] = [range(50) for i in range(numero_especies)]
top1: [float][float] = [range(numero_especies) for i in range(1000)]
top2: [float][float] = [range(numero_especies) for i in range(1000)]

# ArrayList<IntList> line = new ArrayList<IntList>();
# team leaderboard = new team();
# float top_fitness[] = {0, 0, 0, 0, 0, 0};
turno:int = 1
generacion: int = 1
muertes: int = 0
# int div = 0;

#setup
# size(1000, 650);
for t in range(numero_especies): # Numero Especies
    # line.add(new IntList());
    resultado_turno2[0][t] = 0
    resultado_turno2[1][t] = 0
    for i in range(50):  # Numero organismos
      # generation[i][t]= new organism();
      # generation[i][t].random_genome();
      resultado_turno[i][t] = 1000
      resultado_cercano[i][t] = 1500


# Cargar Mapa

#if (turno < 1000):  # MAPA

    # background(150);
    # noFill();
    # rect(3, 3, 800, 494);
    #
    # # draw obstacles
    # fill(  # 4D4C4B);
    #
    #     ellipse(180, 250, 30, 110);
    # ellipse(220, 100, 30, 200);
    # ellipse(220, 400, 30, 200);
    # triangle(250, 247, 350, 247, 350, 150);
    # triangle(250, 253, 350, 253, 350, 350);
    # triangle(250 + 111, 250 + 160, 350 + 111, 150 + 160, 350 + 111, 350 + 160);
    # triangle(250 + 111, 250 - 160, 350 + 111, 150 - 160, 350 + 111, 350 - 160);
    # ellipse(420, 250, 70, 70);
    # rect(500, 225, 200, 50);
    # triangle(530, 220, 735, 250 - 120, 700, 220);
    # triangle(530, 280, 735, 250 + 120, 700, 280);
    # ellipse(420 + 140, 250 - 170, 80, 80);
    # ellipse(420 + 140, 250 + 170, 80, 80);
    # fill(150);
    #
    # noStroke();
    # fill(  # FCBA00);
    #     ellipse(760, 250, 20, 20);
    # stroke(0);

move()