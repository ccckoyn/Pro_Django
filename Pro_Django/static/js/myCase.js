/**
 * Created by Administrator on 2019/5/9.
 */

//创建下拉选项
function cmdAddOption(cmb, obj) {
    let option;
    option = document.createElement("option");
    cmb.options.add(option);
    option.innerHTML = obj.name;
    option.value = obj.id;
}

//清理下拉选项
function clearOption(cmb){
    for(let i=0; i<= cmb.length+1; i++){
        cmb.options.remove(cmb[i]);
    }
}

//获取项目列表
var ProjectInit = function(_cmbProject){
    var cmbProject = document.getElementById(_cmbProject);

    function getProjectListInfo(){
        //获取某个项目的信息
        $.get("/ProManage/getProjectList/",{}, function(resp){
            if(resp.status == 10200){
                // console.log(resp.data);
                let dataList;
                dataList = resp.data;
                for (let i=0; i<dataList.length; i++){
                    cmdAddOption(cmbProject, dataList[i]);
                }
            $('#project_name').selectpicker('refresh');
            $('#project_name').selectpicker('show');
            }
            else{
                window.alert(resp.message)
            }
        })
    }

    //调用getProjectListInfo()
    getProjectListInfo();

};


//获取某一个项目的模块列表
var ModuleInit = function(_cmbProject,pid){
    var cmbModule = document.getElementById(_cmbProject);

    function getModuleListInfo(){
        //获取某个模块的信息
        $.post("/MolManage/getModuleList/",{"pid":pid}, function(resp){
            if(resp.status == 10200){
                // console.log(resp.data);
                let dataList;
                dataList = resp.data;
                clearOption(cmbModule);
                cmdAddOption(cmbModule,{"name":"选择模块","id":"0"});
                for (let i=0; i<dataList.length; i++){
                    cmdAddOption(cmbModule, dataList[i]);
                }
                $('#module_name').selectpicker('refresh');
                $('#module_name').selectpicker('show');
            }
            else{
                window.alert(resp.message)
            }
        })
    }

    //getModuleListInfo()
    getModuleListInfo();

};

