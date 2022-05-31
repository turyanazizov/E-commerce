var updateBtns = document.getElementsByClassName('update-cart')

for (i = 0; i < updateBtns.length; i++) {
	updateBtns[i].addEventListener('click', function(){
		var shopId = this.dataset.shop
		var action = this.dataset.action
		console.log('shopId:', shopId, 'Action:', action)

		console.log('USER:', user)
		if (user == 'AnonymousUser'){
			console.log('User is not authenticated')
			
		}else{
			updateUserOrder(shopId,action)
		}
	})
}

function updateUserOrder(shopId, action){
	console.log('User is authenticated, sending data...')

		var url = '/shop/update_item/'

		fetch(url, {
			method:'POST',
			headers:{
				'Content-Type':'application/json',
				'X-CSRFToken':csrftoken,
			}, 
			body:JSON.stringify({'shopId':shopId, 'action':action})
		})
		.then((response) => {
		   return response.json();
		})
		.then((data) => {
			location.reload()
		});
}