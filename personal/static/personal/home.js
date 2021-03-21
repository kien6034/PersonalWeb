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

var wfWeight;
var wtWeight;

var wfWeightValue;
var wtWeightValue;

var dfWeight;
var dtWeight;

var dfWeightValue;
var dtWeightValue;

var audio;
window.addEventListener('DOMContentLoaded', ()=>{
    getGlobalValue();
    dayWeekDisplay();
    dayTaskEvent();
    weekTaskEvent();

    //remove task
    const tasks = document.querySelectorAll('.weight');
    tasks.forEach(task =>{
        removeTask(task);
    })
    

    const navEle = new Navbar()
})

function dayTaskEvent(){
  
    const form = document.getElementById("addDayTask");

    const url = '/add/Task';

    const taskHandleBar = "addTaskHandleBar"
    const table = "dayTable"

    const type = "day"
    addTask(form, url, taskHandleBar, table, type);

    //check task event
    const checkBoxs= document.querySelectorAll('.checkboxDayTask');
    
    
    checkBoxs.forEach(cb =>{
        checkTask(cb,  type)
    })
  
}

function weekTaskEvent(){
    const form = document.getElementById("addWeekTask");

    const url = '/add/Task';

    const taskHandleBar = "addTaskHandleBar"
    const table = "weekTable"

    const type = "week"
    addTask(form, url, taskHandleBar, table, type);

    //check task event
    const checkBoxs= document.querySelectorAll('.checkboxWeekTask');
    
    checkBoxs.forEach(cb =>{
        checkTask(cb, type)
    })
    
}


function addTask(form, url, taskHandleBar, table, type){
   
    form.addEventListener('submit', e=>{
        
        e.preventDefault();
        //get value
        const inputField = form.querySelector('input');
        inputvalue = inputField.value;

       

        fetch(url, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken':csrftoken,
            },
            body:JSON.stringify({'value': inputvalue, 'type': type})
        })

        .then((response)=>{
            return response.json() 
        })

        .then((data)=>{  
            
            inputField.value = "";
            addTaskHandleBar(data, taskHandleBar, table, type);

        })
    })
}
 
function addTaskHandleBar(data, taskHandleBar, table, type){
    const raw = document.getElementById(taskHandleBar).innerHTML;
    let compliedTemplate = Handlebars.compile(raw);

    let ourGeneratedHtml = compliedTemplate({'data': data});

    let dayTable = document.getElementById(table);
    const node = document.createElement('div');
    node.classList = "taskRow"
    node.innerHTML = ourGeneratedHtml;

    const wg = parseInt(data['weight']);
    if(wg > 9){
        node.querySelector('.weight').classList.add('criticalTask')
    }
    else if (wg > 4){
        node.querySelector('.weight').classList.add('mediumTask')
    }
    else{
        node.querySelector('.weight').classList.add('normalTask')
    }
    
    var taskId;
    //add event
    if(type == "day"){
        taskId = "dt-" + data["id"];
        dtWeightValue += wg;
    }
    else if (type ="week"){
        taskId = "wt-" + data["id"];
        wtWeightValue += wg;
    }
    node.id = taskId;

    const checkBoxEvent = node.querySelector('.left input');
    checkTask(checkBoxEvent, type)
    dayTable.appendChild(node);

    const removeEvent = node.querySelector('.weight');
    removeEvent.setAttribute('data-type', type);
    removeEvent.setAttribute('data-id', data["id"]);
    removeTask(removeEvent);

    //update total weight
    setGlobalValue()
    
}


function checkTask(cb, type){
    const updateUrl = '/update/Task'
    cb.addEventListener('change', ()=>{
    
        taskId = cb.getAttribute('data-id');
        isChecked = cb.checked;
        
        if(isChecked){
            playAudio()
        }
        
        updateDayTask(updateUrl, taskId, isChecked, type); 
        swapCheckPosition(cb, type, isChecked);
    })
}

function updateDayTask(updateUrl, taskId, isChecked, type){
    fetch(updateUrl, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken':csrftoken,
        },
        body:JSON.stringify({'id': taskId, 'isChecked': isChecked, 'type': type})
    })

    .then((response)=>{
        return response.text() 
    })

    .then((text)=>{
      
    })
}

function removeTask(t){
  
    t.addEventListener('dblclick', ()=>{
        const tType = t.getAttribute("data-type");
        const tId = t.getAttribute("data-id");
        
        const url = '/utils/task/delete';
        fetch(url, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken':csrftoken,
            },
            body:JSON.stringify({'type': tType, 'id': tId})
        })
    
        .then((response)=>{
            return response.text() 
        })
    
        .then((text)=>{
            
            if(text == "SUCCEED"){
                
                if(tType=="day"){
                    taskId = "dt-" + tId;
                }
                else{
                    taskId = "wt-" + tId;
                }
                //get transaction
                
                task = document.getElementById(taskId);
                task.style.animationPlayState = "running"
                task.addEventListener('animationend', ()=>{
                    task.remove();
                    
                    //get weight
                    const weight = parseInt(t.innerText);
                   
                    if( tType == "day"){
                        dtWeightValue -= weight;
                    }
                    else if(tType == "week"){
                        wtWeightValue -= weight;
                    }
                    setGlobalValue();
                })
            }
            
        })

    })
   
}


