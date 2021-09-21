'use strict';

// 初期状態
document.getElementById("homework-table").style.display="none";
document.getElementById("homework-message").style.display="none";

let homeworks = [];
// 宿題の提出日と内容が入力された後の動作
document.getElementById("check-botton").onclick = function() {
    document.getElementById("homework-table").style.display="";
    document.getElementById("homework-message").style.display="";
    var homework_deadline = document.getElementById("homework-deadline");
    var homework_content = document.getElementById("homework-content");
    var table = document.getElementById("homework-table");

    // 配列に要素を追加
    homeworks.push({"homework_deadline": homework_deadline.value, "homework_content": 
    homework_content.value});

    // 配列をソート
    homeworks.sort(function(a,b){
        if(a.homework_deadline<b.homework_deadline) return -1;
        if(a.homework_deadline > b.homework_deadline) return 1;
        return 0;
    });

    // tableに要素を追加
    while(table.rows[ 1]) table.deleteRow( 1 );
    for (let i=0; i<homeworks.length; i++) {
        var new_row = table.insertRow();
        var new_cell = new_row.insertCell();
        var new_text = document.createTextNode(homeworks[i].homework_deadline);
        new_cell.appendChild(new_text);
        new_cell = new_row.insertCell();
        new_text = document.createTextNode(homeworks[i].homework_content);
        new_cell.appendChild(new_text);
    }

    // inputのvalueをリセット
    homework_deadline.value = "";
    homework_content.value = "";

};