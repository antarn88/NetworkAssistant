class English:
    def __init__(self):
        # Main app
        self.main_app_title = "Network Assistant"

        # Menu
        self.menubar_lang = "Language"
        self.menubar_lang_eng = "English"
        self.menubar_lang_hun = "Hungarian"

        # Tabs
        self.tab_ip_information = "IP information"
        self.tab_number_conversion = "Number conversion"
        self.tab_ip_subnet_calculation = "IP subnet calculation"
        self.tab_vlsm_calculation = "VLSM calculation"

        # IP information tab
        self.tab_ip_information_prefix_mask_conv = "Prefix-mask conversion"
        self.tab_ip_information_prefix_ptext = "Prefix"
        self.tab_ip_information_mask_ptext = "Mask"
        self.tab_ip_information_conv_btn = "Convert"

        self.tab_ip_information_ipinfo_gbox = "IP information"

        self.tab_ip_information_ipadd_lab = "IP address with prefix:"
        self.tab_ip_information_getinfo_btn = "Get info"

        self.tab_ip_information_copy_btn = "Copy"
        self.tab_ip_information_ipclass_lab = "IP class:"
        self.tab_ip_information_ipclass_a_class_pri = "Class A, private address"
        self.tab_ip_information_ipclass_a_class_pub = "Class A, public address"
        self.tab_ip_information_ipclass_b_class_pri = "Class B, private address"
        self.tab_ip_information_ipclass_b_class_pub = "Class B, public address"
        self.tab_ip_information_ipclass_c_class_pri = "Class C, private address"
        self.tab_ip_information_ipclass_c_class_pub = "Class C, public address"

        self.tab_ip_information_iptype_lab = "IP type:"
        self.tab_ip_information_iptype_netadd = "Network address"
        self.tab_ip_information_iptype_broadd = "Broadcast address"
        self.tab_ip_information_iptype_hostadd = "Host address"

        self.tab_ip_information_netadd_lab = "Network address:"
        self.tab_ip_information_mask_lab = "Subnet mask:"
        self.tab_ip_information_firstip_lab = "First addressable IP:"
        self.tab_ip_information_lastip_lab = "Last addressable IP:"
        self.tab_ip_information_bcastip_lab = "Broadcast IP:"
        self.tab_ip_information_nextnetip_lab = "Next network address:"
        self.tab_ip_information_maxend_lab = "Maximum hosts in the network:"

        self.tab_ip_information_warning01 = "The prefix and mask values cannot be both empty!"
        self.tab_ip_information_warning02 = "Invalid prefix! Check it!"
        self.tab_ip_information_warning03 = "Invalid mask! Check it!"
        self.tab_ip_information_warning04 = "IP address/prefix field cannot be empty!"
        self.tab_ip_information_warning05 = "The address you entered is a loopback address which cannot be allocated!"
        self.tab_ip_information_warning06 = "The address you entered is a group addressing address which cannot be allocated!"
        self.tab_ip_information_warning07 = "The address you entered is a research reserved address which cannot be allocated!"
        self.tab_ip_information_warning08 = "The address you entered is a reserved address for subnet\n" \
                                            "masks which cannot be allocated!"
        self.tab_ip_information_warning09 = "Invalid IP address/prefix pair! Check it!"

        # Number conversion tab
        self.tab_num_conv_inputbox_gbox_name = "Input"
        self.tab_num_conv_inputbox_in_number_lab = "Input number:"
        self.tab_num_conv_inputbox_bin_chkbox = "Binary"
        self.tab_num_conv_inputbox_dec_chkbox = "Decimal"
        self.tab_num_conv_inputbox_hex_chkbox = "Hexadecimal"
        self.tab_num_conv_inputbox_conv_btn = "Convert"

        self.tab_num_conv_outputbox_gbox_name = "Output"
        self.tab_num_conv_outputbox_copy_btn = "Copy"
        self.tab_num_conv_outputbox_bin_lab = "Binary:"
        self.tab_num_conv_outputbox_dec_lab = "Decimal:"
        self.tab_num_conv_outputbox_hex_lab = "Hexadecimal:"

        self.tab_num_conv_ip_mask_conv_gbox_name = "IP address/mask number conversion"
        self.tab_num_conv_ip_mask_conv_in_lab = "Input IP address/mask:"
        self.tab_num_conv_ip_mask_conv_out_lab = "Output IP address/mask:"
        self.tab_num_conv_ip_mask_conv_dectobin = "From decimal to binary"
        self.tab_num_conv_ip_mask_conv_bintodec = "From binary to decimal"
        self.tab_num_conv_ip_mask_conv_copy_btn = "Copy"
        self.tab_num_conv_ip_mask_conv_convert_btn = "Convert"

        self.byte_format_str = "in byte format:"
        self.tab_num_conv_warning01 = "To convert the number, fill in the input number field!"
        self.tab_num_conv_warning02 = "Invalid binary number! Check it!"
        self.tab_num_conv_warning03 = "Invalid decimal number! Check it!"
        self.tab_num_conv_warning04 = "Invalid hexadecimal number! Check it!"
        self.tab_num_conv_warning05 = "The input IP address/mask field cannot be empty!"
        self.tab_num_conv_warning06 = "Invalid decimal IP address or mask! Check it!"
        self.tab_num_conv_warning07 = "Invalid binary IP address or mask! Check it!"

        # Ip subnet calculation tab
        self.tab_ipsubnet_starting_net = "Starting network address:"
        self.tab_ipsubnet_required_subnet_num = "Required subnet number:"
        self.tab_ipsubnet_calc_btn = "Calculate"
        self.tab_ipsubnet_cancel_btn = "Cancel"
        self.tab_ipsubnet_warning01 = "The starting network address cannot be empty!"
        self.tab_ipsubnet_warning02 = "Invalid starting network address! Check it!"
        self.tab_ipsubnet_warning03 = "Enter how many subnets you want!"
        self.tab_ipsubnet_warning04 = "Invalid subnet number entered! Check it!"
        self.tab_ipsubnet_warning05 = "This subnet number cannot be generated for the specified network address!"

        # Table column names
        self.table_column_network_add = "Network address"
        self.table_column_ip_range = "IP range"
        self.table_column_broadcast_add = "Broadcast address"
        self.table_column_subnet_mask = "Subnet mask"
        self.table_column_prefix = "Prefix"
        self.table_column_addressable_host = "Addressable host"

        # VLSM calculator tab
        self.tab_vlsm_starting_net = "Starting network address:"
        self.tab_vlsm_starting_net_prefix = "Prefix of starting network (optional):"
        self.tab_vlsm_endpoint_nums = "Endpoint numbers in the networks (separate with comma(s)):"
        self.tab_vlsm_calc_btn = "Calculate"
        self.tab_vlsm_warning01 = "The starting network address cannot be empty!"
        self.tab_vlsm_warning02 = "Invalid starting network address! Check it!"
        self.tab_vlsm_warning03 = "Enter how many host numbers you want per network!"
        self.tab_vlsm_warning04 = "Invalid host numbers entered! Check it!"
        self.tab_vlsm_warning05 = "The prefix of the starting network is invalid! Check it!"
        self.tab_vlsm_warning06 = "You want unrealistically too many hosts!\nCheck the data!"
        self.tab_vlsm_warning07 = "You want too many hosts compared to a class 'B' /16 main network!\n" \
                                  "Try a class 'A' starting network or a smaller prefix instead!"
        self.tab_vlsm_warning08 = "You want too many hosts compared to a class 'C' /24 main network!\n" \
                                  "Try a class 'B' or a class 'A' starting network, or a smaller prefix."
        self.tab_vlsm_warning09a = "You want too many hosts compared to a"
        self.tab_vlsm_warning09b = "main network!\nCheck the data!"