function swapCheckPosition(cb, type, isChecked){
    //get id 
    const eid = cb.getAttribute("data-id");
    var destination;
    if(type =="day"){

        taskId = "dt-" + eid;
        const task = document.getElementById(taskId);
        const weight = task.querySelector('.weight');
        const weightValue = parseInt(weight.innerText);
        if(isChecked){
            destination = document.getElementById("dayCompletedTable");
            //get the task
            task.classList.add("finishedTask")
            weight.classList.add("hideweight")
            destination.appendChild(task);
            
            dfWeightValue += weightValue;
            
        }
        else{
            destination = document.getElementById("dayTable");
            task.classList.remove("finishedTask");
            weight.classList.remove("hideweight");
            destination.appendChild(task);

            dfWeightValue -= weightValue;
        }
    }
    else if(type == "week"){
        //TODO
        taskId = "wt-" + eid;
        const task = document.getElementById(taskId);
        const weight = task.querySelector('.weight');
        const weightValue = parseInt(weight.innerText);
        if(isChecked){
            destination = document.getElementById("weekCompletedTable");
            //get the task
            task.classList.add("finishedTask")
            weight.classList.add("hideweight")
            destination.appendChild(task);

            wfWeightValue += weightValue;
        }
        else{
            destination = document.getElementById("weekTable");
            task.classList.remove("finishedTask");
            weight.classList.remove("hideweight");
            destination.appendChild(task);

            wfWeightValue -= weightValue;
        }
    }
    setGlobalValue()

}



function getGlobalValue(){
    audio = document.getElementById("audio")
    wfWeight = document.getElementById("week_finished_weight").querySelector(".text");
    wtWeight = document.getElementById("week_total_weight").querySelector(".text");

    wfWeightValue = parseInt(wfWeight.innerText);
    wtWeightValue = parseInt(wtWeight.innerText);

    dfWeight  = document.getElementById("day_finished_weight").querySelector(".text");
    dtWeight =  document.getElementById("day_total_weight").querySelector(".text");

    dfWeightValue = parseInt(dfWeight.innerText);
    dtWeightValue = parseInt(dtWeight.innerText);
    
}

function setGlobalValue(){
    wfWeight.innerText = wfWeightValue;
    wtWeight.innerText = wtWeightValue;

    dfWeight.innerText = dfWeightValue;
    dtWeight.innerText = dtWeightValue;
}


function dayWeekDisplay(){
    const dayWeeks = document.querySelectorAll(".dw");
    dayWeeks.forEach(day =>{
        ///get value 
        var value = day.innerText;
        value = value.slice(0,3);

        day.innerText = value;
    })
}


function playAudio(){
    
    
    audio.play()
}


class Navbar{
    constructor(){
        this.groupTaskInput = document.getElementById('group-task-input');
        this.addGroupTaskToggle = document.getElementById("add-group-task-icon");
        this.openAddGroupTask(this.addGroupTaskToggle);
        this.addGroupTaskFormEvent(this.groupTaskInput);
    }

    openAddGroupTask(toggle){
        toggle.addEventListener('click', ()=>{
            this.groupTaskInput.classList.toggle("hidden");
        })
    }

    addGroupTaskFormEvent(groupTaskInput){
        const form = groupTaskInput.querySelector('form');
        form.addEventListener('submit', e=>{
            e.preventDefault();
            
            //get data
            const input =  form.querySelector('input');
            const data = input.value;
            
            if(data != ""){
                const url = "group/addGroupTask"
                //update on server
                fetch(url, {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json',
                        'X-CSRFToken':csrftoken,
                    },
                    body:JSON.stringify({'data': data})
                })
        
                .then((response)=>{
                    return response.text() 
                })
        
                .then((text)=>{      
                    if(text != "ERROR"){
                        input.value = "";

                        //add new group task
                        const raw = document.getElementById("addGroupTaskHandleBar").innerHTML;
                        let compliedTemplate = Handlebars.compile(raw);
                        let ourGeneratedHtml = compliedTemplate({'name': data});

                        let groupTasks = document.getElementById("groupTasks");
                        const node = document.createElement('a');
                        node.href = 'task/' + parseInt(text)
                        node.target = "_blank";
                        node.classList = "group"
                        node.innerHTML = ourGeneratedHtml;

                        groupTasks.appendChild(node);

                    }
                })

            }
        })
    }
}