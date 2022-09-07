import os
import sys
from time import sleep

print("\nBem vindo ao código penal do ---FAEL---\n")
print("Aqui a baixo está a lista de códigos que você deverá usar.\n ")
print("USE AS SIGLAS NO FINAL, ENTRE PARENTESES:")
print("""*Crimes Básicos:
-Uniforme Mecanico/SAMU/CET	(UI)
-Uniforme Judiciário		(UJ)	
-Uniforme Polica Militar	(UPM)
-Uniforme Policia Federal	(UPF)	
-Traje Balistico		(TB)
-Uso de Máscara			(UM)

*Porte/Posse:
-Taurus / Fiveseven			(PP)
-Glock G19 / G25			(PGL)
-Escopeta				(PE)
-Sub-Metralhadora			(PSM)
-Fuzil de Assalto 7.62			(PFA)	
-Lockpick				(PLP)

**Crimes leves:
-Resistência a Prisão			(RP)
-Tentativa de Fuga			(TF)
-Omissão de Socorro			(OS)
-Dano á Patrimonio Público		(DPP)
-Difamação				(DF)
-Furto					(F)
-Sequestro				(S)
-Ameaça					(A)
-Ameaça ao Servidor Público		(ASP)
-Ameaça á Jurisdição			(AJ)

*Crimes medianos:
-Desobediência				(DS)	
-Desacato				(D)
-Extorsão				(E)
-Falsidade Ideológica			(FI)
-Calunia				(CL)
-Corrupção				(CP)
-Atentado ao Pudor			(AP)
-Pertubação da Paz (Poluição Sonora)	(PB)
-Agressão				(AG)
-Roubo					(RB)
-Apologia ao crime			(AC)
-Discurso de ódio'			(DO)

*Crimes Hediondos:
-Homicídio Culposo (Sem Intenção de Matar)	(HC)
-Homicídio Doloso (Com Intenção de Matar)	(HD)
-Tentativa de homicídio				(TH)
-Latrocínio (Roubo seguido de Morte)		(LT)
-Genocídio/Crimes de ódio			(GC)	
-Tentativa de homicídio de Servidor Público	(THSP)
-Homicídio de Servidor Público			(HSP)
-Assassinato ao Ministro			(ASM)

*Formação de quadrilha:
-2 membros	(FQ2)
-3 á 4 membros	(FQ34)
-4 á 6 membros	(FQ46)
-7 á 10 membros	(FQ710)
-10 ou mais	(FQ10)

  Obs:
	drogas = 1 mes a cada 4kg (2.000 multa a cada mes)
	din. sujo = 1 mes a cada 5.000 (2.000 multa a cada mes)
	semente de droga = 1 mes a cada 4kg (12.000 multa livre)
	componente de arma = 1 mes a cada unidade (2.000 multa a unid.)
	acima de 100 municao = 1 mes a cada 10 (5.000 multa livre)
""")

UI = [0, 10, 5000]
UJ = [5, 15, 5000]
UPM = [5, 20, 15000]
UPF = [5, 25, 15000]
TB = [0, 10, 5000]
UM = [5, 20, 12000]

PP = [10, 20, 15000]
PGL = [15, 25, 15000]
PE = [40, 50, 15000]
PSM = [35, 70, 15000]
PFA = [45, 75, 18000]
PLP = [30, 55, 18000]

RP = [5, 20, 5000]
TF = [10, 20, 15000]
OS = [10, 50, 30000]
DPP = [5, 15, 10000]
DF = [15, 25, 10000]
F = [20, 40, 30000]
S = [20, 35, 25000]
A = [5, 20, 2000]
ASP = [20, 30, 30000]
AJ = [60, 100, 80000]

DS = [10, 20, 15000]
D = [5, 20, 10000]
E = [20, 30, 30000]
FI = [5, 75, 18000]
CL = [40, 55, 25000]
CP = [60, 100, 80000]
AP = [5, 10, 10000]
PB = [5, 25, 20000]
AG = [5, 20, 10000]
RB = [25, 45, 25000]
AC = [25, 50, 30000]
DO = [30, 60, 25000]

HC = [40, 60, 50000]
HD = [80, 95, 70000]
TH = [35, 35, 30000]
LT = [40, 95, 45000]
GC = [100, 100, 50000]
THSP = [45, 45, 37000]
HSP = [80, 80, 200000]
ASM = [180, 180, 400000]

FQ2 = [20, 35, 25000]
FQ34 = [25, 40, 25000]
FQ46 = [30, 40, 25000]
FQ710 = [40, 65, 30000]
FQ10 = [45, 95, 45000]

print("\nVamos lá...\n")
codigo = input("Qual a sigla do código? ").upper()
if codigo == 'UI':
    codigo = UI

