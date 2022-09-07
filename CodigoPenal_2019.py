import os
import sys
from time import sleep

print('\nBem vindo ao código penal do ----FAEL----\n' )
print('Segue a baixo as siglas que devem ser usadas para o funcionamento do código:\n')
print("""*Abuso de autoridade Juiz, Ministro, Promotor  (ABAJMP)
*Abuso de autoridade Polícia (PE)  (ABAPE)
*Abuso de autoridade Polícia (PM)  (ABAPM)
*Agressão   (AG)
*Agressão à autoridade (Juiz)  (AGJ)
*Agressão à autoridade (Polícia/Médico) (AGPM)
*AMEAÇA    (A)
*AMEAÇA À AUTORIDADE (JUIZ,MINISTRO,PROMOTOR)  (AAJMP)
*AMEAÇA À AUTORIDADE (POLÍCIA,MÉDICO)  (AAPM)
*ANDAR SEM CAPACETE   (SC)
*Assassinato   (ASS)
*Assassinato à Juiz   (ASSJ)
*Assassinato à Ministro, Promotor.  (ASSMP)
*Assassinato à polícia (PE) (ASSPE)
*Assassinato à polícia (PM) (ASSPM)
*Assassinato à UNIZK (ASSU)
*ATENTADO AO PUDOR  (AP)
*BLOQUEIO DE VIAS SEM AUTORIZAÇÃO   (BVA)
*CALÚNIA E DIFAMAÇÃO   (CD)
*CALÚNIA E DIFAMAÇÃO À AUTORIDADE (JUIZ,MINISTRO,PROMOTOR)  (CDAJMP)
*CALÚNIA E DIFAMAÇÃO À AUTORIDADE (POLÍCIA,MÉDICO)   (CDA)
*CORRIDA ILEGAL   (CI)
*Corrupção agente UNIZK   (CRUNIZK)
*Corrupção Juiz, Ministro, Promotor  (CRJMP)
*Corrupção Polícia (PE)  (CRPE)
*Corrupção Polícia (PM)  (CRPM)
*DEGRADAÇÃO DE PATRIMÔNIO PÚBLICO (DPB)
*DESACATO À AUTORIDADE (DA)
*Descartar arma (Escopeta).  (DESCOP)
*Descartar arma (Fusil de Assalto 5.56). (DM4)
*Descartar arma (Fusil de Assalto 7.62). (DAK)
*Descartar arma (Pistola AP). (DPISTAP)
*Descartar arma (Pistola de combate).  (DPCOM)
*Descartar arma (Pistola).  (DPIST)
*Descartar arma (Rifle de Precisão). (DSNI)
*Descartar arma (SubMetralhadora). (DSUB)
*Descartar arma (Teaser).  (DTA)
*DESOBEDECER UMA ORDEM DE SEGURANÇA NACIONAL (ORDEM DE UM MINISTRO)  (DOSN)
*DESOBEDECER UMA ORDEM JUDICIAL (MANDADO)   (DOJ)
*DESOBEDECER UMA ORDEM POLICIAL (DOP)
*DESOBEDECER UMA ORDEM POLICIAL (DOP)
*DIREÇÃO PERIGOSA  (DP)
*DIRIGIR NA CONTRAMÃO   (DCO)
*DIRIGIR SEM HABILITAÇÃO  (SH)
*ESTACIONAR EM LOCAL PROIBIDO  (LP)
*FALSIDADE IDEOLÓGICA   (FI)
*FALSO CHAMADO (MECÂNICO,TAXI)   (FCMT)
*FALSO CHAMADO (UNIZK,POLÍCIA,ADVOGADO)   (FCUPA)
*FALSO TESTEMUNHO  (FT)
*Formação de quadrilha, 2 criminosos. (FQ2)
*Formação de quadrilha, 3 a 4 criminosos. (FQ34)
*Formação de quadrilha, 4 a 6 criminosos. (FQ46)
*Formação de quadrilha, 7 ou mais criminosos. (FQ7+)
*Furto (sem ameaça e/ou lesão)   (F)
*INJÚRIA   (INJ)
*Invasão à locais de ofício público sem autorização  (INVLP)
*Invasão à propriedade privada  (INVPV)
*MANOBRAS IRREGULARES (DRIFT, CANTAR PENEU ETC)  (MI)
*OMISSÃO DE SOCORRO   (OS)
*PASSAR DIRETO EM CRUSAMENTOS (SEM REDUZIR A VELOCIDADE)   (PDC)
*PERTUBAÇÃO DO SOSSEGO (MUSICA ALTA, GRITARIA, ETC) (PS)
*Posse/Porte de arma (Escopeta).   (PESCO)
*Posse/Porte de arma (Fusil de Assalto 5.56). (PM4)
*Posse/Porte de arma (Fusil de Assalto 7.62).  (PAK)
*Posse/Porte de arma (Pistola AP).    (PPAP)
*Posse/Porte de arma (Pistola de combate).   (PPC)
*Posse/Porte de arma (Pistola).   (PP)
*Posse/Porte de arma (Rifle de Precisão).   (PSNI)
*Posse/Porte de arma (SubMetralhadora). (PSUB)
*Posse/Porte de arma (Teaser).   (PT)
*Roubo (violência/ameaça) (R)
*Roubo e furto de veículo (RFV)
*Roubo e furto de veículo do estado(UNYZK, PM, PE, JUIZ)   (RFVE)
*Sequestro   (S)
*Sequestro Juiz   (SJ)
*Sequestro polícia (PE)  (SPE)
*Sequestro polícia (PM)  (SPM)
*Sequestro UNIZ   (SUNIZK)
*Tentativa de assassinato  (TA)
*Tentativa de assassinato à Juiz, Ministro, Promotor    (TAJMP)
*Tentativa de assassinato à polícia (PE)   (TAPE)
*Tentativa de assassinato à polícia (PM)   (TAPM)
*TENTATIVA DE FUGA  (TF)
*TENTATIVA DE SUBORNO  (TS)
*Uso de mascara, colete ou qualquer peça balística  (Polícia de Elite)   (UMCPE)
*Uso de qualquer acessório e/ou vestimenta  policia   (Polícia de Elite)  (UAPE)
*Uso de qualquer acessório e/ou vestimenta médica (UNIZK / MECANICO)    (UAUM)
*Uso de qualquer acessório e/ou vestimenta policial (Polícia Militar)   (UAPM)""")

# A partir daqui é o código mesmo

print('\nVamos lá...\n')
codigo = input('Qual a sigla do código? ').upper()
if codigo == 'TS':
    codigo = [25, 40, 20]

elif codigo == 'AP':
    codigo = [0, 10, 10]

elif codigo == 'DPB':
    codigo = [0, 10, 8]

elif codigo == 'PS':
    codigo = [0, 10, 8]

elif codigo == 'OS':
    codigo = [5, 16, 12]

elif codigo == 'DOP':
    codigo = [5, 15, 5]

elif codigo == 'TF':
    codigo = [10, 25, 15]

elif codigo == 'DA':
    codigo = [5, 10, 15]

elif codigo == 'DOJ':
    codigo = [120, 120, 1000000]

elif codigo == 'DOSN':
    codigo = [120, 120, 5000000]

elif codigo == 'A':
    codigo = [10, 25, 12]

elif codigo == 'AAPM':
    codigo = [10, 35, 25]

elif codigo == 'AAJMP':
    codigo = [80, 120, 55]

elif codigo == 'CD':
    codigo = [10, 15, 8]

elif codigo == 'CDA':
    codigo = [10, 20, 12]

elif codigo == 'CDAJMP':
    codigo = [15, 50, 20]

elif codigo == 'FT':
    codigo = [10, 50, 25]

elif codigo == 'FI':
    codigo = [5, 40, 12]

elif codigo == 'INJ':
    codigo = [15, 35, 15]

elif codigo == 'FCUPA':
    codigo = [10, 15, 8]

elif codigo == 'FCMT':
    codigo = [5, 15, 5]

elif codigo == 'SH':
    codigo = [0, 0, 15]

elif codigo == 'SC':
    codigo = [0, 0, 5]

elif codigo == 'LP':
    codigo = [0, 0, 15]

elif codigo == 'PDC':
    codigo = [0, 0, 10]

elif codigo == 'DCO':
    codigo = [0, 0, 10]

elif codigo == 'DCO':
    codigo = [0, 0, 10]

elif codigo == 'MI':
    codigo = [0, 0, 20]

elif codigo == 'DP':
    codigo = [3, 20, 25]

elif codigo == 'CI':
    codigo = [15, 25, 25]

elif codigo == 'BVA':
    codigo = [10, 20, 45]

elif codigo == 'UAUM':
    codigo = [5, 15, 10]

elif codigo == 'UAPM':
    codigo = [10, 25, 15]

elif codigo == 'UAPE':
    codigo = [15, 30, 15]

elif codigo == 'UMCPE':
    codigo = [10, 40, 18]

elif codigo == 'PT':
    codigo = [10, 15, 0]

elif codigo == 'PP':
    codigo = [15, 20, 0]

elif codigo == 'PPC':
    codigo = [20, 30, 0]

elif codigo == 'PPAP':
    codigo = [25, 40, 0]

elif codigo == 'PESCO':
    codigo = [30, 45, 0]

elif codigo == 'PSUB':
    codigo = [35, 50, 0]

elif codigo == 'PM4':
    codigo = [40, 55, 0]

elif codigo == 'PAK':
    codigo = [45, 60, 0]

elif codigo == 'PSNI':
    codigo = [55, 70, 0]

elif codigo == 'F':
    codigo = [5, 15, 10]

elif codigo == 'R':
    codigo = [15, 35, 30]

elif codigo == 'AG':
    codigo = [5, 30, 20]

elif codigo == 'AGPM':
    codigo = [20, 60, 65]

elif codigo == 'AGJ':
    codigo = [30, 80, 80]

