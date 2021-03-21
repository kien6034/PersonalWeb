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
    const globalData = document.getElementById("data-transfer");
    const selection = globalData.getAttribute("data-selection");
    
    if (selection == "watchlist"){
        wl = new WatchList()
        wl.addStock()
    }
   
})


class WatchList{
    constructor(){
        this.items = document.getElementById("wlItems");
        this.addBtn = document.getElementById("wlAddBtn");
        this.inputField = document.getElementById("wlInputField");

        this.stockWlHandleBar = document.getElementById("stockWatchListHandlebar")
        this.addUrl = "/stock/watchlist/add"
    }

    addStock(){
        this.addBtn.addEventListener('click', ()=>{
            const data = this.inputField.value;
            const wlId= this.items.getAttribute("data-id");
            if(data == ""){
                return;
            }

            fetch(this.addUrl, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                    'X-CSRFToken':csrftoken,
                },
                body:JSON.stringify({'data': data, 'wlId': wlId})
            })
        
            .then((response)=>{
                return response.text() 
            })
        
            .then((text)=>{
                alert(text)
            })

            this.addStockHandleBar()
        })
    }

    addStockHandleBar(){
        const raw = this.stockWlHandleBar.innerHTML;
        let compliedTemplate = Handlebars.compile(raw);
    
        let ourGeneratedHtml = compliedTemplate();
    
        const node = document.createElement('div');
        node.classList = "stock-data adding-row"
        
        node.innerHTML = ourGeneratedHtml;
    
        this.items.appendChild(node);
    }
}