elif codigo == 'UJ':
    codigo = UJ

elif codigo == 'UPM':
    codigo = UPM

elif codigo == 'UPF':
    codigo = UPF

elif codigo == 'TB':
    codigo = TB

elif codigo == 'UM':
    codigo = UM

elif codigo == 'PP':
    codigo = PP

elif codigo == 'PGL':
    codigo = PGL

elif codigo == 'PE':
    codigo = PE

elif codigo == 'PSM':
    codigo = PSM

elif codigo == 'PFA':
    codigo = PFA

elif codigo == 'PLP':
    codigo = PLP

elif codigo == 'RP':
    codigo = RP

elif codigo == 'TF':
    codigo = TF

elif codigo == 'OS':
    codigo = OS

elif codigo == 'DPP':
    codigo = DPP

elif codigo == 'DPP':
    codigo = DPP

elif codigo == 'DF':
    codigo = DF

elif codigo == 'F':
    codigo = F

elif codigo == 'S':
    codigo = S

elif codigo == 'A':
    codigo = A

elif codigo == 'ASP':
    codigo = ASP

elif codigo == 'AJ':
    codigo = AJ

elif codigo == 'DS':
    codigo = DS

elif codigo == 'D':
    codigo = D

elif codigo == 'E':
    codigo = E

elif codigo == 'FI':
    codigo = FI

elif codigo == 'CL':
    codigo = CL

elif codigo == 'CP':
    codigo = CP

elif codigo == 'AP':
    codigo = AP

elif codigo == 'PB':
    codigo = PB

elif codigo == 'AG':
    codigo = AG

elif codigo == 'RB':
    codigo = RB

elif codigo == 'AC':
    codigo = AC

elif codigo == 'DO':
    codigo = DO

elif codigo == 'HC':
    codigo = HC

elif codigo == 'HD':
    codigo = HD

elif codigo == 'HD':
    codigo = HD

elif codigo == 'TH':
    codigo = TH

elif codigo == 'LT':
    codigo = LT

elif codigo == 'GC':
    codigo = GC

elif codigo == 'THSP':
    codigo = THSP

elif codigo == 'HSP':
    codigo = HSP

elif codigo == 'ASM':
    codigo = ASM

elif codigo == 'FQ2':
    codigo = FQ2

elif codigo == 'FQ34':
    codigo = FQ34

elif codigo == 'FQ46':
    codigo = FQ46

elif codigo == 'FQ710':
    codigo = FQ710

elif codigo == 'FQ10':
    codigo = FQ10
else:
    print('Este código não existe, reinicie o programa!')
    sleep(5)
    sys.exit()

c1 = input('Tem mais códigos? [S/N]').upper()
if c1 == 'S':
    codigo2 = input('Digite o outro código: ').upper()
    if codigo2 == 'UI':
        codigo2 = UI

    elif codigo2 == 'UJ':
        codigo2 = UJ

    elif codigo2 == 'UPM':
        codigo2 = UPM

    elif codigo2 == 'UPF':
        codigo2 = UPF

    elif codigo2 == 'TB':
        codigo2 = TB

    elif codigo2 == 'UM':
        codigo2 = UM

    elif codigo2 == 'PP':
        codigo2 = PP

    elif codigo2 == 'PGL':
        codigo2 = PGL

    elif codigo2 == 'PE':
        codigo2 = PE

    elif codigo2 == 'PSM':
        codigo2 = PSM

    elif codigo2 == 'PFA':
        codigo2 = PFA

    elif codigo2 == 'PLP':
        codigo2 = PLP

    elif codigo2 == 'RP':
        codigo2 = RP

    elif codigo2 == 'TF':
        codigo2 = TF

    elif codigo2 == 'OS':
        codigo2 = OS

    elif codigo2 == 'DPP':
        codigo2 = DPP

    elif codigo2 == 'DPP':
        codigo2 = DPP

    elif codigo2 == 'DF':
        codigo2 = DF

    elif codigo2 == 'F':
        codigo2 = F

    elif codigo2 == 'S':
        codigo2 = S

    elif codigo2 == 'A':
        codigo2 = A

    elif codigo2 == 'ASP':
        codigo2 = ASP

    elif codigo2 == 'AJ':
        codigo2 = AJ

    elif codigo2 == 'DS':
        codigo2 = DS

    elif codigo2 == 'D':
        codigo2 = D

    elif codigo2 == 'E':
        codigo2 = E

    elif codigo2 == 'FI':
        codigo2 = FI

    elif codigo2 == 'CL':
        codigo2 = CL

    elif codigo2 == 'CP':
        codigo2 = CP

    elif codigo2 == 'AP':
        codigo2 = AP

    elif codigo2 == 'PB':
        codigo2 = PB

    elif codigo2 == 'AG':
        codigo2 = AG

    elif codigo2 == 'RB':
        codigo2 = RB

    elif codigo2 == 'AC':
        codigo2 = AC

    elif codigo2 == 'DO':
        codigo2 = DO

    elif codigo2 == 'HC':
        codigo2 = HC

    elif codigo2 == 'HD':
        codigo2 = HD

    elif codigo2 == 'HD':
        codigo2 = HD

    elif codigo2 == 'TH':
        codigo2 = TH

    elif codigo2 == 'LT':
        codigo2 = LT

    elif codigo2 == 'GC':
        codigo2 = GC

    elif codigo2 == 'THSP':
        codigo2 = THSP

    elif codigo2 == 'HSP':
        codigo2 = HSP

    elif codigo2 == 'ASM':
        codigo2 = ASM

    elif codigo2 == 'FQ2':
        codigo2 = FQ2

    elif codigo2 == 'FQ34':
        codigo2 = FQ34

    elif codigo2 == 'FQ46':
        codigo2 = FQ46

    elif codigo2 == 'FQ710':
        codigo2 = FQ710

    elif codigo2 == 'FQ10':
        codigo2 = FQ10
    else:
        print('Este código não existe, reinicie o programa!')
        sleep(5)
        sys.exit()

