basename=$(echo $1|cut -d. -f1)
tmpname=${basename}.textmp.md
cp $1 ${tmpname}
sed -i 's/(([^)]*))//g' ${tmpname}
sed -i 's/\[\[\([^]]*\)\]\]/\1/g' ${tmpname}
pandoc ${tmpname} -o $basename.pdf --pdf-engine=xelatex --include-in-header <(echo \\usepackage{ebgaramond}) #&> /dev/null
rm ${tmpname}