elif codigo == 'RFV':
    codigo = [40, 65, 25]

elif codigo == 'RFVE':
    codigo = [45, 90, 90]

elif codigo == 'INVPV':
    codigo = [5, 30, 20]

elif codigo == 'INVLP':
    codigo = [10, 40, 30]

elif codigo == 'ABAPM':
    codigo = [10, 30, 30]

elif codigo == 'ABAPE':
    codigo = [15, 35, 45]

elif codigo == 'ABAJMP':
    codigo = [35, 55, 100]

elif codigo == 'CRUNIZK':
    codigo = [10, 30, 30]

elif codigo == 'CRPM':
    codigo = [180, 180, 300]

elif codigo == 'CRPE':
    codigo = [180, 180, 500]

elif codigo == 'CRJMP':
    codigo = [180, 180, 1000000]

elif codigo == 'FQ2':
    codigo = [10, 20, 20]

elif codigo == 'FQ34':
    codigo = [20, 30, 30]

elif codigo == 'FQ46':
    codigo = [40, 50, 40]

elif codigo == 'FQ7+':
    codigo = [55, 80, 60]

elif codigo == 'DTA':
    codigo = [5, 10, 0]

elif codigo == 'DPIST':
    codigo = [10, 15, 0]

elif codigo == 'DPCOM':
    codigo = [10, 20, 0]

elif codigo == 'DPISTAP':
    codigo = [15, 30, 0]

elif codigo == 'DESCOP':
    codigo = [20, 35, 0]

elif codigo == 'DSUB':
    codigo = [25, 40, 0]

elif codigo == 'DM4':
    codigo = [30, 45, 0]

elif codigo == 'DAK':
    codigo = [45, 50, 0]

elif codigo == 'DSNI':
    codigo = [45, 60, 0]

elif codigo == 'S':
    codigo = [20, 50, 25]

elif codigo == 'SPM':
    codigo = [30, 60, 35]

elif codigo == 'SPE':
    codigo = [40, 70, 45]

elif codigo == 'SJ':
    codigo = [60, 120, 85]

elif codigo == 'SUNIZK':
    codigo = [30, 60, 25]

elif codigo == 'TA':
    codigo = [20, 60, 30]

elif codigo == 'TAPM':
    codigo = [30, 70, 0]

elif codigo == 'TAPE':
    codigo = [40, 80, 0]

elif codigo == 'TAJMP':
    codigo = [50, 120, 150]

elif codigo == 'ASS':
    codigo = [50, 90, 0]

elif codigo == 'ASSU':
    codigo = [60, 120, 0]

elif codigo == 'ASSPM':
    codigo = [60, 120, 0]

elif codigo == 'ASSPE':
    codigo = [70, 120, 0]

elif codigo == 'ASSJ':
    codigo = [100, 120, 250]

elif codigo == 'ASSMP':
    codigo = [120, 120, 500]

else:
    print('Este código não existe, reinicie o programa!')
    sleep(5)
    sys.exit()

c1 = input('Tem mais códigos? [S/N]').upper()
if c1 == 'S':
    codigo2 = input('Digite o outro código: ').upper()
    if codigo2 == 'TS':
        codigo2 = [25, 40, 20]

    elif codigo2 == 'AP':
        codigo2 = [0, 10, 10]

    elif codigo2 == 'DPB':
        codigo2 = [0, 10, 8]

    elif codigo2 == 'PS':
        codigo2 = [0, 10, 8]

    elif codigo2 == 'OS':
        codigo2 = [5, 16, 12]

    elif codigo2 == 'DOP':
        codigo2 = [5, 15, 5]

    elif codigo2 == 'TF':
        codigo2 = [10, 25, 15]

    elif codigo2 == 'DA':
        codigo2 = [5, 10, 15]

    elif codigo2 == 'DOJ':
        codigo2 = [120, 120, 1000000]

    elif codigo2 == 'DOSN':
        codigo2 = [120, 120, 5000000]

    elif codigo2 == 'A':
        codigo2 = [10, 25, 12]

    elif codigo2 == 'AAPM':
        codigo2 = [10, 35, 25]

    elif codigo2 == 'AAJMP':
        codigo2 = [80, 120, 55]

    elif codigo2 == 'CD':
        codigo2 = [10, 15, 8]

    elif codigo2 == 'CDA':
        codigo2 = [10, 20, 12]

    elif codigo2 == 'CDAJMP':
        codigo2 = [15, 50, 20]

    elif codigo2 == 'FT':
        codigo2 = [10, 50, 25]

    elif codigo2 == 'FI':
        codigo2 = [5, 40, 12]

    elif codigo2 == 'INJ':
        codigo2 = [15, 35, 15]

    elif codigo2 == 'FCUPA':
        codigo2 = [10, 15, 8]

    elif codigo2 == 'FCMT':
        codigo2 = [5, 15, 5]

    elif codigo2 == 'SH':
        codigo2 = [0, 0, 15]

    elif codigo2 == 'SC':
        codigo2 = [0, 0, 5]

    elif codigo2 == 'LP':
        codigo2 = [0, 0, 15]

    elif codigo2 == 'PDC':
        codigo2 = [0, 0, 10]

    elif codigo2 == 'DCO':
        codigo2 = [0, 0, 10]

    elif codigo2 == 'DCO':
        codigo2 = [0, 0, 10]

    elif codigo2 == 'MI':
        codigo2 = [0, 0, 20]

    elif codigo2 == 'DP':
        codigo2 = [3, 20, 25]

    elif codigo2 == 'CI':
        codigo2 = [15, 25, 25]

    elif codigo2 == 'BVA':
        codigo2 = [10, 20, 45]

    elif codigo2 == 'UAUM':
        codigo2 = [5, 15, 10]

    elif codigo2 == 'UAPM':
        codigo2 = [10, 25, 15]

    elif codigo2 == 'UAPE':
        codigo2 = [15, 30, 15]

    elif codigo2 == 'UMCPE':
        codigo2 = [10, 40, 18]

    elif codigo2 == 'PT':
        codigo2 = [10, 15, 0]

    elif codigo2 == 'PP':
        codigo2 = [15, 20, 0]

    elif codigo2 == 'PPC':
        codigo2 = [20, 30, 0]

    elif codigo2 == 'PPAP':
        codigo2 = [25, 40, 0]

    elif codigo2 == 'PESCO':
        codigo2 = [30, 45, 0]

    elif codigo2 == 'PSUB':
        codigo2 = [35, 50, 0]

    elif codigo2 == 'PM4':
        codigo2 = [40, 55, 0]

    elif codigo2 == 'PAK':
        codigo2 = [45, 60, 0]

    elif codigo2 == 'PSNI':
        codigo2 = [55, 70, 0]

    elif codigo2 == 'F':
        codigo2 = [5, 15, 10]

    elif codigo2 == 'R':
        codigo2 = [15, 35, 30]

    elif codigo2 == 'AG':
        codigo2 = [5, 30, 20]

    elif codigo2 == 'AGPM':
        codigo2 = [20, 60, 65]

    elif codigo2 == 'AGJ':
        codigo2 = [30, 80, 80]

    elif codigo2 == 'RFV':
        codigo2 = [40, 65, 25]

    elif codigo2 == 'RFVE':
        codigo2 = [45, 90, 90]

    elif codigo2 == 'INVPV':
        codigo2 = [5, 30, 20]

    elif codigo2 == 'INVLP':
        codigo2 = [10, 40, 30]

    elif codigo2 == 'ABAPM':
        codigo2 = [10, 30, 30]

    elif codigo2 == 'ABAPE':
        codigo2 = [15, 35, 45]

    elif codigo2 == 'ABAJMP':
        codigo2 = [35, 55, 100]

    elif codigo2 == 'CRUNIZK':
        codigo2 = [10, 30, 30]

    elif codigo2 == 'CRPM':
        codigo2 = [180, 180, 300]

    elif codigo2 == 'CRPE':
        codigo2 = [180, 180, 500]

    elif codigo2 == 'CRJMP':
        codigo2 = [180, 180, 1000000]

    elif codigo2 == 'FQ2':
        codigo2 = [10, 20, 20]

    elif codigo2 == 'FQ34':
        codigo2 = [20, 30, 30]

    elif codigo2 == 'FQ46':
        codigo2 = [40, 50, 40]

    elif codigo2 == 'FQ7+':
        codigo2 = [55, 80, 60]

    elif codigo2 == 'DTA':
        codigo2 = [5, 10, 0]

    elif codigo2 == 'DPIST':
        codigo2 = [10, 15, 0]

    elif codigo2 == 'DPCOM':
        codigo2 = [10, 20, 0]

    elif codigo2 == 'DPISTAP':
        codigo2 = [15, 30, 0]

    elif codigo2 == 'DESCOP':
        codigo2 = [20, 35, 0]

    elif codigo2 == 'DSUB':
        codigo2 = [25, 40, 0]

    elif codigo2 == 'DM4':
        codigo2 = [30, 45, 0]

    elif codigo2 == 'DAK':
        codigo2 = [45, 50, 0]

    elif codigo2 == 'DSNI':
        codigo2 = [45, 60, 0]

    elif codigo2 == 'S':
        codigo2 = [20, 50, 25]

    elif codigo2 == 'SPM':
        codigo2 = [30, 60, 35]

    elif codigo2 == 'SPE':
        codigo2 = [40, 70, 45]

    elif codigo2 == 'SJ':
        codigo2 = [60, 120, 85]

    elif codigo2 == 'SUNIZK':
        codigo2 = [30, 60, 25]

    elif codigo2 == 'TA':
        codigo2 = [20, 60, 30]

    elif codigo2 == 'TAPM':
        codigo2 = [30, 70, 0]

    elif codigo2 == 'TAPE':
        codigo2 = [40, 80, 0]

    elif codigo2 == 'TAJMP':
        codigo2 = [50, 120, 150]

    elif codigo2 == 'ASS':
        codigo2 = [50, 90, 0]

    elif codigo2 == 'ASSU':
        codigo2 = [60, 120, 0]

    elif codigo2 == 'ASSPM':
        codigo2 = [60, 120, 0]

    elif codigo2 == 'ASSPE':
        codigo2 = [70, 120, 0]

    elif codigo2 == 'ASSJ':
        codigo2 = [100, 120, 250]

    elif codigo2 == 'ASSMP':
        codigo2 = [120, 120, 500]

    else:
        print('Este código não existe, reinicie o programa!')
        sleep(5)
        sys.exit()

