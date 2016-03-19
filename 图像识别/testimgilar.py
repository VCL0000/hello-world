from PIL import Image


# img = Image.open('1.jpg')
# new_img = img.convert('L')

def make_regalur_image(img, size=(256, 256)):
    return img.resize(size).convert('RGB')


def hist_similar(lh, rh):
    assert len(lh) == len(rh)
    return sum(1 - (0 if l == r else float(abs(l - r)) / max(l, r)) for l, r in zip(lh, rh)) / len(lh)


def calc_similar(li, ri):
    return hist_similar(li.histogram(), ri.histogram())


def calc_similar_by_path(lf, rf):
    li, ri = make_regalur_image(Image.open(lf)), make_regalur_image(Image.open(rf))
    return calc_similar(li, ri)


if __name__ == '__main__':
    path = r'test/TEST%d/%d.JPG'
    for i in range(1, 7):
        print('test_case_%d: %.3f%%' % (i, calc_similar_by_path('test/TEST%d/%d.JPG' % (i, 1), 'test/TEST%d/%d.JPG' % (i, 2)) * 100))
