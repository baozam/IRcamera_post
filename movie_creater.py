import cv2

fourcc = cv2.VideoWriter_fourcc('m','p','4','v')

dir_name = 'IR_img'
print('++++++++++Edit by kazama 2018++++++++++')
print('What is the parameter ?\nQ = 0\nT = 1\nH = 2')
judge = input('parameter: ')
if judge==0:
    parameter='Q'
elif judge==1:
    parameter='T'
elif judge==2:
    parameter='H'
print('What is Run number ?')
run_number = input('Run number: ')
print('Which place is the IRcamera position ?\nfront = 0\nback = 1')
judge2 = input('position: ')
if judge2==0:
    position='A'
elif judge2==1:
    position='B'
folder_name = parameter + str(run_number) + position
print('How much is the all file ?')
all_frame = input('all file: ')
print('What is frame rate ?')
frame_rate = input('frame rate: ')

out_put_file = './IR_img/' + folder_name + 'f' + str(frame_rate) + '.mp4'
last_frame = all_frame + 1

video = cv2.VideoWriter(out_put_file, fourcc, frame_rate, (640, 640))

for i in range(1, last_frame):
    file_path = './' + dir_name + '/' + folder_name + '/IMG_' + folder_name + 'ZMf' + str(i) + 'D.png'
    print(file_path)
    img = cv2.imread(file_path)
    img = cv2.resize(img, (640,640))
    video.write(img)

video.release()
