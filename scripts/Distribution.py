from arcpy import *
import math

env.workspace=r'C:\Users\Oussama\Desktop\1\classification.gdb'


surface=575109892                                               # C'est 3% de la surface totale en metres
nbPts=200                                                       # C'est le nombre de points par zone ( 6 zones )
surfpts=surface/(nbPts*6)                                       # Surface de chaque petite cercle
List=['Saad','Nadia','Fati','Oussama','Amine','Ayoub']          # Les noms des Zones
distance=str(int(2*math.sqrt(surfpts/math.pi))+1)+' meters'     # Diametre de chaque cercle
bufdist=str(int(math.sqrt(surfpts/math.pi))+1)+' meters'        # Rayon de chaque cercle
i=1                                                             # i est le numero de chaque zone

for e in List :
    zone , pts , shp = 'p'+e , 't'+e , e+str(i)                 # des variable intermidiaire, sauf "shp" c'est le variable de feature class de chaque zone contenant les cercles
    CreateRandomPoints_management(env.workspace,pts,zone,number_of_points_or_field=nbPts,minimum_allowed_distance=distance)  # Creations de 200 points aleatoires dans chaque zone
    Buffer_analysis(pts, shp, bufdist)  # le buffer de chaque point
    i+=1
 