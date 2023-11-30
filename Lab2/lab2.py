import matplotlib.pyplot as matp
def dt_read(path):
    dp_list=[]
    with open(path, "r") as file:
        for line in file:
            dp_list.append([int(i) for i in line.split()])
    file.close()
    return dp_list

def xy_coord(path, var):
    coor=[]
    list_ar=dt_read(dt_p)
    for i in range(len(list_ar)):
        x.append(list_ar[i][var])
    return coor

def create_img(path, path_save):
    matp.scatter(xy_coord(path, 0), xy_coord(path, 1))
    matp.xlim(0,960)
    matp.ylim(0,540)
    matp.xlable("X")
    matp.ylable("Y")
    matp.savefig(path_save+"\\image.png")
    matp.show()

ds_path=input("Enter path where dataset: ")
ds_path_save=input("Enter path where image saves: ")
create_img(ds_path, ds_path_save)
