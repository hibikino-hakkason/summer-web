'use strict';
// 初期状態
let num_page = 1;
document.getElementById("home-yes-botton").style.display="none";
document.getElementById("home-no-botton").style.display="none";

// 最初の画面に戻った時の動作
if (document.getElementById("home-title").innerHTML === "夏休みにやるべきことは終わった？") {
    num_page = 1;
}

// 最初の画面で(診断スタート)ボタンが押された時の動作
document.getElementById("home-main-botton").onclick = function() {
    document.getElementById("home-title").innerHTML = "宿題は終わった？";
    document.getElementById("home-main-botton").style.display="none";
    document.getElementById("home-yes-botton").style.display="";
    document.getElementById("home-no-botton").style.display="";
};

// (Yes)ボタンが押された時の動作
document.getElementById("home-yes-botton").onclick = function() {
    num_page += 1;
    if (num_page === 2) {
        window.location.href = "recommend";
        
    };
};

// (No)ボタンが押された時の動作
document.getElementById("home-no-botton").onclick = function() {
    num_page += 1;
    if (num_page === 2) {
        window.location.href = "homework";
    };
}

// 宿題の提出日と内容が入力された後の動作
let homework_deadline = document.getElementById("homework-deadline");
let homework_content = document.getElementById("homework-content");