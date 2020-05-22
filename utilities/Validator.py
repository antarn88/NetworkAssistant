from re import search


def is_empty(input_field):
    if input_field == "":
        return True
    return False


def is_correct_network_address(network_address):
    if not network_address.replace(".", "").isnumeric():
        return False
    for i in network_address.split("."):
        if not int(i) >= 0 or \
                not int(i) <= 255 or \
                not len(network_address.split(".")) == 4 or \
                not int(network_address.split(".")[-1]) % 2 == 0 or \
                search("^0|^127", network_address.split(".")[0]) or \
                int(network_address.split(".")[0]) > 223:
            return False
    return True


def is_correct_number_of_subnets(number_of_subnets):
    if number_of_subnets.isnumeric():
        return True
    return False


def is_correct_endpoint_numbers_per_network(endpoint_numbers_per_network):
    for i in endpoint_numbers_per_network.split(","):
        i = i.strip()
        if i.isnumeric() and int(i) != 0:
            return True
    return False


def is_correct_prefix(prefix):
    if prefix == "/" or prefix == "\\":
        return False
    prefix = prefix.replace("/", "").replace("\\", "")
    if prefix == "":
        return True
    elif prefix.isnumeric() and 8 <= int(prefix) <= 30:
        return True
    return False


def is_correct_any_ip_dec(ip_dec):
    if not ip_dec.replace(".", "").isnumeric():
        return False
    if not len(ip_dec.split(".")) == 4:
        return False
    for i in ip_dec.split("."):
        if int(i) < 0 or int(i) > 255:
            return False
    return True


def is_correct_any_ip_bin(ip_bin):
    container = set()
    if not len(ip_bin.split(".")) == 4:
        return False
    for i in ip_bin.split("."):
        for x in i:
            container.add(x)
    for b in container:
        if b != "0":
            if b != "1":
                return False
    return True


def is_correct_binary(binary_number):
    try:
        int(binary_number, 2)
        return True
    except ValueError:
        return False


def is_correct_decimal(decimal_number):
    if decimal_number.isnumeric():
        return True
    return False


def is_correct_hexadecimal(hexadecimal_number):
    try:
        int(hexadecimal_number, 16)
        return True
    except ValueError:
        return False


def is_correct_mask(mask):
    mask_32bit = ""
    if not mask.replace(".", "").isnumeric() or \
            str(mask).split(".")[0] != "255":
        return False
    for octet in mask.split("."):
        mask_32bit += f'{bin(int(octet)).replace("0b", "").rjust(8, "0")}'
    if not mask_32bit.startswith("1" * mask_32bit.count("1")) and \
            not mask_32bit.endswith("0" * mask_32bit.count("0")):
        return False
    for octet in mask.split("."):
        if int(octet) > 255 or \
                int(octet) < 0 or \
                len(mask.split(".")) != 4:
            return False
    if mask_32bit.count("1") > 30:
        return False
    return True


def is_correct_ip_with_prefix(ip_with_prefix):
    if "/" not in str(ip_with_prefix):
        return False
    elif len(str(ip_with_prefix).split("/")) != 2:
        return False
    elif not str(ip_with_prefix).split("/")[0].replace(".", "").isnumeric() or \
            not str(ip_with_prefix).split("/")[1].replace(".", "").isnumeric():
        return False
    for octet in str(str(ip_with_prefix).split("/")[0]).split("."):
        if int(octet) > 255:
            return False
    if not is_correct_prefix(str(ip_with_prefix).split("/")[1]):
        return False
    return True