elif c1 == 'N':
    print('TEMPO MÍNIMO: {}'.format(codigo[0]))
    print('TEMPO MÁXIMO: {}'.format(codigo[1]))
    print('MULTA: {}'.format(codigo[2]))
    sleep(300)
    sys.exit()

c2 = input('Tem mais códigos? [S/N]').upper()
if c2 == 'S':
    codigo3 = input('Digite o outro código: ').upper()
    if codigo3 == 'UI':
        codigo3 = UI

    elif codigo3 == 'UJ':
        codigo3 = UJ

    elif codigo3 == 'UPM':
        codigo3 = UPM

    elif codigo3 == 'UPF':
        codigo3 = UPF

    elif codigo3 == 'TB':
        codigo3 = TB

    elif codigo3 == 'UM':
        codigo3 = UM

    elif codigo3 == 'PP':
        codigo3 = PP

    elif codigo3 == 'PGL':
        codigo3 = PGL

    elif codigo3 == 'PE':
        codigo3 = PE

    elif codigo3 == 'PSM':
        codigo3 = PSM

    elif codigo3 == 'PFA':
        codigo3 = PFA

    elif codigo3 == 'PLP':
        codigo3 = PLP

    elif codigo3 == 'RP':
        codigo3 = RP

    elif codigo3 == 'TF':
        codigo3 = TF

    elif codigo3 == 'OS':
        codigo3 = OS

    elif codigo3 == 'DPP':
        codigo3 = DPP

    elif codigo3 == 'DPP':
        codigo3 = DPP

    elif codigo3 == 'DF':
        codigo3 = DF

    elif codigo3 == 'F':
        codigo3 = F

    elif codigo3 == 'S':
        codigo3 = S

    elif codigo3 == 'A':
        codigo3 = A

    elif codigo3 == 'ASP':
        codigo3 = ASP

    elif codigo3 == 'AJ':
        codigo3 = AJ

    elif codigo3 == 'DS':
        codigo3 = DS

    elif codigo3 == 'D':
        codigo3 = D

    elif codigo3 == 'E':
        codigo3 = E

    elif codigo3 == 'FI':
        codigo3 = FI

    elif codigo3 == 'CL':
        codigo3 = CL

    elif codigo3 == 'CP':
        codigo3 = CP

    elif codigo3 == 'AP':
        codigo3 = AP

    elif codigo3 == 'PB':
        codigo3 = PB

    elif codigo3 == 'AG':
        codigo3 = AG

    elif codigo3 == 'RB':
        codigo3 = RB

    elif codigo3 == 'AC':
        codigo3 = AC

    elif codigo3 == 'DO':
        codigo3 = DO

    elif codigo3 == 'HC':
        codigo3 = HC

    elif codigo3 == 'HD':
        codigo3 = HD

    elif codigo3 == 'HD':
        codigo3 = HD

    elif codigo3 == 'TH':
        codigo3 = TH

    elif codigo3 == 'LT':
        codigo3 = LT

    elif codigo3 == 'GC':
        codigo3 = GC

    elif codigo3 == 'THSP':
        codigo3 = THSP

    elif codigo3 == 'HSP':
        codigo3 = HSP

    elif codigo3 == 'ASM':
        codigo3 = ASM

    elif codigo3 == 'FQ2':
        codigo3 = FQ2

    elif codigo3 == 'FQ34':
        codigo3 = FQ34

    elif codigo3 == 'FQ46':
        codigo3 = FQ46

    elif codigo3 == 'FQ710':
        codigo3 = FQ710

    elif codigo3 == 'FQ10':
        codigo3 = FQ10
    else:
        print('Este código não existe, reinicie o programa!')
        sleep(5)
        sys.exit()

