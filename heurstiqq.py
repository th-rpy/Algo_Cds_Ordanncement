from PackageAlgo import Alg
from random import randrange
from tkinter.filedialog import *
from tkinter import *
from tkinter.messagebox import *
from gantt import Gantt


def callback():
    if askyesno('Question', 'Vous avez un document texte du donnes ?'):

        filename = askopenfile(title="Ouvrir votre document", filetypes=[('txt files', '.txt'), ('all files', '.*')])
        Alg(filename.name)

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
            print(frr.count(","))
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

Button(text="Action", command=callback()).pack()

