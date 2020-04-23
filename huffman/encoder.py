#!/usr/bin/python
# -*- coding: utf-8 -*-
# vim:fileencoding=utf-8

class Node:
    letters = list()
    prob = 0

    def __init__(self, letters, prob):
        self.letters = letters
        self.prob = prob

    def print(self):
        print(self.letters, ' : ', self.prob)


class Encoder:
    in_file_name = str()
    out_file_name = str()
    probability_dict = dict()
    letter_and_code = dict()
    letters_number = 0
    symbols_number = 0

    def __init__(self, in_file_name, out_file_name):
        self.in_file_name = in_file_name
        self.out_file_name = out_file_name

    def read_from_file(self, file_name):
        self.in_file_name = file_name
        in_file = open(self.in_file_name, "br")
        for line in in_file:
            decode_line = line.decode('utf-8')
            print(decode_line, end = '')

    def write_to_file(self, file_name):
        out_file = open(file_name, "bw")
        enc_bytes = bytes('abaabaaabaaaab\n', encoding = 'utf-8')
        out_file.write(enc_bytes)
        enc_bytes = bytes('babababab\n', encoding = 'utf-8')
        out_file.write(enc_bytes)
        enc_bytes = bytes('cdadcafdfa\n', encoding = 'utf-8')
        out_file.write(enc_bytes)
        enc_bytes = bytes('ewqwqwqadfadf\n', encoding = 'utf-8')
        out_file.write(enc_bytes)
        enc_bytes = bytes('fdgaklmxdfm\n', encoding = 'utf-8')
        out_file.write(enc_bytes)

    def calculate_probability(self):
        in_file = open(self.in_file_name, "br")
        for line in in_file:
            decode_line = line.decode('utf-8')
            for sym in decode_line:
                self.symbols_number = self.symbols_number + 1
                item = self.probability_dict.get(sym)
                if (item != None):
                    self.probability_dict[sym] = self.probability_dict[sym] + 1
                else:
                    self.probability_dict[sym] = 1
                    self.letter_and_code[sym] = str()
                    self.letters_number = self.letters_number + 1
        for letter in self.probability_dict.keys():
            self.probability_dict[letter] = float(self.probability_dict[letter]) / float(self.symbols_number)

    def print_probability_dict(self):
        print("_________________")
        print("probability_dict:")
        for letter in self.probability_dict.keys():
            print(letter, ': ', self.probability_dict[letter])

    def find_two_min_in_list_of_nodes(self, list_of_nodes):
        min_prob_1 = 1
        min_prob_2 = 1
        min_id_1 = -1
        min_id_2 = -1
        for i in range(0, len(list_of_nodes)):
            if (list_of_nodes[i].prob < min_prob_1):
                min_id_2 = min_id_1
                min_prob_2 = min_prob_1
                min_id_1 = i
                min_prob_1 = list_of_nodes[i].prob
            elif(list_of_nodes[i].prob < min_prob_2):
                min_id_2 = i
                min_prob_2 = list_of_nodes[i].prob
        return [min_id_1, min_id_2]

    def create_Huffman_code(self):
        list_of_nodes = list()
        for letter in self.probability_dict.keys():
            list_of_nodes.append(Node(list(letter), self.probability_dict[letter]))
        for i in range(0, self.letters_number - 1):
            new_list_of_nodes = list()
            min_id_list = self.find_two_min_in_list_of_nodes(list_of_nodes)
            #min_id_list[0] -> 0
            #min_id_list[1] -> 1
            for letter in list_of_nodes[min_id_list[0]].letters:
                self.letter_and_code[letter] = '0' + self.letter_and_code[letter]
            for letter in list_of_nodes[min_id_list[1]].letters:
                self.letter_and_code[letter] = '1' + self.letter_and_code[letter]
            for i in range(0, len(list_of_nodes)):
                if ((i != min_id_list[0]) and (i != min_id_list[1])):
                    new_list_of_nodes.append(Node(list_of_nodes[i].letters, list_of_nodes[i].prob))
            new_letter_list = list_of_nodes[min_id_list[0]].letters + list_of_nodes[min_id_list[1]].letters
            new_prob = list_of_nodes[min_id_list[0]].prob + list_of_nodes[min_id_list[1]].prob
            new_list_of_nodes.append(Node(new_letter_list, new_prob))
            list_of_nodes = list(new_list_of_nodes)
        return self.letter_and_code

    def print_Huffman_code(self):
        for letter in self.letter_and_code.keys():
            print(list(letter), ' : ', self.letter_and_code[letter])
        return

    def create_code_for_input_file(self):
        in_file = open(self.in_file_name, "br")
        out_file = open(self.out_file_name, "ba")
        for line in in_file:
            decode_line = line.decode('utf-8')
            for letter in decode_line:
                enc_bytes = bytes(self.letter_and_code[letter], encoding = 'utf-8')
                out_file.write(enc_bytes)

    def calculate_average_lenght(self):
        average_sum = 0.0
        for letter in self.letter_and_code.keys():
            average_sum = average_sum + len(self.letter_and_code[letter]) * self.probability_dict[letter]
        return average_sum