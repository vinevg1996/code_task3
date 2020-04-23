#!/usr/bin/python
# -*- coding: utf-8 -*-
# vim:fileencoding=utf-8

import sys

def convert_txt_to_bin(input_file_name):
    in_file = open(input_file_name, "r")

    dot_id = input_file_name.rfind(".", 0)
    bin_file = str(input_file_name[0:dot_id]) + '.bin'
    out_file = open(bin_file, "bw")
    for line in in_file:
        enc_bytes = bytes(line, encoding = 'utf-8')
        out_file.write(enc_bytes)
    return

convert_txt_to_bin(sys.argv[1])