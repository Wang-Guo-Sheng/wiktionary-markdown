#!/usr/bin/zsh
# Usage: wiktmd.sh [option] <word> <language> [output-directory]
Help(){
	echo "Usage: wiktmd.sh <word> <language> [output-directory]"
}
while getopts ":h" option; do
   case $option in
      h) # display Help
         Help
         exit;;
      *)
         echo "No such option"
   esac
done

BASEDIR=$(dirname "$0")
outdir=${3:-'.'}
outfile=${outdir}/${1}.md

(pandoc -f html  -t gfm-raw_html <(${BASEDIR}/wiktdl.py $1 $2)) > ${outfile}
sed -i 's/\\\[\[edit\]\(.*\)\\\]//g' ${outfile} # edit buttons
for ln in $(grep -En "File:.*\.(ogg|wav)" ${outfile} | cut -d: -f1); do
	# audio links
	ln0=$(expr ${ln} - 2)
	sed -i "${ln0},${ln}s/.*//" ${outfile}
done

sed -i 's/^\- \[IPA\].*/\- \IPA:/' ${outfile} # IPA instruction links
${BASEDIR}/multiline_brackets.py ${outfile}

# sed -i 's/\[\([^]]*\)\](Appendix:[^)]*)/\1/g' ${outfile}
sed -i 's/\[\([^]]*\)\](\/wiki\/Appendix:\([^)]*\))/\[\1\](https:\/\/en.wiktionary.org\/wiki\/Appendix:\2)/g' ${outfile}
sed -i 's/[(]\/wiki\//(/g' ${outfile} # convert wiktionary links to common links
${BASEDIR}/internal_links.py ${outfile}
${BASEDIR}/compact_etym.py ${outfile}

sed -i '/NewPP limit report/,$d' ${outfile}
sed -i 's/\^((\(.*\)))/\^(\1)\^/g' ${outfile}
sed -i '/^$/d' ${outfile}
sed -i 's/\([^^]\)\s\+/\1 /g' ${outfile}
sed -i 's/^\#/\n\#/' ${outfile}
sed -i 's/ //g' ${outfile}