# Пользовательский мануал
Команда "Электрические жирафы" представляет проект *"Checkers"*!

## Запуск игры
Для запуска игры вам необходимо установить библиотеку *"Pygame"*, загрузить все файлы из репозитория (ветка main) и запустить приложение *main.py*.

## Правила игры
Первыми ходят чёрные. Для того, чтобы выбрать шашку, нажмите на неё кнопкой мыши, при этом синими кружочками подсвечиваются возможные ходы. Изначально каждой шашкой можно ходить только вперёд, однако при достижении шашкой противоположного края доски соотвествующая шашка становится *"королём"*, и может ходить назад. Побеждает тот, кто "съест" все шашки противника!

## Режимы игры
На выбор предлагается режим игры *"PvP"* (человек против человека) и *"Single Player"* - одиночная игра. Приятной игры!

# Для разработчиков
В папке graphics и sounds храняться соответственно картинки и звуки для игры. В файле main.py написан код основного цикла игры. В файлах board.py и main.py прописаны классы доски и шашек соответственно. В файле game.py прописана логика игры, в файле algorithm.py - искусственный интеллект. В файле menu.py прописано меню, в файле values.py хранятся основные константы.
Для обратной связи используйте issues. Будем рады любым предложениям!

