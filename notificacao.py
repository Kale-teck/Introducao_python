from winotify import Notification

#ANTES DE RODAR O PROGRAMA É NECESSÁRIO INSTALAR A LIB NO PC
# É muito simples: biblioteca winotify
# link no pypi: https://pypi.org/project/winotify/

notificacao = Notification(app_id="Programador Kalebe",
                     title="Teste de notificação com Python",
                     msg="Ainda há esperança !",
                     icon=r"c:\Users\kaleb\Pictures\eu.jpeg")

notificacao.show()

