import json
def cria_config_file(dados):
    with open('config.json', 'w', encoding='utf8') as f:
        json.dump(dados, f, ensure_ascii=False, sort_keys=True, indent=4, separators=(',', ':'))
        
configuracao = {    
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
    "xpath_selecione_estacao": '/html/body/form/div[5]/div[2]/div[15]/div/table/tbody/tr[td="Selecione uma esta????o"]/td',
    "xpath_botao_filtar_data_hora": '//*[@id="cphCorpo_ctl01_imbAplicarDrHr"]',
    "xpath_not_dados": '/html/body/form/div[5]/div[2]/div[15]/div/table/tbody/tr[4][td="N??o h?? registro para esta esta????o no per??odo selecionado"]/td',
    "xpath_tabela_html": '/html/body/form/div[5]/div[2]/div[15]/div/table/tbody',
    "lista_estacoes_pesquisa": ['5 - 00968006 - SENA MADUREIRA',
	'5 - 00970003 - SANTA ROSA',
	'5 - 00971002 - JORD??O',
	'5 - 12370000 - THAUMATURGO',
	'5 - 12390000 - PORTO WALTER',
	'5 - 12500000 - CRUZEIRO DO SUL',
	'5 - 12510500 - PONTE DO RIO LIBERDADE',
	'5 - 12557000 - JORD??O',
	'5 - 12590000 - PONTE DE TARAUAC??',
	'5 - 12640000 - SERINGAL SANTA HELENA',
	'5 - 12650000 - FEIJ??',
	'5 - 13169900 - SANTA ROSA DO PURUS - SEDE',
	'5 - 13180000 - MANOEL URBANO',
	'5 - 13310000 - SENA MADUREIRA',
	'5 - 13405000 - SERINGAL GUARANY',
	'5 - 13439000 - ALDEIA DOS PATOS',
	'5 - 13450000 - ASSIS BRASIL',
	'5 - 13470000 - BRASIL??IA',
	'5 - 13490000 - EPITACIOL??NDIA (Col??nia S??o Bento)',
	'5 - 13540000 - COL??NIA DOLORES (XAPURI)',
	'5 - 13550000 - XAPURI',
	'5 - 13568000 - CAPIXABA (Coloca????o S??o Jos??)',
	'5 - 13572000 - ESPALHA (Seringal Belo Horizonte)',
	'5 - 13578000 - RIO ROLA (Ramal do Barro Alto)',
	'5 - 13600002 - RIO BRANCO',
	'5 - 13610001 - PORTO ACRE'
    ]
}

if __name__  == "__main__":
    cria_config_file(configuracao)
    print("Criado com suceso!")
    input()