elif c1 == 'N':
    print('TEMPO MÍNIMO: {}'.format(codigo[0]))
    print('TEMPO MÁXIMO: {}'.format(codigo[1]))
    print('MULTA: {} mil'.format(codigo[2]))
    sleep(300)
    sys.exit()

c2 = input('Tem mais códigos? [S/N]').upper()
if c2 == 'S':
    codigo3 = input('Digite o outro código: ').upper()
    if codigo3 == 'TS':
        codigo3 = [25, 40, 20]

    elif codigo3 == 'AP':
        codigo3 = [0, 10, 10]

    elif codigo3 == 'DPB':
        codigo3 = [0, 10, 8]

    elif codigo3 == 'PS':
        codigo3 = [0, 10, 8]

    elif codigo3 == 'OS':
        codigo3 = [5, 16, 12]

    elif codigo3 == 'DOP':
        codigo3 = [5, 15, 5]

    elif codigo3 == 'TF':
        codigo3 = [10, 25, 15]

    elif codigo3 == 'DA':
        codigo3 = [5, 10, 15]

    elif codigo3 == 'DOJ':
        codigo3 = [120, 120, 1000000]

    elif codigo3 == 'DOSN':
        codigo3 = [120, 120, 5000000]

    elif codigo3 == 'A':
        codigo3 = [10, 25, 12]

    elif codigo3 == 'AAPM':
        codigo3 = [10, 35, 25]

    elif codigo3 == 'AAJMP':
        codigo3 = [80, 120, 55]

    elif codigo3 == 'CD':
        codigo3 = [10, 15, 8]

    elif codigo3 == 'CDA':
        codigo3 = [10, 20, 12]

    elif codigo3 == 'CDAJMP':
        codigo3 = [15, 50, 20]

    elif codigo3 == 'FT':
        codigo3 = [10, 50, 25]

    elif codigo3 == 'FI':
        codigo3 = [5, 40, 12]

    elif codigo3 == 'INJ':
        codigo3 = [15, 35, 15]

    elif codigo3 == 'FCUPA':
        codigo3 = [10, 15, 8]

    elif codigo3 == 'FCMT':
        codigo3 = [5, 15, 5]

    elif codigo3 == 'SH':
        codigo3 = [0, 0, 15]

    elif codigo3 == 'SC':
        codigo3 = [0, 0, 5]

    elif codigo3 == 'LP':
        codigo3 = [0, 0, 15]

    elif codigo3 == 'PDC':
        codigo3 = [0, 0, 10]

    elif codigo3 == 'DCO':
        codigo3 = [0, 0, 10]

    elif codigo3 == 'DCO':
        codigo3 = [0, 0, 10]

    elif codigo3 == 'MI':
        codigo3 = [0, 0, 20]

    elif codigo3 == 'DP':
        codigo3 = [3, 20, 25]

    elif codigo3 == 'CI':
        codigo3 = [15, 25, 25]

    elif codigo3 == 'BVA':
        codigo3 = [10, 20, 45]

    elif codigo3 == 'UAUM':
        codigo3 = [5, 15, 10]

    elif codigo3 == 'UAPM':
        codigo3 = [10, 25, 15]

    elif codigo3 == 'UAPE':
        codigo3 = [15, 30, 15]

    elif codigo3 == 'UMCPE':
        codigo3 = [10, 40, 18]

    elif codigo3 == 'PT':
        codigo3 = [10, 15, 0]

    elif codigo3 == 'PP':
        codigo3 = [15, 20, 0]

    elif codigo3 == 'PPC':
        codigo3 = [20, 30, 0]

    elif codigo3 == 'PPAP':
        codigo3 = [25, 40, 0]

    elif codigo3 == 'PESCO':
        codigo3 = [30, 45, 0]

    elif codigo3 == 'PSUB':
        codigo3 = [35, 50, 0]

    elif codigo3 == 'PM4':
        codigo3 = [40, 55, 0]

    elif codigo3 == 'PAK':
        codigo3 = [45, 60, 0]

    elif codigo3 == 'PSNI':
        codigo3 = [55, 70, 0]

    elif codigo3 == 'F':
        codigo3 = [5, 15, 10]

    elif codigo3 == 'R':
        codigo3 = [15, 35, 30]

    elif codigo3 == 'AG':
        codigo3 = [5, 30, 20]

    elif codigo3 == 'AGPM':
        codigo3 = [20, 60, 65]

    elif codigo3 == 'AGJ':
        codigo3 = [30, 80, 80]

    elif codigo3 == 'RFV':
        codigo3 = [40, 65, 25]

    elif codigo3 == 'RFVE':
        codigo3 = [45, 90, 90]

    elif codigo3 == 'INVPV':
        codigo3 = [5, 30, 20]

    elif codigo3 == 'INVLP':
        codigo3 = [10, 40, 30]

    elif codigo3 == 'ABAPM':
        codigo3 = [10, 30, 30]

    elif codigo3 == 'ABAPE':
        codigo3 = [15, 35, 45]

    elif codigo3 == 'ABAJMP':
        codigo3 = [35, 55, 100]

    elif codigo3 == 'CRUNIZK':
        codigo3 = [10, 30, 30]

    elif codigo3 == 'CRPM':
        codigo3 = [180, 180, 300]

    elif codigo3 == 'CRPE':
        codigo3 = [180, 180, 500]

    elif codigo3 == 'CRJMP':
        codigo3 = [180, 180, 1000000]

    elif codigo3 == 'FQ2':
        codigo3 = [10, 20, 20]

    elif codigo3 == 'FQ34':
        codigo3 = [20, 30, 30]

    elif codigo3 == 'FQ46':
        codigo3 = [40, 50, 40]

    elif codigo3 == 'FQ7+':
        codigo3 = [55, 80, 60]

    elif codigo3 == 'DTA':
        codigo3 = [5, 10, 0]

    elif codigo3 == 'DPIST':
        codigo3 = [10, 15, 0]

    elif codigo3 == 'DPCOM':
        codigo3 = [10, 20, 0]

    elif codigo3 == 'DPISTAP':
        codigo3 = [15, 30, 0]

    elif codigo3 == 'DESCOP':
        codigo3 = [20, 35, 0]

    elif codigo3 == 'DSUB':
        codigo3 = [25, 40, 0]

    elif codigo3 == 'DM4':
        codigo3 = [30, 45, 0]

    elif codigo3 == 'DAK':
        codigo3 = [45, 50, 0]

    elif codigo3 == 'DSNI':
        codigo3 = [45, 60, 0]

    elif codigo3 == 'S':
        codigo3 = [20, 50, 25]

    elif codigo3 == 'SPM':
        codigo3 = [30, 60, 35]

    elif codigo3 == 'SPE':
        codigo3 = [40, 70, 45]

    elif codigo3 == 'SJ':
        codigo3 = [60, 120, 85]

    elif codigo3 == 'SUNIZK':
        codigo3 = [30, 60, 25]

    elif codigo3 == 'TA':
        codigo3 = [20, 60, 30]

    elif codigo3 == 'TAPM':
        codigo3 = [30, 70, 0]

    elif codigo3 == 'TAPE':
        codigo3 = [40, 80, 0]

    elif codigo3 == 'TAJMP':
        codigo3 = [50, 120, 150]

    elif codigo3 == 'ASS':
        codigo3 = [50, 90, 0]

    elif codigo3 == 'ASSU':
        codigo3 = [60, 120, 0]

    elif codigo3 == 'ASSPM':
        codigo3 = [60, 120, 0]

    elif codigo3 == 'ASSPE':
        codigo3 = [70, 120, 0]

    elif codigo3 == 'ASSJ':
        codigo3 = [100, 120, 250]

    elif codigo3 == 'ASSMP':
        codigo3 = [120, 120, 500]

    else:
        print('Este código não existe, reinicie o programa!')
        sleep(5)
        sys.exit()

elif c2 == 'N':
    soma1 = [(a + b) for a, b in zip(codigo, codigo2)]
    print('TEMPO MÍNIMO: {}'.format(soma1[0]))
    print('TEMPO MÁXIMO: {}'.format(soma1[1]))
    print('MULTA: {} mil'.format(soma1[2]))
    sleep(300)
    sys.exit()

