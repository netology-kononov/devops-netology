# devops-netology
# Kononov

# Игнорирование в папке terraform
# \*\*/.terraform/*
# Любой файл находящийся в папке .terraform в любой из папок
# *.tfstate
# Любой файл или папка имя которого заканчивается на .tfstate рекурсивно из текущей папки
# \*.tfstate.*
# Любой файл или папка в имени которого содержится последовательность .tfstate. рекурсивно из текущей папки
# crash.log
# Файлы или папки с именем crash.log рекурсивно из текущей папки
# *.tfvars
# Любой файл или папка имя которого заканчивается на .tfvars рекурсивно из текущей папки
# override.tf
# override.tf.json
# Файлы или папки с именами override.tf и override.tf.json рекурсивно из текущей папки
# *_override.tf
# *_override.tf.json
# Любые файлы или папки имена которых заканчиваются на _override.tf или _override.tf.json рекурсивно из текущей папки
# .terraformrc
# terraform.rc
# Файлы или папки с именами .terraformrc и terraform.rc рекурсивно из текущей папки

