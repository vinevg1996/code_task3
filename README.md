# code_task3
Проект содержит 3 программы:

* Конвертация из ".txt"-формата в ".bin"-формат

* Режим кодирования (encode_mode)

* Режим декодирования (decode_mode)

Используются следующие форматы файлов:

* ".txt": эти файлы лежат в папке "txt\_files". Чтобы конвертировать их в бинарные файлы ".bin" используется конвертер. Программа запускается:

  python3 convert_txt_to_binary.py txt_files/SECTUMSEMPRA.txt

И создаётся бинарный файл "SECTUMSEMPRA.bin".

* ".bin": эти файлы лежат в папке "bin\_files".

## Кодирование по методу Хаффмана

Чтобы закодировать содержимое файла с расширением .bin по методу Хаффмана, зайдите в папку huffman и запустите:

  python3 task3.py encode_mode ../bin_files/SECTUMSEMPRA.bin

Создаётся файл "../bin_files/SECTUMSEMPRA.zmh", в котором все строки, кроме последней содержат список букв и соответствующих им кодовых слов. Последняя строка содержит сам код.

## Декодирование по методу Хаффмана

Чтобы декодировать содержимое файла с расширением .zmh по методу Хаффмана, зайдите в папку huffman и запустите:

  python3 task3.py decode_mode ../bin_files/SECTUMSEMPRA.zmh

Создаётся файл:

* "../bin_files/SECTUMSEMPRA": файл с деодированным по методу Хаффмана сообщением

# Тестирование

Проект тестировался на трёх файлах:

* ../bin_files/test_input.bin

* ../bin_files/harry.bin

* ../bin_files/SECTUMSEMPRA.bin