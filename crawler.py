import PySimpleGUI as sg
import time
import threading
import re
from programa import *
from pytz import timezone
from datetime import datetime
import re
import json
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import pickle
from pytz import timezone
from datetime import datetime
import pyperclip
import json
import logging
from regexS import *
from cria_config import *

logging.basicConfig(filename='logs.log', level=logging.ERROR)
#debug:
#import pdb
#pdb.set_trace()

data_e_hora_atuais = datetime.now()
#data_e_hora_atuais = datetime.date.today()
fuso_horario = timezone('America/Bogota')
data_e_hora_acre = data_e_hora_atuais.astimezone(fuso_horario)
#data_e_hora_acre_em_texto = data_e_hora_acre.strftime('%d-%m-%Y_%H;%M-%S')
hora_acre_em_texto = data_e_hora_acre.strftime('%H:%M-%S')
data_hoje = data_e_hora_acre.strftime('%d/%m/%Y')

def copiar_tab1_func(window):
    with open("dados.txt", "r") as d:
        texto = d.read()
    pyperclip.copy(texto)
    pyperclip.paste()
    texto_cortado = texto.count('\n')
    window['resultado_operacoes_aba1'].update(f'Copiado [{texto_cortado}] registros do arquivo: dados.txt.')
    d.close()
    texto_cortado=''
    texto=''

def copiar_tab2_func(texto2, window):    
    pyperclip.copy(texto2)
    pyperclip.paste()
    texto_cortado2 = texto2.count('\n')
    window['resultado_operacoes_aba2'].update(f'Copiado [{texto_cortado2}] registros.')
    texto2 = ''
    texto_cortado2 = ''

def principal(window,pesquisa, data_inicio, hora_inicio, data_fim, hora_fim):
        auto = Automatizacao(pesquisa, data_inicio, hora_inicio, data_fim, hora_fim)
        auto.navegador(None)
        auto.start_programa()
        todos_os_dados = auto.fim_func()
        todos_os_dados_contado = todos_os_dados.count('\n')
        print(f'Quantidade de dados encontrado: {todos_os_dados_contado}.')    
        window.write_event_value('_evento_final_', '')  
    
def formata_html(texto_html):
    #print('Compilado all')
    remover_tags = re.sub(r'<.+?>', r'\t',texto_html, flags=re.S)
    #print('remover_tags all')
    remover_nbsp = re.sub(r"&nbsp;", '',remover_tags)
    #print('remover_nbsp all')
    remover_cabecalho = regex_remove_cabecalho.sub('',remover_nbsp)
    #print('Remove all')
    troca_ponto_virgula = re.sub( r'\.', ',' , remover_cabecalho)
    #print('troca_ponto_virgula all')
    remover_tabs_inicio_linha = regex_remove_ns_tab.sub('',troca_ponto_virgula)
    rem_tabs = regex_tab_inicio_linha.sub('',remover_tabs_inicio_linha)
    remover_dupla_linha = re.sub(r'\n+', r'\n', rem_tabs)
    primeira_linha = re.sub(r'\n', '', remover_dupla_linha, count=1)
    #print('primeira_linha all')

    final_tab2 = regex_tabela_html.sub(r'\g<DATA_HORA>\t\g<chuva_hora>',primeira_linha)
    
    final_tab2 = final_tab2.split('\n')
    final_tab2.reverse()
    result_tab2 = ''
    for x in final_tab2:
        result_tab2 = result_tab2 + x + '\n'
        
    result_tab2 = re.sub(r'\n', '', result_tab2, count=1)
    #input(self.result)
    return result_tab2

