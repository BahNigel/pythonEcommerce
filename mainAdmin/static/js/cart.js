
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














var count = 0
const sums = document.querySelectorAll('#element');
const num = document.getElementById('logs');

for (i = 0; i < sums.length; i++) {
    count += parseInt(sums[i].dataset.element)
}
num.innerHTML += count

var count2 = 0
const sums2 = document.querySelectorAll('#items');
const num2 = document.getElementById('sItems');

for (i = 0; i < sums2.length; i++) {
    count2 += parseInt(sums2[i].dataset.items)
}
num2.innerHTML += count2

//this is the increase items section

const value = document.querySelectorAll('#quantity')

for ( i = 0; i<value.length; i++){
    value[i].addEventListener("change", function change(){
         var Id = this.dataset.product
         var val = this.value
         val = this.value.toUpperCase();
         var qtyInSt = parseInt(this.dataset.quantity)
         console.log('user:',user)
         if(val > qtyInSt){
            alert("your value is too big")
         }else{
         var qty = this.value
         updateUserCart(Id, qty)
         location.reload()
         }
    });

}

function updateUserCart(productId, value){
        console.log('item is ready to be sen')

        var url = '/updateCart/'

        fetch(url, {
            method: 'POST',
            headers:{
                'Content-Type' : 'application/json',
                'X-CSRFToken': csrftoken,
            },
            body:JSON.stringify({'productId':productId, 'value':value})
        })
        .then((response) => {
            return response.json();
        })
        .then((data) => {
            console.log('Data:', data)
        });
  }

//end of increase items section





//this is the create order  section

//generating a random character

const characters ='ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789';

function generateString(length) {
    let result = ' ';
    const charactersLength = characters.length;
    for ( let i = 0; i < length; i++ ) {
        result += characters.charAt(Math.floor(Math.random() * charactersLength));
    }

    return result;
}

//end of random character generating


const totalPrice = document.getElementById('order')

    totalPrice.addEventListener("click", function total(){
         var Id = generateString(8)
         var total = count
         console.log('total:', total, 'character:', Id)
         addToOrderedItems(Id, total)
         window.location.replace('placeOrder/');
    });

function addToOrderedItems(productId, value){
        console.log('item is ready to be sen')

        var url = '/addToOrderedItems/'

        fetch(url, {
            method: 'POST',
            headers:{
                'Content-Type' : 'application/json',
                'X-CSRFToken': csrftoken,
            },
            body:JSON.stringify({'productId':productId, 'value':value})
        })
        .then((response) => {
            return response.json();
        })
        .then((data) => {
            console.log('Data:', data)
        });
  }

//end of create order section
