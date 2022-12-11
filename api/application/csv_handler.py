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
    for index, line in enumerate(fetched_lines, start=1):
        try:
            result.append(create_cessao_fundo_object(line))
        except Exception as e:
            error_list.append({'line': index,'originador': line[0], 'ccb': line[4], 'error':e.args[0]})

    fetched_object = { 'success': len(result), 'error': {'count':len(error_list), 'error_list': error_list}, 'data': result }     
    return fetched_object
   
def create_cessao_fundo_object(ACSVLine):
    # print(ACSVLine)
    # format
    format = '%Y-%m-%d'
    try:
        object = {
            'ORIGINADOR'          :   ACSVLine[0], # EMPIRICA INVESTIMENTOS
            'DOC_ORIGINADOR'      :   re.sub(r'[.|/|-]','',ACSVLine[1]), # 10.896.871/0001-99 -> 10896871000199
            'CEDENTE'             :   ACSVLine[2], # EMPIRICA HOLDING S.A.
            'DOC_CEDENTE'         :   ACSVLine[3], # 42351640000196
            'CCB'                 :   ACSVLine[4], # 379654
            'ID_EXTERNO'          :   ACSVLine[5], # 12359
            'CLIENTE'             :   ACSVLine[6], # Pessoa exemplo 1
            'CPF_CNPJ'            :   re.sub(r'[.|/|-]','',ACSVLine[7]), # 12.345.678/0001-10 -> 12345678000110
            'ENDERECO'            :   ACSVLine[8], # R RODOVIA ADMAR GONZAGA 125
            'CEP'                 :   ACSVLine[9], # 60752040
            'CIDADE'              :   ACSVLine[10], # FLORIANOPOLIS
            'UF'                  :   ACSVLine[11], # SC
            'VALOR_DO_EMPRESTIMO' :   float(re.sub(r'[,]','.', ACSVLine[12])), # 127,86
            'VALOR_PARCELA'       :   float(re.sub(r'[,]','.', ACSVLine[14])), # 17,87
            'TOTAL_PARCELAS'      :   ACSVLine[19], # 8
            'PARCELA'             :   ACSVLine[20], # 1
            'DATA_DE_EMISSAO'     :   datetime.datetime.strptime(ACSVLine[23], '%d/%m/%Y').strftime('%Y-%m-%d'), # 10/05/2022
            'DATA_DE_VENCIMENTO'  :   datetime.datetime.strptime(ACSVLine[24], '%d/%m/%Y').strftime('%Y-%m-%d'), # 14/07/2022
            'PRECO_DE_AQUISICAO'  :   float(re.sub(r'[,]','.', ACSVLine[26])) # 15.76
        }
    except Exception as Err:
        raise Err

    return object