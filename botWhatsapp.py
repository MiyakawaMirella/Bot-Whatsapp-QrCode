import time

import pywhatkit
import pandas


def mensagem(df, caminho):
    pywhatkit.sendwhats_image(f'+{df.iloc[i, 1]}', f"{caminho}", f"Olá {df.iloc[i, 0]}, tudo bem? "
                                                                 f"Segue o QrCode de identificação, por favor "
                                                                 f"apresentar na entrada da escola Germinare no dia "
                                                                 f"do curso de Python! ", 9, True)
    print(caminho)
    print("Mensagem enviada!")


def sleep():
    time.sleep((60 * 30))


df_python = pandas.read_excel('testeTelefone.xlsx',
                              sheet_name='todos',
                              usecols=['Nome', 'Telefone'])

for i in range(len(df_python)):
    code = df_python.iloc[i, 0].replace(" ", "_")

    caminhoQrCode = "C:\\Users\\alunotemp\\OneDrive - Instituto Germinare\\Documentos\\GerminaTech's\\1_QR_codes\\" \
                    + code + ".png"

    if i in range(0, 40):
        mensagem(df_python, caminhoQrCode)

    if i == 41:
        sleep()

    if i in range(41, 81):
        mensagem(df_python, caminhoQrCode)

    if i == 81:
        sleep()
