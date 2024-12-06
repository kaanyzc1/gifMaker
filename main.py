import imageio.v3 as iio

filenames = ['kpk.png', 'kpk2.png']
images = []


for filename in filenames:
    images.append(iio.imread(filename))

iio.imwrite('kpk.gif', images, duration = 500, loop = 0)
