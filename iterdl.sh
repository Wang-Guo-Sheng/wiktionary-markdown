#!/usr/bin/zsh
for w in $(awk '{print $2}' $1);do
	./wiktdl.py $w $2 >> $(echo $1 | cut -d. -f1).html;
	echo $w Done
	echo ------
done