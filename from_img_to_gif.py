
# images to gif

import os
import imageio

def create_gif(image_list, gif_name):

    frames = []
    for image_name in image_list:
        if image_name.endswith('.png'):
            # print(image_name)
            frames.append(imageio.imread(image_name))
    # Save them as frames into a gif
    imageio.mimsave(gif_name, frames, 'GIF', duration = 0.0001)

    # return

def main(target_dir_num):

    path = r"./{}/".format(target_dir_num)
    image_list = [img for img in os.listdir(path)]
    image_list.sort(key=lambda x: int(x.split('.')[0]))
    # print(image_list)

    image_list = [path+img for img in image_list]
    # for i in image_list:
        # print(i)
        # pass

    gif_name = "swarm_experiment_{}.gif".format(target_dir_num)
    # gif_name = "random_swarm_example_{}.gif".format(target_dir_num)
    create_gif(image_list, gif_name)

if __name__ == "__main__":

    print("input folder number:")

    number_dir = input()

    main(target_dir_num=number_dir)





