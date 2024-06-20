# Automação para extração de arquivos .pdf ou outros
# GitHub: https://github.com/LeonardoHMS
# Linkedin: https://www.linkedin.com/in/leonardohms/

import json
import os
import shutil
from datetime import date, datetime
from time import sleep

number_weekday = date.today().weekday()

with open(r'settings\json\settings_search.json', 'r') as file:
    settings = json.load(file)

with open(r'settings\json\path_ignore.json', 'r') as file:
    skip_path = json.load(file)

with open(r'settings\json\path_search.json', 'r') as file:
    list_directory = json.load(file)

with open(r'settings\json\file_ignore.json', 'r') as file:
    skip_file = json.load(file)


def pdf_search():
    print("\033[31m ____  _____   ______\033[m        _____  ")  # Noqa E501
    print("\033[31m|  _ \\|  __ \\ |  ____|\033[m      / ____|                      ")  # Noqa E501
    print("\033[31m| |_) | |  | || |__\033[m        | (___    ___   __ _  _ __  ____  _    _")  # Noqa E501
    print("\033[31m|  __/| |  | ||  __|\033[m        \\ ___\\  / _ \\ / _` || '__|/  __\\| |__| |")  # Noqa E501
    print("\033[31m| |   | |__| || |\033[m           ____) ||  __/| (_| || |  |  \\___|  __  |")  # Noqa E501
    print("\033[31m|_|   |_____/ |_|\033[m          |_____/  \\___| \\__,_||_|   \\____/|_|  |_|  By:Leonardo Mantovani")  # Noqa E501
    print("")
    print('Buscando arquivos...')
    start = datetime.now()
    count = 0
    files_list = []
    path_list = []
    path_ignore = []
    file_ignore = []
    for path in list_directory:
        for source, diretories, files in os.walk(path):
            skip_path_bool = False
            for item in skip_path:
                if str(item).lower() in str(source).lower():
                    path_ignore.append(str(source).replace('/', '\\'))
                    skip_path_bool = True
                    break
            if skip_path_bool:
                continue
            for file in files:
                file_source = []
                if str(file)[-4:].lower() == settings.get('extension'):
                    skip_file_bool = False
                    for arg in skip_file:
                        if str(arg).lower() in str(file).lower():
                            file_source.append(str(file))
                            file_source.append(os.path.join(source, file))
                            file_ignore.append(file_source)
                            skip_file_bool = True
                            break
                    if skip_file_bool:
                        continue
                    try:
                        count += 1
                        full_path = os.path.join(source, file)
                        full_path = str(full_path).replace('/', '\\')
                        file_name, file_extension = os.path.splitext(file)
                        document_js = f"document.querySelector('#file{count}').textContent"  # Noqa E501
                        files_list.append(
                            f"""<button onclick="OpenPdf({document_js})">{file_name}</button>\n                  <button onclick="CopyText({document_js})"><img src="static/img/copy_icon.png" alt="Copiar"></button>""")  # Noqa E501
                        path_list.append(
                            f'<td align="left" id="file{count}"><a href="{full_path}" target="_blank">{full_path}</td>')  # Noqa E501
                    except Exception as e:
                        print('Erro na busca:', e)

    with open('pages/partials/head.html', 'r', encoding='utf-8') as head_page:
        now_base = datetime.now().strftime('%d/%m/%Y às %H:%M:%S')
        head = head_page.readlines()
        head_page.close()
        with open(f'{settings.get("local_save_html")}index.html', 'w+', encoding='utf-8') as index:  # Noqa E501
            try:
                index.writelines(head)
                for item in range(len(files_list)):
                    text_file_list = str(files_list[item])
                    text_path_list = str(path_list[item])
                    index.write('\n            <tr>\n')
                    index.write(f'               <td align="left">{item+1}</td>\n')  # Noqa E501
                    index.write('               <td align="left">\n')
                    index.write('                 <div class="buttons">\n')
                    index.write(f'                  {text_file_list}\n')
                    index.write('                 </div>\n')
                    index.write('               </td>\n')
                    index.write(f'               {text_path_list}\n')
                    index.write('            </tr>')
                index.write('\n         </tbody>\n')
                index.write('      </table>\n')
                index.write('   </div><!--tabela-->\n')
                index.write('   <div class="message update">\n')
                index.write(f'      <p>Ultima Atualização {now_base}</p>\n')
                index.write(f'      <p>{count} Arquivos listados no total.</p>\n')  # Noqa
                index.write('   </div>\n')
                index.write('   <script src="static/js/jquery.js"></script>\n')
                index.write('   <script src="static/js/script.js"></script>\n')
                index.write('</body>\n')
                index.write('</html>\n')
                index.close()
            except Exception as e:
                print('Erro:', e)
                input('Aperte qualquer tecla para sair...')
    try:
        shutil.copytree(
            'pages/static', f'{settings.get("local_save_html")}static')
    except FileExistsError:
        pass
    end = datetime.now()
    results = end - start
    print(f'{count} arquivo(s) encontrado(s) em {results.seconds} segundos')  # Noqa E501

    with open(f'{settings.get("local_save_html")}not search.txt', 'w', encoding="utf-8") as file:  # Noqa E501
        file.write(
            f"----- Ignored folders ----- ({len(path_ignore)} folders)\n")
        for index, path in enumerate(path_ignore):
            file.write(f'{index+1} - {path}\n')
        file.write('\n')
        file.write(f"----- Ignored files ----- ({len(file_ignore)} files)\n")
        for index, arq in enumerate(file_ignore):
            file.write(f'{index+1} - {arq[0]}  ####  ')
            file.write(f'{str(arq[1]).replace('/', '\\')}\n')


if number_weekday == 1 or number_weekday == 3 and settings.get('search_weekday'):  # Noqa E501
    pdf_search()

elif not settings.get('search_weekday'):
    pdf_search()

else:
    print('Not set to search current day, exiting...')

sleep(2)
