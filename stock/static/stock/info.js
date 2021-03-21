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
    updateTable()
})

function updateTable(){
    //update button
    const updateBtn = document.getElementById('updateTable');
    const cells = document.querySelectorAll('.cell');
        
    cells.forEach(cell =>{
        //get data
        const preValue = cell.innerText;
        cell.addEventListener('blur', ()=>{
            
            const value = cell.innerText
            if(value!=preValue){
                const id = cell.getAttribute("data-id")
                const type = cell.getAttribute("data-type")
                
                updateCell(id, type, value)
            }
            
            
            
        })
        
        
    })
    
}


function updateCell(id, type, value){
    var url = '/stock/update';

    fetch(url, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken':csrftoken,
        },
        body:JSON.stringify({'type': type, 'id': id, 'value': value})
    })

    .then((response)=>{
        return response.text() 
    })

    .then((text)=>{
        
    })
}

