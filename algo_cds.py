def Alg(R):
    """Heurstique de N machines
    :param R:
    :return:
    """
    def func_trait(x,y,h,s):
        S="";j=y
        while j>h:
            j-=0.5
            S+=x*" " + s+"\n"
        return S
    
    import numpy as np
    import matplotlib.pyplot as plt
    from matplotlib import pyplot
    import  pandas as pd
    import csv
    import operator
    from matplotlib.backends.backend_pdf import PdfPages
    from reportlab.lib.pagesizes import letter
    from reportlab.pdfgen import canvas
    from reportlab.lib import colors
    from reportlab.lib.enums import TA_JUSTIFY
    from reportlab.lib.pagesizes import letter
    from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image,Table,TableStyle
    from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
    from reportlab.lib.units import inch
    nbn="Algo_Cds_InputOutput.pdf"
    doc = SimpleDocTemplate( nbn, pagesize=letter,
                            rightMargin=72, leftMargin=72,
                            topMargin=72, bottomMargin=18 )
    Story = []
    tit="Flow-Shop à N machines, Cmax"
    stit="Contexte"
    logo = "/home/rtimopy/Documents/index.png"
    im = Image( logo, 1 * inch, 1 * inch )
    Story.append( im )
    styles = getSampleStyleSheet()
    styles.add( ParagraphStyle( name='Justify', alignment=TA_JUSTIFY ) )
    ptext = '<font size=20 color=red>%s</font>' %tit
    Story.append( Paragraph( ptext, styles["BodyText"] ) )
    Story.append( Spacer( 1, 12 ) )
    ptext = '<font size=16 color=blue > %s:</font>' %stit
    Story.append( Paragraph( ptext, styles["Normal"] ) )
    Story.append( Spacer( 1, 12 ) )
    ptext = ' La minimisation du Cmax dans le cas du flow-shop général est un problème NP-difficile au sens fort (voir Garey et al).\n Plusieurs heuristiques ont été proposées pour le résoudre, et en particulier celle de Campell Dudek et Smith (CDS) et celle de Nawaz, Enscore et Ham (NEH).\nChacune de ces heuristique donne de bons résultats, mais aucune ne garantie la solution optimale.Souvent, on va compléter ces algorithmes avec un 2-opt ou un 3-opt.'
    ptext = ptext.replace( ' ', '&nbsp;' )
    ptext = ptext.replace( '\n', '<br />' )
    ptext = ptext.replace( '\t', '&nbsp;&nbsp;&nbsp;&nbsp;')
    Story.append( Paragraph( ptext, styles["Justify"] ) )
    Story.append( Spacer( 1, 12 ) )

    ptext = '<font size=12>Notation:</font>'
    Story.append( Paragraph( ptext, styles["Justify"] ) )
    Story.append( Spacer( 1, 12 ) )

    ptext = 'n: nombre de jobs. \n m: nombre de machines.\n pij: processing time du job i sur la machine j'
    ptext = ptext.replace( ' ', '&nbsp;' )
    ptext = ptext.replace( '\n', '<br />' )
    ptext = ptext.replace( '\t', '&nbsp;&nbsp;&nbsp;&nbsp;' )
    Story.append( Paragraph( ptext, styles["Justify"] ) )
    Story.append( Spacer( 1, 20 ) )


    ptext = '<font size=12>CDS:</font>'
    Story.append( Paragraph( ptext, styles["Normal"] ) )
    Story.append( Spacer( 1, 12 ) )

    ptext = 'Cette heuristique consiste simplement générer m−1 sous problèmes de type Flow-shop à 2 machines, à les résoudre et à sélectionner la meilleure solution.\n Le sous problème k est défini par :\n processing time sur la machine virtuelle 1 : pi1= la somme de pij (j£[1,k]) \n processing time sur la machine virtuelle 2 : pi2= la sommede pij (j£[k+1,m]) \n Pour chacun de ces problèmes, on calcule l ordre optimal avec l algorithme de Johnson et on applique alors cet ordre sur le problème de base pour obtenir le Cmax(k).\n Ensuite, il suffit de choisir le meilleur sur l ensemble des Cmax(k).'

    ptext = ptext.replace( ' ', '&nbsp;' )
    ptext = ptext.replace( '\n', '<br />' )
    ptext = ptext.replace( '\t', '&nbsp;&nbsp;&nbsp;&nbsp;' )

    Story.append( Paragraph( ptext, styles["Justify"] ) )
    Story.append( Spacer( 1, 12 ))

    ptext = '<font size=12 color=blue> Exemple :</font>'
    Story.append( Paragraph( ptext, styles["Normal"] ) )
    Story.append( Spacer( 1, 12 ) )

    ptext = '<font size=12>Soit le problème suivant:</font>'
    Story.append( Paragraph( ptext, styles["Normal"] ) )
    Story.append( Spacer( 1, 12 ) )


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
    sort = sorted( sort, key=lambda x: int( x[0] ) )
    sortint = []
    for i in range( len( sort ) ):
        for j in range( len( sort[i] ) ):
            sortint.append( int( sort[i][j] ) )
    print(sort)
    #mat = np.array(sort)
    l_0,l_1=["T/i"],["T/i"]
    for i in range(1,len(sort[0])):
        l_0.append("t i/M{0}".format(i))

    for i in range(1,3):
        l_1.append("t i/M_virt{0}".format(i))
    data=[]
    data.append(l_0)
    for i in sort:
        data.append(i)

    t = Table( data, len(data[0]) * [0.5 * inch], len(data)* [0.5 * inch] )
    t.setStyle( TableStyle( [('ALIGN', (1, 1), (-2, -2), 'RIGHT'),
                             ('TEXTCOLOR', (1, 1), (-2, -2), colors.red),
                             ('VALIGN', (0, 0), (0, -1), 'TOP'),
                             ('TEXTCOLOR', (0, 0), (0, -1), colors.blue),
                             ('ALIGN', (0, -1), (-1, -1), 'CENTER'),
                             ('VALIGN', (0, -1), (-1, -1), 'MIDDLE'),
                             ('TEXTCOLOR', (0, -1), (-1, -1), colors.green),
                             ('INNERGRID', (0, 0), (-1, -1), 0.25, colors.black),
                             ('BOX', (0, 0), (-1, -1), 0.25, colors.black),
                             ] ) )


    Story.append(t)
    Story.append( Spacer( 1, 12 ))
    ptext = 'Probleme d ordanncement Flow Shop : {0} Taches sur {1} Machines'.format(len(data)-1,len(data[0])-1)
    Story.append( Paragraph( ptext, styles["Normal"] ) )
    Story.append( Spacer( 1, 12 ) )
    ptext = 'On résoult les {0} Problemes d ordanncement (Virtuel) Flow Shop à 2 machines avec l algorithme de Johnson  '.format( len( data[0] ) - 2)
    Story.append( Paragraph( ptext, styles["Normal"] ) )
    Story.append( Spacer( 1, 12 ) )

    ptext = '<font size=14 color=blue > Resultats: </font>'
    Story.append( Paragraph( ptext, styles["Normal"] ) )
    Story.append( Spacer( 1, 12 ))

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
    print(lll)
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
    klk ,klks={},{}
    for i in range( len( li ) // v ):
        fl.append( li[i * v:(i + 1) * v] )
    s = fl
    pdflis=[]
    for p in range(len(s)):
        
        print(
            "\n===================================================" + '\n' + START + "\033[1;31m la sequence heurstiq \033[1;m" + END )
        fe.write( "\n===================================================" + '\n' + "la sequence heurstiq" + "\n" )
        h,hc = [],[]
        for i in range( len( s[p] ) - 1 ):
            print( "{}".format( s[p][i] ) )
            h.append( s[p][i] )
            fvg=str(s[p][i])+"=>"
            hc.append(fvg)
            fe.write( "{},".format( s[p][i] ) )
        print( '===>' + ' \033[1;41m Cmax(heurstiq)={} \033[1;m'.format( s[p][v - 1] ) )
        fe.write( '===>' + '  Cmax(heurstiq)={} '.format( s[p][v - 1] ) )
        fl_1 = fl[p][:-1]
        list_gantt = []
        # print(fl_1)
        for i in fl_1:
            list_gantt.append( liste[i - 1] )

        # print(list_gantt)

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
            return db1, db2

        lc = []
        for j in list_gantt:
            for i in range( 1, len( list_gantt[0] ) - 1 ):
                lc.append( [j[0], j[i], j[i + 1]] )

        # print(lc)
        b = len( liste[0] ) - 2
        c = len( fl_1 )
        lcf = []
        for j in range( 0, b ):
            x = b + j
            for i in range( 0, c ):
                lcf.append( lc[x - b] )
                x += b

        cc = lcf[0:c]
        # print("rfrfr",cc)
        db1 = gant_list( cc )[0]
        db3 = gant_list( cc )[1]
        list_excel = [db1, db3]
        # print( db1 )
        # print( db3 )
        for i in range( 1, b ):
            cc1 = lcf[(c * i):c * (i + 1)]
            db4 = []
            db4.append( [db3[0][1], db3[0][1] + cc1[0][2]] )
            for i in range( 1, len( db3 ) ):
                if db3[i][1] >= db4[i - 1][1]:
                    db4.append( [db3[i][1], db3[i][1] + cc1[i][2]] )
                else:
                    db4.append( [db4[i - 1][1], db4[i - 1][1] + cc1[i][2]] )
            # print( db4 )
            db3 = db4
            list_excel.append( db4 )

        print( list_excel )
        ded = open( "gantt__file({0}).txt".format(p), "w" )
        k = 0

        for i in list_excel:
            k += 1
            ch = "{0},".format( k )
            for j in i:
                ch += "{0},{1},".format( j[0], j[1] )
            ch1 = ch[:-1] + "\n"
            ded.write( ch1 )
        ded.close()
        f = int( v / 2 ) + 1
        new = np.loadtxt( "gantt__file({0}).txt".format(p), delimiter=",", unpack=True )
        # print(new)
        htl = []
        for j in range( 1, new.shape[0] ):
            htl.append( new[j][0] )
        # print(htl)
        ht = list( set( htl ) )
        ht = sorted( ht )
        htt1 = [(ht[i] + ht[i + 1]) / 2 for i in range( len( ht ) - 1 )]
        # print(set(htl))
        htt = sorted( htt1 )
        # print(htt)
        cmap = plt.get_cmap( "gnuplot" )
        colors = [cmap( i ) for i in np.linspace( 0, 1, 2 * v )]
        for i in range( 1, new.shape[0] - 1, 2 ):
            plt.hlines( new[0][0], new[i], new[i + 1], colors=colors[i], lw=28 )
            plt.text( htt[int( (i - 1) / 2 )], 1, str( h[int( i / 2 )] ) )
            cv=0.0
            while cv<new[0][0]:
                if cv==0.0:
                    plt.text(new[i][0]-0.1/2,cv-0.25,str(new[i][0]),color=colors[i])
                    plt.text(new[i+1][0]-0.1/2,cv-0.25,str(new[i+1][0]),color=colors[i])
                plt.text(new[i][0]-0.1,cv,"|",color=colors[i])
                plt.text(new[i+1][0]-0.1,cv,"|",color=colors[i])
                cv+=0.2
            plt.grid( True )
            # print(i)
        for j in range( 1, new.shape[1] ):
            for o in range( 1, new.shape[0] ):
                htl.append( new[o][0] )
            ht = list( set( htl ) )
            htt = [(ht[i] + ht[i + 1]) / 2 for i in range( len( ht ) - 1 )]
            for i in range( 1, new.shape[0] - 1, 2 ):
                plt.hlines( new[0][j], new[i][j], new[i + 1][j], colors=colors[i], lw=28, )
                plt.text( (new[i + 1][j] + new[i][j]) / 2, new[0][j], str( h[int( i / 2 )] ) )
                cv=0.0
                while cv<new[0][j]:
                    if cv==0.0:
                        plt.text(new[i][j]-0.05,cv+(new[0][j]-1)*.1,str(new[i][j]),color=colors[i])
                        plt.text(new[i+1][j]-.05,cv+(new[0][j]-1)*.1,str(new[i+1][j]),color=colors[i])
                    plt.text(new[i][j]-0.1,cv,"|",color=colors[i])
                    plt.text(new[i+1][j]-0.1,cv,"|",color=colors[i])
                    cv+=0.2
                plt.grid(True)
        plt.xlabel( "time(j)" )
        plt.title( "Ordanncement FlowShop: {0} machines et {1} Taches".format( b + 1,
                                                                               v - 1 ) + "\n" + "\t" + "Diagramme de Gantt (seq ={0} avec Cmax({2})={1})".format(
            h, list_excel[-1][-1][-1],p ) )
        chh =""
        for i in hc:
            chh+=i
        chh=chh[:-2]
        klk[chh]=[s[p][v-1],list_excel[-1][-1][-1]]
        klks[chh] =[list_excel[-1][-1][-1]]
        plt.ylim( 0, b + 2 )
        plt.xlim( [0, list_excel[-1][-1][-1] + 2] )
        plt.margins( 0, 1 )
        S=func_trait(list_excel[-1][-1][-1],b+1,0,"|")
        plt.annotate( "Cmax=" + str( list_excel[-1][-1][-1] ),xy=(list_excel[-1][-1][-1],b+1),xytext=(0.75*list_excel[-1][-1][-1], b+1.6),arrowprops=dict(facecolor='green', shrink=0.05))
        #plt.text( list_excel[-1][-1][-1], b + 1, S )
        manager = plt.get_current_fig_manager()
        manager.window.showMaximized()
        plt.savefig( "output_diagram_gantt({0}).png".format( p ) ,bbox_inches='tight')
        pp = PdfPages( 'output_diagram_gantt({0}).pdf'.format( p ) )
        pp.savefig()
        pp.close()
        plt.show()
        print(klk)
        pdflis.append([b,h,list_excel[-1][-1][-1]])
    print(pdflis)
    pp=0
    dfre = open("Output_Final_Cds.txt","w")
    klks= sorted(klks.items(), key=operator.itemgetter(1))
    for keyy,values in klk.items():
        pp+=1
        data1=[]
        dfre.write("La solution N°{0}".format(pp)+"\n"+"\n"+"* L ordonnancement optimal est donc || {0} ||".format('=>'.join(keyy)) + "\n" + "** Le Cmax du problème virtuel est de {0}".format(values[0])+"\n" + "*** Le Cmax du problème réel est de {0} ".format(values[1])+"\t"+"\n"+"========================================================="+"\n" )
        ptext="<font size=13 color=green>{0}) La Resultat du probleme virtuel N°{0}</font>".format(pp)
        Story.append( Paragraph( ptext, styles["Justify"] ) )
        Story.append( Spacer( 1, 12 ) )
        ptext = "Le problème virtuel N°{0} à résoudre est :".format( pp )
        Story.append( Paragraph( ptext, styles["Justify"] ) )
        Story.append( Spacer( 1, 12 ) )
        data1.append(l_1)
        for i in lll[pp - 1]:
            data1.append( [str(i[0]),str(i[1]),str(i[2])] )
        print(data1)
        """tt = Table( data1, len( data1[0] ) * [0.5 * inch], len( data1 ) * [0.5 * inch] )"""

        tt = Table( data1, [0.8 * inch, 0.8 * inch, 0.8 * inch, 0.8 * inch, 0.8 * inch, 0.8 * inch],
                    (len(data1))*[0.5 * inch] )
        tt.setStyle( TableStyle( [('ALIGN', (0, 0), (-1, 0), 'CENTER'),
                                 ('ALIGN', (1, 0), (-1, -1), 'CENTER'),
                                 ('ALIGN', (2, 1), (2, -1), 'LEFT'),
                                 ('FONT', (0, 0), (-1, 0), 'Times-Bold'),
                                 ('BOX', (0, 0), (-1, -1), 0.25, "black"),
                                 ('INNERGRID', (0, 0), (-1, -1), 0.25, "black"),
                                 ] ) )


        Story.append( tt )
        Story.append( Spacer( 1, 10 ) )

        ptext="* L ordonnancement optimal est donc || {0} ||".format(keyy) + "\n" + "** Le Cmax du problème virtuel est de {0}".format(values[0])+"\n" + "*** Le Cmax du problème réel est de {0} ".format(values[1])+"\t"+"\n"+"\n"

        ptext = ptext.replace( ' ', '&nbsp;' )
        ptext = ptext.replace( '\n', '<br />' )
        ptext = ptext.replace( '\t', '&nbsp;&nbsp;&nbsp;&nbsp;' )
        Story.append( Paragraph( ptext, styles["Justify"] ) )
        Story.append( Spacer( 1, 12 ) )

        im = Image( "output_diagram_gantt({0}).png".format( pp-1 ))
        Story.append( im )
        ptext="\t \t \t \t Diagramme de Gantt (seq ={0}) avec Cmax({2})={1})".format(
            pdflis[pp-1][1],pdflis[pp-1][2], pp )
        ptext = ptext.replace( ' ', '&nbsp;' )
        ptext = ptext.replace( '\n', '<br />' )
        ptext = ptext.replace( '\t', '&nbsp;&nbsp;&nbsp;&nbsp;' )
        Story.append( Paragraph( ptext, styles["Justify"] ) )
        Story.append( Spacer( 1, 12 ) )


    dfre.write(
        "\n " + "\n" + "==>Pour Conclure On retient La solution de Sequence Optimal:|| {0} || et d'ordonnancement optimal de Cmax = {1} ".format(klks[0][0],klks[0][1][0]))

    ptext = '<font size=14 color=blue>Conclusion: </font>'
    Story.append( Paragraph( ptext, styles["Normal"] ) )
    Story.append( Spacer( 1, 12 ) )
    ptext= "\n" + "Pour Conclure On retient La solution de Sequence Optimal:|| {0} || et d'ordonnancement optimal de Cmax = {1} ".format(klks[0][0],klks[0][1][0])
    ptext = ptext.replace( ' ', '&nbsp;' )
    ptext = ptext.replace( '\n', '<br />' )
    ptext = ptext.replace( '\t', '&nbsp;&nbsp;&nbsp;&nbsp;' )
    Story.append( Paragraph( ptext, styles["Justify"] ) )
    Story.append( Spacer( 1, 12 ) )
    dfre.close()
    doc.build( Story )
    print(klks)


from random import randrange
from tkinter.filedialog import *
from tkinter import *
from tkinter.messagebox import *
import smtplib
import mimetypes
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import email.mime.application
#from tabula import read_pdf
import os
from wand.image import Image
from PIL import Image as PI
import pyocr
import pyocr.builders
import io
import sys
import hashlib
import getpass



def callback():
    if askyesno('Question', 'Vous avez un document texte du donnes ?'):
        filename = askopenfile(title="Ouvrir votre document", filetypes=[('txt files', '.txt'),('Pdf files','.pdf'),('Img File','.png'),('img File','.jpeg'),('img file','.jpg')])
        rrf=filename.name
        fileName, fileExtension = os.path.splitext( rrf )
        print(type(fileExtension))
        if fileExtension ==".txt":
            Alg(filename.name)
        if fileExtension==".pdf":
            tool = pyocr.get_available_tools()[0]
            lang = tool.get_available_languages()[1]

            req_image = []
            final_text = []

            image_pdf = Image( filename=filename.name, resolution=300 )
            image_jpeg = image_pdf.convert( 'jpeg' )

            for img in image_jpeg.sequence:
                img_page = Image( image=img )
                req_image.append( img_page.make_blob( 'jpeg' ) )
            chh = []
            for img in req_image:
                txt = tool.image_to_string(
                    PI.open( io.BytesIO( img ) ),
                    lang=lang,
                    builder=pyocr.builders.TextBuilder()
                )
                final_text.append( txt )

            ch, chhh = "", ""
            l = []
            for i in final_text:
                for j in i:
                    ch += j
            jk = ch.rsplit()
            print( jk )
            for i in range( len( jk ) ):
                if jk[i] == '16+':
                    c = jk[i][0:2]
                    l.append( int( c ) )
                else:
                    l.append( int( jk[i] ) )
            """a, b = 6, 5"""
            a=int(input("Enter The Numer of Jobs : "))
            b=int(input("Enter The Number Of Machine :"))
            ll = []
            # print(l)
            lr = len( l )
            frg = open( "inputCds.txt", "w" )
            for i in range( 0, b ):
                ll.append( l[i * a:(i + 1) * a] )
            for i in ll[0]:
                frg.write( "{}".format( i ) )
                for j in range( 1, b ):
                    frg.write( ",{0}".format( ll[j][i - 1] ) )
                frg.write( "\n" )
            # print(ll)
            frg.close()
            Alg(frg.name)

        if fileExtension==".jpeg":
            tool = pyocr.get_available_tools()[0]
            lang = tool.get_available_languages()[1]
            req_image = []
            final_text = []

            """image_pdf = Image(filename="/home/rtimopy/Downloads/Untitled 1.pdf", resolution=300)
            image_jpeg = image_pdf.convert('jpeg')"""
            image_jpeg = Image( filename=filename.name, resolution=300 )

            for img in image_jpeg.sequence:
                img_page = Image( image=img )
                req_image.append( img_page.make_blob( 'jpeg' ) )
            chh = []
            for img in req_image:
                txt = tool.image_to_string(
                    PI.open( io.BytesIO( img ) ),
                    lang=lang,
                    builder=pyocr.builders.TextBuilder()
                )
                final_text.append( txt )

            ch, chhh = "", ""
            l = []
            for i in final_text:
                for j in i:
                    ch += j
            jk = ch.rsplit()
            print( jk )
            for i in range( len( jk ) ):
                if jk[i] == '16+':
                    c = jk[i][0:2]
                    l.append( int( c ) )
                else:
                    l.append( int( jk[i] ) )
            #a, b = 6, 5
            a = int( input( "Enter The Numer of Jobs : " ) )
            b = int( input( "Enter The Number Of Machine :" ) )
            ll = []
            # print(l)
            lr = len( l )
            frg = open( "inputCds.txt", "w" )
            for i in range( 0, b ):
                ll.append( l[i * a:(i + 1) * a] )
            for i in ll[0]:
                frg.write( "{}".format( i ) )
                for j in range( 1, b ):
                    frg.write( ",{0}".format( ll[j][i - 1] ) )
                frg.write( "\n" )
            # print(ll)
            frg.close()
            Alg(frg.name)

        if fileExtension in [".png",".jpg"]:
            tool = pyocr.get_available_tools()[0]
            lang = tool.get_available_languages()[1]
            req_image = []
            final_text = []

            """image_pdf = Image(filename="/home/rtimopy/Downloads/Untitled 1.pdf", resolution=300)
            image_jpeg = image_pdf.convert('jpeg')"""
            imagee = Image( filename=filename.name, resolution=300 )
            image_jpeg = imagee.convert("pdf").convert('jpeg')
            for img in image_jpeg.sequence:
                img_page = Image( image=img )
                req_image.append( img_page.make_blob( 'jpeg' ) )
            chh = []
            for img in req_image:
                txt = tool.image_to_string(
                    PI.open( io.BytesIO( img ) ),
                    lang=lang,
                    builder=pyocr.builders.TextBuilder()
                )
                final_text.append( txt )

            ch, chhh = "", ""
            l = []
            for i in final_text:
                for j in i:
                    ch += j
            jk = ch.rsplit()
            print( jk )
            for i in range( len( jk ) ):
                if jk[i] == '16+':
                    c = jk[i][0:2]
                    l.append( int( c ) )
                else:
                    l.append( int( jk[i] ) )
            #a, b = 6, 5
            a = int( input( "Enter The Numer of Jobs : " ) )
            b = int( input( "Enter The Number Of Machine:" ) )
            ll = []
            # print(l)
            lr = len( l )
            frg = open( "inputCds.txt", "w" )
            for i in range( 0, b ):
                ll.append( l[i * a:(i + 1) * a] )
            for i in ll[0]:
                frg.write( "{}".format( i ) )
                for j in range( 1, b ):
                    frg.write( ",{0}".format( ll[j][i - 1] ) )
                frg.write( "\n" )
            # print(ll)
            frg.close()
            Alg( frg.name )
            

    else:
        print("Donner nom de fichier:")
        filname = input() + ".txt"
        f = open(filname, "w")
        a = int(input("Combien de taches a ordonnacer :"))
        b = int(input("Combien des machines :"))
        for i in range(a):
            print("Ecrire les durees de taches {0} sur les {1} machines (exp :{0},{2},{3},{4},..)".format(i + 1, b,
                                                                                                          randrange(10),
                                                                                                          randrange(20),
                                                                                                          randrange(12),
                                                                                                          b))
            frr = input("{},".format(i + 1))
            #print(frr.count(","))
            while frr.count(",") != b - 1:
                if frr.count(",") < b - 1:
                    print(
                        "error : les donnees entrantes du tache N{} sont inf au nombre du machine,Repeter svp".format(
                            i + 1))
                else:
                    print(
                        "error : les donnees entrantes du tache N{} sont sup au nombre du machine,Repeter svp".format(
                            i + 1))
                frr = input("{},".format(i + 1))
            f.write("{},".format(i + 1) + frr + '\n')
        ff = f
        f.close()
        Alg(filname)



from tkinter import *
import os
def sendd():
    a=input("You want to send the file pdf to adress email ?! :(ENTER or (Y) to Continue) ,(Any key or (N) to Exit the Program)")
    import time
    from progress.bar import Bar
    def barr():
        bar = Bar('Processing', max=20, suffix=' %(percent).1f%% - %(eta)ds')
        for i in range(20):
            time.sleep(.09) # Do some work
            bar.next()
        bar.finish()
    if a not in ["","Y","y"]:
        barr()
        print("Check your File pef to see the result .. Enjoy :)  ")
        time.sleep(1.0)
        exit()
    else :
        msg = MIMEMultipart()
    
    msg['Subject'] = 'File pdf : Result of Algo CDS'
    msg['From'] = input('Enter Your Gmail (exp : xyz@gmail.com):')
    passwd="thamersarray1994"
    assd = int(input("enter THe nmbr of recp :"))
    too =[]
    for i in range(assd):
        msg['To'] = input( 'Enter The List of Receiption : (exp : xyz@gmail.com,frf@gmail.com)' )
        too.append( msg['To'])
    frm = msg['From']
    body = MIMEText("""Hello, how are you? I am fine.
    This is a rather nice letter, don't you think?""")
    msg.attach(body)

    # PDF attachment
    filename="Algo_Cds_InputOutput.pdf"
    fp=open(filename,'rb')
    att = email.mime.application.MIMEApplication(fp.read(),_subtype="pdf")
    fp.close()
    att.add_header('Content-Disposition','attachment',filename=filename)
    msg.attach(att)
    s = smtplib.SMTP('smtp.gmail.com')
    s.starttls()
    s.login(frm,passwd)
    j=0 
    for i in too:
        j+=1
        barr();print("email N°{} to {} sent successfully".format(j,i))
        s.sendmail(frm,i, msg.as_string())
    
    print("Your(s) message(s) was successfully delivered to the destination(s)..Thank you :) <3 ")
    time.sleep(1.0)
    s.quit()


creds = 'tempfile.temp' # This just sets the variable creds to 'tempfile.temp'
 
def Signup(): # This is the signup definition, 
    global pwordE # These globals just make the variables global to the entire script, meaning any definition can use them
    global nameE
    global roots
 
    roots = Tk() # This creates the window, just a blank one.
    roots.title('Signup') # This renames the title of said window to 'signup'
    intruction = Label(roots, text='Please Enter new Credidentials\n') # This puts a label, so just a piece of text saying 'please enter blah'
    intruction.grid(row=0, column=0, sticky=E) # This just puts it in the window, on row 0, col 0. If you want to learn more look up a tkinter tutorial :)
 
    nameL = Label(roots, text='New Username: ') # This just does the same as above, instead with the text new username.
    pwordL = Label(roots, text='New Password: ') # ^^
    nameL.grid(row=1, column=0, sticky=W) # Same thing as the instruction var just on different rows. :) Tkinter is like that.
    pwordL.grid(row=2, column=0, sticky=W) # ^^
 
    nameE = Entry(roots) # This now puts a text box waiting for input.
    pwordE = Entry(roots, show='*') # Same as above, yet 'show="*"' What this does is replace the text with *, like a password box :D
    nameE.grid(row=1, column=1) # You know what this does now :D
    pwordE.grid(row=2, column=1) # ^^
 
    signupButton = Button(roots, text='Signup', command=FSSignup) # This creates the button with the text 'signup', when you click it, the command 'fssignup' will run. which is the def
    signupButton.grid(columnspan=2, sticky=W)
    roots.mainloop() # This just makes the window keep open, we will destroy it soon
 
def FSSignup():
    with open(creds, 'w') as f: # Creates a document using the variable we made at the top.
        f.write(nameE.get()) # nameE is the variable we were storing the input to. Tkinter makes us use .get() to get the actual string.
        f.write('\n') # Splits the line so both variables are on different lines.
        f.write(pwordE.get()) # Same as nameE just with pword var
        f.close() # Closes the file
 
    roots.destroy() # This will destroy the signup window. :)
    Login() # This will move us onto the login definition :D
 
def Login():
    global nameEL
    global pwordEL # More globals :D
    global rootA
 
    rootA = Tk() # This now makes a new window.
    rootA.title('Login') # This makes the window title 'login'
 
    intruction = Label(rootA, text='Please Login\n') # More labels to tell us what they do
    intruction.grid(sticky=E) # Blahdy Blah
 
    nameL = Label(rootA, text='Username: ') # More labels
    pwordL = Label(rootA, text='Password: ') # ^
    nameL.grid(row=1, sticky=W)
    pwordL.grid(row=2, sticky=W)
 
    nameEL = Entry(rootA) # The entry input
    pwordEL = Entry(rootA, show='*')
    nameEL.grid(row=1, column=1)
    pwordEL.grid(row=2, column=1)
 
    loginB = Button(rootA, text='Login', command=CheckLogin) # This makes the login button, which will go to the CheckLogin def.
    loginB.grid(columnspan=2, sticky=W)
 
    rmuser = Button(rootA, text='Delete User', fg='red', command=DelUser) # This makes the deluser button. blah go to the deluser def.
    rmuser.grid(columnspan=2, sticky=W)
    rootA.mainloop()
 
def CheckLogin():
    import time
    with open(creds) as f:
        data = f.readlines() # This takes the entire document we put the info into and puts it into the data variable
        uname = data[0].rstrip() # Data[0], 0 is the first line, 1 is the second and so on.
        pword = data[1].rstrip() # Using .rstrip() will remove the \n (new line) word from before when we input it
 
    if nameEL.get() == uname and pwordEL.get() == pword: # Checks to see if you entered the correct data.
        r = Tk() # Opens new window
        r.title('Yeah Welcome :)')
        r.geometry('250x50') # Makes the window a certain size
        rlbl = Label(r, text='\n[+] Logged In') # "logged in" label
        rlbl.grid() # Pack is like .grid(), just different
        time.sleep(1.0)
        r.mainloop()
        
     
    else:
        r = Tk()
        r.title('Yeah Welcome :)')
        r.geometry('250x50')
        rlbl = Label(r, text='\n[!] Invalid Login')
        rlbl.pack()
        r.mainloop()
        
 
def DelUser():
    os.remove(creds) # Removes the file
    rootA.destroy() # Destroys the login window
    Signup() # And goes back to the start!
 
if os.path.isfile(creds):
    Login()
    msg = MIMEMultipart()
    Button(text="Action", command=callback()).pack()
    sendd()
else: # This if else statement checks to see if the file exists. If it does it will go to Login, if not it will go to Signup :)
    Signup()
