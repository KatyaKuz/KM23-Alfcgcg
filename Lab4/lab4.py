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

def create_img(point, path_save):
    point_z=[100]
    for i in range(0, len(point)):
        np.append(point, [int(i) for i in point_z], axis= 1 )
    proection = np.array([[1, 0, 0, 0][-540/ 960, 0, 0, -1/ 960], [0, 0, 1, 0], [0, 0, 0, 1]])
    tr_p = np.dot(point, proection)
    matp.scatter(xy_coord(tr_p, 0), xy_coord(tr_p, 1), xy_coord(tr_p, 2), color='blue')
    matp.xlim(0, 960)
    matp.ylim(0, 960)
    matp.savefig(path_save+"\\image_lab4.png")
    matp.show()

ds_path=input("Enter path where dataset: ")
ds_path_save=input("Enter path where image saves: ")
points_dt=dt_read(ds_path)
create_img(points_dt, ds_path_save)

