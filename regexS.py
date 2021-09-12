import re

regex_tabela_html = re.compile(r"(?P<DATA_HORA>\d{2}\/\d{2}\/\d{4}[ ]?\d{2}\:\d{2}:\d{2})(\t)?(\t)?(?P<chuva_hora>\d+,?\d+)?(\t)?(\t)?(?P<chuva_transmitida>\d+,?\d+)?(\t)?(\t)?(?P<chuva_adotada>\d+,?\d+)?(\t)?(\t)?(?P<nivel_pressao>\d+,?\d+)?(\t)?(\t)?(?P<nivel_display>\d+,?\d+)?(\t)?(\t)?(?P<nivel_manual>\d+,?\d+)?(\t)?(\t)?(?P<nivel_adotado>\d+,?\d+)?(\t)?(\t)?(?P<vazao>\d+,?\d+)?(\t)?(\t)?(?P<bateria>\d+,?\d+)?(\t)?(\t)?(?P<temp_interna>\d+,?\d+)?", re.M)

regex_remove_cabecalho = re.compile(r'Qualidade.+Interna' , re.M | re.S)

regex_remove_ns_tab = re.compile(r'^\t+' , re.M | re.S)

regex_tab_inicio_linha = re.compile(r'\t+?$' , re.M | re.S)

regex_data = re.compile(r"^(?:(?:31(\/)(?:0[13578]|1[02]))\1|(?:(?:29|30)(\/)(?:0[13-9]|1[0-2])\2))(?:(?:1[6-9]|[2-9]\d)?\d{2})$|^(?:29(\/)02\3(?:(?:(?:1[6-9]|[2-9]\d)?(?:0[48]|[2468][048]|[13579][26])|(?:(?:16|[2468][048]|[3579][26])00))))$|^(?:0[1-9]|1\d|2[0-8])(\/)(?:(?:0[1-9])|(?:1[0-2]))\4(?:(?:1[6-9]|[2-9]\d)?\d{2})$")

regex_hora = re.compile(r"^(0[0-9]|1[0-9]|2[0-3]):[0-5][0-9]$")

'''configuracao_aqui = {    
    "titulo": "Crawler: Sistema HIDRO - Telemetria",
    "tema": "DarkGrey",
    "opcoes_tema": ['Black', 'BlueMono', 'BluePurple', 'BrightColors', 'BrownBlue', 'Dark', 'Dark2', 'DarkAmber', 'DarkBlack', 'DarkBlack1', 'DarkBlue', 'DarkBlue1', 'DarkBlue10', 'DarkBlue11', 'DarkBlue12', 'DarkBlue13', 'DarkBlue14', 'DarkBlue15', 'DarkBlue16', 'DarkBlue17', 'DarkBlue2', 'DarkBlue3', 'DarkBlue4', 'DarkBlue5', 'DarkBlue6', 'DarkBlue7', 'DarkBlue8', 'DarkBlue9', 'DarkBrown', 'DarkBrown1', 'DarkBrown2', 'DarkBrown3', 'DarkBrown4', 'DarkBrown5', 'DarkBrown6', 'DarkBrown7', 'DarkGreen', 'DarkGreen1', 'DarkGreen2', 'DarkGreen3', 'DarkGreen4', 'DarkGreen5', 'DarkGreen6', 'DarkGreen7', 'DarkGrey', 'DarkGrey1', 'DarkGrey10', 'DarkGrey11', 'DarkGrey12', 'DarkGrey13', 'DarkGrey14', 'DarkGrey2', 'DarkGrey3', 'DarkGrey4', 'DarkGrey5', 'DarkGrey6', 'DarkGrey7', 'DarkGrey8', 'DarkGrey9', 'DarkPurple', 'DarkPurple1', 'DarkPurple2', 'DarkPurple3', 'DarkPurple4', 'DarkPurple5', 'DarkPurple6', 'DarkPurple7', 'DarkRed', 'DarkRed1', 'DarkRed2', 'DarkTanBlue', 'DarkTeal', 'DarkTeal1', 'DarkTeal10', 'DarkTeal11', 'DarkTeal12', 'DarkTeal2', 'DarkTeal3', 'DarkTeal4', 'DarkTeal5', 'DarkTeal6', 'DarkTeal7', 'DarkTeal8', 'DarkTeal9', 'Default', 'Default1', 'DefaultNoMoreNagging', 'Green', 'GreenMono', 'GreenTan', 'HotDogStand', 'Kayak', 'LightBlue', 'LightBlue1', 'LightBlue2', 'LightBlue3', 'LightBlue4', 'LightBlue5', 'LightBlue6', 'LightBlue7', 'LightBrown', 'LightBrown1', 'LightBrown10', 'LightBrown11', 'LightBrown12', 'LightBrown13', 'LightBrown2', 'LightBrown3', 'LightBrown4', 'LightBrown5', 'LightBrown6', 'LightBrown7', 'LightBrown8', 'LightBrown9', 'LightGray1', 'LightGreen', 'LightGreen1', 'LightGreen10', 'LightGreen2', 'LightGreen3', 'LightGreen4', 'LightGreen5', 'LightGreen6', 'LightGreen7', 'LightGreen8', 'LightGreen9', 'LightGrey', 'LightGrey1', 'LightGrey2', 'LightGrey3', 'LightGrey4', 'LightGrey5', 'LightGrey6', 'LightPurple', 'LightTeal', 'LightYellow', 'Material1', 'Material2', 'NeutralBlue', 'Purple', 'Python', 'Reddit', 'Reds', 'SandyBeach', 'SystemDefault', 'SystemDefault1', 'SystemDefaultForReal', 'Tan', 'TanBlue', 'TealMono', 'Topanga'],
	"icone": "img\icone.ico",
    "tempo_padrao": 2,
    "cookies_file": "cookies.pkl",
    "WebDriverWait_time": 40,
    "WebDriverWait_time_maximo": 500,
    "hora_inicio": "00:00",
    "hora_fim": "23:59",
    "tempo_minimo": 0.55,
    "xpath_pesquisa": '//*[@id="cphCorpo_ctl01_txtPesquisa"]',
    "xpath_selecione_estacao": '/html/body/form/div[5]/div[2]/div[15]/div/table/tbody/tr[td="Selecione uma estação"]/td',
    "xpath_botao_filtar_data_hora": '//*[@id="cphCorpo_ctl01_imbAplicarDrHr"]',
    "xpath_not_dados": '/html/body/form/div[5]/div[2]/div[15]/div/table/tbody/tr[4][td="Não há registro para esta estação no período selecionado"]/td',
    "xpath_tabela_html": '/html/body/form/div[5]/div[2]/div[15]/div/table/tbody'
}
'''