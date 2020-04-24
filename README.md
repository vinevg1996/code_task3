# code_task3
Проект содержит 3 программы:

* Конвертация из ".txt"-формата в ".bin"-формат

* Режим кодирования (encode_mode)

* Режим декодирования (decode_mode)

Используются следующие форматы файлов:

* ".txt": эти файлы лежат в папке "txt\_files". Чтобы конвертировать их в бинарные файлы ".bin" используется конвертер. Программа запускается ::

  python3 convert_txt_to_binary.py txt_files/SECTUMSEMPRA.txt

И создаётся бинарный файл "SECTUMSEMPRA.bin".

* ".bin": эти файлы лежат в папке "bin\_files".

## Кодирование по методу Хаффмана

Программа кодировки по методу Хаффмана лежит в папке huffman и запускается ::

  python3 task3.py encode_mode ../bin_files/SECTUMSEMPRA.bin

Создаются файлы:

* "../bin_files/SECTUMSEMPRA.lac": файл с буквами и их кодами

* "../bin_files/SECTUMSEMPRA.zmh": файл с кодом

## Декодирование по методу Хаффмана

Программа кодировки по методу Хаффмана лежит в папке huffman и запускается ::

  python3 task3.py decode_mode ../bin_files/SECTUMSEMPRA.lac ../bin_files/SECTUMSEMPRA.zmh

Создаётся файл:

* ".dec": файл с деодированным по методу Хаффмана сообщением

# Тестирование

Проект тестировался на трёх файлах:

* ../bin_files/test_input.bin

* ../bin_files/harry.bin

* ../bin_files/SECTUMSEMPRA.bin