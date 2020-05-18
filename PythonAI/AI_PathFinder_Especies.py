import math
import sys
import random

from organismo import Organismo
from pymongo import MongoClient
from PIL import Image

def copiar_genoma(genoma_antiguo):
    genoma_nuevo = [1] * 1000

    for i in range(1000):

        genoma_nuevo[i] = genoma_antiguo[i]

    return genoma_nuevo


def esMeta(posX, posY):
    global mapa

    rgb_pixel_value = mapa.getpixel((posX, posY))

    # Salida                 rgb(184,61,186)
    # Rojo relleno Salida    rgb(255, 127, 39)
    # Rojo borde Salida      rgb(236, 28, 36)

    # Meta borde             rgb(14,209,69)
    # Meta interior          rgb(196,255,14)
    # Meta                   rgb(0,255,72)

    # Terreno pisable        rgb(185, 242, 240)

    # Gris fuera             rgb(195,195,195)
    # Negro fuera            rgb(0,0,0)

    if rgb_pixel_value == (0,255,72):
        return True
    else:
        return False



def esObstaculo(posX, posY):
    global mapa

    rgb_pixel_value = mapa.getpixel((posX, posY))

    # Salida                 rgb(184,61,186)
    # Rojo relleno Salida    rgb(255, 127, 39)
    # Rojo borde Salida      rgb(236, 28, 36)

    # Meta borde             rgb(14,209,69)
    # Meta interior          rgb(196,255,14)
    # Meta                   rgb(0,255,72)

    # Terreno pisable        rgb(185, 242, 240)

    # Gris fuera             rgb(195,195,195)
    # Negro fuera            rgb(0,0,0)

    if rgb_pixel_value == (195,195,195) or rgb_pixel_value == (0,0,0):
        return True
    else:
        return False


