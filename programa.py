import PySimpleGUI as sg
import re
from parsel import Selector
from time import sleep
import json
from cria_config import *
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
from regexS import * 

try:
    configuracao_open = open("config.json") #se não conseguir abrir o arquivo de configuração, vai criar um novo
except IOError:
    print("Erro ao abrir: config.json")
    print("Criando o arquivo novamente...")
    cria_config_file(configuracao) # criar um arquivo de configuração novo
    
finally:    
    pass
def ler_config(): #ler o arquivo de configuração novo ou o antigo
    configuracao_open = open('config.json', 'r', encoding='utf8')
    return json.load(configuracao_open)

try: 
    config_json = ler_config() #se não conseguir ler o arquivo de configuração, vai criar um novo
except:
    print("Erro ao ler: config.json")
    print("Criando o arquivo novamente...")
    cria_config_file(configuracao) #cria um arquivo de configuração novo
    
config_json = ler_config()
titulo_config = config_json["titulo"]
icone_config = config_json["icone"]
lista_estacoes_pesquisa_config = config_json["lista_estacoes_pesquisa"]
tempo_minimo = config_json["tempo_minimo"]
WebDriverWait_time_maximo = config_json["WebDriverWait_time_maximo"]
WebDriverWait_time = config_json["WebDriverWait_time"]
file_cookies_file = config_json["cookies_file"]
tempo_padrao = config_json["tempo_padrao"]
xpath_pesquisa_config = config_json["xpath_pesquisa"]
xpath_selecione_estacao_config = config_json["xpath_selecione_estacao"]
xpath_botao_filtar_data_hora_config = config_json["xpath_botao_filtar_data_hora"]
xpath_not_dados_config = config_json["xpath_not_dados"]
xpath_tabela_html_config = config_json["xpath_tabela_html"]

