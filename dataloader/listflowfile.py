import torch.utils.data as data

from PIL import Image
import os
import os.path

IMG_EXTENSIONS = [
    '.jpg', '.JPG', '.jpeg', '.JPEG',
    '.png', '.PNG', '.ppm', '.PPM', '.bmp', '.BMP',
]


def is_image_file(filename):
    return any(filename.endswith(extension) for extension in IMG_EXTENSIONS)


def dataloader(filepath):
    # filepath = filepath_ + '/'
    classes = [d for d in os.listdir(filepath) if os.path.isdir(os.path.join(filepath, d))]
    image = [img for img in classes if img.find('frames_cleanpass') > -1]
    disp = [dsp for dsp in classes if dsp.find('disparity') > -1]
    
    monkaa_path = filepath + [x for x in image if 'monkaa' in x][0]
    monkaa_disp = filepath + [x for x in disp if 'monkaa' in x][0]
    
    monkaa_dir = os.listdir(monkaa_path)
    all_left_img = []
    all_right_img = []
    all_left_disp = []
    test_left_img = []
    test_right_img = []
    test_left_disp = []
    #
    for dd in monkaa_dir:
        for im in os.listdir(monkaa_path + '/' + dd + '/left/'):
            if is_image_file(monkaa_path + '/' + dd + '/left/' + im):
                all_left_img.append(monkaa_path + '/' + dd + '/left/' + im)
                all_left_disp.append(monkaa_disp + '/' + dd + '/left/' + im.split(".")[0] + '.pfm')
    
        for im in os.listdir(monkaa_path + '/' + dd + '/right/'):
            if is_image_file(monkaa_path + '/' + dd + '/right/' + im):
                all_right_img.append(monkaa_path + '/' + dd + '/right/' + im)
    flying_path = filepath + [x for x in image if x == 'frames_cleanpass'][0]
    flying_disp = filepath + [x for x in disp if x == 'frames_disparity'][0]
    flying_dir = flying_path + '/train/'

    imm_l = os.listdir(flying_dir + '/left/')

    print(len(imm_l))
    for im in imm_l:
        if is_image_file(flying_dir + '/left/' + im):
            all_left_img.append(flying_dir + '/left/' + im)

        all_left_disp.append(flying_disp + '/train' + '/left/' + im.split(".")[0] + '.pfm')

        if is_image_file(flying_dir + '/right/' + im):
            all_right_img.append(flying_dir + '/right/' + im)

    flying_dir = flying_path + '/test/'

    imm_l = os.listdir(flying_dir + '/left/')
    for im in imm_l:
        if is_image_file(flying_dir + '/left/' + im):
            test_left_img.append(flying_dir + '/left/' + im)

        test_left_disp.append(flying_disp + '/test/' + '/left/' + im.split(".")[0] + '.pfm')

        if is_image_file(flying_dir + '/right/' + im):
            test_right_img.append(flying_dir + '/right/' + im)
    return all_left_img, all_right_img, all_left_disp, test_left_img, test_right_img, test_left_disp
