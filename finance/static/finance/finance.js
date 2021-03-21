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
var displayRatio = 2;

var spendCircle;
var earnCircle;

var yearEarn;
var yearSpend;
var yearCash;
var yearStock;
var yearCrypto;

var monthEarn;
var monthSpend;
var monthCash;
var monthStock;
var monthCrypto;


var total_spend;
var total_earn;
var total_cash;

var yspendValue;
var yearnValue;
var ycashValue;
var ystockValue;
var ycryptoValue;

var monthId;

var canvas;


window.addEventListener('DOMContentLoaded', ()=>{
    setGlobalVariable();
    setMonthOverview();
    addTransaction();

    selectionEvent();

    addTransfer();
    //update stock value
    const ystock = document.getElementById("ystock");
    updateField(ystock, 'STOCK');

    const ycrypto = document.getElementById("ycrypto");
    updateField(ycrypto, 'CRYPTO')
    //delete transaction
    const transactions = document.querySelectorAll('.t-date');
    
    transactions.forEach(transaction =>{
        deleteTransactionEvent(transaction, "transaction");
    })
    

    //delete transfer
    const transfers = document.querySelectorAll('.transfer-date');
    transfers.forEach(transfer =>{
        deleteTransactionEvent(transfer, "transfer");
    })
})

function setGlobalVariable(){
    const data = document.getElementById("data-transfer");
    monthId = data.getAttribute("data-id");

    //set global variable
    spendCircle = document.getElementById("spendCircle");
    earnCircle = document.getElementById("earnCircle");
    //get month total earn, spend
    total_earn =  parseInt(earnCircle.getAttribute("data-value"))
    total_spend = parseInt(spendCircle.getAttribute("data-value"))

    //get month spend, earn, cash
    mSpendId = "mspend-" + monthId
    monthSpend = document.getElementById(mSpendId);

    mEarnId = "mearn-" + monthId
    monthEarn = document.getElementById(mEarnId)

    mCashId = "mcash-" + monthId
    monthCash = document.getElementById(mCashId)
    total_cash = parseInt(monthCash.getAttribute("data-value"))

    mStockId = "mstock-" +monthId;
    monthStock = document.getElementById(mStockId)
    
    mCryptoId = "mcrypto-" + monthId;
    monthCrypto = document.getElementById(mCryptoId)
    
    //get year and set year value
    yearSpend = document.getElementById("yspend")
    yspendValue = parseInt(yearSpend.getAttribute("data-value"))

    yearEarn = document.getElementById("yearn")
    yearnValue = parseInt(yearEarn.getAttribute("data-value"))

    yearCash = document.getElementById("ycash")
    ycashValue = parseInt(yearCash.getAttribute("data-value"))
    
    canvas = document.getElementById('canvas');

    yearStock = document.getElementById("ystock")
    ystockValue = parseInt(yearStock.getAttribute("data-value"));

    yearCrypto = document.getElementById("ycrypto")
    ycryptoValue = parseFloat(yearCrypto.getAttribute("data-value"));
}

function setMonthOverview(){
    
    //get a length of the square
    earn_a = (Math.sqrt(total_earn)) * 1.41
    spend_a = Math.sqrt(total_spend) * 1.41

    //normalize to suit the screen
    earn_a = parseInt(earn_a * displayRatio)
    spend_a = parseInt(spend_a * displayRatio)

    //minumm a
    if (earn_a <50){
        earn_a = 50;
    }
    if(spend_a < 50){
        spend_a = 50;
    }

    //update hight width of the circle
    earnCircle.style.width = earn_a + "px";
    earnCircle.style.height = earn_a + "px";

    spendCircle.style.width =  spend_a + "px";
    spendCircle.style.height = spend_a + "px";

    //update font size for text inside circle
    spendCircle.querySelector('.value').style.fontSize = parseInt(spend_a/6) + "px"
    earnCircle.querySelector('.value').style.fontSize = parseInt(earn_a/6) + "px"

    //set value inside
    earnCircle.querySelector(".value").innerText = total_earn
    spendCircle.querySelector(".value").innerText = total_spend
}

