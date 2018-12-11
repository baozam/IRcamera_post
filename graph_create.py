import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.axes_grid1 import make_axes_locatable
from pylab import rcParams
import os

print('++++++++++Edit by kazama 2018++++++++++')
print('What is the parameter ?\nQ = 0\nT = 1\nH = 2\nI = 3\nR = 4')
judge = input('parameter: ')
if judge==0:
    graph_parameter='Q'
elif judge==1:
    graph_parameter='T'
elif judge==2:
    graph_parameter='H'
elif judge==3:
    graph_parameter='I'
elif judge==4:
    graph_parameter='R'
print('What is Run number ?')
graph_run = input('Run number: ')
print('Which place is the IRcamera position ?\nfront = 0\nback = 1')
judge2 = input('position: ')
if judge2==0:
    graph_position='A'
elif judge2==1:
    graph_position='B'
folder_name = graph_parameter + str(graph_run) + graph_position
print('How much is the all file ?')
max_frame = input('all file: ')

rcParams['figure.figsize'] = 15,15

new_dir_path_depth = "./IR_img/" + graph_parameter + str(graph_run) + graph_position + "/"


def my_makedirs( path ):
    if not os.path.isdir( path ):
        os.makedirs( path )

my_makedirs( new_dir_path_depth )

for num_exection in range(max_frame):
    plt.cla()
    graph_frame = str( num_exection + 1 )
    if judge<=2:
        graph_title = graph_parameter + str(graph_run) + graph_position + "ZMf" + graph_frame + "D"
    else:
        graph_title = graph_parameter +  "data/" + graph_parameter + str(graph_run) + graph_position + "ZMf" + graph_frame + "D"
    graph_file = graph_title + ".csv"
    graph_path = "./RAW_data/" + str(graph_run) + "/" + graph_file

    print( "Visualizing Now : " + graph_path )
    if judge<=2:
        out_image =  new_dir_path_depth + "IMG_" + graph_title + ".png"
    else:
        out_image =  new_dir_path_depth + "IMG_" + graph_parameter + str(graph_run) + graph_position + "ZMf" + graph_frame + "D" + ".png"
    print( "Output file     : " + out_image )

    if judge<3:
        val = np.loadtxt( graph_path ,delimiter = ',')
    elif judge>2:
        val = np.loadtxt( graph_path ,delimiter = ';')

    xx,yy = [],[]
    x = val[0,:]
    y = val[:,0]

    for num in range( len( x ) ):
        xx.append( x )
    for num in range( len( y ) ):
        yy.append( y )
        X = np.array( xx )
        Y = np.array( yy ).T
    
    fig,ax = plt.subplots()
    ax.set_ylim( ax.get_ylim()[::-1] )
    plt.tick_params( labelleft = 'False' )
    plt.tick_params( labelbottom = 'False' )
    plt.tick_params( length = 0 )
    plt.title( graph_title, fontsize = 25 )
    if judge==1:
       image = ax.contourf( val,cmap = 'rainbow' , vmax = 300 , levels = [0,10,20,30,40,50,60,70,80,90,100,110,120,130,140,150,160,170,180,190,200,210,220,230,240,250,260,270,280,290,300,310,320] )
 #      image = ax.contourf( val,cmap = 'rainbow' , levels = [20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45] )
    elif judge==0:
        image = ax.contourf( val,cmap = 'rainbow' , levels = [0,10,20,30,40,50,60,70,80,90,100,110,120,130,140,150,160,170,180,190,200,210,220])
    elif judge==2:
        image = ax.contourf( val,cmap = 'rainbow' , levels = [0,5,10,15,20,25,30,35,40,45,50,55,60,65,70,75,80,85,90,95,100])
    elif judge>2:
        image = ax.contourf( val,cmap = 'rainbow' , vmax = 300 , levels = [0,10,20,30,40,50,60,70,80,90,100,110,120,130,140,150,160,170,180,190,200,210,220,230,240,250,260,270,280,290,300,310,320] )
    ax.axis( "image" )
    divider = make_axes_locatable( ax )
    ax_cb = divider.new_horizontal( size = "5%" , pad = 0.1 )
    fig.add_axes( ax_cb )
    
    cbar = plt.colorbar( image,cax = ax_cb )
    cbar.ax.tick_params( labelsize = 20 )
    if judge==1:
        cbar.set_label( "Temperature (degC)" , labelpad = 30 , size = 25 , rotation = 270 )
    elif judge==0:
        cbar.set_label( "Heat Flux (kW/m2)" , labelpad = 30 , size = 25 , rotation = 270 )
    elif judge==2:
        cbar.set_label( "Thermal Conductive (W/m2/K)" , labelpad = 30 , size = 25 , rotation = 270 )
    elif judge>2:
        cbar.set_label( "Temperature (degC)" , labelpad = 30 , size = 25 , rotation = 270 )
    #plt.show()
    plt.savefig( out_image )
    plt.close(fig)
    print( "Finish                  : " + out_image )
print( "All done !!" )
