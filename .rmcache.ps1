#
# the airticle link reference:
#
#   1. https://docs.microsoft.com/zh-cn/powershell/scripting/samples/working-with-files-and-folders?view=powershell-7.1
#   2. https://docs.microsoft.com/zh-cn/powershell/scripting/samples/working-with-registry-keys?view=powershell-7.1
#

### THE DELETE FILES
Get-ChildItem -Path . -include *.pyc -Recurse | Remove-Item

### THE DELETE DIRECTORY
## .tox/*
Remove-Item -Path .\.tox\* -Recurse
## ./build/*
Remove-Item -Path .\build\* -Recurse
## ./src/com.dvsnier.*.egg-info
Remove-Item -Path .\src\com.dvsnier.*.egg-info -Recurse
# Get-ChildItem -Path .\src\com.dvsnier.*.egg-info -Recurse
## ./dist/*
Remove-Item -Path .\dist\* -Recurse
## ./out/log/*
Remove-Item -Path .\out\log\* -Recurse
## __pycache__
Get-ChildItem -Path . -include __pycache__ -Recurse | Remove-Item
