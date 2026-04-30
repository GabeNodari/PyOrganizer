# PyOrganizer: File Organizer 📁
Um script de automação simples e eficiente para manter sua pasta de Downloads organizada!

<hr>

## Funcionamento
O script varre a pasta de Downloads e move os arquivos para subpastas específicas
com base na extensão do arquivo. Se a pasta de destino não existir, o sistema operacional se
encarrega de gerenciar o fluxo (recomenda-se garantir que as pastas existam ou utilizar
os.makedirs).

As categorias atuais são:
- 📄 Documentos: .pdf, .docx, .txt
- 🖼️ Imagens: .jpg, .png, .jpeg
- ⚙️ Instaladores: .exe, .msi
- 📦 Compactados: .zip, .rar, .7z

## Requisitos

- Python 3.8 ou superior

## Executável e Automação
## 🪟 Windows: 
Para facilitar o uso e economizar recursos do sistema, este projeto pode ser convertido em um
executável (.exe) utilizando o PyInstaller e, posteriormente, agendado via Task Scheduler/Agendador de Tarefas.

#### Como gerar o executável:
1. Instale o PyInstaller: `python -m pip install pyinstaller`
2. Gere o arquivo: `pyinstaller --onefile --noconsole app.py`

O arquivo final estará na pasta dist. O uso da flag --noconsole permite que o script rode de
forma invisível, o que é ideal para integração no dia a dia.

## 🐧 Linux:
No Linux, a automação é feita de forma nativa utilizando o Cron.

#### Como configurar o agendamento (Cron):
1. Abra o terminal e acesse o editor de tarefas: `crontab -e`
2. Adicione uma linha ao final do arquivo para definir quando o script deve rodar.

Exemplo para rodar todo dia, de hora em hora:

`00 * * * * /usr/bin/python3 /caminho/completo/para/app.py`

