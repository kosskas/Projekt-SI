import numpy as np
from matplotlib import pyplot as plt
from kNN import NearestNeighborClasiffier
from Linear import LinearClasiffier
from load_data import load_data, get_classes_num


###
load_data.N_OF_CLASSES = 36#36
#
print(f"liczba klas = {get_classes_num()}")
print("wczytywanie")
train_data, test_data = load_data()
print("start")

#model = NearestNeighborClasiffier(klasy=get_classes_num(),norma = 2, k = 1)

model = LinearClasiffier(klasy=get_classes_num(), iters=5,step=0.0001)
model.wczytaj_model("./Modele/model_36_100000")
#model.train(*train_data)
avg,confmat = model.evaluate(*test_data)
#model.zapisz_model("nowy_model")

#row_sums=confmat.sum(axis=1,keepdims=True)
#norm_mat=confmat/row_sums
#norm_mat*=100

#plt.matshow(norm_mat, cmap=plt.cm.Blues)
##plt.title("Klasyfikator liniowy dla {0} klas\nDokładność = {1:.2%}\n".format(get_classes_num(),avg))
##plt.title("Klasyfikator kNN dla {0} klas\nDokładność = {1}%\n".format(get_classes_num(),avg*100))
#plt.ylabel("Rzeczywiste klasy")
#plt.xlabel("Przewidywane klasy")
#for i in range(confmat.shape[0]):
#    for j in range(confmat.shape[1]):
#        plt.text(j, i, f"{int(confmat[i, j])}", ha="center", va="center", color="w")
#plt.colorbar(format='%.0f%%')
#plt.clim(0, 100)
#plt.show()


#np.fill_diagonal(norm_mat,0)
#plt.matshow(norm_mat, cmap=plt.cm.Greys)
#plt.title("Błędy popełnione przy klasyfikacji")
#plt.ylabel("Rzeczywiste klasy")
#plt.xlabel("Przewidywane klasy")
#for i in range(norm_mat.shape[0]):
#    for j in range(norm_mat.shape[1]):
#        if j == i:
#            plt.text(j, i, f"0", ha="center", va="center", color="w")
#        else:
#            plt.text(j, i, f"{int(confmat[i, j])}", ha="center", va="center", color="w")
#plt.colorbar(format='%.2f%%')
#plt.show()



###############
#print("liczenie wg k")

#output = []
#for i in [3, 36]:
#    load_data.N_OF_CLASSES = i
#    print(f"liczba klas = {get_classes_num()}")
#    print("wczytywanie")
#    train_data, test_data = load_data()
#    print("start")
#    for k in [3, 5]:
#        model = NearestNeighborClasiffier(klasy=i, k=k, norma=2)
#        model.train(*train_data)
#        avg,_ = model.evaluate(*test_data)
#        print(f"k={k} n=2 avg={avg}")
#        output.append(f"{k},2,{avg}")
#print("k,n,avg")
#for o in output:
#    print(o)