def move():
    global turno
    global generacion
    global muertes
    global SalidaX
    global SalidaY
    global MetaX
    global MetaY

    #  if turno == 1:
    print("-----Generation: " + str(generacion) + "-----")
    print("-----Turno: " + str(turno) + "-----")

    # if turno == 200:
        # leaderboard.reset_new_score()

    # POSITION UPDATES
    for e in range(numero_especies): # Numero de especies
        especieMongoDB = especies.find_one({"numeroEspecie": e + 1})
        for o in range(50): # Numero de organismos
            organismoMongoDB = organismos.find_one({"especie": e+1,"numero_miembro": o+1})

            organismoAux: Organismo = Organismo(organismoMongoDB["coordX"],
                                                organismoMongoDB["coordY"],
                                                organismoMongoDB["angulo"],
                                                organismoMongoDB["genoma"],
                                                organismoMongoDB["estado"],
                                                organismoMongoDB["especie"],
                                                organismoMongoDB["numero_miembro"],
                                                especieMongoDB["ratioMutacion"],
                                                especieMongoDB["color"])

            if organismoAux.estado == 0:
                #print("Mover " + str(organismoAux.especie) + " " + str(organismoAux.numero_miembro))

                organismoAux.mover(turno-1)

                distancia:float = 0
                distancia = math.hypot(MetaX - organismoAux.posX, MetaY - organismoAux.posY)
                if distancia < resultado_cercano[e][o]:
                    resultado_cercano[e][o] = distancia

                # print("Organismo " + str(o) + " de la especie " + str(e) + "-- POS -- (" + str(organismoAux.posX) + "," + str(organismoAux.posY) + ") " + str(organismoAux.angulo))

                if organismoAux.posX > mapa.size[0] or organismoAux.posY > mapa.size[1] or organismoAux.posY < 3 or esObstaculo(organismoAux.posX, organismoAux.posY):
                    organismoAux.estado = -1
                    muertes = muertes + 1
                    resultado_turno[e][o] = turno
                else:
                    if esMeta(organismoAux.posX, organismoAux.posY):
                        organismoAux.set_state(1)
                        resultado_turno[e][o] = turno
                        muertes = muertes + 1
                        print("goal in turn: " + turno)

            # Guardar todos los hijos modificados
            organismos.update_one(
                {"especie": organismoAux.especie, "numero_miembro": organismoAux.numero_miembro},
                {"$set":
                     {"coordX": organismoAux.posX,
                      "coordY": organismoAux.posY,
                      "angulo": organismoAux.angulo,
                      "genoma": organismoAux.genoma,
                      "estado": organismoAux.estado,
                      "especie": organismoAux.especie,
                      "numero_miembro": organismoAux.numero_miembro}
                 })

        # print("Organismos muertos: " + str(muertes) + " de " + str(50 * numero_especies))
        #
        # print("resultado especie: " + str(e+1))
        # print("--- " + str(resultado_turno[e]))
        # print("resultado cercano: " + str(e+1))
        # print("--- " + str(resultado_cercano[e]))

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
    print("Organismos muertos: " + str(muertes) + " de " + str(50 * numero_especies))
    # check if last turn
    if turno == 999 or muertes == (50 * numero_especies):
        for e in range(numero_especies):  # Numero de especies
            especieMongoDB = especies.find_one({"numeroEspecie": e + 1})
            for o in range(50):  # Numero de organismos

                organismoMongoDB = organismos.find_one({"especie": e + 1, "numero_miembro": o + 1})

                organismoAux: Organismo = Organismo(organismoMongoDB["coordX"],
                                                    organismoMongoDB["coordY"],
                                                    organismoMongoDB["angulo"],
                                                    organismoMongoDB["genoma"],
                                                    organismoMongoDB["estado"],
                                                    organismoMongoDB["especie"],
                                                    organismoMongoDB["numero_miembro"],
                                                    especieMongoDB["ratioMutacion"],
                                                    especieMongoDB["color"])

                resultado: float
                distancia_final = math.hypot(SalidaX - organismoAux.posX, SalidaY - organismoAux.posY)
                if organismoAux.estado == 1:
                    resultado = 1 * (1500-distancia_final)+0.5 * (1500-distancia_final)+1 * (1000-resultado_turno[e][o]) + 0.3 * (1000-resultado_turno[e][o])
                else:
                    resultado = 1 * (1500-distancia_final)+0.5 * (1500-resultado_cercano[e][o])+1 * (1000-1000)+0.3 * (1000 - resultado_turno[e][o])

                #  print("Especie " + str(e+1) + " Organismo " + str(o+1) + " - Distancia - " + str(resultado) + " mejor resultado: " + str(resultado_turno2[0][o]))

                if resultado > resultado_turno2[0][e]:  # 1st
                    resultado_turno2[1][o] = resultado_turno2[0][o]
                    top2[o] = copiar_genoma(top1[o])
                    resultado_turno2[0][e] = resultado
                    top1[o] = copiar_genoma(organismoAux.genoma)
                    # leaderboard.set_new_true(t);
                else:
                    if resultado > resultado_turno2[1][o] and e != 0:  # 2nd
                        resultado_turno2[1][o] = resultado
                        top2[e] = copiar_genoma(organismoAux.genoma)

            # update graph
            # line.get(t).append((int(top2_score[0][t])));
            #
            # top_fitness=top2_score[0];
            # leaderboard.reset();
            # for (int x=0; x < 6; x++)
            # leaderboard.update(top2_score[0][x], x);

            # nuevo genoma
            for o in range(50):

                organismoMongoDB = organismos.find_one({"especie": e + 1, "numero_miembro": o + 1})

                organismoAux: Organismo = Organismo(organismoMongoDB["coordX"],
                                                    organismoMongoDB["coordY"],
                                                    organismoMongoDB["angulo"],
                                                    organismoMongoDB["genoma"],
                                                    organismoMongoDB["estado"],
                                                    organismoMongoDB["especie"],
                                                    organismoMongoDB["numero_miembro"],
                                                    especieMongoDB["ratioMutacion"],
                                                    especieMongoDB["color"])

                organismoAux.hijo(top1[e], top2[e], especieMongoDB["ratioMutacion"])

                # Guardar todos los hijos modificados
                organismos.update_one({"especie": organismoAux.especie, "numero_miembro": organismoAux.numero_miembro},
                                      {"$set":
                                           {"coordX": organismoAux.posX,
                                            "coordY": organismoAux.posY,
                                            "angulo": organismoAux.angulo,
                                            "genoma": organismoAux.genoma,
                                            "estado": organismoAux.estado,
                                            "especie": organismoAux.especie,
                                            "numero_miembro": organismoAux.numero_miembro}
                                       })

                #print("Acuralizo " + str(organismoAux.especie) + " " + str(organismoAux.numero_miembro))

                # top2_score[0]=0;
                # top2_score[1]=0;
                organismoAux.reset()
                resultado_turno[e][o] = 1000
                resultado_cercano[e][o] = 1500

        # reset things
        turno = 0
        muertes = 0
        generacion = generacion + 1

        # Evento de refresco para Angular

    #print("top1 score: " + str(resultado_turno2[0]))
    #print("top2 score: " + str(resultado_turno2[1]))


    turno = turno + 1

    if turno != 999:
        move()




