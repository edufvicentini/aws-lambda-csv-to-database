import csv
import re
import datetime

def handle_csv(data):
    # remove headers
    data.pop(0)

    fetched_lines = []
    for line in data:
        fetched_lines.append(line.split(';'))

    # fetch into a array
    result = []
    error_list = []    
    for line in fetched_lines:
        try:
            result.append(create_cessao_fundo_object(line))
        except Exception as e:
            error_list.append(e)

    fetched_object = { 'success': len(result), 'error': {'count':len(error_list), 'error_list': error_list}, 'data': result }        
    return fetched_object
   
def create_cessao_fundo_object(ALine):
    # print(ALine)
    # format
    format = '%Y-%m-%d'
    
    object = {
        'ORIGINADOR'          :   ALine[0], # EMPIRICA INVESTIMENTOS
        'DOC_ORIGINADOR'      :   re.sub(r'[.|/|-]','',ALine[1]), # 10.896.871/0001-99 -> 10896871000199
        'CEDENTE'             :   ALine[2], # EMPIRICA HOLDING S.A.
        'DOC_CEDENTE'         :   ALine[3], # 42351640000196
        'CCB'                 :   ALine[4], # 379654
        'ID_EXTERNO'          :   ALine[5], # 12359
        'CLIENTE'             :   ALine[6], # Pessoa exemplo 1
        'CPF_CNPJ'            :   re.sub(r'[.|/|-]','',ALine[7]), # 12.345.678/0001-10 -> 12345678000110
        'ENDERECO'            :   ALine[8], # R RODOVIA ADMAR GONZAGA 125
        'CEP'                 :   ALine[9], # 60752040
        'CIDADE'              :   ALine[10], # FLORIANOPOLIS
        'UF'                  :   ALine[11], # SC
        'VALOR_DO_EMPRESTIMO' :   float(re.sub(r'[,]','.', ALine[12])), # 127,86
        'VALOR_PARCELA'       :   float(re.sub(r'[,]','.', ALine[14])), # 17,87
        'TOTAL_PARCELAS'      :   ALine[19], # 8
        'PARCELA'             :   ALine[20], # 1
        'DATA_DE_EMISSAO'     :   datetime.datetime.strptime(ALine[23], '%d/%m/%Y').strftime('%Y-%m-%d'), # 10/05/2022
        'DATA_DE_VENCIMENTO'  :   datetime.datetime.strptime(ALine[24], '%d/%m/%Y').strftime('%Y-%m-%d'), # 14/07/2022
        'PRECO_DE_AQUISICAO'  :   float(re.sub(r'[,]','.', ALine[26])) # 15.76
    }

    return object