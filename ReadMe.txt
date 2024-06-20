PDF Search - Developed by Leonardo Mantovani
GitHub: https://github.com/LeonardoHMS
Linkedin: https://www.linkedin.com/in/leonardohms/

######### Português(BR) #########

Antes de iniciar o programa, primeiramente deve ser configurado os Arquivos Json:

settings\json\path_ignore.json
    - Adicione na lista, o nome das pastas que não deseja procurar os pdf
        - Exemplo: ["$Recycle.Bin", "$RECYCLE.BIN", "Não acessar"]
    - Caso deseja procurar todas as pastas, deixe a lista vazia -> []

settings\json\file_ignore.json
    - Adicione na lista, o nome do arquivo que não deseja procurar
        - Exemplo: ["boleto", "curriculo", "fim do mês"]
    - Caso deseja procurar todos os arquivos, deixe a lista vazia -> []

settings\json\path_search.json
    - Adicione na lista, os locais como, HD, SSD, que você deseja procurar os arquivos:
        - Exemplo: ["C:/", "E:/"]

settings\json\settings_search.json
    - "extension": Coloque o tipo de arquivo a ser procurado, por padrão precisa de 4 dígitos para funcionar
        - Exemplo: ".pdf"
    - "search_weekday": False - o programa irá funcionar todos os dias, True: O programa irá funcionar somente de Terça-feira e Quinta-feira,
    pois está definido como padrão
    - "local_save_html": Coloque o local que deseja salvar a lista html gerada
        - Exemplo: "extension": "C:/Users/username/Downloads/teste/" -> Sempre coloque a barra "/" no final


######### English #########

Before starting the program, the Json Files must first be configured:

settings\json\path_ignore.json
    - Add the name of the folders in which you do not want to search for PDFs to the list
        - Example: ["$Recycle.Bin", "$RECYCLE.BIN", "Do not access"]
    - If you want to search all folders, leave the list empty -> []

settings\json\file_ignore.json
    - Add the name of the file you do not want to search to the list
        - Example: ["money", "resume", "end of the month"]
    - If you want to search all files, leave the list empty -> []

settings\json\path_search.json
    - Add to the list the locations, such as HD, SSD, where you want to look for the files:
        - Example: ["C:/", "E:/"]

settings\json\settings_search.json
    - "extension": Enter the type of file to be searched for, by default it needs 4 digits to work
        - Example: ".pdf"
    - "search_weekday": False - The program will work every day, True: The program will only operate on Tuesday and Thursday, as it is set as default
    - "local_save_html": Enter the location where you want to save the generated html list
        - Example: "extension": "C:/Users/username/Downloads/teste/" -> Always put the slash "/" at the end