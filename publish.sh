# activate pelican 
echo "activating pelican ..."
cd /home/jh/virtualenvs/pelican
. bin/activate
echo "... done"

# publish to output folder
echo "publishing to output folder ..."
cd /home/jh/src/Csound-Web
make publish
echo "... done"

# replace previous csound.github.io content
echo "copying to csound.github.io folder ..."
#rm -r ../csound.github.io
cp -r ./output/* ../csound.github.io
echo "... done"

# push to github
echo "pushing to github ..."
cd ../csound.github.io
git add --all
#echo "Please enter git commit message as a string:"
#read gitmess
git commit #$gitmess
git push
echo "... done"
