#
# the airticle link reference:
#
#   1. https://docs.microsoft.com/zh-cn/powershell/scripting/samples/working-with-files-and-folders?view=powershell-7.1
#   2. https://docs.microsoft.com/zh-cn/powershell/scripting/samples/working-with-registry-keys?view=powershell-7.1
#
# the delete files
Get-ChildItem -Path . -include *.pyc -Recurse | Remove-Item
# the delete directory
Get-ChildItem -Path . -include __pycache__ -Recurse | Remove-Item
Remove-Item -Path .\build\* -Recurse
Remove-Item -Path .\out\log\* -Recurse
