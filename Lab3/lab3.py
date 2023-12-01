import matplotlib.pyplot as matp
import math
import numpy as np
def dt_read(ds_path):
    dp_list=[]
    with open(ds_path, "r") as file:
        for line in file:
            dp_list.append([int(i) for i in line.split()])
    file.close()
    return dp_list

def xy_coord(point, var):
    coor=[]
    for i in range(len(point)):
        coor.append(point[i][var])
    return coor

def affine_transf(point, al_angle):
    al_angle_rad = np. radians(al_angle)
    al_sin=np.sin(al_angle)
    al_cos=np.cos(al_angle)
    matrix = np. array([[al_cos, -al_sin],[al_sin, al_cos]])
    transf_p = np.dot(point - np.array([480, 480]), matrix.T) + np.array([480, 480])
    return transf_p

def create_img(tr_p, path_save):
    matp.scatter(xy_coord(tr_p, 0), xy_coord(tr_p, 1), color='blue')
    matp.xlim(0, 960)
    matp.ylim(0, 960)
    matp.savefig(path_save+"\\image_affine.png")
    matp.show()

ds_path=input("Enter path where dataset: ")
ds_path_save=input("Enter path where image saves: ")
n=9
points_dt=dt_read(ds_path)
alpha_angle=10*(n+1)
transform=affine_transf(points_dt, alpha_angle)
create_img(transform, ds_path_save)
