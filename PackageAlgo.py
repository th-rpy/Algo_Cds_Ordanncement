def Alg(R):
    """Heurstique de N machines
    :param R:
    :return:
    """
    import numpy as np
    import matplotlib.pyplot as plt
    from matplotlib import pyplot
    import csv
    import operator
    fil = "outputCDS.txt"
    fe = open( fil, "w" )
    try:
        hrs = open( R, "r" )
    except FileNotFoundError:
        print( "Le nom de fichier est introuvable" )
    except IOError:
        print( "Error d'ouverture" )
    Csv = csv.reader( hrs, delimiter=',' )
    sort = sorted( Csv, key=operator.itemgetter( 0 ) )
    l = len( sort[0] )
    sortint = []
    for i in range( len( sort ) ):
        for j in range( len( sort[i] ) ):
            sortint.append( int( sort[i][j] ) )
    liste, liste2 = [], []
    for n in range( len( sortint ) // l ):
        liste.append( sortint[n * l:(n + 1) * l] )

    def calcul(k, liste):
        for n in range( len( liste ) ):
            liste2.append( [liste[n][0], sum( liste[n][1:k] ), sum( liste[n][-1:-k:-1] )] )
        return (liste2)

    r = [i + 2 for i in range( l - 2 )]
    #print(r)
    #print(liste)

    for i in r:
        kk = calcul( i, liste )
        #print(kk)
    lll = []
    for i in range( len( kk ) // len( sort ) ):
        lll.append( kk[i * len( sort ):(i + 1) * len( sort )] )
    listfinal, li = [], []
    for T in lll:
        import operator
        sort1 = sorted( T, key=operator.itemgetter( 1 ) )
        sort2 = sorted( T, key=operator.itemgetter( 2 ), reverse=True )
        A, B = [], []
        for j in range( len( sort1 ) ):
            if int( sort1[j][1] ) < int( sort1[j][2] ) or int( sort1[j][1] ) == int( sort1[j][2] ):
                A.append( sort1[j] )
        l = len( sort2 )
        for j in range( l ):
            if int( sort2[j][1] ) > int( sort2[j][2] ):
                B.append( sort2[j] )
        C = A + B
        #print( C )
        START = '\033[4m'

        END = '\033[0m'
        print(START+'\033[1;34m la sequence optimal\033[1;m'+END)
        fe.write(' la sequence optimal'+"\n")
        for i in range( len( C ) ):
            print( "{}".format( C[i][0] ) )
            fe.write("{},".format( C[i][0] ))
            li.append(C[i][0])

        db1, db2 = [], []


        db1.append([0,C[0][1]])
        for i in range(1, len( C ) ):
            db1.append( [db1[i-1][1],db1[i-1][1] + C[i][1]] )
        db2.append( [db1[0][1],db1[0][1]+C[0][2]] )
        for i in range(1, len( db1 )  ):
            if db1[i][1] >= db2[i-1][1]:
                db2.append( [db1[i][1],db1[i][1]+C[i][2]] )
            else:
                db2.append( [db2[i - 1][1],db2[i-1][1] + C[i][2]] )
        print( '===>'+ '\033[1;44m Cmax={} \033[1;m'.format( db2[-1][1]  ) + "\n"+"===================================================" )
        fe.write('===>'+ 'Cmax={} '.format( db2[-1][1]  ) + "\n"+"==================================================="+"\n" )

        #print(db2)
        #print(db1)
        li.append( db2[-1][1] )
    fl = []
    v = len( sort ) + 1

    for i in range( len( li ) // v ):
        fl.append( li[i * v:(i + 1) * v] )
    s = sorted( fl, key=operator.itemgetter( v - 1 ) )
    print( "\n==================================================="+'\n'+START+"\033[1;31m la sequence heurstiq \033[1;m"+END )
    fe.write("\n==================================================="+'\n'+ "la sequence heurstiq"+"\n"  )
    h = []
    for i in range( len( s[0] ) - 1 ):
        print( "{}".format( s[0][i] ) )
        h.append(s[0][i])
        fe.write("{},".format( s[0][i] ))
    print( '===>'+' \033[1;41m Cmax(heurstiq)={} \033[1;m'.format( s[0][v - 1] ) )
    fe.write('===>'+'  Cmax(heurstiq)={} '.format( s[0][v - 1] ))
    fl_1 = fl[0][:-1]
    list_gantt = []
    #print(fl_1)
    for i in fl_1 :
        list_gantt.append(liste[i-1])
    #print(list_gantt)

    def gant_list(C):
        db1, db2 = [], []

        db1.append( [0, C[0][1]] )
        for i in range( 1, len( C ) ):
            db1.append( [db1[i - 1][1], db1[i - 1][1] + C[i][1]] )
        db2.append( [db1[0][1], db1[0][1] + C[0][2]] )
        for i in range( 1, len( db1 ) ):
            if db1[i][1] >= db2[i - 1][1]:
                db2.append( [db1[i][1], db1[i][1] + C[i][2]] )
            else:
                db2.append( [db2[i - 1][1], db2[i - 1][1] + C[i][2]] )
        return db1,db2
    lc = []
    for j in list_gantt:
        for i in range(1,len(list_gantt[0])-1):
            lc.append([j[0],j[i],j[i+1]])

    #print(lc)
    b=len(liste[0])-2
    c=len(fl_1)
    lcf = []
    for j in range(0,b):
        x=b + j
        for i in range( 0, c ):
            lcf.append( lc[x-b] )
            x+=b

    cc=lcf[0:c]
    #print("rfrfr",cc)
    db1=gant_list(cc)[0]
    db3 = gant_list( cc )[1]
    list_excel = [db1 , db3]
    #print( db1 )
    #print( db3 )
    #print( "ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff" )
    for i in range(1,b):
        cc1 = lcf[(c * i):c * (i + 1)]
        db4 = []
        db4.append( [db3[0][1], db3[0][1] + cc1[0][2]] )
        for i in range( 1, len( db3 ) ):
            if db3[i][1] >= db4[i - 1][1]:
                db4.append( [db3[i][1], db3[i][1] + cc1[i][2]] )
            else:
                db4.append( [db4[i - 1][1], db4[i - 1][1] + cc1[i][2]] )
        #print( db4 )
        db3=db4
        list_excel.append(db4)

    #print("vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv")
    print(list_excel)
    ded = open( "gantt__file.txt", "w" )
    k = 0

    for i in list_excel:
        k += 1
        ch = "{0},".format( k )
        for j in i:
            ch += "{0},{1},".format( j[0], j[1] )
        ch1 = ch[:-1] + "\n"
        ded.write( ch1 )
    ded.close()
    f =int(v/2)+ 1
    new=np.loadtxt("gantt__file.txt",delimiter=",",unpack=True)
    #print(new)
    htl = []
    for j in range(1,new.shape[0]):
        htl.append(new[j][0])
    ht=list(set(htl))
    htt=[(ht[i]+ht[i+1])/2 for i in range(len(ht)-1)]
    #print(htt)
    cmap=plt.get_cmap("gnuplot")
    colors=[cmap(i)for i in np.linspace(0,1,2*v)]
    for i in range( 1, new.shape[0] - 1, 2 ):
        plt.hlines( new[0][0], new[i], new[i + 1],colors=colors[i], lw=24 )
        plt.text( htt[int((i-1)/2)], 1, str( h[int( i / 2 )] ) )
        #print(i)
    for j in range(1,new.shape[1]):
        for o in range( 1, new.shape[0] ):
            htl.append( new[o][0] )
        ht = list( set( htl ) )
        htt = [(ht[i] + ht[i + 1]) / 2 for i in range( len( ht ) - 1 )]
        for i in range( 1, new.shape[0] - 1,2 ):
            plt.hlines(new[0][j], new[i][j],new[i+1][j],colors=colors[i],lw=24)
            plt.text( (new[i+1][j] + new[i][j]) / 2, new[0][j], str( h[int( i / 2 )] ) )
    plt.xlabel("time(j)")
    plt.title("Ordanncement FlowShop: {0} machines et {1} Taches".format(b+1,v-1) +"\n"+"\t"+"Diagramme de Gantt (seq ={0} avec Cmax={1})".format(h,list_excel[-1][-1][-1]))
    plt.ylim(0,b+2)
    plt.xlim([0,list_excel[-1][-1][-1]+1])
    plt.margins(0,1)
    plt.savefig( "output_diagram_gantt.png" )
    plt.text( list_excel[-1][-1][-1],b+1, "Cmax="+str( list_excel[-1][-1][-1] ) )
    plt.show()
