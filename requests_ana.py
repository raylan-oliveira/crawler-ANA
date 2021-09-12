import requests

cookies = {
    'GestorPCD_CookieLayout_Firefox': '~/PrincipalRhn.Master',
    'Seguranca_Cookie': '36380E90F492BD295CFE0288AF33B98CC528C564F8A180801DD69AC3C504C8D7BEAB97EB16DF412F9DA7DD7AF77AD41DD131A99AEFACE4A823475AE92C4A3062A88CF98382233588A0C03DB976E62C2824C40E6C60C46E50C2929BCCA5C4088F77CB1A8D0B9AF5722A3873939819197800837B81B2AFFFD4AD75E8B317227F124F4BF8977EE39CEAB45CF8800590D04270BA382ACA0A6E485F3E802CC5AC8B971134DD92158A25FCA62A2B69EBA5D4DA5754A05E0C24326460B9C83F8B1ECD9639713C3562B53C993A5F7F609BC6275C4D5B91B334B87831B9009D9ACB0A0E4A67983EB1898F80AF47E8EBDBCC435694229D4C649B5C43FCFFF5A6FF85AEF9E5E6A25C75B56BA710D40C928853DDE2A53C574D22AA43120B22953C66E869CA06DC8783EDD9C5AF8F6B3CB18861A9B9E3B5CCA8A8DA869F9E22CB9B74D185F785',
    'GestorPCD': '158',
    'ASP.NET_SessionId': 'ihh0cnekb3s3nurpy1jeggdu',
}

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:84.0) Gecko/20100101 Firefox/84.0',
    'Accept': '*/*',
    'Accept-Language': 'pt-BR,pt;q=0.8,en-US;q=0.5,en;q=0.3',
    'X-Requested-With': 'XMLHttpRequest',
    'X-MicrosoftAjax': 'Delta=true',
    'Cache-Control': 'no-cache',
    'Content-Type': 'application/x-www-form-urlencoded; charset=utf-8',
    'Origin': 'http://www.snirh.gov.br',
    'Connection': 'keep-alive',
    'Referer': 'http://www.snirh.gov.br/hidrotelemetria/serieHistorica.aspx',
}
#In [1]: type(data)
#dict
#data['ctl00$cphCorpo$ctl01$txtPeriodoDe']
#'17/12/2020'
data = {
  'ctl00$ScriptManager1': 'ctl00$cphCorpo$ctl01$UpdatePanel1|ctl00$cphCorpo$ctl01$lstEstacoes',
  'ctl00$hdfInPaste': 'False',
  'ctl00$cphCorpo$ctl01$rbTipo': '02',
  'ctl00$cphCorpo$ctl01$hdfOrigemAction': 'show',
  'ctl00$cphCorpo$ctl01$lstEstados': '2',
  'ctl00$cphCorpo$ctl01$lstOrigem': '0',
  'ctl00$cphCorpo$ctl01$lstBacia': '0',
  'ctl00$cphCorpo$ctl01$lstSub': '0',
  'ctl00$cphCorpo$ctl01$lstEstacoes': '95967480',
  'ctl00$cphCorpo$ctl01$rblPesquisaPor': '00',
  'ctl00$cphCorpo$ctl01$hdfValidaTxtPesquisa': 'ok',
  'ctl00$cphCorpo$ctl01$txtPesquisa': '',
  'ctl00$cphCorpo$ctl01$chkStatus$0': '00',
  'ctl00$cphCorpo$ctl01$chkTipoQualificacao$0': '00',
  'ctl00$cphCorpo$ctl01$chkTipoQualificacao$2': '02',
  'ctl00$cphCorpo$ctl01$chkTipoQualificacao$1': '01',
  'ctl00$cphCorpo$ctl01$chkTipoQualificacao$3': '99',
  'ctl00$cphCorpo$ctl01$txtPeriodoDe': '17/12/2020',
  'ctl00$cphCorpo$ctl01$txtPeriodoDeHr': '18:59',
  'ctl00$cphCorpo$ctl01$txtDifDatas': '7',
  'ctl00$cphCorpo$ctl01$txtPeriodoA': '24/12/2020',
  'ctl00$cphCorpo$ctl01$txtPeriodoAHr': '18:59',
  'ctl00$cphCorpo$ctl01$rbPeriodoDiario': '7',
  'ctl00$cphCorpo$ctl01$txtLinkCriado': '',
  'ctl00$cphCorpo$ctl01$txtCriterio2': '',
  'ctl00$cphCorpo$ctl01$ckbCriterio3': 'on',
  'ctl00$cphCorpo$ctl01$txtCriterio3': '',
  'ctl00$cphCorpo$ctl01$ckbCriterio4': 'on',
  'ctl00$cphCorpo$ctl01$txtCriterio4': '',
  'ctl00$cphCorpo$ctl01$txtCriterio5': '',
  'ctl00$cphCorpo$ctl01$ckbCriterio6': 'on',
  'ctl00$cphCorpo$ctl01$txtCriterio7': '',
  'ctl00$cphCorpo$ctl01$ckbCriterio8': 'on',
  'ctl00$cphCorpo$ctl01$ckbCriterio9': 'on',
  'ctl00$cphCorpo$ctl01$txtCriterio9': '',
  'ctl00$cphCorpo$ctl01$txtCriterio10': '',
  'ctl00$cphCorpo$ctl01$txtCriterio11': '',
  'ctl00$cphCorpo$ctl01$ckbCriterio13': 'on',
  'ctl00$cphCorpo$ctl01$txtCriterio13': '',
  'ctl00$cphCorpo$ctl01$txtCriterio15': '',
  'ctl00$cphCorpo$ctl01$ckbCriterio16': 'on',
  'ctl00$cphCorpo$ctl01$txtCriterio16': '',
  'ctl00$cphCorpo$ctl01$txtCriterio17': '',
  'ctl00$cphCorpo$ctl01$ckbCriterio18': 'on',
  'ctl00$cphCorpo$ctl01$txtCriterio19': '',
  'ctl00$cphCorpo$ctl01$txtCriterio20': '',
  'ctl00$cphCorpo$ctl01$txtCriterio21': '',
  'ctl00$cphCorpo$ctl01$ckbCriterio22': 'on',
  'ctl00$cphCorpo$ctl01$txtCriterio22': '',
  'ctl00$cphCorpo$ctl01$txtCriterio23': '',
  'ctl00$cphCorpo$ctl01$txtCriterio24': '',
  'ctl00$cphCorpo$ctl01$ckbCriterio25': 'on',
  'ctl00$cphCorpo$ctl01$txtCriterio25': '',
  'ctl00$cphCorpo$ctl01$txtCriterio26': '',
  'ctl00$cphCorpo$ctl01$txtCriterio28': '',
  'ctl00$cphCorpo$ctl01$txtCriterio29': '',
  'ctl00$cphCorpo$ctl01$txtCriterio30': '',
  'ctl00$cphCorpo$ctl01$txtCriterio31': '',
  'ctl00$cphCorpo$ctl01$ckbCriterio32': 'on',
  'ctl00$cphCorpo$ctl01$ckbCriterio34': 'on',
  'ctl00$cphCorpo$ctl01$txtCriterio34': '',
  'ctl00$cphCorpo$ctl01$ckbCriterio35': 'on',
  'ctl00$cphCorpo$ctl01$txtCriterio35': '',
  'ctl00$cphCorpo$ctl01$txtCriterio36': '',
  'ctl00$cphCorpo$ctl01$txtCriterio37': '',
  'ctl00$cphCorpo$ctl01$txtCriterio38': '',
  'ctl00$cphCorpo$ctl01$txtCriterio46': '',
  'ctl00$cphCorpo$ctl01$txtCriterio47': '',
  'ctl00$cphCorpo$ctl01$txtCriterio48': '',
  'ctl00$cphCorpo$ctl01$txtCriterio49': '',
  'ctl00$cphCorpo$ctl01$txtCriterio50': '',
  'ctl00$cphCorpo$ctl01$txtCriterio51': '',
  'ctl00$cphCorpo$ctl01$ckbCriterio53': 'on',
  'ctl00$cphCorpo$ctl01$txtCriterio53': '',
  'ctl00$cphCorpo$ctl01$txtCriterio56': '',
  'ctl00$cphCorpo$ctl01$txtCriterio57': '',
  'ctl00$cphCorpo$ctl01$txtCriterio58': '',
  'ctl00$cphCorpo$ctl01$hdfCriterioCampo': '',
  'ctl00$cphCorpo$ctl01$txtIgualA': '',
  'ctl00$cphCorpo$ctl01$txtMaiorIgualA': '',
  'ctl00$cphCorpo$ctl01$txtMenorIgualA': '',
  'ctl00$cphCorpo$ctl01$txtContem': '',
  'ctl00$cphCorpo$hdfExportar': '0',
  'ctl00$cphCorpo$hdfOrderCol': 'Asc',
  '__EVENTTARGET': 'ctl00$cphCorpo$ctl01$lstEstacoes',
  '__EVENTARGUMENT': '',
  '__LASTFOCUS': '',
  '__VIEWSTATEGENERATOR': '01F96EAB',
  '__ASYNCPOST': 'true',
  '': ''
}
if __name__  == "__main__":
    response_ana = requests.post('http://www.snirh.gov.br/hidrotelemetria/serieHistorica.aspx', headers=headers, cookies=cookies, data=data)
    
    with open('res_html.html', 'w', encoding='utf8') as f:
        f.write(response_ana.text)