

$(document).on('click',".btncart",function(e){
  var pid=$(this).closest('.cart_data').find('.pid').val();
  var qty=$(".qty").val();
  $.ajax({
    method:'POST',
    url:'/cart/',
    data:{
      "pid":pid,
      "qty":qty,
      'csrfmiddlewaretoken': $('[name="csrfmiddlewaretoken"]').val()
    },
    datatype:"json",
    success: function (response){

        $("#"+pid).hide();
        $("#add"+pid).show();
        $("#qty_ipnut"+pid).val(response.quantity)
        location.reload(true);


      alertify.warning(response.status)
    }
  })
})


$(document).on('click',".btnplus",function(e){
  var pid=$(this).closest('.cart_data').find('.pid').val();
  $.ajax({
    method:'POST',
    url:'/cartplus/',
    data:{
      "pid":pid,
      'csrfmiddlewaretoken': $('[name="csrfmiddlewaretoken"]').val()
    },
    datatype:"json",
    success: function (response){
      $("#qty_ipnut"+pid).val(response.quantity.quantity)
    }
})
})

$(document).on('click',".btnminus",function(e){
  var pid=$(this).closest('.cart_data').find('.pid').val();
  $.ajax({
    method:'POST',
    url:'/cartminus/',
    data:{
      "pid":pid,
      'csrfmiddlewaretoken': $('[name="csrfmiddlewaretoken"]').val()
    },
    datatype:"json",
    success: function (response){
      $("#qty_ipnut"+pid).val(response.quantity)
    }
})
})
