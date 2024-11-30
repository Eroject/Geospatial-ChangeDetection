polygones=r'C:\Users\lenovo\Desktop\shapefiles\Oussama4.shp' #Chemin Vers Les polygones à classés 
sr='4326' #Référence spatial
nbr=0 #Id du polygone par lequel on va commencer
L=[]
# on remplit L avec les coordonees des cercles.
with da.SearchCursor(polygones,['shape@X','shape@Y'],spatial_reference=sr) as cursor:
        for row in cursor:
            latitude=row[0]
            longitude=row[1]
            L.append((longitude,latitude))
# on classe les cercles.
for i in range(nbr,len(L)):
    b=str(L[i])
    r=1
    while r==1:
        try:
            c=str(input('donner la classe'+b+'\nentrer K si vous voulez quitter'))
            r=0
        except:
            print('entre une valeur string ne pas oublier les quotes \'\'')
            r=1

    if c==str('k'):
        print("Vous avez arrèté au polygone d'ID : "+str(i))
    with da.UpdateCursor(polygones,['Classname'] ) as cursor:
        occ=0
        for row in cursor:
            if occ==i:
                row[0]=c
                cursor.updateRow (row)
            occ=occ+1