function addTransaction(){
    const addArea = document.getElementById("add_transaction");
    earnCircle.addEventListener('click', ()=>{
        addArea.classList.remove("hidden");
        addArea.querySelector('button').classList.remove("spendBtn")
        addArea.querySelector('button').classList.add("earnBtn")
        addArea.setAttribute("data-type", "plus");
    })
    spendCircle.addEventListener('click', ()=>{
        addArea.classList.remove("hidden");
        addArea.querySelector('button').classList.remove("earnBtn")
        addArea.querySelector('button').classList.add("spendBtn")
        addArea.setAttribute("data-type", "minus");
    })

    addArea.querySelector("button").addEventListener("click", ()=>{
        const value = addArea.querySelector("input").value;
        const action = addArea.getAttribute("data-type");
        
        
        if (value != "" && value.includes("-- ")){
            const url = '/finance/month/add_transaction';
            fetch(url, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                    'X-CSRFToken':csrftoken,
                },
                body:JSON.stringify({'value': value, 'action':action})
            })
        
            .then((response)=>{
                return response.text() 
            })
        
            .then((text)=>{
                
                if (text == "ERROR"){
                    alert("ERROR");
                }
                if(text != "ERROR"){
                    const values = value.split("-- ")
                    const amount =  parseInt(values[1])
                    if (action == "plus"){
                        total_earn += amount;
                        yearnValue += amount;
                        ycashValue += amount;
                        total_cash += amount;
                        
                    }
                    else{
                        total_spend += amount;
                        yspendValue += amount;
                        
                        ycashValue -= amount;
                        total_cash -= amount;
                    }   
                    addTransactionHandleBar(value, action, parseInt(text));
                    updateInfoValue();
                    setMonthOverview()
                }
               
            })
        }
    })
}


function addTransactionHandleBar(value, action, tId){
    
    var today = new Date();
    var dd = String(today.getDate());
    
    var values = value.split("-- ")
    const raw = document.getElementById("addTransactionHandlebar").innerHTML;
    let compliedTemplate = Handlebars.compile(raw);
    let ourGeneratedHtml = compliedTemplate({'tId': tId, 'date': dd, 'name': values[0], 'amount': values[1]});

    const node = document.createElement('div');
    const transactionId = "ts-" + tId;
    node.classList = "transaction"
    node.id = transactionId;
    node.innerHTML = ourGeneratedHtml;
    document.getElementById("transactions").appendChild(node);
    if (action == "plus"){
        node.querySelector('.amount').classList.add("plus")
        node.setAttribute('data-action', 'Plus')
    }
    else{
        node.querySelector('.amount').classList.add("minus")
        node.setAttribute('data-action', 'Minus')
    }

    const tEventId = "t-" + tId;
    const transaction = document.getElementById(tEventId)
    deleteTransactionEvent(transaction, "transaction");

}


function deleteTransactionEvent(transaction, type){
    
    transaction.addEventListener('dblclick', ()=>{
        var amount = parseInt(transaction.getAttribute("data-value"));
        amount = normalizeNumber(amount.toString())
        transactionId = transaction.getAttribute("data-id");
        const url = '/finance/month/delete_transaction';
        fetch(url, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken':csrftoken,
            },
            body:JSON.stringify({'transactionId': transactionId, 'type': type})
        })
    
        .then((response)=>{
            return response.text() 
        })
    
        .then((text)=>{
            if(text == "SUCCEED"){
                if(type == "transaction"){
                    //get transaction
                    tsId = "ts-" + transactionId 
                }
                else if(type =="transfer"){
                    tsId = "tf-"+ transactionId;
                }
                ts = document.getElementById(tsId);
                
                ts.style.animationPlayState = "running"
                ts.addEventListener('animationend', ()=>{
                    var action;
                    var tfrom;
                    var tto;

                    if(type =="transaction"){
                        action = ts.getAttribute("data-action")
                        if(action== "Plus"){
                            ycashValue -= amount;
                            total_cash -= amount;
                            
                            total_earn -= amount;
                            yearnValue -= amount;
                        }
                        else{
                            total_spend -= amount;
                            yspendValue -= amount;
    
                            ycashValue += amount;
                            total_cash += amount;
                            
                        }

                    }
                    else if(type == "transfer"){
                        tfrom = ts.getAttribute("data-tfrom");
                        tto = ts.getAttribute("data-tto");
                      
                        changeTransferAmount(tfrom, tto, amount, -1);
                    }
                   

                    ts.remove();
                    updateInfoValue();
                    setMonthOverview();
                })
            }
            
        })
    })
}



function updateField(object, type){
  
    const preValue = object.innerText;
    object.addEventListener('blur', ()=>{
        const value = object.innerText;
        if (value != preValue){
            //update on server for year stock and month stock
            const url = '/finance/month/update_stock';
            fetch(url, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                    'X-CSRFToken':csrftoken,
                },
                body:JSON.stringify({'value': value, 'type': type})
            })
        
            .then((response)=>{
                return response.text() 
            })
        
            .then((text)=>{
        
                if(text == "SUCCEED"){
                    if(type == "STOCK"){
                        //remove comma
                        const newValue = normalizeNumber(value)

                        object.innerText = setComma(newValue)

                        const mId = "mstock-" + monthId
                        document.getElementById(mId).innerText = setComma(newValue)
                    }
                    else{
                        const newValue = normalizeNumber(value)
                        object.innerText = setComma(newValue)

                        const mId = "mcrypto-" + monthId
                        document.getElementById(mId).innerText = setComma(newValue)
                    }
                    
                } 
                
            })
        }
    })
}

