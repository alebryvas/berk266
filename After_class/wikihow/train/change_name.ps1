foreach ($file in gci) {
$newFileName=$file.name.replace("bk_bert","wikihow")
Rename-Item $file $newFileName
}