elif c2 == 'N':
    soma1 = [(a + b) for a, b in zip(codigo, codigo2)]
    print('TEMPO MÍNIMO: {}'.format(soma1[0]))
    print('TEMPO MÁXIMO: {}'.format(soma1[1]))
    print('MULTA: {}'.format(soma1[2]))
    sleep(300)
    sys.exit()

c3 = input('Tem mais códigos? [S/N]').upper()
if c3 == 'S':
    codigo4 = input('Digite o outro código: ').upper()

    if codigo4 == 'UI':
        codigo4 = UI

    elif codigo4 == 'UJ':
        codigo4 = UJ

    elif codigo4 == 'UPM':
        codigo4 = UPM

    elif codigo4 == 'UPF':
        codigo4 = UPF

    elif codigo4 == 'TB':
        codigo4 = TB

    elif codigo4 == 'UM':
        codigo4 = UM

    elif codigo4 == 'PP':
        codigo4 = PP

    elif codigo4 == 'PGL':
        codigo4 = PGL

    elif codigo4 == 'PE':
        codigo4 = PE

    elif codigo4 == 'PSM':
        codigo4 = PSM

    elif codigo4 == 'PFA':
        codigo4 = PFA

    elif codigo4 == 'PLP':
        codigo4 = PLP

    elif codigo4 == 'RP':
        codigo4 = RP

    elif codigo4 == 'TF':
        codigo4 = TF

    elif codigo4 == 'OS':
        codigo4 = OS

    elif codigo4 == 'DPP':
        codigo4 = DPP

    elif codigo4 == 'DPP':
        codigo4 = DPP

    elif codigo4 == 'DF':
        codigo4 = DF

    elif codigo4 == 'F':
        codigo4 = F

    elif codigo4 == 'S':
        codigo4 = S

    elif codigo4 == 'A':
        codigo4 = A

    elif codigo4 == 'ASP':
        codigo4 = ASP

    elif codigo4 == 'AJ':
        codigo4 = AJ

    elif codigo4 == 'DS':
        codigo4 = DS

    elif codigo4 == 'D':
        codigo4 = D

    elif codigo4 == 'E':
        codigo4 = E

    elif codigo4 == 'FI':
        codigo4 = FI

    elif codigo4 == 'CL':
        codigo4 = CL

    elif codigo4 == 'CP':
        codigo4 = CP

    elif codigo4 == 'AP':
        codigo4 = AP

    elif codigo4 == 'PB':
        codigo4 = PB

    elif codigo4 == 'AG':
        codigo4 = AG

    elif codigo4 == 'RB':
        codigo4 = RB

    elif codigo4 == 'AC':
        codigo4 = AC

    elif codigo4 == 'DO':
        codigo4 = DO

    elif codigo4 == 'HC':
        codigo4 = HC

    elif codigo4 == 'HD':
        codigo4 = HD

    elif codigo4 == 'HD':
        codigo4 = HD

    elif codigo4 == 'TH':
        codigo4 = TH

    elif codigo4 == 'LT':
        codigo4 = LT

    elif codigo4 == 'GC':
        codigo4 = GC

    elif codigo4 == 'THSP':
        codigo4 = THSP

    elif codigo4 == 'HSP':
        codigo4 = HSP

    elif codigo4 == 'ASM':
        codigo4 = ASM

    elif codigo4 == 'FQ2':
        codigo4 = FQ2

    elif codigo4 == 'FQ34':
        codigo4 = FQ34

    elif codigo4 == 'FQ46':
        codigo4 = FQ46

    elif codigo4 == 'FQ710':
        codigo4 = FQ710

    elif codigo4 == 'FQ10':
        codigo4 = FQ10
    else:
        print('Este código não existe, reinicie o programa!')
        sleep(5)
        sys.exit()

elif c3 == 'N':
    # soma todas os 1 números das listas
    somamin = codigo[0] + codigo2[0] + codigo3[0]
    # soma todas os 2 números das listas
    somamax = codigo[1] + codigo2[1] + codigo3[1]
    # soma todas os 3 números das listas
    somamulta = codigo[2] + codigo3[2] + codigo2[2]

    print('TEMPO MÍNIMO: {}'.format(somamin))
    print('TEMPO MÁXIMO: {}'.format(somamax))
    print('MULTA: {}'.format(somamulta))
    sleep(300)
    sys.exit()