class Automatizacao():
    def __init__(self, pesquisa, data_inicio, hora_inicio, data_final, hora_final):
        self.pesquisa = pesquisa
        self.data_inicio = data_inicio
        self.hora_inicio = hora_inicio
        self.data_final = data_final
        self.hora_final = hora_final  
        self.resultado_final = ''
        

    def navegador(self, method):
        
        print()
        print('Pesquisando: ' + self.pesquisa)
        print('Data início: ' + self.data_inicio)
        print('Hora início: ' + self.hora_inicio)
        print('Data final: '+ self.data_final)
        print('Hora final: ' + self.hora_final)
        print()
        
        data_e_hora_atuais = datetime.now()
        fuso_horario = timezone('America/Bogota')
        data_e_hora_acre = data_e_hora_atuais.astimezone(fuso_horario)
        #data_e_hora_acre_em_texto = data_e_hora_acre.strftime('%d-%m-%Y_%H;%M-%S')
        hora_acre_em_texto = data_e_hora_acre.strftime('%H:%M-%S')
        print(f"Abrindo o navegador [{hora_acre_em_texto}]...")
        
        self.driver = webdriver.Firefox()
        #self.driver = webdriver.Chrome()

        self.vars = {}

    def finalizar(self):
        self.driver.close()

    def start_programa(self):        

        #<selenium.webdriver.firefox.webdriver.WebDriver (session="1ef5a7f1-a740-4b3a-9662-aa0d9022c196")>
        nome_navegador = str(self.driver)
        nome_navegador = nome_navegador.split('.')
        n_navegador = nome_navegador[2]
        data_e_hora_atuais = datetime.now()
        fuso_horario = timezone('America/Bogota')
        data_e_hora_acre = data_e_hora_atuais.astimezone(fuso_horario)
        #data_e_hora_acre_em_texto = data_e_hora_acre.strftime('%d-%m-%Y_%H;%M-%S')
        hora_acre_em_texto = data_e_hora_acre.strftime('%H:%M-%S')
        print(f"[{n_navegador.upper()}] aberto! [{hora_acre_em_texto}]")
        print("Abrindo o site...")
        self.driver.get("http://www.snirh.gov.br/hidrotelemetria/serieHistorica.aspx")
        
        cookies = pickle.load(open(file_cookies_file, "rb"))
        for cookie in cookies:
            self.driver.add_cookie(cookie)
        
        data_e_hora_atuais = datetime.now()
        fuso_horario = timezone('America/Bogota')
        data_e_hora_acre = data_e_hora_atuais.astimezone(fuso_horario)
        #data_e_hora_acre_em_texto = data_e_hora_acre.strftime('%d-%m-%Y_%H;%M-%S')
        hora_acre_em_texto = data_e_hora_acre.strftime('%H:%M-%S')

        print(f"Abrindo séries históricas [{hora_acre_em_texto}]...")
        self.driver.get("http://www.snirh.gov.br/hidrotelemetria/serieHistorica.aspx")
        # 2 | setWindowSize | 970x1024 |  |
        #self.driver.set_window_size(970, 1024) #EM CASA
        #print("Definindo o tamanho da tela...")
        #self.driver.set_window_size(730, 865)

        
        #print("Criando cookies")
        #pickle.dump( self.driver.get_cookies() , open("cookies.pkl","w"))
        
    def fim_func(self):
        data_e_hora_atuais = datetime.now()
        fuso_horario = timezone('America/Bogota')
        data_e_hora_acre = data_e_hora_atuais.astimezone(fuso_horario)
        #data_e_hora_acre_em_texto = data_e_hora_acre.strftime('%d-%m-%Y_%H;%M-%S')
        hora_acre_em_texto = data_e_hora_acre.strftime('%H:%M-%S')
        #2d parte
        
        print(f"Esperando o campo [{xpath_pesquisa_config}] aparecer [{hora_acre_em_texto}]...")
        sleep(tempo_padrao) #=2
        
        try:#Esperando o menu Visualizar dados aparecer
            element = WebDriverWait(self.driver, WebDriverWait_time).until(
                EC.presence_of_element_located((By.XPATH, xpath_pesquisa_config))
            )
        finally:
            data_e_hora_atuais = datetime.now()
            fuso_horario = timezone('America/Bogota')
            data_e_hora_acre = data_e_hora_atuais.astimezone(fuso_horario)
            #data_e_hora_acre_em_texto = data_e_hora_acre.strftime('%d-%m-%Y_%H;%M-%S')
            hora_acre_em_texto = data_e_hora_acre.strftime('%H:%M-%S')
            print(f"Campo [{xpath_pesquisa_config}] apareceu [{hora_acre_em_texto}]...")


        self.driver.find_element(By.XPATH, xpath_pesquisa_config).send_keys(Keys.CONTROL + 'a')
        self.driver.find_element(By.XPATH, xpath_pesquisa_config).send_keys(self.pesquisa[15:])
        self.driver.find_element(By.XPATH, xpath_pesquisa_config).send_keys(Keys.ENTER)
        
        
        data_e_hora_atuais = datetime.now()
        fuso_horario = timezone('America/Bogota')
        data_e_hora_acre = data_e_hora_atuais.astimezone(fuso_horario)
        #data_e_hora_acre_em_texto = data_e_hora_acre.strftime('%d-%m-%Y_%H;%M-%S')
        hora_acre_em_texto = data_e_hora_acre.strftime('%H:%M-%S')
        
        print(f"Esperando [FILTRO DE DATA E HORA] aparecer [{hora_acre_em_texto}]...")
        sleep(tempo_padrao) #=2
        try:#Esperando o menu Visualizar dados aparecer
            element = WebDriverWait(self.driver, WebDriverWait_time).until(
                EC.presence_of_element_located((By.XPATH, xpath_selecione_estacao_config))
            )
        finally:
            data_e_hora_atuais = datetime.now()
            fuso_horario = timezone('America/Bogota')
            data_e_hora_acre = data_e_hora_atuais.astimezone(fuso_horario)
            #data_e_hora_acre_em_texto = data_e_hora_acre.strftime('%d-%m-%Y_%H;%M-%S')
            hora_acre_em_texto = data_e_hora_acre.strftime('%H:%M-%S')
            print(f"Filtrando data e hora [{hora_acre_em_texto}]...")
            sleep(tempo_minimo)
            self.driver.find_element(By.ID, "cphCorpo_ctl01_txtPeriodoDe").send_keys(Keys.CONTROL + 'a')
            sleep(tempo_minimo)
            self.driver.find_element(By.ID, "cphCorpo_ctl01_txtPeriodoDe").send_keys(self.data_inicio)
            sleep(tempo_minimo)
            self.driver.find_element(By.ID, "cphCorpo_ctl01_txtPeriodoDeHr").send_keys(Keys.CONTROL + 'a')
            sleep(tempo_minimo)
            self.driver.find_element(By.ID, "cphCorpo_ctl01_txtPeriodoDeHr").send_keys(self.hora_inicio)
            sleep(tempo_minimo)
            self.driver.find_element(By.ID, "cphCorpo_ctl01_txtPeriodoA").send_keys(Keys.CONTROL + 'a')
            sleep(tempo_minimo)
            self.driver.find_element(By.ID, "cphCorpo_ctl01_txtPeriodoA").send_keys(self.data_final)
            sleep(tempo_minimo)
            self.driver.find_element(By.ID, "cphCorpo_ctl01_txtPeriodoAHr").send_keys(Keys.CONTROL + 'a')
            sleep(tempo_minimo)
            self.driver.find_element(By.ID, "cphCorpo_ctl01_txtPeriodoAHr").send_keys(self.hora_final)
            sleep(tempo_minimo)
            self.driver.find_element(By.XPATH, xpath_botao_filtar_data_hora_config).click()
            sleep(tempo_minimo)

        #/html/body/form/div[5]/div[2]/div[8]/div[1]/div/select/option[@title="5 - 13600002 - RIO BRANCO"]'
        xpath_result_pesquisa = '/html/body/form/div[5]/div[2]/div[8]/div[1]/div/select/option[@title="'+self.pesquisa+'"]' #resultado pesquisa
        
        data_e_hora_atuais = datetime.now()
        fuso_horario = timezone('America/Bogota')
        data_e_hora_acre = data_e_hora_atuais.astimezone(fuso_horario)
        hora_acre_em_texto = data_e_hora_acre.strftime('%H:%M-%S')

        print(f'Esperando o resultado da pesquisa aparecer [{hora_acre_em_texto}]...')
        sleep(tempo_padrao) #=2
        
        element = WebDriverWait(self.driver, WebDriverWait_time_maximo).until(
                EC.presence_of_element_located((By.XPATH, xpath_result_pesquisa))
            )
            
        data_e_hora_atuais = datetime.now()
        fuso_horario = timezone('America/Bogota')
        data_e_hora_acre = data_e_hora_atuais.astimezone(fuso_horario)
        #data_e_hora_acre_em_texto = data_e_hora_acre.strftime('%d-%m-%Y_%H;%M-%S')
        hora_acre_em_texto = data_e_hora_acre.strftime('%H:%M-%S')
        
        print(f'Clicando no resultado da pesquisa: [{self.pesquisa}] [{hora_acre_em_texto}]')
        sleep(tempo_padrao) #=2
        
        element = WebDriverWait(self.driver, WebDriverWait_time_maximo).until(
                EC.presence_of_element_located((By.XPATH, xpath_result_pesquisa))
            )
        sleep(tempo_padrao)
        self.driver.find_element(By.XPATH, xpath_result_pesquisa).click()

        pesquisa_result = re.sub(r'[ ][\-][ ]SEDE', '', self.pesquisa)
        #xpath_estado_na_tabela = '//*[@id="cphCorpo_gdDados"]/tbody/tr[2][td="Estação: 5 - 12370000 - THAUMATURGO"]/td'
        xpath_estado_na_tabela = '//*[@id="cphCorpo_gdDados"]/tbody/tr[2][td="Estação: '+ pesquisa_result +'"]/td'


        data_e_hora_atuais = datetime.now()
        fuso_horario = timezone('America/Bogota')
        data_e_hora_acre = data_e_hora_atuais.astimezone(fuso_horario)
        #data_e_hora_acre_em_texto = data_e_hora_acre.strftime('%d-%m-%Y_%H;%M-%S')
        hora_acre_em_texto = data_e_hora_acre.strftime('%H:%M-%S')

        print(f'Esperando [{pesquisa_result}] aparecer na tabela [{hora_acre_em_texto}]')
        sleep(tempo_padrao) #=2
        element = WebDriverWait(self.driver, WebDriverWait_time_maximo).until(
                EC.presence_of_element_located((By.XPATH, xpath_estado_na_tabela))
            )
        
        data_e_hora_atuais = datetime.now()
        fuso_horario = timezone('America/Bogota')
        data_e_hora_acre = data_e_hora_atuais.astimezone(fuso_horario)
        #data_e_hora_acre_em_texto = data_e_hora_acre.strftime('%d-%m-%Y_%H;%M-%S')
        hora_acre_em_texto = data_e_hora_acre.strftime('%H:%M-%S')
        
        print(f'Esperando dados [{hora_acre_em_texto}]...')

        try:
            contem_dados = self.driver.find_element(By.XPATH, xpath_not_dados_config).text
            data_e_hora_atuais = datetime.now()
            fuso_horario = timezone('America/Bogota')
            data_e_hora_acre = data_e_hora_atuais.astimezone(fuso_horario)
            #data_e_hora_acre_em_texto = data_e_hora_acre.strftime('%d-%m-%Y_%H;%M-%S')
            hora_acre_em_texto = data_e_hora_acre.strftime('%H:%M-%S')
            print(f'{contem_dados} [{hora_acre_em_texto}].')
        except:
            data_e_hora_atuais = datetime.now()
            fuso_horario = timezone('America/Bogota')
            data_e_hora_acre = data_e_hora_atuais.astimezone(fuso_horario)
            #data_e_hora_acre_em_texto = data_e_hora_acre.strftime('%d-%m-%Y_%H;%M-%S')
            hora_acre_em_texto = data_e_hora_acre.strftime('%H:%M-%S')
            print('Dados obtidos.')
            print(f'Processando dados... [{hora_acre_em_texto}]')
            
            #tabela = ana.driver.find_element(By.XPATH, '/html/body/form/div[5]/div[2]/div[15]/div/table/tbody').text
            tabela = self.driver.find_element(By.XPATH, xpath_tabela_html_config).get_attribute('innerHTML')         
            #print(tabela)
            #input()
            remover_tags = re.sub(r'<.+?>', r"\t",tabela, flags=re.S)
            
            regex_nbsp = re.sub(r"&nbsp;", '',remover_tags)
            
            remover_cabecalho = regex_remove_cabecalho.sub('',regex_nbsp)
            
            troca_ponto_virgula = re.sub( r'\.', ',' , remover_cabecalho)               

            remover_tabs_inicio_linha = regex_tab_inicio_linha.sub('',troca_ponto_virgula)
            rem_tabs = regex_remove_ns_tab.sub('',remover_tabs_inicio_linha)
            remover_dupla_linha = re.sub(r'\n+', r'\n', rem_tabs)
            primeira_linha = re.sub(r'\n', '', remover_dupla_linha, count=1)
            
            self.resultado_final = regex_tabela_html.sub(r'\g<DATA_HORA>\t\g<chuva_hora>',primeira_linha)
            
            
            self.resultado_final = self.resultado_final.split('\n')
            self.resultado_final.reverse()
            self.result = ''
            for x in self.resultado_final:
                self.result = self.result + x + '\n'

            self.result = re.sub(r'\n', '', self.result, count=1)
            #input(self.result)
            #cont_dados = self.resultado_final.count('\n')
            ata_e_hora_atuais = datetime.now()
            fuso_horario = timezone('America/Bogota')
            data_e_hora_acre = data_e_hora_atuais.astimezone(fuso_horario)
            #data_e_hora_acre_em_texto = data_e_hora_acre.strftime('%d-%m-%Y_%H;%M-%S')
            hora_acre_em_texto = data_e_hora_acre.strftime('%H:%M-%S')
            with open('dados.txt', 'w', encoding='utf8') as dados:
                dados.write(self.result)
                print(f"Arquivo [dados.txt] gerado. [{hora_acre_em_texto}]")
            #print(resultado)
        return self.result
if __name__  == "__main__":
    auto = Automatizacao('5 - 13600002 - RIO BRANCO' ,'13/12/2020','00:00','13/12/2020','23:00')
    auto.navegador(None)
    auto.start_programa()
    tamto = auto.fim_func()    
    print(len(tamto))

#ana.teardown_method(None)
