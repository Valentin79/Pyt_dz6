
#=========================== задача2 ==============================

# Реализовать RLE алгоритм. реализовать модуль сжатия и восстановления данных. 
# Входные и выходные данные хранятся в отдельных файлах 
# (в одном файлике отрывок из какой-то книги, а втором файлике — 
# сжатая версия этого текста). 

# with open('rle_decoded.txt', 'r') as data:
#     text = data.read()

# def encode_rle(string):
#     print(string)
#     len_str = len(string)
#     end = 0
#     str_code = ''
#     prev_el = ''
#     count = 1
#     for el in string:
#         if el == prev_el:
#             count +=1
#             end += 1
#             if end == len_str: # что бы писать последний символ
#                 str_code += str(count) + prev_el
#         elif el != prev_el and count > 1:
#             str_code += str(count) + prev_el
#             prev_el = el
#             count = 1
#             end += 1
#         else:
#             str_code += prev_el
#             prev_el = el
#             count = 1
#             end += 1
#     return str_code

            
# str_code = encode_rle(text)
# print(str_code)

# with open('rle_encoded.txt', 'w') as data:
#     data.write(str_code)

# with open('rle_encoded.txt', 'r') as data:
#     text_1 = data.read()

# def decoding_rle(string):
#     count = 1
#     str_decode = ''
#     for el in string:
#         if el.isdigit():
#             count = el
#         else:
#             for i in range(int(count)):
#                 str_decode += el
#             count = 1
#     return str_decode

# str_decode = decoding_rle(text_1)
# print(str_decode)

# #=================================== Задача 3 ==========================

# # ROT13 - это простой шифр подстановки букв, который заменяет букву буквой, 
# # которая идет через 13 букв после нее в алфавите. 
# # ROT13 является примером шифра Цезаря.

# def rot13(text, decode = False):
#     alpfabet = 'abcdefghijklmnopqrstuvwxyz'
#     result = ''
#     for i in text:
#         if i in alpfabet:
#             if decode: 
#                 result += alpfabet[(alpfabet.index(i) - 13) % 26]
#             else:
#                 result += alpfabet[(alpfabet.index(i) + 13) % 26]
#         else:
#             result += i
#     return result

# input_text = 'abcdefghijklmnopqrstuvwxyz' 
# print('input text = ', input_text)
# encode_text = rot13(input_text)
# print('encode text = ', encode_text)
# decode_text = rot13(encode_text, decode = True)
# print('decode text = ', decode_text)