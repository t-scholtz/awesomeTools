from flask import Blueprint, render_template, request, flash, jsonify
import struct

numConverter = Blueprint('numConverter', __name__)

@numConverter.route('/baseConverter', methods=['GET', 'POST'])
def baseConverter():
    return render_template("baseConverter.html")

@numConverter.route('/unitConverter', methods=['GET', 'POST'])
def unitConverter():
    return render_template("unitConverter.html")





@numConverter.route('/deciUpdate', methods=['POST'])
def deciUpdate():
    data = request.get_json()
    
    decimal_value = int(data['decimalValue'])
    sign = int(data['unsignedSliderValue'])
    num_bits = (1 + int(data['bitSliderValue'])) * 8

    if sign == 0:
        absolute_value = abs(decimal_value)
        binary_value = '0b'+bin(absolute_value & ((1 << num_bits) - 1))[2:].zfill(num_bits)
        hex_value = '0x'+hex(absolute_value & ((1 << num_bits) - 1))[2:].zfill((num_bits + 3) // 4)
        if decimal_value < 0:
            binary_value = '-' + binary_value
            hex_value = '-' + hex_value
    elif sign == 1: 
        if decimal_value >0:
            binary_value = '0b'+bin(decimal_value & ((1 << num_bits) - 1))[2:].zfill(num_bits)
            hex_value = '0x' + hex(decimal_value & ((1 << num_bits) - 1))[2:].zfill((num_bits + 3) // 4)
        else:
            binary_value = '0b' + bin((1 << num_bits) - 1 - (-1*decimal_value) & ((1 << num_bits) - 1))[2:].zfill(num_bits)
            hex_value = '0x' + hex((1 << num_bits) - 1 - (-1*decimal_value) & ((1 << num_bits) - 1))[2:].zfill((num_bits + 3) // 4)
        
    elif sign == 2:
        binary_value = '0b'+bin(decimal_value & ((1 << num_bits) - 1))[2:].zfill(num_bits)
        hex_value = '0x'+hex(decimal_value & ((1 << num_bits) - 1))[2:].zfill((num_bits + 3) // 4)

    return jsonify({'binaryValue': binary_value, 'hexValue': hex_value})


@numConverter.route('/binUpdate', methods=['POST'])
def binUpdate():
    data = request.get_json()
    binary_value = str(data['binaryValue']).replace('0b', '')
    sign= int(data['unsignedSliderValue'])
    num_bits = (1 + int(data['bitSliderValue'])) * 8
    decimal_value=0
    if(sign==0):
        flag = 0
        if binary_value[0] == '-':
            flag = 1
            binary_value = binary_value.replace('-', '')
        for bit in binary_value:
            decimal_value = decimal_value * 2 + int(bit)
        if flag==1:
            decimal_value*=-1
        hex_value = '0x'+hex(abs(decimal_value) & ((1 << num_bits) - 1))[2:].zfill((num_bits + 3) // 4)
        if decimal_value < 0:
            hex_value = '-' + hex_value
    elif(sign==1):
        binary_value =binary_value.replace('-', '')
        sign_bit =binary_value[0]
        if sign_bit == 1:
            binary_value = ''.join('1' if bit == '0' else '0' for bit in binary_value)
        for bit in binary_value:
            decimal_value = decimal_value * 2 + int(bit)
        if sign_bit == 1:
            decimal_value = -decimal_value
        hex_value = '0x' + hex(decimal_value & ((1 << num_bits) - 1))[2:].zfill((num_bits + 3) // 4)
    elif(sign==2):
        binary_value =binary_value.replace('-', '')
        binary_value = int(binary_value, 2)
        hex_value = '0x'+hex(decimal_value & ((1 << num_bits) - 1))[2:].zfill((num_bits + 3) // 4)

    return jsonify({'hexValue': hex_value, 'decimalInput': decimal_value})

@numConverter.route('/hexUpdate', methods=['POST'])
def hexUpdate():
    data = request.get_json()
    
    hex_value = (data['hexValue']).replace('0x', '')
    sign= int(data['unsignedSliderValue'])
    num_bits= (1+int(data['bitSliderValue']))*8

    if(sign==0):
        flag = 0
        if hex_value[0] == '-':
            flag = 1
            hex_value = hex_value.replace('-', '')
        decimal_value = int(hex_value, 16)
        binary_value = '0b'+bin(decimal_value & ((1 << num_bits) - 1))[2:].zfill(num_bits)
        if flag==1:
            decimal_value*=-1
            binary_value+='-'
        binary_value = bin(decimal_value & ((1 << num_bits) - 1))
    elif(sign==1):
        binary_value = bin(decimal_value & ((1 << num_bits) - 1))
        ones_complement = '0b' + ''.join('1' if bit == '0' else '0' for bit in binary_value[2:])
        binary_value =ones_complement.zfill(num_bits + 2)
    elif(sign==2):
        binary_value = bin(decimal_value & ((1 << num_bits) - 1))[2:]
        twos_complement = bin((1 << num_bits) + decimal_value)[2:]
        binary_value= twos_complement.zfill(num_bits)

    return jsonify({'binaryValue': binary_value, 'decimalInput': decimal_value})

@numConverter.route('/updateFromReal', methods=['POST'])
def updateFromReal():
    data = request.get_json()
    
    real_value = float(data['realValue'])
    binOrHex= int(data['binOrHex'])

    if binOrHex==0:
        float_rep = struct.pack('!f', real_value)
        float_value = '0b' +''.join(format(byte, '08b') for byte in float_rep)
        double_rep = struct.pack('!d', real_value)
        double_value = '0b' +''.join(format(byte, '08b') for byte in double_rep)
    
    elif binOrHex==1:
        binary_representation = struct.pack('!f', real_value)
        float_value = '0x' +''.join(format(byte, '02X') for byte in binary_representation)
        hex_representation = struct.pack('!d', real_value)
        double_value = '0x' +''.join(format(byte, '02X') for byte in hex_representation)
    

    return jsonify({'double': double_value, 'float': float_value})