def validar_campos(values, window):    
    if values['campo_pesquisa'] == '':
        sg.popup('Erro!', 'Campo de pesquisa vazio!')
        window.FindElement('campo_pesquisa').SetFocus() 
    elif values['campo_pesquisa'] not in lista_estacoes_pesquisa_config:
        sg.popup('Erro!', 'Campo de pesquisa não é uma estação válida!')
        window.FindElement('campo_pesquisa').SetFocus() 
    elif values['calendario_inicio'] == '':
        sg.popup('Erro!', 'Campo de data inicial vazia!')
        window.FindElement('calendario_inicio').SetFocus() 
    elif not(regex_data.match(values['calendario_inicio'])):
        sg.popup('Erro!', 'Campo de data inicial com formato incorreto!')
        window.FindElement('calendario_inicio').SetFocus() 
    elif values['hora_inicio'] == '':
        sg.popup('Erro!', 'Campo de hora inicial vazio!')
        window.FindElement('hora_inicio').SetFocus() 
    elif not(regex_hora.match(values['hora_inicio'])):
        sg.popup('Erro!', 'Campo de hora inicial com formato incorreto!')
        window.FindElement('hora_inicio').SetFocus() 
    elif values['calendario_fim'] == '':
        sg.popup('Erro!', 'Campo de data final vazio!')
        window.FindElement('calendario_fim').SetFocus() 
    elif not(regex_data.match(values['calendario_fim'])):
        sg.popup('Erro!', 'Campo de data final com formato incorreto!')
        window.FindElement('calendario_fim').SetFocus() 
    elif values['hora_fim'] == '':
        sg.popup('Erro!', 'Campo de hora final vazio!')
        window.FindElement('hora_fim').SetFocus() 
    elif not(regex_hora.match(values['hora_fim'])):
        sg.popup('Erro!', 'Campo de hora final com formato incorreto!')
        window.FindElement('hora_fim').SetFocus() 
    else:
        iniciar_crawler(values, window)
        
def iniciar_crawler(values, window):
    data_e_hora_atuais = datetime.now()
    #data_e_hora_atuais = datetime.date.today()
    fuso_horario = timezone('America/Bogota')
    data_e_hora_acre = data_e_hora_atuais.astimezone(fuso_horario)
    #data_e_hora_acre_em_texto = data_e_hora_acre.strftime('%d-%m-%Y_%H;%M-%S')
    hora_acre_em_texto = data_e_hora_acre.strftime('%H:%M-%S')
    print(f'Iniciando [{hora_acre_em_texto}]...')
    
    horario_inicio = values['hora_inicio'][:5] 
    horario_fim = values['hora_fim'][:5]
    
    threading.Thread(target=principal, args=(window,values['campo_pesquisa'], values['calendario_inicio'], horario_inicio, values['calendario_fim'], horario_fim), daemon=True).start()
    
def make_window():
    tema_config = ler_config()["tema"]
    # Set theme based on previously saved
    sg.theme(sg.user_settings_get_entry('theme', tema_config))
    
    aba1 = [
        [sg.Text(' Escolha a estação: ')],
        [sg.Input(size=(70, 1), enable_events=True, key='campo_pesquisa'), sg.Button(' Limpar ',  pad=(10,0,0,0), key='limpar_pesquisa')],
        [sg.Listbox(lista_estacoes_pesquisa_config, size=(70, 10), enable_events=True, key='lista_estacoes')],
        [sg.In(data_hoje,key='calendario_inicio', size=(9,1), change_submits=True, do_not_clear=True), sg.Text('ex: 29/02/2020', pad=(0,0)), sg.CalendarButton('Data de Início',  target='calendario_inicio', format='%d/%m/%Y', locale='de_DE', no_titlebar=True, begin_at_sunday_plus=1 , month_names=('Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro')), 
        sg.In(config_json["hora_inicio"],key='hora_inicio', size=(5,1), change_submits=True, do_not_clear=True ), 
        sg.T(': ex: [00:00]', pad=(0,0)), 
        sg.Text('Hora iní.'),
        sg.Button(' Limpar ', key='limpar_data_hora_inicio')],
        [sg.In(data_hoje,key='calendario_fim', size=(9,1), change_submits=True, do_not_clear=True), sg.Text('ex: 29/02/2020', pad=(0,0)), sg.CalendarButton(' Data de final ',  pad=(4,4), target='calendario_fim', format='%d/%m/%Y', locale='de_DE', no_titlebar=True, begin_at_sunday_plus=1 , month_names=('Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro')), 
        sg.In(config_json["hora_fim"],key='hora_fim', size=(5,1), change_submits=True, do_not_clear=True ), 
        sg.T(': ex: [23:59]', pad=(0,0)),
        sg.Text('Hora fin.'),
        sg.Button('Buscar', key='busca_ana'),
        sg.Button(' Limpar ', key='limpar_data_hora_fim')],
        [sg.Output(key='logs_tab1', size=(70,20))], #Output |
        [sg.Button(' Valores '),sg.Button(' Limpar ', key='limpar_input_tab1'),sg.Button(' Copiar dados ', key="copiar_tab1"), sg.Text('', size=(45,1), key='resultado_operacoes_aba1')],       
    ]#[sg.Output(key='logs_tab1', size=(70,20), echo_stdout_stderr=False)], #Output |
    aba2 = [[sg.Multiline(key='logs_tab2', size=(70,38))], # 
            [sg.Button(" Abrir arquivo "), sg.Button(' Limpar ', key='limpar_input_tab2'), sg.Button(" Copiar dados ", key="copiar_tab2"), sg.Text('', size=(36,1), key='resultado_operacoes_aba2')]
            ]
    grupo_tab = [[sg.Tab(' Busca ', aba1, font='Courier 15', key='_TAB1_'),
                    sg.Tab(' Excel ', aba2, font='Courier 15', key='_TAB2_'),                     
                ]
                ]
               
    layout = [[sg.Text(" Tema:"), sg.Combo(sg.theme_list(), default_value=tema_config, k='_THEME_LIST_', readonly=True, enable_events=True)], 
        [sg.TabGroup(grupo_tab,
            enable_events=True,
            key='_TABGROUP_')],
        [sg.Button(' Fechar programa ', key="fechar_programa")]]
    tab_keys = ('_TAB1_','_TAB2_')  
    return sg.Window(config_json["titulo"], layout, icon=config_json["icone"], no_titlebar=False, grab_anywhere=False, finalize=True)

