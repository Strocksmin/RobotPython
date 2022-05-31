import struct


def main(byte_stack):
    dict_c = {}
    dict_d = {}
    dict_for_return = {}
    dict_for_return['A1'] = struct.unpack_from('H', byte_stack, offset=4)[0]
    size_b = struct.unpack_from('I', byte_stack, offset=6)[0]
    address_b = struct.unpack_from('H', byte_stack, offset=10)[0]
    dict_for_return['A2'] = []
    for i in range(size_b):
        dict_b = {}
        dict_b['B1'] = struct.unpack_from('f', byte_stack, address_b)[0]
        address_b += 4
        dict_b['B2'] = struct.unpack_from('H', byte_stack, offset=address_b)[0]
        address_b += 2
        dict_for_return['A2'].append(dict_b)
    address_c = struct.unpack_from('I', byte_stack, offset=12)[0]
    dict_for_return['A3'] = dict_c
    dict_for_return['A4'] = dict_d

    dict_c['C1'] = struct.unpack_from('H', byte_stack, offset=address_c)[0]
    dict_c['C2'] = struct.unpack_from('b', byte_stack, offset=address_c+2)[0]
    dict_c['C3'] = struct.unpack_from('H', byte_stack, offset=address_c+3)[0]
    dict_c['C4'] = struct.unpack_from('h', byte_stack, offset=address_c+5)[0]
    dict_c['C5'] = struct.unpack_from('H', byte_stack, offset=address_c+7)[0]
    dict_c['C6'] = ''
    size_char = struct.unpack_from('H', byte_stack, offset=address_c+9)[0]
    address_char = struct.unpack_from('H', byte_stack, offset=address_c+11)[0]
    for y in range(size_char):
        dict_c['C6'] += (struct.unpack_from('c', byte_stack, address_char)[0]
                         .decode())
        address_char += 1
    dict_c['C7'] = struct.unpack_from('I', byte_stack, offset=address_c+13)[0]
    dict_c['C8'] = struct.unpack_from('h', byte_stack, offset=address_c+17)[0]

    dict_d['D1'] = []
    size_uint8 = struct.unpack_from('H', byte_stack, offset=16)[0]
    address_uint8 = struct.unpack_from('I', byte_stack, offset=18)[0]
    for y in range(size_uint8):
        dict_d['D1'].\
            append(struct.unpack_from('B', byte_stack, address_uint8)[0])
        address_uint8 += 1
    dict_d['D2'] = []
    size_int64 = struct.unpack_from('H', byte_stack, offset=22)[0]
    address_int64 = struct.unpack_from('H', byte_stack, offset=24)[0]
    for y in range(size_int64):
        dict_d['D2']. \
            append(struct.unpack_from('q', byte_stack, address_int64)[0])
        address_int64 += 8
    dict_d['D3'] = struct.unpack_from('I', byte_stack, offset=26)[0]

    return dict_for_return
