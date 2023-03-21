import speech_recognition as sr
import gtts
from playsound import playsound
from gtts import gTTS
import os
# Cria um reconhecedor de fala
r = sr.Recognizer()

# Usa o microfone como entrada de áudio
while True:
    with sr.Microphone() as source:
        print("Diga algo!")
        audio = r.listen(source)

    # Usa o reconhecimento de fala em português do Brasil para reconhecer a fala
    try:
        print("Você disse: " + r.recognize_google(audio, language='pt-BR'))
    except sr.UnknownValueError:
        print("Não foi possível entender o áudio")
    except sr.RequestError as e:
        print("Erro ao solicitar o reconhecimento de fala; {0}".format(e))   


    #Fazer o python falar

    # Teste de comando de voz procurando uma fala em específico, no caso, usamos "encontre"
    fala = r.recognize_google(audio, language='pt-BR')   # 'fala=' utiliza o reconhecimento de voz
    fala = fala.lower()                                  # fala.lower() transforma todas as letras em minúsculas, solucionando erros com a palavra "Encontre"
    comando = 'encontre' in fala
    if comando != False:
        playsound('frase.mp3') 

    '''with open ('teste1403.txt','r') as arquivo:
        for linha in arquivo:
            frase= gtts.gTTS(linha, lang= 'pt-br')
            frase.save('frase.mp3')'''

    with open ('arquivotexto_teste.txt', 'w') as arquivo:
        for escrita in fala:
            arquivo.write(str(escrita))

    
    # Ler o arquivo de texto
    with open('arquivotexto_teste.txt', 'r') as file:
        texto = file.read()

    # Configurar a linguagem e criar o objeto gTTS
    language = 'pt-br'
    objeto = gTTS(text=texto, lang=language, slow=False)

    # Salvar o arquivo de áudio
    objeto.save("audio.mp3")

    # Reproduzir o arquivo de áudio
    os.system("audio.mp3")

