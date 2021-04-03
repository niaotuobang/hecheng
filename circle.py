import sys
import os

from PIL import Image, ImageOps, ImageDraw

size_map = {
    52: (52, 52, 'ad16ccdc-975e-4393-ae7b-8ac79c3795f2.png'),
    80: (80, 80, '0cbb3dbb-2a85-42a5-be21-9839611e5af7.png'),
    108: (108, 108, 'd0c676e4-0956-4a03-90af-fee028cfabe4.png'),
    119: (119, 119, '74237057-2880-4e1f-8a78-6d8ef00a1f5f.png'),
    153: (153, 152, '132ded82-3e39-4e2e-bc34-fc934870f84c.png'),
    183: (183, 183, '03c33f55-5932-4ff7-896b-814ba3a8edb8.png'),
    193: (193, 193, '665a0ec9-6c43-4858-974c-025514f2a0e7.png'),
    258: (258, 258, '84bc9d40-83d0-480c-b46a-3ef59e603e14.png'),
    308: (308, 308, '5fa0264d-acbf-4a7b-8923-c106ec3b9215.png'),
    309: (308, 309, '564ba620-6a55-4cbe-a5a6-6fa3edd80151.png'),
    408: (408, 408, '5035266c-8df3-4236-8d82-a375e97a0d9c.png'),
}

'''
葡萄 52 * 52
樱桃 80 * 80
橘子 108 * 108
柠檬 119 * 119
猕猴桃 153 * 152
西红柿 183 * 183
桃 193 * 193
菠萝 258 * 258
椰子 308 * 308
西瓜 308 * 309
大西瓜 408 * 408
'''

'''
./raw-assets/0c/0cbb3dbb-2a85-42a5-be21-9839611e5af7.png (80, 80)
./raw-assets/66/665a0ec9-6c43-4858-974c-025514f2a0e7.png (193, 193)
./raw-assets/50/5035266c-8df3-4236-8d82-a375e97a0d9c.png (408, 408)
./raw-assets/03/03c33f55-5932-4ff7-896b-814ba3a8edb8.png (183, 183)
./raw-assets/56/564ba620-6a55-4cbe-a5a6-6fa3edd80151.png (308, 309)
./raw-assets/5f/5fa0264d-acbf-4a7b-8923-c106ec3b9215.png (308, 308)
./raw-assets/ad/ad16ccdc-975e-4393-ae7b-8ac79c3795f2.png (52, 52)
./raw-assets/d0/d0c676e4-0956-4a03-90af-fee028cfabe4.png (108, 108)
./raw-assets/74/74237057-2880-4e1f-8a78-6d8ef00a1f5f.png (119, 119)
./raw-assets/84/84bc9d40-83d0-480c-b46a-3ef59e603e14.png (258, 258)
./raw-assets/13/132ded82-3e39-4e2e-bc34-fc934870f84c.png (153, 152)
'''

# https://stackoverflow.com/questions/890051/how-do-i-generate-circular-thumbnails-with-pil

def main(filein, size):
    size_x, size_y, fileout = size_map[size]
    size_tp = (size_x, size_y)

    im = Image.open(filein)
    im.resize(size_tp)

    mask = Image.new('L', size_tp, 0)
    draw = ImageDraw.Draw(mask)
    draw.ellipse((0, 0) + size_tp, fill=255)

    output = ImageOps.fit(im, mask.size, centering=(0.5, 0.5))
    output.putalpha(mask)

    try:
        dirs = './raw-assets/' + fileout[:2] + '/'
        os.makedirs(dirs)
    except Exception as e:
        print(e)
        pass

    output.save(dirs + fileout)


if __name__ == '__main__':
    main(sys.argv[1], int(sys.argv[2]))
