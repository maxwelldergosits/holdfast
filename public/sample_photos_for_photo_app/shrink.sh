for i in *.jpg; do
  magick $i -define jpeg:extent=30kb -resize 150x 30kb_$i
done
