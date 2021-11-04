**1. Найдите полный хеш и комментарий коммита, хеш которого начинается на aefea.**
> git show aefea  

commit aefead2207ef7e2aa5dc81a34aedf0cad4c32545 <- *Полный хеш*  
Update CHANGELOG.md <- *Комментарий*

**2. Какому тегу соответствует коммит 85024d3.**
> git show 85024d3  
 
commit 85024d3100126de36331c6982bfaac02cdab9e76 (tag: v0.12.23) <- *Тег v0.12.23*

**3. Сколько родителей у коммита b8d720? Напишите их хеши.**
> git log --oneline --all --graph | grep b8d720 -A 4  

| * | | | | | | | | | | |   b8d720f83 Merge pull request #23916 from hashicorp/cgriggs01-stable  
| |\ \ \ \ \ \ \ \ \ \ \ \  
| | * | | | | | | | | | | | 9ea88f22f add/update community provider listings  
| |/ / / / / / / / / / / /  
| * | | | | | | | | | | |   56cd7859e Merge pull request #23857 from hashicorp/cgriggs01-stable  
*В графическом представлении видно, что у коммита 2 предка c хешами 9ea88f22f и 56cd7859e*  

*Можно получить эту же информацию из полного журнала*
> git log | grep b8d720 -A 2  

commit b8d720f8340221f2146e4e4870bf2ee0bc48f2d5  
Merge: 56cd7859e 9ea88f22f <- *Искомые хэши предков*

*Можно также методом перебора найти предков командами*
> git show b8d720^  
> git show b8d720^2

**4. Перечислите хеши и комментарии всех коммитов которые были сделаны между тегами v0.12.23 и v0.12.24.**
> git log --oneline v0.12.24 --not v0.12.23  
 
33ff1c03b (tag: v0.12.24) v0.12.24  
b14b74c49 [Website] vmc provider links  
3f235065b Update CHANGELOG.md  
6ae64e247 registry: Fix panic when server is unreachable  
5c619ca1b website: Remove links to the getting started guide's old location  
06275647e Update CHANGELOG.md  
d5f9411f5 command: Fix bug when using terraform login on Windows  
4b6d06cc5 Update CHANGELOG.md  
dd01a3507 Update CHANGELOG.md  
225466bc3 Cleanup after v0.12.23 release

**5. Найдите коммит в котором была создана функция func providerSource, ее определение в коде выглядит так func providerSource(...) (вместо троеточего перечислены аргументы).**
> git log -S'func providerSource(' --oneline  
 
8c928e835 main: Consult local directories as potential mirrors of providers

**6. Найдите все коммиты в которых была изменена функция globalPluginDirs.**
> git log -S'func globalPluginDirs(' --oneline  

8364383c3 Push plugin discovery down into command package <- *Определяет коммит, когда функция была создана*
> git show 8364383c3  
 
+++ b/plugins.go <- *Показывает, в каком файле эта функция используется*  
+func globalPluginDirs() []string {
> git log -L :globalPluginDirs:plugins.go --no-patch  
 
*Даёт список коммитов, в которых функция была изменена:*  
commit 78b12205587fe839f10d946ea3fdc06719decb05  
commit 52dbf94834cb970b510f2fba853a5b49ad9b1a46  
commit 41ab0aef7a0fe030e84018973a64135b11abcd70  
commit 66ebff90cdfaa6938f26f908c7ebad8d547fea17  
commit 8364383c359a6b738a436d1b7745ccdce178df47  

**7. Кто автор функции synchronizedWriters.**
> git log -S'func synchronizedWriters(' --oneline  
 
*Показывает в каких коммитах функция была создана или удалена:*  
bdfea50cc remove unused  
5ac311e2a main: synchronize writes to VT100-faker on Windows  
> git show 5ac311e2a  

commit 5ac311e2a91e381e2f52234668b49ba670aa0fe5  
Author: Martin Atkins <mart@degeneration.co.uk> <- *Автор*  
+func synchronizedWriters(targets ...io.Writer) []io.Writer { <- *Функция создана*