c3 = input('Tem mais códigos? [S/N]').upper()
if c3 == 'S':
    codigo4 = input('Digite o outro código: ').upper()

    if codigo4 == 'TS':
        codigo4 = [25, 40, 20]

    elif codigo4 == 'AP':
        codigo4 = [0, 10, 10]

    elif codigo4 == 'DPB':
        codigo4 = [0, 10, 8]

    elif codigo4 == 'PS':
        codigo4 = [0, 10, 8]

    elif codigo4 == 'OS':
        codigo4 = [5, 16, 12]

    elif codigo4 == 'DOP':
        codigo4 = [5, 15, 5]

    elif codigo4 == 'TF':
        codigo4 = [10, 25, 15]

    elif codigo4 == 'DA':
        codigo4 = [5, 10, 15]

    elif codigo4 == 'DOJ':
        codigo4 = [120, 120, 1000000]

    elif codigo4 == 'DOSN':
        codigo4 = [120, 120, 5000000]

    elif codigo4 == 'A':
        codigo4 = [10, 25, 12]

    elif codigo4 == 'AAPM':
        codigo4 = [10, 35, 25]

    elif codigo4 == 'AAJMP':
        codigo4 = [80, 120, 55]

    elif codigo4 == 'CD':
        codigo4 = [10, 15, 8]

    elif codigo4 == 'CDA':
        codigo4 = [10, 20, 12]

    elif codigo4 == 'CDAJMP':
        codigo4 = [15, 50, 20]

    elif codigo4 == 'FT':
        codigo4 = [10, 50, 25]

    elif codigo4 == 'FI':
        codigo4 = [5, 40, 12]

    elif codigo4 == 'INJ':
        codigo4 = [15, 35, 15]

    elif codigo4 == 'FCUPA':
        codigo4 = [10, 15, 8]

    elif codigo4 == 'FCMT':
        codigo4 = [5, 15, 5]

    elif codigo4 == 'SH':
        codigo4 = [0, 0, 15]

    elif codigo4 == 'SC':
        codigo4 = [0, 0, 5]

    elif codigo4 == 'LP':
        codigo4 = [0, 0, 15]

    elif codigo4 == 'PDC':
        codigo4 = [0, 0, 10]

    elif codigo4 == 'DCO':
        codigo4 = [0, 0, 10]

    elif codigo4 == 'DCO':
        codigo4 = [0, 0, 10]

    elif codigo4 == 'MI':
        codigo4 = [0, 0, 20]

    elif codigo4 == 'DP':
        codigo4 = [3, 20, 25]

    elif codigo4 == 'CI':
        codigo4 = [15, 25, 25]

    elif codigo4 == 'BVA':
        codigo4 = [10, 20, 45]

    elif codigo4 == 'UAUM':
        codigo4 = [5, 15, 10]

    elif codigo4 == 'UAPM':
        codigo4 = [10, 25, 15]

    elif codigo4 == 'UAPE':
        codigo4 = [15, 30, 15]

    elif codigo4 == 'UMCPE':
        codigo4 = [10, 40, 18]

    elif codigo4 == 'PT':
        codigo4 = [10, 15, 0]

    elif codigo4 == 'PP':
        codigo4 = [15, 20, 0]

    elif codigo4 == 'PPC':
        codigo4 = [20, 30, 0]

    elif codigo4 == 'PPAP':
        codigo4 = [25, 40, 0]

    elif codigo4 == 'PESCO':
        codigo4 = [30, 45, 0]

    elif codigo4 == 'PSUB':
        codigo4 = [35, 50, 0]

    elif codigo4 == 'PM4':
        codigo4 = [40, 55, 0]

    elif codigo4 == 'PAK':
        codigo4 = [45, 60, 0]

    elif codigo4 == 'PSNI':
        codigo4 = [55, 70, 0]

    elif codigo4 == 'F':
        codigo4 = [5, 15, 10]

    elif codigo4 == 'R':
        codigo4 = [15, 35, 30]

    elif codigo4 == 'AG':
        codigo4 = [5, 30, 20]

    elif codigo4 == 'AGPM':
        codigo4 = [20, 60, 65]

    elif codigo4 == 'AGJ':
        codigo4 = [30, 80, 80]

    elif codigo4 == 'RFV':
        codigo4 = [40, 65, 25]

    elif codigo4 == 'RFVE':
        codigo4 = [45, 90, 90]

    elif codigo4 == 'INVPV':
        codigo4 = [5, 30, 20]

    elif codigo4 == 'INVLP':
        codigo4 = [10, 40, 30]

    elif codigo4 == 'ABAPM':
        codigo4 = [10, 30, 30]

    elif codigo4 == 'ABAPE':
        codigo4 = [15, 35, 45]

    elif codigo4 == 'ABAJMP':
        codigo4 = [35, 55, 100]

    elif codigo4 == 'CRUNIZK':
        codigo4 = [10, 30, 30]

    elif codigo4 == 'CRPM':
        codigo4 = [180, 180, 300]

    elif codigo4 == 'CRPE':
        codigo4 = [180, 180, 500]

    elif codigo4 == 'CRJMP':
        codigo4 = [180, 180, 1000000]

    elif codigo4 == 'FQ2':
        codigo4 = [10, 20, 20]

    elif codigo4 == 'FQ34':
        codigo4 = [20, 30, 30]

    elif codigo4 == 'FQ46':
        codigo4 = [40, 50, 40]

    elif codigo4 == 'FQ7+':
        codigo4 = [55, 80, 60]

    elif codigo4 == 'DTA':
        codigo4 = [5, 10, 0]

    elif codigo4 == 'DPIST':
        codigo4 = [10, 15, 0]

    elif codigo4 == 'DPCOM':
        codigo4 = [10, 20, 0]

    elif codigo4 == 'DPISTAP':
        codigo4 = [15, 30, 0]

    elif codigo4 == 'DESCOP':
        codigo4 = [20, 35, 0]

    elif codigo4 == 'DSUB':
        codigo4 = [25, 40, 0]

    elif codigo4 == 'DM4':
        codigo4 = [30, 45, 0]

    elif codigo4 == 'DAK':
        codigo4 = [45, 50, 0]

    elif codigo4 == 'DSNI':
        codigo4 = [45, 60, 0]

    elif codigo4 == 'S':
        codigo4 = [20, 50, 25]

    elif codigo4 == 'SPM':
        codigo4 = [30, 60, 35]

    elif codigo4 == 'SPE':
        codigo4 = [40, 70, 45]

    elif codigo4 == 'SJ':
        codigo4 = [60, 120, 85]

    elif codigo4 == 'SUNIZK':
        codigo4 = [30, 60, 25]

    elif codigo4 == 'TA':
        codigo4 = [20, 60, 30]

    elif codigo4 == 'TAPM':
        codigo4 = [30, 70, 0]

    elif codigo4 == 'TAPE':
        codigo4 = [40, 80, 0]

    elif codigo4 == 'TAJMP':
        codigo4 = [50, 120, 150]

    elif codigo4 == 'ASS':
        codigo4 = [50, 90, 0]

    elif codigo4 == 'ASSU':
        codigo4 = [60, 120, 0]

    elif codigo4 == 'ASSPM':
        codigo4 = [60, 120, 0]

    elif codigo4 == 'ASSPE':
        codigo4 = [70, 120, 0]

    elif codigo4 == 'ASSJ':
        codigo4 = [100, 120, 250]

    elif codigo4 == 'ASSMP':
        codigo4 = [120, 120, 500]

    else:
        print('Este código não existe, reinicie o programa!')
        sleep(5)
        sys.exit()

elif c3 == 'N':
    somamin = codigo[0] + codigo2[0] + codigo3[0]  # soma todas os 1 números das listas
    somamax = codigo[1] + codigo2[1] + codigo3[1]  # soma todas os 2 números das listas
    somamulta = codigo[2] + codigo3[2] + codigo2[2]  # soma todas os 3 números das listas

    print('TEMPO MÍNIMO: {}'.format(somamin))
    print('TEMPO MÁXIMO: {}'.format(somamax))
    print('MULTA: {} mil'.format(somamulta))
    sleep(300)
    sys.exit()

