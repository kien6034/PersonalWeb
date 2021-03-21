function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
const csrftoken = getCookie('csrftoken');

window.addEventListener('DOMContentLoaded', ()=>{
    addTaskEvent();
    editTask();
})


function addTaskEvent(){
    const addBtn = document.getElementById("buttonAddTask");
    const inputField = document.getElementById("inputAddTask");

    const url = '/group/add/task';

    const taskHandleBar = "addTaskHandleBar"
    const table = "table"

    const groupID = document.querySelector('#data').getAttribute("data-id");

    addTask(addBtn, inputField, url, taskHandleBar, table, groupID);

    //check task event
    const checkBoxs= document.querySelectorAll('.checkboxTask');
    const updateUrl = '/group/update/task'
    
    checkTask(checkBoxs, updateUrl)
}


function addTask(addBtn, inputField, url, taskHandleBar, table, groupID){
   
    addBtn.addEventListener('click', ()=>{    
        //get value
        inputvalue = inputField.value;

        fetch(url, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken':csrftoken,
            },
            body:JSON.stringify({'value': inputvalue, 'groupID': groupID})
        })

        .then((response)=>{
            return response.text() 
        })

        .then((text)=>{
            console.log(text)
            addTaskHandleBar(text, taskHandleBar, table);
        })
    })
}

function addTaskHandleBar(text, taskHandleBar, table){
   
    const raw = document.getElementById(taskHandleBar).innerHTML;
    let compliedTemplate = Handlebars.compile(raw);

    let ourGeneratedHtml = compliedTemplate({'value': text});

    let dayTable = document.getElementById(table);
    const node = document.createElement('div');
    node.classList = "taskRow"
    
    node.innerHTML = ourGeneratedHtml;

    dayTable.appendChild(node);
}

function checkTask(checkBoxs, updateUrl){
    checkBoxs.forEach(cb =>{
        cb.addEventListener('change', ()=>{
            taskId = cb.getAttribute('data-id');
            isChecked = cb.checked;
            
            updateDayTask(updateUrl, taskId, isChecked);
        })
    })
}



function updateDayTask(updateUrl, taskId, isChecked){
    fetch(updateUrl, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken':csrftoken,
        },
        body:JSON.stringify({'id': taskId, 'isChecked': isChecked})
    })

    .then((response)=>{
        return response.text() 
    })

    .then((text)=>{
        
        if(text == "SUCCEED"){
            
        }
    })
}

function editTask(){
    //get the task row
    const tasks = document.querySelectorAll(".uf"); //unfinished
   
    tasks.forEach(task =>{
        //get id
        const taskId = task.getAttribute("data-id");
        
        //add event listen to changes
        const taskName = task.querySelector('.info .name');
        const taskWeight = task.querySelector('.weight');

        const preName = taskName.innerText;
        const preWeight = taskWeight.innerText;

        taskName.addEventListener('blur', ()=>{
            var name = taskName.innerText;
            if (name != preName){
                editTaskOnServer("name", name, taskId, taskName, taskWeight)
            }
        })
        
        taskWeight.addEventListener('click', ()=>{
            taskWeight.contentEditable = "true";
            taskWeight.addEventListener('blur', ()=>{
                const weight = taskWeight.innerText;
                if (weight != preWeight){
                    editTaskOnServer("weight", weight, taskId, taskName, taskWeight)
                }
            })
        })
        
        taskWeight.addEventListener('dblclick', ()=>{
            const weight = taskWeight.innerText;
            editTaskOnServer("weight", 0, taskId, taskName, taskWeight)
        })
    })
}


function editTaskOnServer(type, value, taskId, taskName, taskWeight){
    console.log(type)
    const url = '/group/edit/task'
    fetch(url, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken':csrftoken,
        },
        body:JSON.stringify({'type': type, 'value': value, 'taskId': taskId})
    })

    .then((response)=>{
        return response.text() 
    })

    .then((text)=>{
        if(text == "DELETE"){
            //find task
            deleteTaskUI(taskId)
        }
        
    })
}

function deleteTaskUI(taskId){
    const tId = "taskRow-" + taskId
    const task = document.getElementById(tId);
    task.style.animationPlayState = "running"
    task.addEventListener('animationend', ()=>{
        task.remove()
    })
}

function deleteTaskEvent(){

}