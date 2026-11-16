#!/bin/bash
num=11 # bash는 띄어쓰기 안됨 파이썬처럼 num = 11로 하면 안됨

# bash 조건문
if [ $num -gt 10 ]; then
    echo "10보다 커"
else
    echo "10보다 작아"
fi # 필수

# bash 반복문
for i in {1..5} # 범위 지정은 중괄호 {} 중간 ..

do
    echo $i
done # 필수

say_hello() {
    echo "안녕 $1"
}
say_hello "jinchul"

score=90

if [ $score -ge 90 ]; then
    echo "A"
elif [ $score -ge 80 ]; then
    echo "B"
else
    echo "C"
fi

for j in {1..10}

do
    if [ $(($j % 2)) -eq 0 ]; then
        echo $j
    fi
done

plus_number() {
    echo $(($1 + $2))
}
plus_number 1 2