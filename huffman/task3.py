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
    #write letter_and_code in .lac
    bin_file = sys.argv[2]
    dot_id = bin_file.rfind(".", 0)
    zmh_file = str(bin_file[0:dot_id]) + '.zmh'
    lac_file = str(bin_file[0:dot_id]) + '.lac'
    
    enc = Encoder(bin_file, zmh_file)
    enc.calculate_probability()
    letter_and_code = enc.create_Huffman_code()
    enc.create_code_for_input_file()
    out_lac = open(lac_file, 'w')
    for letter in letter_and_code.keys():
        out_lac.write(str(list(letter)))
        out_lac.write("$")
        out_lac.write(letter_and_code[letter])
        out_lac.write("\n")
elif (sys.argv[1] == "decode_mode"):
    #sys.argv[2] -- input_file_with_letter_and_code
    #sys.argv[3] -- input_bin_file_for_decoding
    #write decode file in .dec
    letter_and_code = dict()
    lac_file = open(sys.argv[2], 'r')
    for line in lac_file:
        line_list = line.split('$', 2)
        sym = str(line_list[0][2 : len(line_list[0]) - 2])
        if ((sym[0] == '\\') and (sym[1] == 'n')):
            sym = '\n'
        if ((sym[0] == '\\') and (sym[1] == 't')):
            sym = '\t'
        if ((sym[0] == '\\') and (sym[1] == 'r')):
            sym = '\r'
        if ((sym[0] == '\\') and (sym[1] == 'x')):
            sym = '\xad'
        code = line_list[1][0 : len(line_list[1]) - 1]
        letter_and_code[sym] = code
    root = Node(None, False, letter_and_code, str())
    root.create_tree()
    bin_file = sys.argv[3]
    dot_id = bin_file.rfind(".", 0)
    dec_file = str(bin_file[0:dot_id]) + '.dec'
    dec = Decoder(bin_file, dec_file, root)
    info = dec.decode_input_file()
    print(info)
else:
    print("please, enter mode")
