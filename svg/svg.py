import svgwrite
import sys
from svgwrite import px

LINE = 25.
script_filename = sys.argv[1]

script = open(script_filename).readlines()

STEP = 0
IIDX = 0
def get_length(text):
    if (len (text) < 2): return 0
    space = text.count (' ')
    others = len (text) - space
    if (text[-1] == '\n'): others -= 1
    print (' >> ', text, space, others)
    return others * 72 + space * 30 

while (True):
    print ('STEP ', STEP)
    input_text = script[STEP]
    length = len (input_text)
    print ('  ', input_text, '  length:', length)


    if (length < 2): #텍스트가 없으면 다음 줄로..
        STEP += 1
        continue

    for idx in range (int(1 + length / LINE)):
        text = input_text [int(LINE * idx):int (LINE * idx + LINE)] 
        text_length = get_length (text)
        print (idx, text)

        out_filename = '%03d_script.svg'%IIDX
        print (out_filename)

        dwg = svgwrite.Drawing (out_filename, size = (1920, 1080))
        # 그림 추가
        dwg.add (dwg.image (href='/home/hubbup/test/my.gif', insert=(100, 100)))
        # 박스 추가
        dwg.add (dwg.rect(insert=(960 - int(text_length/2.), 920), size=(text_length, 100 * px), fill='green', stroke_width=0, fill_opacity=0.3))

        # 텍스트 추가
        g = dwg.g (font_size = 80, stroke='black', fill='white', font_weight=500, font_family = '굴림')
        g.add (dwg.text (text, insert=(980 - int(text_length/2.), 1000)))
        dwg.add (g)
        dwg.save()
        IIDX += 1

    STEP += 1

    if (STEP >= len (script)): break
