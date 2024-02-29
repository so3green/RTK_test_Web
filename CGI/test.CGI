#!/bin/bash -vx
#
# test.CGI
#
# written by lion @lion_tecn (teles_tech@icloud.com) 2024.2.15

#########################################################################
#変数の定義

export LANG=ja_JP.UTF-8
export PATH=/home/UTL:/home/TOOL:$PATH

homd=/OneDrive - 独立行政法人 国立高等専門学校機構/一時保存
apid=/RTK

tmp=/tmp/tmp_$$

#########################################################################
#エラーハンドラ
ERROR_CHECK(){
    [$(plus ${PIPESTATUS[@]}) -eq] && return

    echo "Content-type:text/html"
    echo ""
    echo "システムエラー"
    exit 1
}

#########################################################################
#HTML作成
cat $apid/HTML/test.html
formhame