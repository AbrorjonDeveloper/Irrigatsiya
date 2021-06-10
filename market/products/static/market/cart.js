

var updateBtns = document.getElementsByClassName("update-details");
console.log(updateBtns);

for (let i=0; i<updateBtns.length; i++) {
    updateBtns[i].addEventListener('click', function (){
        console.log(this.dataset.product);
        product = this.dataset.product;
        action = this.dataset.action;
        console.log(product, action);
        if (user == 'AnonymousUser'){
            console.log("Ro'yhatdan o'tmagan foydalanuvchi.")
        }
else {
    update_order_details(product, action);
        }


    })
}
function update_order_details(product, action){
    console.log("Serverga jo'natiluvchi ma'lumot.")
    url = '/market/update_details/'
    fetch(url, {
        method:'POST',
        headers:{
            'Content-Type':'application/json',
            'X-CSRFToken':csrftoken,
        },
        body:JSON.stringify({'product':product, 'action':action})
    })
    .then((response)=>{
        return response.json()
    })
    .then((data)=>{
        location.reload()
    })
    console.log("data has been sent.")
}