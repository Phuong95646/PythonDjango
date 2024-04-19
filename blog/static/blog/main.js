function calculateSingleItemPrice() {
   var cartRows = document.getElementsByClassName("cart-item");
   var subTotal = 0;
 
   for (var i = 0; i < cartRows.length; i++) {
     var itemQuantity =
       parseInt(
         cartRows[i].getElementsByClassName("currentProductQuantity")[0].value
       ) || 0;
     var itemPrice =
       parseFloat(
         cartRows[i].getElementsByClassName("currentProductPrice")[0].value
       ) || 0;
 
     var totalPrice = itemQuantity * itemPrice;
     cartRows[i].getElementsByClassName("currentProductTotal")[0].value =
       totalPrice;
     subTotal += totalPrice;
     document.getElementById("total").value = subTotal;
   }
 }
 
//  window.onload(calculateSingleItemPrice());