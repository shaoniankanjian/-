var text = document.getElementById("content");
var question = document.getElementById("question");
var q_tittle = ["B1","B2","B3a","B4","B5","B6","D1","D2","D3","D4"];
var file_json = "展示数据.json";

$.getJSON(file_json, function(data){  //查找一级标题需要标红的
	    content = data;
		for(i in content){ //找到每个题号
			if (eval(content[i])[3] <= 0.4){  //判断阈值
				for(var j=0;j<q_tittle.length;j++){//在大题号中寻找
					if (i.search(q_tittle[j]) != -1){
						document.getElementById(q_tittle[j]).style.color = "red";
					}
				}
			}
		}
		
	})


function clk(id){
	document.getElementById("sim").innerText = 0; //清零
	find(id);
	set_name(id);
	// $.getJSON("1.json", function(data){
	//     content = data;
	// 	aw = content[id];
	// 	text.innerHTML = "<span>&emsp;&emsp;"+aw+"</span>";
	// // alert(content.hasOwnProperty('C1'));
	// })
	$.getJSON(file_json, function(data){
	    content = data;
		aw = eval(content[id]);
		text.innerHTML = "<span>&emsp;&emsp;"+aw[0]+"</span><span class='qwe'>"+aw[1]+"</span><span>"+aw[2]+"</span>";
		document.getElementById("sim").innerText = aw[3];
		for(i in content){
			if(i.search(id+"-") != -1){
				if(eval(content[i])[3] <= 0.4){
					document.getElementById(i).style.color = "red";
				}
			}
			if(i==id){
				if(eval(content[i])[3] <= 0.4){
					document.getElementById(i+"@").style.color = "red";
				}
			}
		}
		
	})
}

function clk2(id){
	if (id.search("@") != -1){
		id = id.replace("@","");
	}
	
	document.getElementById("sim").innerText = 0; //清零
	set_name(id);
	$.getJSON(file_json, function(data){
	    content = data;
		aw = eval(content[id]);
		text.innerHTML = "<span>&emsp;&emsp;"+aw[0]+"</span><span class='qwe'>"+aw[1]+"</span><span>"+aw[2]+"</span>";
		document.getElementById("sim").innerText = aw[3];
	})
}

// 显示题目函数
function set_name(num){
	document.getElementById("num1").innerText = num;
	$.getJSON("3.json", function(data){
	    content = data;
		document.getElementById("num2").innerText = content[num];
	})
}

