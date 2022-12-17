#!/usr/bin/zsh
# Usage: wiktmd.sh <word> <language> [output-directory]
outdir=${3:-'.'}
outfile=${outdir}/${1}.md

(pandoc -f html  -t gfm-raw_html <(./wiktdl.py $1 $2)) > ${outfile}
sed -i 's/\\\[\[edit\]\(.*\)\\\]//g' ${outfile} # edit buttons
for ln in $(grep -En "File:.*\.ogg" ${outfile} | cut -d: -f1); do
	# audio links
	ln0=$(expr ${ln} - 2)
	sed -i "${ln0},${ln}s/.*//" ${outfile}
done

sed -i 's/^\- \[IPA\].*/\- \IPA:/' ${outfile} # IPA instruction links
./multiline_brackets.py ${outfile}

# sed -i 's/\[\([^]]*\)\](Appendix:[^)]*)/\1/g' ${outfile}
sed -i 's/\[\([^]]*\)\](\/wiki\/Appendix:\([^)]*\))/\[\1\](https:\/\/en.wiktionary.org\/wiki\/Appendix:\2)/g' ${outfile}
sed -i 's/[(]\/wiki\//(/g' ${outfile} # convert wiktionary links to common links
sed -i 's/\[\([^]]*\)\]([^h][^t][^t][^p][^)]*\("[^"]*"\)\?)/\[\[\1\]\]/g' ${outfile} # other internal links

sed -i '/NewPP limit report/,$d' ${outfile}
sed -i '/^$/d' ${outfile}