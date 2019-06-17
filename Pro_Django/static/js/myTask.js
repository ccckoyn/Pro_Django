/**
 * Created by Administrator on 2019/6/5.
 */

var caseTreeInit = function(){

    var zTreeObj;
	// zTree 的参数配置，深入使用请参考 API 文档（setting 配置详解）
	var setting = {
		check: {
			enable: true,
			chkStyle: 'checkbox'
		}
	};
	// zTree 的数据属性，深入使用请参考 API 文档（zTreeNode 节点数据详解）

	$(document).ready(function () {

	    $.get("/TaskManage/getCaseTree/",{},
	    function (resp) {
	        if (resp.status == 10200){
	            // window.alert("创建任务成功!");
	            var zNodes = resp.data;
	            zTreeObj = $.fn.zTree.init($("#treeDemo"), setting, zNodes);
		        zTreeObj.expandAll(false);  //通过设置true和false来控制是否展开
            }

        });

	});



}