c4 = input('Tem mais códigos? [S/N]').upper()
if c4 == 'S':
    codigo5 = input('Digite o outro código: ').upper()

    if codigo5 == 'UI':
        codigo5 = UI

    elif codigo5 == 'UJ':
        codigo5 = UJ

    elif codigo5 == 'UPM':
        codigo5 = UPM

    elif codigo5 == 'UPF':
        codigo5 = UPF

    elif codigo5 == 'TB':
        codigo5 = TB

    elif codigo5 == 'UM':
        codigo5 = UM

    elif codigo5 == 'PP':
        codigo5 = PP

    elif codigo5 == 'PGL':
        codigo5 = PGL

    elif codigo5 == 'PE':
        codigo5 = PE

    elif codigo5 == 'PSM':
        codigo5 = PSM

    elif codigo5 == 'PFA':
        codigo5 = PFA

    elif codigo5 == 'PLP':
        codigo5 = PLP

    elif codigo5 == 'RP':
        codigo5 = RP

    elif codigo5 == 'TF':
        codigo5 = TF

    elif codigo5 == 'OS':
        codigo5 = OS

    elif codigo5 == 'DPP':
        codigo5 = DPP

    elif codigo5 == 'DPP':
        codigo5 = DPP

    elif codigo5 == 'DF':
        codigo5 = DF

    elif codigo5 == 'F':
        codigo5 = F

    elif codigo5 == 'S':
        codigo5 = S

    elif codigo5 == 'A':
        codigo5 = A

    elif codigo5 == 'ASP':
        codigo5 = ASP

    elif codigo5 == 'AJ':
        codigo5 = AJ

    elif codigo5 == 'DS':
        codigo5 = DS

    elif codigo5 == 'D':
        codigo5 = D

    elif codigo5 == 'E':
        codigo5 = E

    elif codigo5 == 'FI':
        codigo5 = FI

    elif codigo5 == 'CL':
        codigo5 = CL

    elif codigo5 == 'CP':
        codigo5 = CP

    elif codigo5 == 'AP':
        codigo5 = AP

    elif codigo5 == 'PB':
        codigo5 = PB

    elif codigo5 == 'AG':
        codigo5 = AG

    elif codigo5 == 'RB':
        codigo5 = RB

    elif codigo5 == 'AC':
        codigo5 = AC

    elif codigo5 == 'DO':
        codigo5 = DO

    elif codigo5 == 'HC':
        codigo5 = HC

    elif codigo5 == 'HD':
        codigo5 = HD

    elif codigo5 == 'HD':
        codigo5 = HD

    elif codigo5 == 'TH':
        codigo5 = TH

    elif codigo5 == 'LT':
        codigo5 = LT

    elif codigo5 == 'GC':
        codigo5 = GC

    elif codigo5 == 'THSP':
        codigo5 = THSP

    elif codigo5 == 'HSP':
        codigo5 = HSP

    elif codigo5 == 'ASM':
        codigo5 = ASM

    elif codigo5 == 'FQ2':
        codigo5 = FQ2

    elif codigo5 == 'FQ34':
        codigo5 = FQ34

    elif codigo5 == 'FQ46':
        codigo5 = FQ46

    elif codigo5 == 'FQ710':
        codigo5 = FQ710

    elif codigo5 == 'FQ10':
        codigo5 = FQ10
    else:
        print('Este código não existe, reinicie o programa!')
        sleep(5)
        sys.exit()

elif c4 == 'N':
    somamin = codigo[0] + codigo2[0] + codigo3[0] + \
        codigo4[0]  # soma todas os 1 números das listas
    somamax = codigo[1] + codigo2[1] + codigo3[1] + \
        codigo4[1]  # soma todas os 2 números das listas
    somamulta = codigo[2] + codigo2[2] + codigo3[2] + \
        codigo4[2]  # soma todas os 3 números das listas

    print('TEMPO MÍNIMO: {}'.format(somamin))
    print('TEMPO MÁXIMO: {}'.format(somamax))
    print('MULTA: {} mil'.format(somamulta))
    sleep(300)
    sys.exit()

