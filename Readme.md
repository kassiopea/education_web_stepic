# Практика на курсе Web-технологии
  от [stepik и mail.ru Group](https://stepik.org/course/154/syllabus)

## описание
Сайт - базовый шаблон-прототип stack overflow с реализованной авторизацией, добавлением нового вопроса, ответов, карточки вопроса с ответами на него, выборкой по 10 новым и 10 популярным записям.

[Tехническое задание](https://stepik.org/lesson/14827/step/10?unit=4176). В курсе практических заданий отсутствует блок с реализацией лайков. В связи с этим, в проекте эта реализация тоже отсутствует.

### технологии
  - python 3
  - django 2
  - nginx
  - gunicorn

  -----------
#### Дополнение к рабочим файлам
В init.sh лежат скрипты для запуска на виртуальной машине stepik. Конфигурационные файлы в папке etc (без пометки "real") относятся только к виртуальному окружению для stepik (в том числе прописанные пути).

Для запуска реального проекта в конфигурационных файлах (содержащих в названии "real") в папке etc необходимо изменить пути до рабочих директорий, там, где это необходимо.

В файле init_real.sh прописаны команды в терминале для разворачивания проекта на локальной машине.

-------------

На локальной машине nginx и gunicorn настраивались по другим путям и с дополнениями.
Запускалось виртуальное окружение, все зависимости лежат в файле "requierments.txt" (на виртуальной машине при обучении использовались более старые версии)


Приложение немного доработано. Добавлены:
- Стили (оформление css всех страниц)
- Реализация метода logout
- Реализация меню (навигация по сайту)
