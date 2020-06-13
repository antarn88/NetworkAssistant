class Hungarian:
    def __init__(self):
        # Main app
        self.main_app_title = "Network Assistant"

        # Menu
        self.menubar_lang = "Nyelv"
        self.menubar_lang_eng = "Angol"
        self.menubar_lang_hun = "Magyar"

        # Tabs
        self.tab_ip_information = "IP információk"
        self.tab_number_conversion = "Számátváltás"
        self.tab_ip_subnet_calculation = "Azonos méretű alhálózatokra bontás"
        self.tab_vlsm_calculation = "VLSM számítás"

        # IP information tab
        self.tab_ip_information_prefix_mask_conv = "Prefix-maszk konverzió"
        self.tab_ip_information_prefix_ptext = "Prefix"
        self.tab_ip_information_mask_ptext = "Maszk"
        self.tab_ip_information_conv_btn = "Konvertálás"

        self.tab_ip_information_ipinfo_gbox = "IP információk"

        self.tab_ip_information_ipadd_lab = "IP cím prefix-szel:"
        self.tab_ip_information_getinfo_btn = "Kérem az infókat!"

        self.tab_ip_information_copy_btn = "Másolás"
        self.tab_ip_information_ipclass_lab = "IP osztály:"
        self.tab_ip_information_ipclass_a_class_pri = "A osztályú privát cím"
        self.tab_ip_information_ipclass_a_class_pub = "A osztályú publikus cím"
        self.tab_ip_information_ipclass_b_class_pri = "B osztályú privát cím"
        self.tab_ip_information_ipclass_b_class_pub = "B osztályú publikus cím"
        self.tab_ip_information_ipclass_c_class_pri = "C osztályú privát cím"
        self.tab_ip_information_ipclass_c_class_pub = "C osztályú publikus cím"

        self.tab_ip_information_iptype_lab = "IP típus:"
        self.tab_ip_information_iptype_netadd = "Hálózatcím"
        self.tab_ip_information_iptype_broadd = "Szórási cím"
        self.tab_ip_information_iptype_hostadd = "Állomáscím"

        self.tab_ip_information_netadd_lab = "Hálózatcím:"
        self.tab_ip_information_mask_lab = "Alhálózati maszk:"
        self.tab_ip_information_firstip_lab = "Első kiosztható cím:"
        self.tab_ip_information_lastip_lab = "Utolsó kiosztható cím:"
        self.tab_ip_information_bcastip_lab = "Szórási cím:"
        self.tab_ip_information_nextnetip_lab = "Következő hálózatcím:"
        self.tab_ip_information_maxend_lab = "Maximum végpont a hálózatban:"

        self.tab_ip_information_warning01 = "Nem lehet üres a prefix és a maszk értéke is!"
        self.tab_ip_information_warning02 = "Hibás prefix! Ellenőrizd!"
        self.tab_ip_information_warning03 = "Hibás maszk! Ellenőrizd!"
        self.tab_ip_information_warning04 = "Nem lehet üres az IP cím/prefix mező!"
        self.tab_ip_information_warning05 = "Az általad megadott cím egy loopback cím, ami nem kiosztható!"
        self.tab_ip_information_warning06 = "Az általad megadott cím egy csoportcímzési cím, ami nem kiosztható!"
        self.tab_ip_information_warning07 = "Az általad megadott cím egy kutatási célokra fenntartott\n" \
                                            "cím, ami nem kiosztható!"
        self.tab_ip_information_warning08 = "Az általad megadott cím az alhálózati maszkok számára\n" \
                                            "fenntartott cím, ami nem kiosztható!"
        self.tab_ip_information_warning09 = "Hibás IP cím/prefix páros! Ellenőrizd!"

        # Number conversion tab
        self.tab_num_conv_inputbox_gbox_name = "Bemenet"
        self.tab_num_conv_inputbox_in_number_lab = "Bemeneti szám:"
        self.tab_num_conv_inputbox_bin_chkbox = "Bináris"
        self.tab_num_conv_inputbox_dec_chkbox = "Decimális"
        self.tab_num_conv_inputbox_hex_chkbox = "Hexadecimális"
        self.tab_num_conv_inputbox_conv_btn = "Átváltás"

        self.tab_num_conv_outputbox_gbox_name = "Kimenet"
        self.tab_num_conv_outputbox_copy_btn = "Másolás"
        self.tab_num_conv_outputbox_bin_lab = "Bináris:"
        self.tab_num_conv_outputbox_dec_lab = "Decimális:"
        self.tab_num_conv_outputbox_hex_lab = "Hexadecimális:"

        self.tab_num_conv_ip_mask_conv_gbox_name = "IP cím/maszk számátváltás"
        self.tab_num_conv_ip_mask_conv_in_lab = "Bemeneti IP cím/maszk:"
        self.tab_num_conv_ip_mask_conv_out_lab = "Kimeneti IP cím/maszk:"
        self.tab_num_conv_ip_mask_conv_dectobin = "Decimálisból binárisba"
        self.tab_num_conv_ip_mask_conv_bintodec = "Binárisból decimálisba"
        self.tab_num_conv_ip_mask_conv_copy_btn = "Másolás"
        self.tab_num_conv_ip_mask_conv_convert_btn = "Átváltás"

        self.byte_format_str = "byte formában:"
        self.tab_num_conv_warning01 = "A számátváltáshoz töltsd ki a bemeneti szám mezőt!"
        self.tab_num_conv_warning02 = "Hibás bináris szám! Ellenőrizd!"
        self.tab_num_conv_warning03 = "Hibás decimális szám! Ellenőrizd!"
        self.tab_num_conv_warning04 = "Hibás hexadecimális szám! Ellenőrizd!"
        self.tab_num_conv_warning05 = "A bemeneti IP cím/maszk mező nem lehet üres!"
        self.tab_num_conv_warning06 = "Érvénytelen decimális IP cím vagy maszk! Ellenőrizd!"
        self.tab_num_conv_warning07 = "Érvénytelen bináris IP cím vagy maszk! Ellenőrizd!"

        # Ip subnet calculation tab
        self.tab_ipsubnet_starting_net = "Kiindulási hálózatcím:"
        self.tab_ipsubnet_required_subnet_num = "Szükséges alhálózatszám:"
        self.tab_ipsubnet_calc_btn = "Számítás"
        self.tab_ipsubnet_cancel_btn = "Mégse"
        self.tab_ipsubnet_warning01 = "A kiindulási hálózatcím nem lehet üres!"
        self.tab_ipsubnet_warning02 = "Érvénytelen a kiindulási hálózatcím! Ellenőrizd!"
        self.tab_ipsubnet_warning03 = "Add meg, hogy hány alhálózatot szeretnél!"
        self.tab_ipsubnet_warning04 = "Érvénytelen az alhálózatszám megadása! Ellenőrizd!"
        self.tab_ipsubnet_warning05 = "Ennyi alhálózatot nem lehet legenerálni a megadott hálózati címhez!"

        # Table column names
        self.table_column_network_add = "Hálózatcím"
        self.table_column_ip_range = "IP tartomány"
        self.table_column_broadcast_add = "Szórási cím"
        self.table_column_subnet_mask = "Alhálózati maszk"
        self.table_column_prefix = "Prefix"
        self.table_column_addressable_host = "Címezhető host"

        # VLSM calculator tab
        self.tab_vlsm_starting_net = "Kiindulási hálózatcím:"
        self.tab_vlsm_starting_net_prefix = "Kiindulási hálózat prefixe (opcionális):"
        self.tab_vlsm_endpoint_nums = "Végpontszámok a hálózatokban (vesszővel válaszd el őket!):"
        self.tab_vlsm_calc_btn = "Számítás"
        self.tab_vlsm_warning01 = "A kiindulási hálózatcím nem lehet üres!"
        self.tab_vlsm_warning02 = "Érvénytelen a kiindulási hálózatcím! Ellenőrizd!"
        self.tab_vlsm_warning03 = "Add meg, hogy hány gépszámú hálózatokat szeretnél!"
        self.tab_vlsm_warning04 = "Érvénytelen a gépszámok megadása! Ellenőrizd!"
        self.tab_vlsm_warning05 = "Érvénytelen a kiindulási hálózat prefixe! Ellenőrizd!"
        self.tab_vlsm_warning06 = "Irreálisan sok állomást szeretnél!\nEllenőrizd az adatokat!"
        self.tab_vlsm_warning07 = "Túl sok állomást szeretnél egy 'B' osztályú /16 főhálózathoz képest!\n" \
                                  "Próbálkozz inkább egy 'A' osztályú kiindulási hálózattal, vagy egy\nkisebb prefix-szel!"
        self.tab_vlsm_warning08 = "Túl sok állomást szeretnél egy 'C' osztályú /24 főhálózathoz képest!\n" \
                                  "Próbálkozz inkább egy 'B' vagy egy 'A' osztályú kiindulási hálózattal, esetleg kisebb prefix-szel!"
        self.tab_vlsm_warning09a = "Túl sok állomást szeretnél egy"
        self.tab_vlsm_warning09b = "főhálózathoz képest!\nEllenőrizd az adatokat!"