c5 = input('Tem mais códigos? [S/N]').upper()
if c5 == 'S':
    codigo6 = input('Digite o outro código: ').upper()

    if codigo6 == 'UI':
        codigo6 = UI

    elif codigo6 == 'UJ':
        codigo6 = UJ

    elif codigo6 == 'UPM':
        codigo6 = UPM

    elif codigo6 == 'UPF':
        codigo6 = UPF

    elif codigo6 == 'TB':
        codigo6 = TB

    elif codigo6 == 'UM':
        codigo6 = UM

    elif codigo6 == 'PP':
        codigo6 = PP

    elif codigo6 == 'PGL':
        codigo6 = PGL

    elif codigo6 == 'PE':
        codigo6 = PE

    elif codigo6 == 'PSM':
        codigo6 = PSM

    elif codigo6 == 'PFA':
        codigo6 = PFA

    elif codigo6 == 'PLP':
        codigo6 = PLP

    elif codigo6 == 'RP':
        codigo6 = RP

    elif codigo6 == 'TF':
        codigo6 = TF

    elif codigo6 == 'OS':
        codigo6 = OS

    elif codigo6 == 'DPP':
        codigo6 = DPP

    elif codigo6 == 'DPP':
        codigo6 = DPP

    elif codigo6 == 'DF':
        codigo6 = DF

    elif codigo6 == 'F':
        codigo6 = F

    elif codigo6 == 'S':
        codigo6 = S

    elif codigo6 == 'A':
        codigo6 = A

    elif codigo6 == 'ASP':
        codigo6 = ASP

    elif codigo6 == 'AJ':
        codigo6 = AJ

    elif codigo6 == 'DS':
        codigo6 = DS

    elif codigo6 == 'D':
        codigo6 = D

    elif codigo6 == 'E':
        codigo6 = E

    elif codigo6 == 'FI':
        codigo6 = FI

    elif codigo6 == 'CL':
        codigo6 = CL

    elif codigo6 == 'CP':
        codigo6 = CP

    elif codigo6 == 'AP':
        codigo6 = AP

    elif codigo6 == 'PB':
        codigo6 = PB

    elif codigo6 == 'AG':
        codigo6 = AG

    elif codigo6 == 'RB':
        codigo6 = RB

    elif codigo6 == 'AC':
        codigo6 = AC

    elif codigo6 == 'DO':
        codigo6 = DO

    elif codigo6 == 'HC':
        codigo6 = HC

    elif codigo6 == 'HD':
        codigo6 = HD

    elif codigo6 == 'HD':
        codigo6 = HD

    elif codigo6 == 'TH':
        codigo6 = TH

    elif codigo6 == 'LT':
        codigo6 = LT

    elif codigo6 == 'GC':
        codigo6 = GC

    elif codigo6 == 'THSP':
        codigo6 = THSP

    elif codigo6 == 'HSP':
        codigo6 = HSP

    elif codigo6 == 'ASM':
        codigo6 = ASM

    elif codigo6 == 'FQ2':
        codigo6 = FQ2

    elif codigo6 == 'FQ34':
        codigo6 = FQ34

    elif codigo6 == 'FQ46':
        codigo6 = FQ46

    elif codigo6 == 'FQ710':
        codigo6 = FQ710

    elif codigo6 == 'FQ10':
        codigo6 = FQ10
    else:
        print('Este código não existe, reinicie o programa!')
        sleep(5)
        sys.exit()

elif c5 == 'N':
    somamin = codigo[0] + codigo2[0] + codigo3[0] + codigo4[0] + \
        codigo5[0]  # soma todas os 1 números das listas
    somamax = codigo[1] + codigo2[1] + codigo3[1] + codigo4[1] + \
        codigo5[1]  # soma todas os 2 números das listas
    somamulta = codigo[2] + codigo2[2] + codigo3[2] + \
        codigo4[2] + codigo5[2]  # soma todas os 3 números das listas

    print('TEMPO MÍNIMO: {}'.format(somamin))
    print('TEMPO MÁXIMO: {}'.format(somamax))
    print('MULTA: {}'.format(somamulta))
    sleep(300)
    sys.exit()

