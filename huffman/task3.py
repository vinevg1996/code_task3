#!/usr/bin/python
# -*- coding: utf-8 -*-
# vim:fileencoding=utf-8

from encoder import Encoder
from decoder import Node
from decoder import Decoder

import sys
import json
import random

#sys.argv[1] = encode_mode | decode_mode
if (sys.argv[1] == "encode_mode"):
    #sys.argv[2] -- input_bin_file_for_encoding
    #write encode file in .zmh
    bin_file = sys.argv[2]
    dot_id = bin_file.rfind(".", 0)
    zmh_file = str(bin_file[0:dot_id]) + '.zmh'
    enc = Encoder(bin_file)
    enc.calculate_probability()
    letter_and_code = enc.create_Huffman_code()
    out_zmh = open(zmh_file, "bw")
    for letter in letter_and_code.keys():
        enc_bytes = bytes(str(list(letter)), encoding = 'utf-8')
        out_zmh.write(enc_bytes)
        enc_bytes = bytes(letter_and_code[letter], encoding = 'utf-8')
        out_zmh.write(enc_bytes)
        enc_bytes = bytes("\n", encoding = 'utf-8')
        out_zmh.write(enc_bytes)
    enc.create_code_for_input_file(out_zmh)
elif (sys.argv[1] == "decode_mode"):
    #sys.argv[2] -- input_bin_file_for_decoding
    #write decode in file without .zmh
    bin_file = sys.argv[2]
    dot_id = bin_file.rfind(".", 0)
    if (bin_file[dot_id + 1 : ] != "zmh"):
        print("extention is not zmh")
        exit(0)
    zmh_file = open(sys.argv[2], 'r')
    letter_and_code = dict()
    for line in zmh_file:
        if (line[0] == '['):
            id_bracket = line.rfind(']', 0)
            sym = line[2 : id_bracket - 1]
            if ((sym[0] == '\\') and (sym[1] == 'n')):
                sym = '\n'
            elif ((sym[0] == '\\') and (sym[1] == 'a')):
                sym = '\a'
            elif ((sym[0] == '\\') and (sym[1] == 'b')):
                sym = '\b'
            elif ((sym[0] == '\\') and (sym[1] == 'f')):
                sym = '\f'
            elif ((sym[0] == '\\') and (sym[1] == 'r')):
                sym = '\r'
            elif ((sym[0] == '\\') and (sym[1] == 't')):
                sym = '\t'
            elif ((sym[0] == '\\') and (sym[1] == 'v')):
                sym = '\v'
            elif ((sym[0] == '\\') and (sym[1] == 'x')):
                sym = '\xad'
            elif ((sym[0] == '\\') and (sym[1] == '\\')):
                sym = '\\'
            code = line[id_bracket + 1 : len(line) - 1]
            letter_and_code[sym] = code
        else:
            last_line = line
    root = Node(None, False, letter_and_code, str())
    root.create_tree()
    dec_file = str(bin_file[0:dot_id])
    dec = Decoder(bin_file, dec_file, root)
    info = dec.decode_input_file(last_line)
    print(info)
else:
    print("please, enter mode")

#\n  Перевод строки
#\a  Звонок
#\b  Забой
#\f  Перевод страницы
#\r  Возврат каретки
#\t  Горизонтальная табуляция
#\v  Вертикальная табуляция