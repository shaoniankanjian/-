// 设置二级标题
function find(id){
	if (id.search("B1") != -1){
		question.innerHTML = '<a id="B1@" href="javascript:void(0);" onclick="clk2(this.id)">[题干]</a>\
		<a id="B1-1" href="javascript:void(0);" onclick="clk2(this.id)">[B1-1]</a>\
		<a id="B1-2" href="javascript:void(0);" onclick="clk2(this.id)">[B1-2]</a>\
		<a id="B1-3" href="javascript:void(0);" onclick="clk2(this.id)">[B1-3]</a>\
		<a id="B1-4" href="javascript:void(0);" onclick="clk2(this.id)">[B1-4]</a>\
		<a id="B1-5" href="javascript:void(0);" onclick="clk2(this.id)">[B1-5]</a>\
		<a id="B1-6" href="javascript:void(0);" onclick="clk2(this.id)">[B1-6]</a>\
		<a id="B1-7" href="javascript:void(0);" onclick="clk2(this.id)">[B1-7]</a>\
		<a id="B1-8" href="javascript:void(0);" onclick="clk2(this.id)">[B1-8]</a>\
		<a id="B1-9" href="javascript:void(0);" onclick="clk2(this.id)">[B1-9]</a>\
		<a id="B1-10" href="javascript:void(0);" onclick="clk2(this.id)">[B1-10]</a>\
		<a id="B1-11" href="javascript:void(0);" onclick="clk2(this.id)">[B1-11]</a>';
	}
	if (id.search("B2") != -1){
		question.innerHTML = '<a id="B2@" href="javascript:void(0);" onclick="clk2(this.id)">[题干]</a>\
		<a id="B2-1" href="javascript:void(0);" onclick="clk2(this.id)">[B2-1]</a>\
		<a id="B2-2" href="javascript:void(0);" onclick="clk2(this.id)">[B2-2]</a>\
		<a id="B2-3" href="javascript:void(0);" onclick="clk2(this.id)">[B2-3]</a>\
		<a id="B2-4" href="javascript:void(0);" onclick="clk2(this.id)">[B2-4]</a>\
		<a id="B2-5" href="javascript:void(0);" onclick="clk2(this.id)">[B2-5]</a>\
		<a id="B2-6" href="javascript:void(0);" onclick="clk2(this.id)">[B2-6]</a>';
	}
	if (id.search("B3a") != -1){
		question.innerHTML = '<a id="B3@" href="javascript:void(0);" onclick="clk2(this.id)">[题干]</a>\
		<a id="B3a-1" href="javascript:void(0);" onclick="clk2(this.id)">[B3-1]</a>\
		<a id="B3a-2" href="javascript:void(0);" onclick="clk2(this.id)">[B3-2]</a>\
		<a id="B3a-4" href="javascript:void(0);" onclick="clk2(this.id)">[B3-4]</a>\
		<a id="B3a-5" href="javascript:void(0);" onclick="clk2(this.id)">[B3-5]</a>\
		<a id="B3a-6" href="javascript:void(0);" onclick="clk2(this.id)">[B3-6]</a>\
		<a id="B3a-7" href="javascript:void(0);" onclick="clk2(this.id)">[B3-7]</a>\
		<a id="B3a-10" href="javascript:void(0);" onclick="clk2(this.id)">[B3-10]</a>';
	}
	if (id.search("B4") != -1){
		question.innerHTML = '<a id="B4@" href="javascript:void(0);" onclick="clk2(this.id)">[题干]</a>\
		<a id="B4-1" href="javascript:void(0);" onclick="clk2(this.id)">[B4-1]</a>\
		<a id="B4-2" href="javascript:void(0);" onclick="clk2(this.id)">[B4-2]</a>\
		<a id="B4-3" href="javascript:void(0);" onclick="clk2(this.id)">[B4-3]</a>\
		<a id="B4-4" href="javascript:void(0);" onclick="clk2(this.id)">[B4-4]</a>\
		<a id="B4-5" href="javascript:void(0);" onclick="clk2(this.id)">[B4-5]</a>';
	}
	if (id.search("B5") != -1){
		question.innerHTML = '<a id="B5@" href="javascript:void(0);" onclick="clk2(this.id)">[题干]</a>\
		<a id="B5-1" href="javascript:void(0);" onclick="clk2(this.id)">[B5-1]</a>\
		<a id="B5-2" href="javascript:void(0);" onclick="clk2(this.id)">[B5-2]</a>\
		<a id="B5-3" href="javascript:void(0);" onclick="clk2(this.id)">[B5-3]</a>\
		<a id="B5-4" href="javascript:void(0);" onclick="clk2(this.id)">[B5-4]</a>\
		<a id="B5-5" href="javascript:void(0);" onclick="clk2(this.id)">[B5-5]</a>\
		<a id="B5-6" href="javascript:void(0);" onclick="clk2(this.id)">[B5-6]</a>\
		<a id="B5-7" href="javascript:void(0);" onclick="clk2(this.id)">[B5-7]</a>\
		<a id="B5-8" href="javascript:void(0);" onclick="clk2(this.id)">[B5-8]</a>\
		<a id="B5-9" href="javascript:void(0);" onclick="clk2(this.id)">[B5-9]</a>\
		<a id="B5-10" href="javascript:void(0);" onclick="clk2(this.id)">[B5-10]</a>\
		<a id="B5-11" href="javascript:void(0);" onclick="clk2(this.id)">[B5-11]</a>\
		<a id="B5-12" href="javascript:void(0);" onclick="clk2(this.id)">[B5-12]</a>';
	}
	if (id.search("B6") != -1){
		question.innerHTML = '<a id="B6@" href="javascript:void(0);" onclick="clk2(this.id)">[题干]</a>\
		<a id="B6-1" href="javascript:void(0);" onclick="clk2(this.id)">[B6-1]</a>\
		<a id="B6-2" href="javascript:void(0);" onclick="clk2(this.id)">[B6-2]</a>\
		<a id="B6-3" href="javascript:void(0);" onclick="clk2(this.id)">[B6-3]</a>\
		<a id="B6-4" href="javascript:void(0);" onclick="clk2(this.id)">[B6-4]</a>';
	}
	if (id.search("D1") != -1){
		question.innerHTML = '<a id="D1@" href="javascript:void(0);" onclick="clk2(this.id)">[题干]</a>\
		<a id="D1-0" href="javascript:void(0);" onclick="clk2(this.id)">[D1-0]</a>\
		<a id="D1-1" href="javascript:void(0);" onclick="clk2(this.id)">[D1-1]</a>\
		<a id="D1-2" href="javascript:void(0);" onclick="clk2(this.id)">[D1-2]</a>\
		<a id="D1-3" href="javascript:void(0);" onclick="clk2(this.id)">[D1-3]</a>\
		<a id="D1-4" href="javascript:void(0);" onclick="clk2(this.id)">[D1-4]</a>\
		<a id="D1-5" href="javascript:void(0);" onclick="clk2(this.id)">[D1-5]</a>';
	}
	if (id.search("D2") != -1){
		question.innerHTML = '<a id="D2@" href="javascript:void(0);" onclick="clk2(this.id)">[题干]</a>\
		<a id="D2-0" href="javascript:void(0);" onclick="clk2(this.id)">[D2-0]</a>\
		<a id="D2-1" href="javascript:void(0);" onclick="clk2(this.id)">[D2-1]</a>\
		<a id="D2-2" href="javascript:void(0);" onclick="clk2(this.id)">[D2-2]</a>\
		<a id="D2-3" href="javascript:void(0);" onclick="clk2(this.id)">[D2-3]</a>\
		<a id="D2-4" href="javascript:void(0);" onclick="clk2(this.id)">[D2-4]</a>\
		<a id="D2-5" href="javascript:void(0);" onclick="clk2(this.id)">[D2-5]</a>';
	}
	if (id.search("D3") != -1){
		question.innerHTML = '<a id="D3@" href="javascript:void(0);" onclick="clk2(this.id)">[题干]</a>\
		<a id="D3-0" href="javascript:void(0);" onclick="clk2(this.id)">[D3-0]</a>\
		<a id="D3-1" href="javascript:void(0);" onclick="clk2(this.id)">[D3-1]</a>\
		<a id="D3-2" href="javascript:void(0);" onclick="clk2(this.id)">[D3-2]</a>\
		<a id="D3-3" href="javascript:void(0);" onclick="clk2(this.id)">[D3-3]</a>\
		<a id="D3-4" href="javascript:void(0);" onclick="clk2(this.id)">[D3-4]</a>\
		<a id="D3-5" href="javascript:void(0);" onclick="clk2(this.id)">[D3-5]</a>';
	}
	if (id.search("D4") != -1){
		question.innerHTML = '<a id="D4@" href="javascript:void(0);" onclick="clk2(this.id)">[题干]</a>\
		<a id="D4-0" href="javascript:void(0);" onclick="clk2(this.id)">[D4-0]</a>\
		<a id="D4-1" href="javascript:void(0);" onclick="clk2(this.id)">[D4-1]</a>\
		<a id="D4-2" href="javascript:void(0);" onclick="clk2(this.id)">[D4-2]</a>\
		<a id="D4-3" href="javascript:void(0);" onclick="clk2(this.id)">[D4-3]</a>\
		<a id="D4-4" href="javascript:void(0);" onclick="clk2(this.id)">[D4-4]</a>\
		<a id="D4-5" href="javascript:void(0);" onclick="clk2(this.id)">[D4-5]</a>';
	}
	
}