c6 = input('Tem mais códigos? [S/N]').upper()
if c6 == 'S':
    codigo7 = input('Digite o outro código: ').upper()

    if codigo7 == 'UI':
        codigo7 = UI

    elif codigo7 == 'UJ':
        codigo7 = UJ

    elif codigo7 == 'UPM':
        codigo7 = UPM

    elif codigo7 == 'UPF':
        codigo7 = UPF

    elif codigo7 == 'TB':
        codigo7 = TB

    elif codigo7 == 'UM':
        codigo7 = UM

    elif codigo7 == 'PP':
        codigo7 = PP

    elif codigo7 == 'PGL':
        codigo7 = PGL

    elif codigo7 == 'PE':
        codigo7 = PE

    elif codigo7 == 'PSM':
        codigo7 = PSM

    elif codigo7 == 'PFA':
        codigo7 = PFA

    elif codigo7 == 'PLP':
        codigo7 = PLP

    elif codigo7 == 'RP':
        codigo7 = RP

    elif codigo7 == 'TF':
        codigo7 = TF

    elif codigo7 == 'OS':
        codigo7 = OS

    elif codigo7 == 'DPP':
        codigo7 = DPP

    elif codigo7 == 'DPP':
        codigo7 = DPP

    elif codigo7 == 'DF':
        codigo7 = DF

    elif codigo7 == 'F':
        codigo7 = F

    elif codigo7 == 'S':
        codigo7 = S

    elif codigo7 == 'A':
        codigo7 = A

    elif codigo7 == 'ASP':
        codigo7 = ASP

    elif codigo7 == 'AJ':
        codigo7 = AJ

    elif codigo7 == 'DS':
        codigo7 = DS

    elif codigo7 == 'D':
        codigo7 = D

    elif codigo7 == 'E':
        codigo7 = E

    elif codigo7 == 'FI':
        codigo7 = FI

    elif codigo7 == 'CL':
        codigo7 = CL

    elif codigo7 == 'CP':
        codigo7 = CP

    elif codigo7 == 'AP':
        codigo7 = AP

    elif codigo7 == 'PB':
        codigo7 = PB

    elif codigo7 == 'AG':
        codigo7 = AG

    elif codigo7 == 'RB':
        codigo7 = RB

    elif codigo7 == 'AC':
        codigo7 = AC

    elif codigo7 == 'DO':
        codigo7 = DO

    elif codigo7 == 'HC':
        codigo7 = HC

    elif codigo7 == 'HD':
        codigo7 = HD

    elif codigo7 == 'HD':
        codigo7 = HD

    elif codigo7 == 'TH':
        codigo7 = TH

    elif codigo7 == 'LT':
        codigo7 = LT

    elif codigo7 == 'GC':
        codigo7 = GC

    elif codigo7 == 'THSP':
        codigo7 = THSP

    elif codigo7 == 'HSP':
        codigo7 = HSP

    elif codigo7 == 'ASM':
        codigo7 = ASM

    elif codigo7 == 'FQ2':
        codigo7 = FQ2

    elif codigo7 == 'FQ34':
        codigo7 = FQ34

    elif codigo7 == 'FQ46':
        codigo7 = FQ46

    elif codigo7 == 'FQ710':
        codigo7 = FQ710

    elif codigo7 == 'FQ10':
        codigo7 = FQ10
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
    print('MULTA: {}'.format(somamulta))
    sleep(300)
    sys.exit()

c7 = input('Tem mais códigos? [S/N]').upper()
if c7 == 'S':
    codigo8 = input('Digite o outro código: ').upper()

    if codigo8 == 'UI':
        codigo8 = UI

    elif codigo8 == 'UJ':
        codigo8 = UJ

    elif codigo8 == 'UPM':
        codigo8 = UPM

    elif codigo8 == 'UPF':
        codigo8 = UPF

    elif codigo8 == 'TB':
        codigo8 = TB

    elif codigo8 == 'UM':
        codigo8 = UM

    elif codigo8 == 'PP':
        codigo8 = PP

    elif codigo8 == 'PGL':
        codigo8 = PGL

    elif codigo8 == 'PE':
        codigo8 = PE

    elif codigo8 == 'PSM':
        codigo8 = PSM

    elif codigo8 == 'PFA':
        codigo8 = PFA

    elif codigo8 == 'PLP':
        codigo8 = PLP

    elif codigo8 == 'RP':
        codigo8 = RP

    elif codigo8 == 'TF':
        codigo8 = TF

    elif codigo8 == 'OS':
        codigo8 = OS

    elif codigo8 == 'DPP':
        codigo8 = DPP

    elif codigo8 == 'DPP':
        codigo8 = DPP

    elif codigo8 == 'DF':
        codigo8 = DF

    elif codigo8 == 'F':
        codigo8 = F

    elif codigo8 == 'S':
        codigo8 = S

    elif codigo8 == 'A':
        codigo8 = A

    elif codigo8 == 'ASP':
        codigo8 = ASP

    elif codigo8 == 'AJ':
        codigo8 = AJ

    elif codigo8 == 'DS':
        codigo8 = DS

    elif codigo8 == 'D':
        codigo8 = D

    elif codigo8 == 'E':
        codigo8 = E

    elif codigo8 == 'FI':
        codigo8 = FI

    elif codigo8 == 'CL':
        codigo8 = CL

    elif codigo8 == 'CP':
        codigo8 = CP

    elif codigo8 == 'AP':
        codigo8 = AP

    elif codigo8 == 'PB':
        codigo8 = PB

    elif codigo8 == 'AG':
        codigo8 = AG

    elif codigo8 == 'RB':
        codigo8 = RB

    elif codigo8 == 'AC':
        codigo8 = AC

    elif codigo8 == 'DO':
        codigo8 = DO

    elif codigo8 == 'HC':
        codigo8 = HC

    elif codigo8 == 'HD':
        codigo8 = HD

    elif codigo8 == 'HD':
        codigo8 = HD

    elif codigo8 == 'TH':
        codigo8 = TH

    elif codigo8 == 'LT':
        codigo8 = LT

    elif codigo8 == 'GC':
        codigo8 = GC

    elif codigo8 == 'THSP':
        codigo8 = THSP

    elif codigo8 == 'HSP':
        codigo8 = HSP

    elif codigo8 == 'ASM':
        codigo8 = ASM

    elif codigo8 == 'FQ2':
        codigo8 = FQ2

    elif codigo8 == 'FQ34':
        codigo8 = FQ34

    elif codigo8 == 'FQ46':
        codigo8 = FQ46

    elif codigo8 == 'FQ710':
        codigo8 = FQ710

    elif codigo8 == 'FQ10':
        codigo8 = FQ10
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
    print('MULTA: {}'.format(somamulta))
    sleep(300)
    sys.exit()

