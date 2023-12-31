# git - система контроля версий - это система, записывающая изменения в файл или набор
# файлов  в течении времени

# Существует 3 вида систем контроля версий:
# Локальная 
# Централизованная 
# Распределительная

# 1. Локальная система представляет собой систему с простой базой данных, которая хранит записи о всех
# изменениях в файлах

# 2. Централизованная - система которая хранит все файлы в одной базе данных
#  Однако здесь есть большой минус. Если база данных слетит, то все не смогут войти в 
# эту базу данных, не смогут вносить изменения и делится ими.

# GIT - Распределенная система контоля версий записывающая изменения в файл или набор файлов 
# в течении времени и позволяющая вернуться позже к определенной версии.
# У git есть 3 основных состяния:
# Зафиксированная(commited) - Файл уже сохранен в локальной базе
# Измененное (modified) - Файлы, которые поменялись, но еще не были зафиксированны
# Подготовленное (stage) - Измененные файлы, отмеченные для включения в следующий коммит

# Репозиторий - место, где хранятся и поддерживаются какие либо данные 

'''
GIT - СИСТЕМА КОНТРОЛЯ ВЕРСИЙ
GITHUB - ONLINE SERVICE КОТОРЫЙ ПРЕДОСТОВЛЯЕТ УСЛУГИ ДЛЯ ХРАНЕНИЯ ВАШИХ ПРОЕКТОВ(РЕПОЗИТОРИЙ)
'''

# git init - project inisialisation(система контроля версий следит за проектом) после появляется .git

# git remote add origin url - добавляет удаленный репозиторий, который находится на каком то сервере

# git pull origin master(название ветки) - стягивние изменений с ветки

# git status - показывает статус

# git add - добавляет файлы в рабочей папке в индекс(индекс в git - специальная промедуточная 
# область в которой хранятся изменеия файлов от рабочей директории до удаленного репозитория)

# git add file_name file_name1- добавляет какой то файл

# git add . - добавляет все файлы

# git commit  - добавляет все файлы которые находятся в индексе (которые добавили с помощью команды git add)
# они локально созраняют ваш проект

# git commit -m 'названия комментария' комментарий для вашего сохранения

# git branch - показывает список веток

# git branch name_branch - (git branch erlan) - создает новую ветку

# git checkout name_branch - переключение веток

# git push name_branch - (get push origin master) отвечает за отправку кода в удаленныe репозиторий 

# git reset file_name - удаляет файл из индекса

# git rm (-r если папка) - cashed name перестает следить за ним

# git branch -D name - удаление ветки

# git merge - erlan(filr_name) - слияние веток

# git log - список коммитов

# БУДУТ ПРОБЛЕМЫ С ГИТОМ - ГУГЛИТЬ НАДО!!!

# git push --force origin

# get reset [commit/tag] - отменить все коммиты после указанного коммита (изменения будут сохранены локально)

# get reset --hard[commit] - принудительно вернуться к указанному коммиту