colores = ["Rojo", "Naranja", "Verde_Oscuro", "Verde_Claro", "Amarillo",
          "Azul_Marino", "Cian", "Violeta", "Marron"]
numero_especies: int = 0

global mapa
mapa = Image.open("/home/roberto/Escritorio/Web/PythonAI/mapa2.png")
mapa = mapa.convert("RGB")

# Salida                 rgb(184,61,186)
# Rojo relleno Salida    rgb(255, 127, 39)
# Rojo borde Salida      rgb(236, 28, 36)

# Meta borde             rgb(14,209,69)
# Meta interior          rgb(196,255,14)
# Meta                   rgb(0,255,72)

# Terreno pisable        rgb(185, 242, 240)

# Gris fuera             rgb(195,195,195)
# Negro fuera            rgb(0,0,0)

global SalidaX
global SalidaY
global MetaX
global MetaY

colorSalida = (184,61,186)
colorMeta = (0,255,72)
for x in range(mapa.size[0]):
    for y in range(mapa.size[1]):
        if colorSalida == mapa.getpixel((x, y)):
            SalidaX = x
            SalidaY = y
        if colorMeta == mapa.getpixel((x, y)):
            MetaX = x
            MetaY = y

# Step 1: Connect to MongoDB - Note: Change connection string as needed
client = MongoClient('localhost', 27017)
db = client.PathFinder

especies = db.especies
especies.drop()

organismos = db.organismos
organismos.drop()
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
        genoma = [0] * 1000
        for n in range(1000):
            genoma[n] = random.uniform(-0.2, 0.2)

        organismoMongoDB = {
            'coordX': SalidaX,
            'coordY': SalidaY,
            'angulo': 0,
            'especie': x+1,
            'numero_miembro': i+1,
            'estado': 0,
            'genoma': genoma
        }
        # Step 3: Insert business object directly into MongoDB via isnert_one
        result = db.organismos.insert_one(organismoMongoDB)

        # Step 4: Print to the console the ObjectID of the new document
        # print('Creado organismo {0} de 50 de la especie {1} as {2}'.format(i+1, numero_especies, result.inserted_id))

# Proceso finalizado OK
print('Proceso finalizado OK')
resultado_turno = [[4000] * 50 for i in range(numero_especies)]
resultado_cercano = [[4000] * 50 for i in range(numero_especies)]
resultado_turno2 = [[0] * 2 for i in range(numero_especies)]
top1 = [[0] * 1000 for i in range(numero_especies)]
top2 = [[0] * 1000 for i in range(numero_especies)]

# ArrayList<IntList> line = new ArrayList<IntList>();
# team leaderboard = new team();
# float top_fitness[] = {0, 0, 0, 0, 0, 0};
global turno
turno = 1
global generacion
generacion = 1
global muertes
muertes = 0
# int div = 0;

#setup
# size(1000, 650);
# for t in range(numero_especies): # Numero Especies
#     # line.add(new IntList());
#     resultado_turno2[0][t] = 0
#     resultado_turno2[1][t] = 0
#     for i in range(50):  # Numero organismos
#       # generation[i][t]= new organism();
#       # generation[i][t].random_genome();
#       resultado_turno[i][t] = 1000
#       resultado_cercano[i][t] = 1500


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