c4 = input('Tem mais códigos? [S/N]').upper()
if c4 == 'S':
    codigo5 = input('Digite o outro código: ').upper()

    if codigo5 == 'TS':
        codigo5 = [25, 40, 20]

    elif codigo5 == 'AP':
        codigo5 = [0, 10, 10]

    elif codigo5 == 'DPB':
        codigo5 = [0, 10, 8]

    elif codigo5 == 'PS':
        codigo5 = [0, 10, 8]

    elif codigo5 == 'OS':
        codigo5 = [5, 16, 12]

    elif codigo5 == 'DOP':
        codigo5 = [5, 15, 5]

    elif codigo5 == 'TF':
        codigo5 = [10, 25, 15]

    elif codigo5 == 'DA':
        codigo5 = [5, 10, 15]

    elif codigo5 == 'DOJ':
        codigo5 = [120, 120, 1000000]

    elif codigo5 == 'DOSN':
        codigo5 = [120, 120, 5000000]

    elif codigo5 == 'A':
        codigo5 = [10, 25, 12]

    elif codigo5 == 'AAPM':
        codigo5 = [10, 35, 25]

    elif codigo5 == 'AAJMP':
        codigo5 = [80, 120, 55]

    elif codigo5 == 'CD':
        codigo5 = [10, 15, 8]

    elif codigo5 == 'CDA':
        codigo5 = [10, 20, 12]

    elif codigo5 == 'CDAJMP':
        codigo5 = [15, 50, 20]

    elif codigo5 == 'FT':
        codigo5 = [10, 50, 25]

    elif codigo5 == 'FI':
        codigo5 = [5, 40, 12]

    elif codigo5 == 'INJ':
        codigo5 = [15, 35, 15]

    elif codigo5 == 'FCUPA':
        codigo5 = [10, 15, 8]

    elif codigo5 == 'FCMT':
        codigo5 = [5, 15, 5]

    elif codigo5 == 'SH':
        codigo5 = [0, 0, 15]

    elif codigo5 == 'SC':
        codigo5 = [0, 0, 5]

    elif codigo5 == 'LP':
        codigo5 = [0, 0, 15]

    elif codigo5 == 'PDC':
        codigo5 = [0, 0, 10]

    elif codigo5 == 'DCO':
        codigo5 = [0, 0, 10]

    elif codigo5 == 'DCO':
        codigo5 = [0, 0, 10]

    elif codigo5 == 'MI':
        codigo5 = [0, 0, 20]

    elif codigo5 == 'DP':
        codigo5 = [3, 20, 25]

    elif codigo5 == 'CI':
        codigo5 = [15, 25, 25]

    elif codigo5 == 'BVA':
        codigo5 = [10, 20, 45]

    elif codigo5 == 'UAUM':
        codigo5 = [5, 15, 10]

    elif codigo5 == 'UAPM':
        codigo5 = [10, 25, 15]

    elif codigo5 == 'UAPE':
        codigo5 = [15, 30, 15]

    elif codigo5 == 'UMCPE':
        codigo5 = [10, 40, 18]

    elif codigo5 == 'PT':
        codigo5 = [10, 15, 0]

    elif codigo5 == 'PP':
        codigo5 = [15, 20, 0]

    elif codigo5 == 'PPC':
        codigo5 = [20, 30, 0]

    elif codigo5 == 'PPAP':
        codigo5 = [25, 40, 0]

    elif codigo5 == 'PESCO':
        codigo5 = [30, 45, 0]

    elif codigo5 == 'PSUB':
        codigo5 = [35, 50, 0]

    elif codigo5 == 'PM4':
        codigo5 = [40, 55, 0]

    elif codigo5 == 'PAK':
        codigo5 = [45, 60, 0]

    elif codigo5 == 'PSNI':
        codigo5 = [55, 70, 0]

    elif codigo5 == 'F':
        codigo5 = [5, 15, 10]

    elif codigo5 == 'R':
        codigo5 = [15, 35, 30]

    elif codigo5 == 'AG':
        codigo5 = [5, 30, 20]

    elif codigo5 == 'AGPM':
        codigo5 = [20, 60, 65]

    elif codigo5 == 'AGJ':
        codigo5 = [30, 80, 80]

    elif codigo5 == 'RFV':
        codigo5 = [40, 65, 25]

    elif codigo5 == 'RFVE':
        codigo5 = [45, 90, 90]

    elif codigo5 == 'INVPV':
        codigo5 = [5, 30, 20]

    elif codigo5 == 'INVLP':
        codigo5 = [10, 40, 30]

    elif codigo5 == 'ABAPM':
        codigo5 = [10, 30, 30]

    elif codigo5 == 'ABAPE':
        codigo5 = [15, 35, 45]

    elif codigo5 == 'ABAJMP':
        codigo5 = [35, 55, 100]

    elif codigo5 == 'CRUNIZK':
        codigo5 = [10, 30, 30]

    elif codigo5 == 'CRPM':
        codigo5 = [180, 180, 300]

    elif codigo5 == 'CRPE':
        codigo5 = [180, 180, 500]

    elif codigo5 == 'CRJMP':
        codigo5 = [180, 180, 1000000]

    elif codigo5 == 'FQ2':
        codigo5 = [10, 20, 20]

    elif codigo5 == 'FQ34':
        codigo5 = [20, 30, 30]

    elif codigo5 == 'FQ46':
        codigo5 = [40, 50, 40]

    elif codigo5 == 'FQ7+':
        codigo5 = [55, 80, 60]

    elif codigo5 == 'DTA':
        codigo5 = [5, 10, 0]

    elif codigo5 == 'DPIST':
        codigo5 = [10, 15, 0]

    elif codigo5 == 'DPCOM':
        codigo5 = [10, 20, 0]

    elif codigo5 == 'DPISTAP':
        codigo5 = [15, 30, 0]

    elif codigo5 == 'DESCOP':
        codigo5 = [20, 35, 0]

    elif codigo5 == 'DSUB':
        codigo5 = [25, 40, 0]

    elif codigo5 == 'DM4':
        codigo5 = [30, 45, 0]

    elif codigo5 == 'DAK':
        codigo5 = [45, 50, 0]

    elif codigo5 == 'DSNI':
        codigo5 = [45, 60, 0]

    elif codigo5 == 'S':
        codigo5 = [20, 50, 25]

    elif codigo5 == 'SPM':
        codigo5 = [30, 60, 35]

    elif codigo5 == 'SPE':
        codigo5 = [40, 70, 45]

    elif codigo5 == 'SJ':
        codigo5 = [60, 120, 85]

    elif codigo5 == 'SUNIZK':
        codigo5 = [30, 60, 25]

    elif codigo5 == 'TA':
        codigo5 = [20, 60, 30]

    elif codigo5 == 'TAPM':
        codigo5 = [30, 70, 0]

    elif codigo5 == 'TAPE':
        codigo5 = [40, 80, 0]

    elif codigo5 == 'TAJMP':
        codigo5 = [50, 120, 150]

    elif codigo5 == 'ASS':
        codigo5 = [50, 90, 0]

    elif codigo5 == 'ASSU':
        codigo5 = [60, 120, 0]

    elif codigo5 == 'ASSPM':
        codigo5 = [60, 120, 0]

    elif codigo5 == 'ASSPE':
        codigo5 = [70, 120, 0]

    elif codigo5 == 'ASSJ':
        codigo5 = [100, 120, 250]

    elif codigo5 == 'ASSMP':
        codigo5 = [120, 120, 500]

    else:
        print('Este código não existe, reinicie o programa!')
        sleep(5)
        sys.exit()


elif c4 == 'N':
    somamin = codigo[0] + codigo2[0] + codigo3[0] + codigo4[0]  # soma todas os 1 números das listas
    somamax = codigo[1] + codigo2[1] + codigo3[1] + codigo4[1]  # soma todas os 2 números das listas
    somamulta = codigo[2] + codigo2[2] + codigo3[2] + codigo4[2]  # soma todas os 3 números das listas

    print('TEMPO MÍNIMO: {}'.format(somamin))
    print('TEMPO MÁXIMO: {}'.format(somamax))
    print('MULTA: {} mil'.format(somamulta))
    sleep(300)
    sys.exit()

c5 = input('Tem mais códigos? [S/N]').upper()
if c5 == 'S':
    codigo6 = input('Digite o outro código: ').upper()

    if codigo6 == 'TS':
        codigo6 = [25, 40, 20]

    elif codigo6 == 'AP':
        codigo6 = [0, 10, 10]

    elif codigo6 == 'DPB':
        codigo6 = [0, 10, 8]

    elif codigo6 == 'PS':
        codigo6 = [0, 10, 8]

    elif codigo6 == 'OS':
        codigo6 = [5, 16, 12]

    elif codigo6 == 'DOP':
        codigo6 = [5, 15, 5]

    elif codigo6 == 'TF':
        codigo6 = [10, 25, 15]

    elif codigo6 == 'DA':
        codigo6 = [5, 10, 15]

    elif codigo6 == 'DOJ':
        codigo6 = [120, 120, 1000000]

    elif codigo6 == 'DOSN':
        codigo6 = [120, 120, 5000000]

    elif codigo6 == 'A':
        codigo6 = [10, 25, 12]

    elif codigo6 == 'AAPM':
        codigo6 = [10, 35, 25]

    elif codigo6 == 'AAJMP':
        codigo6 = [80, 120, 55]

    elif codigo6 == 'CD':
        codigo6 = [10, 15, 8]

    elif codigo6 == 'CDA':
        codigo6 = [10, 20, 12]

    elif codigo6 == 'CDAJMP':
        codigo6 = [15, 50, 20]

    elif codigo6 == 'FT':
        codigo6 = [10, 50, 25]

    elif codigo6 == 'FI':
        codigo6 = [5, 40, 12]

    elif codigo6 == 'INJ':
        codigo6 = [15, 35, 15]

    elif codigo6 == 'FCUPA':
        codigo6 = [10, 15, 8]

    elif codigo6 == 'FCMT':
        codigo6 = [5, 15, 5]

    elif codigo6 == 'SH':
        codigo6 = [0, 0, 15]

    elif codigo6 == 'SC':
        codigo6 = [0, 0, 5]

    elif codigo6 == 'LP':
        codigo6 = [0, 0, 15]

    elif codigo6 == 'PDC':
        codigo6 = [0, 0, 10]

    elif codigo6 == 'DCO':
        codigo6 = [0, 0, 10]

    elif codigo6 == 'DCO':
        codigo6 = [0, 0, 10]

    elif codigo6 == 'MI':
        codigo6 = [0, 0, 20]

    elif codigo6 == 'DP':
        codigo6 = [3, 20, 25]

    elif codigo6 == 'CI':
        codigo6 = [15, 25, 25]

    elif codigo6 == 'BVA':
        codigo6 = [10, 20, 45]

    elif codigo6 == 'UAUM':
        codigo6 = [5, 15, 10]

    elif codigo6 == 'UAPM':
        codigo6 = [10, 25, 15]

    elif codigo6 == 'UAPE':
        codigo6 = [15, 30, 15]

    elif codigo6 == 'UMCPE':
        codigo6 = [10, 40, 18]

    elif codigo6 == 'PT':
        codigo6 = [10, 15, 0]

    elif codigo6 == 'PP':
        codigo6 = [15, 20, 0]

    elif codigo6 == 'PPC':
        codigo6 = [20, 30, 0]

    elif codigo6 == 'PPAP':
        codigo6 = [25, 40, 0]

    elif codigo6 == 'PESCO':
        codigo6 = [30, 45, 0]

    elif codigo6 == 'PSUB':
        codigo6 = [35, 50, 0]

    elif codigo6 == 'PM4':
        codigo6 = [40, 55, 0]

    elif codigo6 == 'PAK':
        codigo6 = [45, 60, 0]

    elif codigo6 == 'PSNI':
        codigo6 = [55, 70, 0]

    elif codigo6 == 'F':
        codigo6 = [5, 15, 10]

    elif codigo6 == 'R':
        codigo6 = [15, 35, 30]

    elif codigo6 == 'AG':
        codigo6 = [5, 30, 20]

    elif codigo6 == 'AGPM':
        codigo6 = [20, 60, 65]

    elif codigo6 == 'AGJ':
        codigo6 = [30, 80, 80]

    elif codigo6 == 'RFV':
        codigo6 = [40, 65, 25]

    elif codigo6 == 'RFVE':
        codigo6 = [45, 90, 90]

    elif codigo6 == 'INVPV':
        codigo6 = [5, 30, 20]

    elif codigo6 == 'INVLP':
        codigo6 = [10, 40, 30]

    elif codigo6 == 'ABAPM':
        codigo6 = [10, 30, 30]

    elif codigo6 == 'ABAPE':
        codigo6 = [15, 35, 45]

    elif codigo6 == 'ABAJMP':
        codigo6 = [35, 55, 100]

    elif codigo6 == 'CRUNIZK':
        codigo6 = [10, 30, 30]

    elif codigo6 == 'CRPM':
        codigo6 = [180, 180, 300]

    elif codigo6 == 'CRPE':
        codigo6 = [180, 180, 500]

    elif codigo6 == 'CRJMP':
        codigo6 = [180, 180, 1000000]

    elif codigo6 == 'FQ2':
        codigo6 = [10, 20, 20]

    elif codigo6 == 'FQ34':
        codigo6 = [20, 30, 30]

    elif codigo6 == 'FQ46':
        codigo6 = [40, 50, 40]

    elif codigo6 == 'FQ7+':
        codigo6 = [55, 80, 60]

    elif codigo6 == 'DTA':
        codigo6 = [5, 10, 0]

    elif codigo6 == 'DPIST':
        codigo6 = [10, 15, 0]

    elif codigo6 == 'DPCOM':
        codigo6 = [10, 20, 0]

    elif codigo6 == 'DPISTAP':
        codigo6 = [15, 30, 0]

    elif codigo6 == 'DESCOP':
        codigo6 = [20, 35, 0]

    elif codigo6 == 'DSUB':
        codigo6 = [25, 40, 0]

    elif codigo6 == 'DM4':
        codigo6 = [30, 45, 0]

    elif codigo6 == 'DAK':
        codigo6 = [45, 50, 0]

    elif codigo6 == 'DSNI':
        codigo6 = [45, 60, 0]

    elif codigo6 == 'S':
        codigo6 = [20, 50, 25]

    elif codigo6 == 'SPM':
        codigo6 = [30, 60, 35]

    elif codigo6 == 'SPE':
        codigo6 = [40, 70, 45]

    elif codigo6 == 'SJ':
        codigo6 = [60, 120, 85]

    elif codigo6 == 'SUNIZK':
        codigo6 = [30, 60, 25]

    elif codigo6 == 'TA':
        codigo6 = [20, 60, 30]

    elif codigo6 == 'TAPM':
        codigo6 = [30, 70, 0]

    elif codigo6 == 'TAPE':
        codigo6 = [40, 80, 0]

    elif codigo6 == 'TAJMP':
        codigo6 = [50, 120, 150]

    elif codigo6 == 'ASS':
        codigo6 = [50, 90, 0]

    elif codigo6 == 'ASSU':
        codigo6 = [60, 120, 0]

    elif codigo6 == 'ASSPM':
        codigo6 = [60, 120, 0]

    elif codigo6 == 'ASSPE':
        codigo6 = [70, 120, 0]

    elif codigo6 == 'ASSJ':
        codigo6 = [100, 120, 250]

    elif codigo6 == 'ASSMP':
        codigo6 = [120, 120, 500]

    else:
        print('Este código não existe, reinicie o programa!')
        sleep(5)
        sys.exit()