c8 = input('Tem mais códigos? [S/N]').upper()
if c8 == 'S':
    codigo9 = input('Digite o seu último código: ').upper()

    if codigo9 == 'UI':
        codigo9 = UI

    elif codigo9 == 'UJ':
        codigo9 = UJ

    elif codigo9 == 'UPM':
        codigo9 = UPM

    elif codigo9 == 'UPF':
        codigo9 = UPF

    elif codigo9 == 'TB':
        codigo9 = TB

    elif codigo9 == 'UM':
        codigo9 = UM

    elif codigo9 == 'PP':
        codigo9 = PP

    elif codigo9 == 'PGL':
        codigo9 = PGL

    elif codigo9 == 'PE':
        codigo9 = PE

    elif codigo9 == 'PSM':
        codigo9 = PSM

    elif codigo9 == 'PFA':
        codigo9 = PFA

    elif codigo9 == 'PLP':
        codigo9 = PLP

    elif codigo9 == 'RP':
        codigo9 = RP

    elif codigo9 == 'TF':
        codigo9 = TF

    elif codigo9 == 'OS':
        codigo9 = OS

    elif codigo9 == 'DPP':
        codigo9 = DPP

    elif codigo9 == 'DPP':
        codigo9 = DPP

    elif codigo9 == 'DF':
        codigo9 = DF

    elif codigo9 == 'F':
        codigo9 = F

    elif codigo9 == 'S':
        codigo9 = S

    elif codigo9 == 'A':
        codigo9 = A

    elif codigo9 == 'ASP':
        codigo9 = ASP

    elif codigo9 == 'AJ':
        codigo9 = AJ

    elif codigo9 == 'DS':
        codigo9 = DS

    elif codigo9 == 'D':
        codigo9 = D

    elif codigo9 == 'E':
        codigo9 = E

    elif codigo9 == 'FI':
        codigo9 = FI

    elif codigo9 == 'CL':
        codigo9 = CL

    elif codigo9 == 'CP':
        codigo9 = CP

    elif codigo9 == 'AP':
        codigo9 = AP

    elif codigo9 == 'PB':
        codigo9 = PB

    elif codigo9 == 'AG':
        codigo9 = AG

    elif codigo9 == 'RB':
        codigo9 = RB

    elif codigo9 == 'AC':
        codigo9 = AC

    elif codigo9 == 'DO':
        codigo9 = DO

    elif codigo9 == 'HC':
        codigo9 = HC

    elif codigo9 == 'HD':
        codigo9 = HD

    elif codigo9 == 'HD':
        codigo9 = HD

    elif codigo9 == 'TH':
        codigo9 = TH

    elif codigo9 == 'LT':
        codigo9 = LT

    elif codigo9 == 'GC':
        codigo9 = GC

    elif codigo9 == 'THSP':
        codigo9 = THSP

    elif codigo9 == 'HSP':
        codigo9 = HSP

    elif codigo9 == 'ASM':
        codigo9 = ASM

    elif codigo9 == 'FQ2':
        codigo9 = FQ2

    elif codigo9 == 'FQ34':
        codigo9 = FQ34

    elif codigo9 == 'FQ46':
        codigo9 = FQ46

    elif codigo9 == 'FQ710':
        codigo9 = FQ710

    elif codigo9 == 'FQ10':
        codigo9 = FQ10
    else:
        print('Este código não existe, reinicie o programa!')
        sleep(5)
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
    print('MULTA: {}'.format(somamulta))
    sleep(300)
    sys.exit()
