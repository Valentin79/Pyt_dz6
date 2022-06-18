#=============================== Задача 1 ============================
# калькулятор в строке
# все таки дописал. Без скобок, возможно с косяками, но вроде как приооритет операций
# выполняется. 


# string1 = '12+34-6*2/3'
# string1 = '2*4-4/2+4'
# string1 = '10/2+3*2-1+5'

# num_list = []
# num_str = ''
# op_str = ''
# i = 0
# lenght = len(string1)
# for el in string1:
#     if el.isdigit():
#         num_str += el
#         i+=1
#         if i == lenght:
#             num_list.append(num_str)
#     else:
#         num_list.append(num_str)
#         num_str = ''
#         op_str += el
#         i+=1

# print(num_list)
# print(op_str)

# for el in op_str:
#     if el == '*':
#         operator = op_str.index('*')
#         result = int(num_list[operator])*int(num_list[operator+1])
#         num_list[operator] = result
#         num_list.pop(operator+1)
#         op_str = op_str.replace('*','',1)
#     if el == '/':
#         operator = op_str.index('/')
#         result = int(num_list[operator])/int(num_list[operator+1])
#         num_list[operator] = result
#         num_list.pop(operator+1)
#         op_str = op_str.replace('/','',1)
        
# for el in op_str:
#     if el == '+':
#         operator = op_str.index('+')
#         result = int(num_list[operator])+int(num_list[operator+1])
#         num_list[operator] = result
#         num_list.pop(operator+1)
#         op_str = op_str.replace('+','',1)
#     if el == '-':
#         operator = op_str.index('-')
#         result = int(num_list[operator])-int(num_list[operator+1])
#         num_list[operator] = result
#         num_list.pop(operator+1)
#         op_str = op_str.replace('-','',1)

# print(f'{string1} = {result}')


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