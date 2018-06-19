"""
Adaptado de: 
@author: edielson - https://github.com/edielsonpf
"""
# Simulador de colonia de passaros na solucao de problemas.
# Baseado no artigo Partical Swarm Optimization de James Kennedy.
#
# Por Edielson Prevato Frigieri

from ParticleSwarmOptimization.pso_numeric_spheric import pso
import matplotlib.pyplot as plt

import sys
import os.path
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

def Spheric(x1,x2, x3):
    return (x1)**2 + (x2)**2 + (x3)**2;

if __name__ == '__main__': 
 
    #define as constantes da colonia
    NUM_BIRDS = 500
    NUM_INTERACTIONS = 10000
    MAX_SIZE = 50
    MAX_ERRO = 0.000001
    NUM_VARS = 3
    
    OPTION = 'CORNFIELD_VECTOR'
    #OPTION = 'NEAREST_NEIGHBOR_VELOCITY_MATCHING'
    
    #Define a posicao da comida aleatoriamente
    roostPoint = [0,0,0] #Minimo global para a funcao Spheric
    print(roostPoint)
    TARGET = Spheric(roostPoint[0],roostPoint[1], roostPoint[2])
     
    swarm = pso(NUM_BIRDS,NUM_VARS,NUM_INTERACTIONS,OPTION)
    gbest_val_vec, best_particle, gbest_val = swarm.search(TARGET,MAX_ERRO)
    
    print('Best individual %s' %best_particle)
    print('Best fitness %g' %gbest_val)   
    
    interaction=[i for i in range(len(gbest_val_vec))]

    plt.plot(interaction,gbest_val_vec)
    plt.show()  
    