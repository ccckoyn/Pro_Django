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

//选择模块
function selectedModule(mid){

        let module_options = document.querySelectorAll("#module_name > option");
        console.log(module_options.length)
        console.log(module_options)
        for(let n=0; n<module_options.length; n++){
            let m = module_options[n].value;
            if(m == mid){
                module_options[n].selected = true;
                let module_text = module_options[n].text
                document.querySelectorAll(".filter-option-inner-inner")[1].innerText= module_text;
            }
        }
}

//选择项目
function selectedProject(pid,cb){
        let project_options = document.querySelectorAll("#project_name > option");
        console.log(project_options.length)
        for(let i=0; i<project_options.length; i++){
            let v = project_options[i].value;
            if(v == pid){
                project_options[i].selected = true;
                let text = project_options[i].text
                document.querySelectorAll(".filter-option-inner-inner")[0].innerText= text;
                cb&&cb();
            }
        }
}

//获取项目列表
var ProjectInit = function(_cmbProject,cb){
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
            cb&&cb();
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
var ModuleInit = function(_cmbProject,pid,cb){
    var cmbModule = document.getElementById(_cmbProject);

    function getModuleListInfo(){
        //获取某个项目下模块的信息
        $.post("/MolManage/getModuleList/",{"pid":pid}, function(resp){
            if(resp.status == 10200){
                // console.log(resp.data);
                let dataList;
                dataList = resp.data;
                clearOption(cmbModule);
                // cmdAddOption(cmbModule,{"name":"选择模块","id":"0"});
                for (let i=0; i<dataList.length; i++){
                    cmdAddOption(cmbModule, dataList[i]);
                }
                $('#module_name').selectpicker('refresh');
                // $('#module_name').selectpicker('show');
                cb&&cb();
            }
            else{
                window.alert(resp.message)
            }
        })
    }

    //getModuleListInfo()
    getModuleListInfo();

};


//获取用例信息
var TestCaseInit = function(cb){

    var url = document.location;

    var cid = url.pathname.split("/")[3]

    $.post("/CaseManage/getCaseInfo/",
        {
            cid:cid,
        },
    function (resp,status) {

        //console.log("返回结果", resp.data);
        document.querySelector("#case_name").value = resp.data.name;
        document.querySelector("#AreaId").value = resp.data.method;
        document.querySelector("#req_url").value = resp.data.url;
        document.querySelector("#headers").value = resp.data.headers;
        //console.log("type",resp.data.parameter_type)
        //参数类型
        if (resp.data.parameter_type == "json"){
            document.querySelector("#json").setAttribute("checked","");
        }else{
            document.querySelector("#form").setAttribute("checked","");
        }

        document.querySelector("#parameter").value = resp.data.parameter_data;

        //console.log("assert_type",resp.data.assert_type)
        //断言类型
        if (resp.data.assert_type == "equal"){
            document.querySelector("#equal").setAttribute("checked","");
        }else{
            document.querySelector("#include").setAttribute("checked","");
        }

        document.querySelector("#assert_content").value = resp.data.assert_res;


        let project_options = document.querySelectorAll("#project_name > option");
        console.log(project_options.length)
        for(let i=0; i<project_options.length; i++){
            let v = project_options[i].value;
            if(v == resp.data.project_id){
                project_options[i].selected = true;
                let text = project_options[i].text
                document.querySelectorAll(".filter-option-inner-inner")[0].innerText= text;
            }
        }

        console.log("xxxxx",document.querySelector("#project_name").value)

        var project_id = document.querySelector("#project_name").value
        var module_id = resp.data.module_id
        cb&&cb(project_id,module_id);

        // console.log("fsdfd")
        //
        // ModuleInit("module_name",resp.data.project_id);
        //
        // console.log(document.querySelector("#module_name > option"))
        // //
        // // $('#module_name').selectpicker('refresh');
        // // $('#module_name').selectpicker('show');
        //
        // console.log("abcccc")
        //
        // let module_options = document.querySelectorAll("#module_name > option");
        // ModuleInit("module_name",resp.data.project_id);
        // //window.alert("xxxxxxxxxx")
        // console.log(module_options.length)
        // console.log(module_options)
        // for(let n=0; n<module_options.length; n++){
        //     let m = module_options[n].value;
        //     if(m == resp.data.module_id){
        //         module_options[n].selected = true;
        //         let module_text = module_options[n].text
        //         document.querySelectorAll(".filter-option-inner-inner")[1].innerText= module_text;
        //     }
        // }





        // document.querySelectorAll(".filter-option-inner-inner")[1].innerText= resp.data.module_id;


    })



}


