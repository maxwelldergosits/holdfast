for i in *.jpg; do
  out=${i%.jpg}.webp
  echo $out
  magick $i -define jpeg:extent=30kb -resize 150x $out
done