function addTransfer(){
    const transferToggle = document.getElementById("transfer-toggle");
    transferToggle.addEventListener('click', ()=>{
        //get transfer add box
        const transferBox = document.getElementById('transfer-add-box');

        //open
        transferBox.classList.remove('hidden');
        canvas.classList.remove('hidden');

        //close event
        const xBtn = transferBox.querySelector('.bar .quit-btn');
        xBtn.addEventListener('click', ()=>{
            transferBox.classList.add('hidden');
            canvas.classList.add('hidden');
        })

        //get property 
        const transferForm = transferBox.querySelector('form');
        transferForm.addEventListener('submit', event=>{
            event.preventDefault()
            //get from and to value
            const fromValue = document.getElementById("transfer-from-button").innerText.trim();
            const toValue = document.getElementById("transfer-to-button").innerText.trim();
            
            //get name and amount
            const nameValue = document.getElementById("transfer-name-input").value;
            const amountValue = document.getElementById("transfer-amount-input").value;
            
            //send value to server
            const url = '/finance/month/add_transfer';
            fetch(url, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                    'X-CSRFToken':csrftoken,
                },
                body:JSON.stringify({'fromValue': fromValue, 'toValue': toValue, 'nameValue': nameValue, 'amountValue': amountValue})
            })
        
            .then((response)=>{
                return response.text() 
            })
        
            .then((text)=>{
                
                if(text == "INTERNAL ERROR"){
                    alert(text)
                }
                else{
                    const amount = parseInt(amountValue)
                    changeTransferAmount(fromValue, toValue, amount, 1);
                    addTransferHandleBar(fromValue, toValue, nameValue, amountValue, parseInt(text));
                    updateInfoValue()
                }
                
            })

            
        })
    })
}


function addTransferHandleBar(fromValue, toValue, nameValue, amountValue, tId){
    var today = new Date();
    var dd = String(today.getDate());

    const raw = document.getElementById("addTransferHandleBar").innerHTML;
    let compliedTemplate = Handlebars.compile(raw);
    let ourGeneratedHtml = compliedTemplate({'tfrom': fromValue, 'tto': toValue, 'tId': tId, 'date': dd, 'name': nameValue, 'amount': setComma(amountValue)});

    const node = document.createElement('div');
    const transactionId = "tf-" + tId;
    node.classList = "month-transfer";
    node.id = transactionId;
    node.setAttribute("data-tfrom", fromValue);
    node.setAttribute("data-tto", toValue);
    node.innerHTML = ourGeneratedHtml;
    document.getElementById("transfers").appendChild(node);

    const eventId = "tfdate-" + tId;
    const transfer = document.getElementById(eventId)
    deleteTransactionEvent(transfer, "transfer")
}



function selectionEvent(){
    const selections = document.querySelectorAll('.selection-group');

    selections.forEach(selection =>{
        const mainDisplay = selection.querySelector('button');
        const aTags = selection.querySelectorAll('.dropdown-menu a');

        aTags.forEach(aTag =>{
            aTag.addEventListener('click', ()=>{
                const value = aTag.innerText;
                const mainValue = mainDisplay.innerText;
                mainDisplay.innerText = value;
                aTag.innerText = mainValue;
            })
        })
    })
}


function updateInfoValue(){
    yearEarn.innerText = setComma(yearnValue);
    yearCash.innerText = setComma(ycashValue);
    yearSpend.innerText =setComma(yspendValue);
    yearStock.innerText = setComma(ystockValue);
    yearCrypto.innerText = setComma(ycryptoValue);


    monthEarn.innerText = setComma(total_earn);
    monthCash.innerText = setComma(total_cash);
    monthSpend.innerText =setComma(total_spend);
    monthStock.innerText = setComma(ystockValue);
    monthCrypto.innerText = setComma(ycryptoValue);
}


function setComma(amount){
    return amount.toString().replace(/\B(?=(\d{3})+(?!\d))/g, ",");
}

function normalizeNumber(amount){
    return amount.replace(/,/g, '')
}


function changeTransferAmount(fromValue, toValue, amount, coe){
    if(fromValue == "Cash"){
        ycashValue -=  coe * amount;
        total_cash -= coe *amount;
    }
    else if(fromValue == "Stock"){
        ystockValue -=  coe * amount;
    }
    else if(fromValue == "Crypto"){
        ycryptoValue -= coe * amount;
    }

    if(toValue == "Cash"){
        ycashValue += coe * amount;
        total_cash += coe * amount;
    }
    else if(toValue == "Stock"){
        ystockValue += coe * amount;
        
    }
    else if(toValue == "Crypto"){
        ycryptoValue += coe * amount;
    }
}