elif c5 == 'N':
    somamin = codigo[0] + codigo2[0] + codigo3[0] + codigo4[0] + codigo5[0]  # soma todas os 1 números das listas
    somamax = codigo[1] + codigo2[1] + codigo3[1] + codigo4[1] + codigo5[1]  # soma todas os 2 números das listas
    somamulta = codigo[2] + codigo2[2] + codigo3[2] + codigo4[2] + codigo5[2]  # soma todas os 3 números das listas

    print('TEMPO MÍNIMO: {}'.format(somamin))
    print('TEMPO MÁXIMO: {}'.format(somamax))
    print('MULTA: {} mil'.format(somamulta))
    sleep(300)
    sys.exit()

c6 = input('Tem mais códigos? [S/N]').upper()
if c6 == 'S':
    codigo7 = input('Digite o outro código: ').upper()

    if codigo7 == 'TS':
        codigo7 = [25, 40, 20]

    elif codigo7 == 'AP':
        codigo7 = [0, 10, 10]

    elif codigo7 == 'DPB':
        codigo7 = [0, 10, 8]

    elif codigo7 == 'PS':
        codigo7 = [0, 10, 8]

    elif codigo7 == 'OS':
        codigo7 = [5, 16, 12]

    elif codigo7 == 'DOP':
        codigo7 = [5, 15, 5]

    elif codigo7 == 'TF':
        codigo7 = [10, 25, 15]

    elif codigo7 == 'DA':
        codigo7 = [5, 10, 15]

    elif codigo7 == 'DOJ':
        codigo7 = [120, 120, 1000000]

    elif codigo7 == 'DOSN':
        codigo7 = [120, 120, 5000000]

    elif codigo7 == 'A':
        codigo7 = [10, 25, 12]

    elif codigo7 == 'AAPM':
        codigo7 = [10, 35, 25]

    elif codigo7 == 'AAJMP':
        codigo7 = [80, 120, 55]

    elif codigo7 == 'CD':
        codigo7 = [10, 15, 8]

    elif codigo7 == 'CDA':
        codigo7 = [10, 20, 12]

    elif codigo7 == 'CDAJMP':
        codigo7 = [15, 50, 20]

    elif codigo7 == 'FT':
        codigo7 = [10, 50, 25]

    elif codigo7 == 'FI':
        codigo7 = [5, 40, 12]

    elif codigo7 == 'INJ':
        codigo7 = [15, 35, 15]

    elif codigo7 == 'FCUPA':
        codigo7 = [10, 15, 8]

    elif codigo7 == 'FCMT':
        codigo7 = [5, 15, 5]

    elif codigo7 == 'SH':
        codigo7 = [0, 0, 15]

    elif codigo7 == 'SC':
        codigo7 = [0, 0, 5]

    elif codigo7 == 'LP':
        codigo7 = [0, 0, 15]

    elif codigo7 == 'PDC':
        codigo7 = [0, 0, 10]

    elif codigo7 == 'DCO':
        codigo7 = [0, 0, 10]

    elif codigo7 == 'DCO':
        codigo7 = [0, 0, 10]

    elif codigo7 == 'MI':
        codigo7 = [0, 0, 20]

    elif codigo7 == 'DP':
        codigo7 = [3, 20, 25]

    elif codigo7 == 'CI':
        codigo7 = [15, 25, 25]

    elif codigo7 == 'BVA':
        codigo7 = [10, 20, 45]

    elif codigo7 == 'UAUM':
        codigo7 = [5, 15, 10]

    elif codigo7 == 'UAPM':
        codigo7 = [10, 25, 15]

    elif codigo7 == 'UAPE':
        codigo7 = [15, 30, 15]

    elif codigo7 == 'UMCPE':
        codigo7 = [10, 40, 18]

    elif codigo7 == 'PT':
        codigo7 = [10, 15, 0]

    elif codigo7 == 'PP':
        codigo7 = [15, 20, 0]

    elif codigo7 == 'PPC':
        codigo7 = [20, 30, 0]

    elif codigo7 == 'PPAP':
        codigo7 = [25, 40, 0]

    elif codigo7 == 'PESCO':
        codigo7 = [30, 45, 0]

    elif codigo7 == 'PSUB':
        codigo7 = [35, 50, 0]

    elif codigo7 == 'PM4':
        codigo7 = [40, 55, 0]

    elif codigo7 == 'PAK':
        codigo7 = [45, 60, 0]

    elif codigo7 == 'PSNI':
        codigo7 = [55, 70, 0]

    elif codigo7 == 'F':
        codigo7 = [5, 15, 10]

    elif codigo7 == 'R':
        codigo7 = [15, 35, 30]

    elif codigo7 == 'AG':
        codigo7 = [5, 30, 20]

    elif codigo7 == 'AGPM':
        codigo7 = [20, 60, 65]

    elif codigo7 == 'AGJ':
        codigo7 = [30, 80, 80]

    elif codigo7 == 'RFV':
        codigo7 = [40, 65, 25]

    elif codigo7 == 'RFVE':
        codigo7 = [45, 90, 90]

    elif codigo7 == 'INVPV':
        codigo7 = [5, 30, 20]

    elif codigo7 == 'INVLP':
        codigo7 = [10, 40, 30]

    elif codigo7 == 'ABAPM':
        codigo7 = [10, 30, 30]

    elif codigo7 == 'ABAPE':
        codigo7 = [15, 35, 45]

    elif codigo7 == 'ABAJMP':
        codigo7 = [35, 55, 100]

    elif codigo7 == 'CRUNIZK':
        codigo7 = [10, 30, 30]

    elif codigo7 == 'CRPM':
        codigo7 = [180, 180, 300]

    elif codigo7 == 'CRPE':
        codigo7 = [180, 180, 500]

    elif codigo7 == 'CRJMP':
        codigo7 = [180, 180, 1000000]

    elif codigo7 == 'FQ2':
        codigo7 = [10, 20, 20]

    elif codigo7 == 'FQ34':
        codigo7 = [20, 30, 30]

    elif codigo7 == 'FQ46':
        codigo7 = [40, 50, 40]

    elif codigo7 == 'FQ7+':
        codigo7 = [55, 80, 60]

    elif codigo7 == 'DTA':
        codigo7 = [5, 10, 0]

    elif codigo7 == 'DPIST':
        codigo7 = [10, 15, 0]

    elif codigo7 == 'DPCOM':
        codigo7 = [10, 20, 0]

    elif codigo7 == 'DPISTAP':
        codigo7 = [15, 30, 0]

    elif codigo7 == 'DESCOP':
        codigo7 = [20, 35, 0]

    elif codigo7 == 'DSUB':
        codigo7 = [25, 40, 0]

    elif codigo7 == 'DM4':
        codigo7 = [30, 45, 0]

    elif codigo7 == 'DAK':
        codigo7 = [45, 50, 0]

    elif codigo7 == 'DSNI':
        codigo7 = [45, 60, 0]

    elif codigo7 == 'S':
        codigo7 = [20, 50, 25]

    elif codigo7 == 'SPM':
        codigo7 = [30, 60, 35]

    elif codigo7 == 'SPE':
        codigo7 = [40, 70, 45]

    elif codigo7 == 'SJ':
        codigo7 = [60, 120, 85]

    elif codigo7 == 'SUNIZK':
        codigo7 = [30, 60, 25]

    elif codigo7 == 'TA':
        codigo7 = [20, 60, 30]

    elif codigo7 == 'TAPM':
        codigo7 = [30, 70, 0]

    elif codigo7 == 'TAPE':
        codigo7 = [40, 80, 0]

    elif codigo7 == 'TAJMP':
        codigo7 = [50, 120, 150]

    elif codigo7 == 'ASS':
        codigo7 = [50, 90, 0]

    elif codigo7 == 'ASSU':
        codigo7 = [60, 120, 0]

    elif codigo7 == 'ASSPM':
        codigo7 = [60, 120, 0]

    elif codigo7 == 'ASSPE':
        codigo7 = [70, 120, 0]

    elif codigo7 == 'ASSJ':
        codigo7 = [100, 120, 250]

    elif codigo7 == 'ASSMP':
        codigo7 = [120, 120, 500]

    else:
        print('Este código não existe, reinicie o programa!')
        sleep(5)
        sys.exit()