def while_func():
    window = make_window()
    while True:             # Event Loop
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == 'fechar_programa':
            break
        if event == '_THEME_LIST_':
            window.close()
            sg.user_settings_set_entry('theme', values['_THEME_LIST_'])
            configuracao['tema'] = values['_THEME_LIST_']
            cria_config_file(configuracao)                       
            window = make_window()    
        if event == 'copiar_tab1':
            copiar_tab1_func(window)
        if event == 'copiar_tab2':
            if len(values['logs_tab2']) == 1:
                sg.popup("Erro!", "Sem dados!")
            else:
                window['resultado_operacoes_aba2'].update('')
                with open('dados_excel.txt', 'r') as copiar_dd_excel:
                    copiar_tab2_func(copiar_dd_excel.read(), window)
        if event == 'calendario_inicio':
            window.FindElement(event).Update(re.sub("[^0-9/]", "", values[event]))
        if event == 'calendario_inicio' and len(window.FindElement(event).Get()) == 2:
            window.FindElement(event).Update(values[event] + '/')
        if event == 'calendario_inicio' and len(window.FindElement(event).Get()) == 5:
            window.FindElement(event).Update(values[event] + '/')
        if event == 'calendario_inicio' and len(window.FindElement(event).Get()) == 10:
            window.FindElement('hora_inicio').SetFocus() 
            
        if event == 'calendario_fim':
            window.FindElement(event).Update(re.sub("[^0-9/]", "", values[event]))
        if event == 'calendario_fim' and len(window.FindElement(event).Get()) == 2:
            window.FindElement(event).Update(values[event] + '/')
        if event == 'calendario_fim' and len(window.FindElement(event).Get()) == 5:
            window.FindElement(event).Update(values[event] + '/')
        if event == 'calendario_fim' and len(window.FindElement(event).Get()) == 10:
            window.FindElement('hora_fim').SetFocus() 
            
        if event == 'hora_inicio':
            window.FindElement(event).Update(re.sub("[^0-9:]", "", values[event]))
        if event == 'hora_inicio' and len(window.FindElement(event).Get()) == 2:
            window.FindElement(event).Update(values[event] + ':')
        if event == 'hora_inicio' and len(window.FindElement(event).Get()) == 5:
            window.FindElement('calendario_fim').SetFocus() 
            #len(window.FindElement(event).Get()) == 2
            #window.FindElement(event).Update(re.sub("(\d{2})(.+)", "\1", values[event]))
            
        if event == 'hora_fim':
            window.FindElement(event).Update(re.sub("[^0-9:]", "", values[event]))
        if event == 'hora_fim' and len(window.FindElement(event).Get()) == 2:
            window.FindElement(event).Update(values[event] + ':')
        if event == 'hora_fim' and len(window.FindElement(event).Get()) == 5:
            window.FindElement('busca_ana').SetFocus() 
            #len(window.FindElement(event).Get()) == 2
            #window.FindElement(event).Update(re.sub("(\d{2})(.+)", "\1", values[event]))
        if event == '_TABGROUP_':
            window['campo_pesquisa'].update('')
            window['logs_tab1'].update('')
            window['logs_tab2'].update('')
            window['lista_estacoes'].update(lista_estacoes_pesquisa_config)
            window['resultado_operacoes_aba1'].update('')
        if event == 'limpar_pesquisa':
            window['campo_pesquisa'].update('')
            window['lista_estacoes'].update(lista_estacoes_pesquisa_config)
            window['resultado_operacoes_aba1'].update('')
            #sg.popup(texto)
            continue
        if event == 'limpar_data_hora_inicio':
            window['calendario_inicio'].update('')
            window['hora_inicio'].update('')
            window['resultado_operacoes_aba1'].update('')
            #sg.popup(texto)
            continue
        if event == 'limpar_data_hora_fim':
            window['calendario_fim'].update('')
            window['hora_fim'].update('')
            window['resultado_operacoes_aba1'].update('')
            #sg.popup(texto)
            continue
        if values['campo_pesquisa'] != '':
            search = values['campo_pesquisa']
            search = str(search).upper()
            new_values = [x for x in lista_estacoes_pesquisa_config if search in x]  # do the filtering
            window['lista_estacoes'].update(new_values)     # display in the listbox
        else:
            # display original unfiltered list
            window['lista_estacoes'].update(lista_estacoes_pesquisa_config)
        # if a list item is chosen
        if event == 'lista_estacoes' and len(values['lista_estacoes']):
            listVALUE = ['']
            listVALUE[0] = values['lista_estacoes']
            new_values = values['lista_estacoes']
            new_values = re.sub(r"\'|\[|\]", "", str(new_values))
            window['campo_pesquisa'].update(new_values)
            window['lista_estacoes'].update(listVALUE[0])
            
        if event == ' Valores ':
            campos = 'Estação: ' + values['campo_pesquisa'] + '\nData e hora de início: ' + values['calendario_inicio'] + ' ' + values['hora_inicio'][:5] + '\nData e hora de fim: ' + values['calendario_fim'] + ' ' + values['hora_fim'][:5]
            sg.popup('Valores dos campos', campos)
        if event == 'limpar_input_tab1':
            window['logs_tab1'].update('')
            window['resultado_operacoes_aba1'].update('')
        if event == 'limpar_input_tab2':
            window['logs_tab2'].update('')
            window['resultado_operacoes_aba2'].update('')
        elif event == 'busca_ana':
            window['logs_tab1'].update('')
            validar_campos(values, window)
            window['resultado_operacoes_aba1'].update('')
        elif event == '_evento_final_':
            data_e_hora_atuais = datetime.now()
            #data_e_hora_atuais = datetime.date.today()
            fuso_horario = timezone('America/Bogota')
            data_e_hora_acre = data_e_hora_atuais.astimezone(fuso_horario)
            #data_e_hora_acre_em_texto = data_e_hora_acre.strftime('%d-%m-%Y_%H;%M-%S')
            hora_acre_em_texto = data_e_hora_acre.strftime('%H:%M-%S')
            print(f'Finalizado! [{hora_acre_em_texto}]')
        if event == ' Abrir arquivo ':
            
            try:
                filename = sg.popup_get_file('Selecione o arquivo: ', file_types=(("Excel Files","*.xls"),))
                with open(filename, "r") as infile:                    
                    texto3 = infile.read()
                    selector = Selector(text=str(texto3))
                    dados_tabela = selector.xpath('//*[@id="cphCorpo_gdDados"]').get()
                    dados_formatados = formata_html(dados_tabela) #type(dados_formatados) => str
                    #.popup("Erro!", "atrioiiii")
                    dados_copiar_tab2 = str(dados_formatados)
                    with open('dados_excel.txt', 'w') as f_dd_excel:
                        f_dd_excel.write(dados_copiar_tab2)
                    
                    f_dd_excel.close()
                    linhas = ''
                    with open('dados_excel.txt', 'r') as fp:
                        line = fp.readline()                        
                        cnt = 0
                        while line:
                            line = fp.readline()
                            linhas = linhas + line
                            cnt += 1
                            if cnt == 100:
                                break
                                
                    fp.close()
                window['logs_tab2'].update(str(linhas))
                dados_formatados = ''
                dados_tabela = ''
                line = ''
                selector = ''
                linhas = ''
                infile.close()
                dados_copiar_tab2 = ''
                window['resultado_operacoes_aba2'].update('')
                
            except:
                sg.popup("Erro!", "Selecione o arquivo")
                
            
                

              
    
        

    window.close()

if __name__ == '__main__':
    while_func()