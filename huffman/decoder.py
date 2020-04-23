#!/usr/bin/python
# -*- coding: utf-8 -*-
# vim:fileencoding=utf-8

class Node:

    def __init__(self, letter, is_leaf, letter_and_code, curr_code):
        self.letter = letter
        self.is_leaf = is_leaf
        self.letter_and_code = letter_and_code
        self.zeroSonNode = None
        self.oneSonNode = None
        self.curr_code = curr_code

    def print_bfs_tree(self):
        queue = []
        if (self.zeroSonNode):
            queue.append(self.zeroSonNode)
        if (self.oneSonNode):
            queue.append(self.oneSonNode)
        while (len(queue) > 0):
            curr_node = queue.pop(0)
            if (curr_node.is_leaf == True):
                print(list(curr_node.letter), ' : ', curr_node.curr_code)
            else:
                if (curr_node.zeroSonNode):
                    queue.append(curr_node.zeroSonNode)
                if (curr_node.oneSonNode):
                    queue.append(curr_node.oneSonNode)
        return

    def create_tree(self):
        zero_letter_and_code = dict()
        one_letter_and_code = dict()
        zero_letters = list()
        one_letters = list()
        for letter in self.letter_and_code.keys():
            if (self.letter_and_code[letter][0] == '0'):
                zero_letter_and_code[letter] = self.letter_and_code[letter][1:]
                zero_letters.append(letter)
            elif (self.letter_and_code[letter][0] == '1'):
                one_letter_and_code[letter] = self.letter_and_code[letter][1:]
                one_letters.append(letter)
        if (len(self.letter_and_code.keys()) == 2):
            self.zeroSonNode = Node(zero_letters[0], True, zero_letter_and_code, self.curr_code + '0')
            self.oneSonNode = Node(one_letters[0], True, one_letter_and_code, self.curr_code + '1')
        elif (len(self.letter_and_code.keys()) == 1):
            if (len(zero_letters) == 1):
                self.zeroSonNode = Node(zero_letters[0], True, zero_letter_and_code, self.curr_code + '0')
            else:
                self.oneSonNode = Node(one_letters[0], True, one_letter_and_code, self.curr_code + '1')
        elif (len(self.letter_and_code.keys()) > 2):
            if (len(zero_letters) == 1):
                self.zeroSonNode = Node(zero_letters[0], True, zero_letter_and_code, self.curr_code + '0')
                self.oneSonNode = Node(None, False, one_letter_and_code, self.curr_code + '1')
                self.oneSonNode.create_tree()
            elif (len(one_letters) == 1):
                self.oneSonNode = Node(one_letters[0], True, one_letter_and_code, self.curr_code + '1')
                self.zeroSonNode = Node(None, False, zero_letter_and_code, self.curr_code + '0')
                self.zeroSonNode.create_tree()
            else:
                self.zeroSonNode = Node(None, False, zero_letter_and_code, self.curr_code + '0')
                self.zeroSonNode.create_tree()
                self.oneSonNode = Node(None, False, one_letter_and_code, self.curr_code + '1')
                self.oneSonNode.create_tree()
        return

    def print_tree(self):
        if (self.is_leaf):
            print(list(self.letter), ' : ', self.curr_code)
        else:
            if (self.zeroSonNode != None):
                self.zeroSonNode.print_tree()
            if (self.oneSonNode != None):
                self.oneSonNode.print_tree()
        return

class Decoder:

    def __init__(self, in_file_name, out_file_name, tree_root):
        self.in_file_name = in_file_name
        self.out_file_name = out_file_name
        self.tree_root = tree_root

    def decode_input_file(self):
        in_file = open(self.in_file_name, "br")
        out_file = open(self.out_file_name, "bw")
        curr_node = self.tree_root
        for line in in_file:
            decode_line = line.decode('utf-8')
            letter_list = list()
            for letter in decode_line:
                letter_list.append(letter)
                if (letter == '0'):
                    if (curr_node.zeroSonNode == None):
                        return 'damage file'
                    curr_node = curr_node.zeroSonNode
                elif (letter == '1'):
                    if (curr_node.oneSonNode == None):
                        return 'damage file'
                    curr_node = curr_node.oneSonNode
                else:
                    return 'damage file'
                if (curr_node.is_leaf == True):
                    enc_bytes = bytes(curr_node.letter, encoding = 'utf-8')
                    out_file.write(enc_bytes)
                    curr_node = self.tree_root
                    letter_list = list()
        return "everything is OK"