elif c6 == 'N':
    somamin = codigo[0] + codigo2[0] + codigo3[0] + codigo4[0] + codigo5[0] + codigo6[
        0]  # soma todas os 1 números das listas
    somamax = codigo[1] + codigo2[1] + codigo3[1] + codigo4[1] + codigo5[1] + codigo6[
        1]  # soma todas os 2 números das listas
    somamulta = codigo[2] + codigo2[2] + codigo3[2] + codigo4[2] + codigo5[2] + codigo6[
        2]  # soma todas os 3 números das listas

    print('TEMPO MÍNIMO: {}'.format(somamin))
    print('TEMPO MÁXIMO: {}'.format(somamax))
    print('MULTA: {} mil'.format(somamulta))
    sleep(300)
    sys.exit()

c7 = input('Tem mais códigos? [S/N]').upper()
if c7 == 'S':
    codigo8 = input('Digite o outro código: ').upper()

    if codigo8 == 'TS':
        codigo8 = [25, 40, 20]

    elif codigo8 == 'AP':
        codigo8 = [0, 10, 10]

    elif codigo8 == 'DPB':
        codigo8 = [0, 10, 8]

    elif codigo8 == 'PS':
        codigo8 = [0, 10, 8]

    elif codigo8 == 'OS':
        codigo8 = [5, 16, 12]

    elif codigo8 == 'DOP':
        codigo8 = [5, 15, 5]

    elif codigo8 == 'TF':
        codigo8 = [10, 25, 15]

    elif codigo8 == 'DA':
        codigo8 = [5, 10, 15]

    elif codigo8 == 'DOJ':
        codigo8 = [120, 120, 1000000]

    elif codigo8 == 'DOSN':
        codigo8 = [120, 120, 5000000]

    elif codigo8 == 'A':
        codigo8 = [10, 25, 12]

    elif codigo8 == 'AAPM':
        codigo8 = [10, 35, 25]

    elif codigo8 == 'AAJMP':
        codigo8 = [80, 120, 55]

    elif codigo8 == 'CD':
        codigo8 = [10, 15, 8]

    elif codigo8 == 'CDA':
        codigo8 = [10, 20, 12]

    elif codigo8 == 'CDAJMP':
        codigo8 = [15, 50, 20]

    elif codigo8 == 'FT':
        codigo8 = [10, 50, 25]

    elif codigo8 == 'FI':
        codigo8 = [5, 40, 12]

    elif codigo8 == 'INJ':
        codigo8 = [15, 35, 15]

    elif codigo8 == 'FCUPA':
        codigo8 = [10, 15, 8]

    elif codigo8 == 'FCMT':
        codigo8 = [5, 15, 5]

    elif codigo8 == 'SH':
        codigo8 = [0, 0, 15]

    elif codigo8 == 'SC':
        codigo8 = [0, 0, 5]

    elif codigo8 == 'LP':
        codigo8 = [0, 0, 15]

    elif codigo8 == 'PDC':
        codigo8 = [0, 0, 10]

    elif codigo8 == 'DCO':
        codigo8 = [0, 0, 10]

    elif codigo8 == 'DCO':
        codigo8 = [0, 0, 10]

    elif codigo8 == 'MI':
        codigo8 = [0, 0, 20]

    elif codigo8 == 'DP':
        codigo8 = [3, 20, 25]

    elif codigo8 == 'CI':
        codigo8 = [15, 25, 25]

    elif codigo8 == 'BVA':
        codigo8 = [10, 20, 45]

    elif codigo8 == 'UAUM':
        codigo8 = [5, 15, 10]

    elif codigo8 == 'UAPM':
        codigo8 = [10, 25, 15]

    elif codigo8 == 'UAPE':
        codigo8 = [15, 30, 15]

    elif codigo8 == 'UMCPE':
        codigo8 = [10, 40, 18]

    elif codigo8 == 'PT':
        codigo8 = [10, 15, 0]

    elif codigo8 == 'PP':
        codigo8 = [15, 20, 0]

    elif codigo8 == 'PPC':
        codigo8 = [20, 30, 0]

    elif codigo8 == 'PPAP':
        codigo8 = [25, 40, 0]

    elif codigo8 == 'PESCO':
        codigo8 = [30, 45, 0]

    elif codigo8 == 'PSUB':
        codigo8 = [35, 50, 0]

    elif codigo8 == 'PM4':
        codigo8 = [40, 55, 0]

    elif codigo8 == 'PAK':
        codigo8 = [45, 60, 0]

    elif codigo8 == 'PSNI':
        codigo8 = [55, 70, 0]

    elif codigo8 == 'F':
        codigo8 = [5, 15, 10]

    elif codigo8 == 'R':
        codigo8 = [15, 35, 30]

    elif codigo8 == 'AG':
        codigo8 = [5, 30, 20]

    elif codigo8 == 'AGPM':
        codigo8 = [20, 60, 65]

    elif codigo8 == 'AGJ':
        codigo8 = [30, 80, 80]

    elif codigo8 == 'RFV':
        codigo8 = [40, 65, 25]

    elif codigo8 == 'RFVE':
        codigo8 = [45, 90, 90]

    elif codigo8 == 'INVPV':
        codigo8 = [5, 30, 20]

    elif codigo8 == 'INVLP':
        codigo8 = [10, 40, 30]

    elif codigo8 == 'ABAPM':
        codigo8 = [10, 30, 30]

    elif codigo8 == 'ABAPE':
        codigo8 = [15, 35, 45]

    elif codigo8 == 'ABAJMP':
        codigo8 = [35, 55, 100]

    elif codigo8 == 'CRUNIZK':
        codigo8 = [10, 30, 30]

    elif codigo8 == 'CRPM':
        codigo8 = [180, 180, 300]

    elif codigo8 == 'CRPE':
        codigo8 = [180, 180, 500]

    elif codigo8 == 'CRJMP':
        codigo8 = [180, 180, 1000000]

    elif codigo8 == 'FQ2':
        codigo8 = [10, 20, 20]

    elif codigo8 == 'FQ34':
        codigo8 = [20, 30, 30]

    elif codigo8 == 'FQ46':
        codigo8 = [40, 50, 40]

    elif codigo8 == 'FQ7+':
        codigo8 = [55, 80, 60]

    elif codigo8 == 'DTA':
        codigo8 = [5, 10, 0]

    elif codigo8 == 'DPIST':
        codigo8 = [10, 15, 0]

    elif codigo8 == 'DPCOM':
        codigo8 = [10, 20, 0]

    elif codigo8 == 'DPISTAP':
        codigo8 = [15, 30, 0]

    elif codigo8 == 'DESCOP':
        codigo8 = [20, 35, 0]

    elif codigo8 == 'DSUB':
        codigo8 = [25, 40, 0]

    elif codigo8 == 'DM4':
        codigo8 = [30, 45, 0]

    elif codigo8 == 'DAK':
        codigo8 = [45, 50, 0]

    elif codigo8 == 'DSNI':
        codigo8 = [45, 60, 0]

    elif codigo8 == 'S':
        codigo8 = [20, 50, 25]

    elif codigo8 == 'SPM':
        codigo8 = [30, 60, 35]

    elif codigo8 == 'SPE':
        codigo8 = [40, 70, 45]

    elif codigo8 == 'SJ':
        codigo8 = [60, 120, 85]

    elif codigo8 == 'SUNIZK':
        codigo8 = [30, 60, 25]

    elif codigo8 == 'TA':
        codigo8 = [20, 60, 30]

    elif codigo8 == 'TAPM':
        codigo8 = [30, 70, 0]

    elif codigo8 == 'TAPE':
        codigo8 = [40, 80, 0]

    elif codigo8 == 'TAJMP':
        codigo8 = [50, 120, 150]

    elif codigo8 == 'ASS':
        codigo8 = [50, 90, 0]

    elif codigo8 == 'ASSU':
        codigo8 = [60, 120, 0]

    elif codigo8 == 'ASSPM':
        codigo8 = [60, 120, 0]

    elif codigo8 == 'ASSPE':
        codigo8 = [70, 120, 0]

    elif codigo8 == 'ASSJ':
        codigo8 = [100, 120, 250]

    elif codigo8 == 'ASSMP':
        codigo8 = [120, 120, 500]

    else:
        print('Este código não existe, reinicie o programa!')
        sleep(5)
        sys.exit()


