devops-netology  
Kononov  

##Игнорирование в папке terraform  
- &ast;&ast;/.terraform/&ast;  
*Любой файл находящийся в папке .terraform в любой из папок*  
- &ast;.tfstate  
*Любой файл или папка имя которого заканчивается на .tfstate рекурсивно из текущей папки*  
- &ast;.tfstate.&ast;  
*Любой файл или папка в имени которого содержится последовательность .tfstate. рекурсивно из текущей папки*  
- crash.log  
*Файлы или папки с именем crash.log рекурсивно из текущей папки*  
- &ast;.tfvars  
*Любой файл или папка имя которого заканчивается на .tfvars рекурсивно из текущей папки*  
- override.tf  
- override.tf.json  
*Файлы или папки с именами override.tf и override.tf.json рекурсивно из текущей папки*  
- &ast;_override.tf  
- &ast;_override.tf.json  
*Любые файлы или папки имена которых заканчиваются на _override.tf или _override.tf.json рекурсивно из текущей папки*  
- .terraformrc  
- terraform.rc  
*Файлы или папки с именами .terraformrc и terraform.rc рекурсивно из текущей папки*  
