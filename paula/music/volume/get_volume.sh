mixer=$(amixer get Master | grep 'Mono:' | sed -e 's/^[^\[]*//' -e 's/^.//' -e 's/%.*$//')
echo $mixer