elif c7 == 'N':
    somamin = codigo[0] + codigo2[0] + codigo3[0] + codigo4[0] + codigo5[0] + codigo6[0] + codigo7[
        0]  # soma todas os 1 números das listas
    somamax = codigo[1] + codigo2[1] + codigo3[1] + codigo4[1] + codigo5[1] + codigo6[1] + codigo7[
        1]  # soma todas os 2 números das listas
    somamulta = codigo[2] + codigo2[2] + codigo3[2] + codigo4[2] + codigo5[2] + codigo6[2] + codigo7[
        2]  # soma todas os 3 números das listas

    print('TEMPO MÍNIMO: {}'.format(somamin))
    print('TEMPO MÁXIMO: {}'.format(somamax))
    print('MULTA: {} mil'.format(somamulta))
    sleep(300)
    sys.exit()

c8 = input('Tem mais códigos? [S/N]').upper()
if c8 == 'S':
    codigo9 = input('Digite o seu último código: ').upper()

    if codigo9 == 'TS':
        codigo9 = [25, 40, 20]

    elif codigo9 == 'AP':
        codigo9 = [0, 10, 10]

    elif codigo9 == 'DPB':
        codigo9 = [0, 10, 8]

    elif codigo9 == 'PS':
        codigo9 = [0, 10, 8]

    elif codigo9 == 'OS':
        codigo9 = [5, 16, 12]

    elif codigo9 == 'DOP':
        codigo9 = [5, 15, 5]

    elif codigo9 == 'TF':
        codigo9 = [10, 25, 15]

    elif codigo9 == 'DA':
        codigo9 = [5, 10, 15]

    elif codigo9 == 'DOJ':
        codigo9 = [120, 120, 1000000]

    elif codigo9 == 'DOSN':
        codigo9 = [120, 120, 5000000]

    elif codigo9 == 'A':
        codigo9 = [10, 25, 12]

    elif codigo9 == 'AAPM':
        codigo9 = [10, 35, 25]

    elif codigo9 == 'AAJMP':
        codigo9 = [80, 120, 55]

    elif codigo9 == 'CD':
        codigo9 = [10, 15, 8]

    elif codigo9 == 'CDA':
        codigo9 = [10, 20, 12]

    elif codigo9 == 'CDAJMP':
        codigo9 = [15, 50, 20]

    elif codigo9 == 'FT':
        codigo9 = [10, 50, 25]

    elif codigo9 == 'FI':
        codigo9 = [5, 40, 12]

    elif codigo9 == 'INJ':
        codigo9 = [15, 35, 15]

    elif codigo9 == 'FCUPA':
        codigo9 = [10, 15, 8]

    elif codigo9 == 'FCMT':
        codigo9 = [5, 15, 5]

    elif codigo9 == 'SH':
        codigo9 = [0, 0, 15]

    elif codigo9 == 'SC':
        codigo9 = [0, 0, 5]

    elif codigo9 == 'LP':
        codigo9 = [0, 0, 15]

    elif codigo9 == 'PDC':
        codigo9 = [0, 0, 10]

    elif codigo9 == 'DCO':
        codigo9 = [0, 0, 10]

    elif codigo9 == 'DCO':
        codigo9 = [0, 0, 10]

    elif codigo9 == 'MI':
        codigo9 = [0, 0, 20]

    elif codigo9 == 'DP':
        codigo9 = [3, 20, 25]

    elif codigo9 == 'CI':
        codigo9 = [15, 25, 25]

    elif codigo9 == 'BVA':
        codigo9 = [10, 20, 45]

    elif codigo9 == 'UAUM':
        codigo9 = [5, 15, 10]

    elif codigo9 == 'UAPM':
        codigo9 = [10, 25, 15]

    elif codigo9 == 'UAPE':
        codigo9 = [15, 30, 15]

    elif codigo9 == 'UMCPE':
        codigo9 = [10, 40, 18]

    elif codigo9 == 'PT':
        codigo9 = [10, 15, 0]

    elif codigo9 == 'PP':
        codigo9 = [15, 20, 0]

    elif codigo9 == 'PPC':
        codigo9 = [20, 30, 0]

    elif codigo9 == 'PPAP':
        codigo9 = [25, 40, 0]

    elif codigo9 == 'PESCO':
        codigo9 = [30, 45, 0]

    elif codigo9 == 'PSUB':
        codigo9 = [35, 50, 0]

    elif codigo9 == 'PM4':
        codigo9 = [40, 55, 0]

    elif codigo9 == 'PAK':
        codigo9 = [45, 60, 0]

    elif codigo9 == 'PSNI':
        codigo9 = [55, 70, 0]

    elif codigo9 == 'F':
        codigo9 = [5, 15, 10]

    elif codigo9 == 'R':
        codigo9 = [15, 35, 30]

    elif codigo9 == 'AG':
        codigo9 = [5, 30, 20]

    elif codigo9 == 'AGPM':
        codigo9 = [20, 60, 65]

    elif codigo9 == 'AGJ':
        codigo9 = [30, 80, 80]

    elif codigo9 == 'RFV':
        codigo9 = [40, 65, 25]

    elif codigo9 == 'RFVE':
        codigo9 = [45, 90, 90]

    elif codigo9 == 'INVPV':
        codigo9 = [5, 30, 20]

    elif codigo9 == 'INVLP':
        codigo9 = [10, 40, 30]

    elif codigo9 == 'ABAPM':
        codigo9 = [10, 30, 30]

    elif codigo9 == 'ABAPE':
        codigo9 = [15, 35, 45]

    elif codigo9 == 'ABAJMP':
        codigo9 = [35, 55, 100]

    elif codigo9 == 'CRUNIZK':
        codigo9 = [10, 30, 30]

    elif codigo9 == 'CRPM':
        codigo9 = [180, 180, 300]

    elif codigo9 == 'CRPE':
        codigo9 = [180, 180, 500]

    elif codigo9 == 'CRJMP':
        codigo9 = [180, 180, 1000000]

    elif codigo9 == 'FQ2':
        codigo9 = [10, 20, 20]

    elif codigo9 == 'FQ34':
        codigo9 = [20, 30, 30]

    elif codigo9 == 'FQ46':
        codigo9 = [40, 50, 40]

    elif codigo9 == 'FQ7+':
        codigo9 = [55, 80, 60]

    elif codigo9 == 'DTA':
        codigo9 = [5, 10, 0]

    elif codigo9 == 'DPIST':
        codigo9 = [10, 15, 0]

    elif codigo9 == 'DPCOM':
        codigo9 = [10, 20, 0]

    elif codigo9 == 'DPISTAP':
        codigo9 = [15, 30, 0]

    elif codigo9 == 'DESCOP':
        codigo9 = [20, 35, 0]

    elif codigo9 == 'DSUB':
        codigo9 = [25, 40, 0]

    elif codigo9 == 'DM4':
        codigo9 = [30, 45, 0]

    elif codigo9 == 'DAK':
        codigo9 = [45, 50, 0]

    elif codigo9 == 'DSNI':
        codigo9 = [45, 60, 0]

    elif codigo9 == 'S':
        codigo9 = [20, 50, 25]

    elif codigo9 == 'SPM':
        codigo9 = [30, 60, 35]

    elif codigo9 == 'SPE':
        codigo9 = [40, 70, 45]

    elif codigo9 == 'SJ':
        codigo9 = [60, 120, 85]

    elif codigo9 == 'SUNIZK':
        codigo9 = [30, 60, 25]

    elif codigo9 == 'TA':
        codigo9 = [20, 60, 30]

    elif codigo9 == 'TAPM':
        codigo9 = [30, 70, 0]

    elif codigo9 == 'TAPE':
        codigo9 = [40, 80, 0]

    elif codigo9 == 'TAJMP':
        codigo9 = [50, 120, 150]

    elif codigo9 == 'ASS':
        codigo9 = [50, 90, 0]

    elif codigo9 == 'ASSU':
        codigo9 = [60, 120, 0]

    elif codigo9 == 'ASSPM':
        codigo9 = [60, 120, 0]

    elif codigo9 == 'ASSPE':
        codigo9 = [70, 120, 0]

    elif codigo9 == 'ASSJ':
        codigo9 = [100, 120, 250]

    elif codigo9 == 'ASSMP':
        codigo9 = [120, 120, 500]

    else:
        print('Este código não existe, reinicie o programa!')
        sleep(5)
        sys.exit()



    somamin = codigo[0] + codigo2[0] + codigo3[0] + codigo4[0] + codigo5[0] + codigo6[0] + codigo7[0] + codigo8[0] + \
              codigo9[0]  # soma todas os 1 números das listas
    somamax = codigo[1] + codigo2[1] + codigo3[1] + codigo4[1] + codigo5[1] + codigo6[1] + codigo7[1] + codigo8[1] + \
              codigo9[1]  # soma todas os 2 números das listas
    somamulta = codigo[2] + codigo2[2] + codigo3[2] + codigo4[2] + codigo5[2] + codigo6[2] + codigo7[2] + codigo8[2] + \
                codigo9[2]  # soma todas os 3 números das listas

    print('TEMPO MÍNIMO: {}'.format(somamin))
    print('TEMPO MÁXIMO: {}'.format(somamax))
    print('MULTA: {} mil'.format(somamulta))
    sleep(300)
    sys.exit()

elif c8 == 'N':
    somamin = codigo[0] + codigo2[0] + codigo3[0] + codigo4[0] + codigo5[0] + codigo6[0] + codigo7[0] + codigo8[
        0]  # soma todas os 1 números das listas
    somamax = codigo[1] + codigo2[1] + codigo3[1] + codigo4[1] + codigo5[1] + codigo6[1] + codigo7[1] + codigo8[
        1]  # soma todas os 2 números das listas
    somamulta = codigo[2] + codigo2[2] + codigo3[2] + codigo4[2] + codigo5[2] + codigo6[2] + codigo7[2] + codigo8[
        2]  # soma todas os 3 números das listas

    print('TEMPO MÍNIMO: {}'.format(somamin))
    print('TEMPO MÁXIMO: {}'.format(somamax))
    print('MULTA: {} mil'.format(somamulta))
    sleep(300)
    sys.exit()
