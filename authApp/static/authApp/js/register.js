//$(document).ready(function(){
//    $('#nxtBtn').click(function(){
//        if($('#emailInput').val()==''){
//           $('#emailInput').parent().append("<span style='color:red;font-size:smaller;'>Please Enter Your Email</span>");
//           return;
//        }
//        $('#emailInput').animate({left:"-900px"});
//        $('#nxtBtn').slideUp();
//        $('#emailInput').parent().parent().hide();
//        $('#nxtBtn').parent().parent().hide();
//        $('.scndStage').show('slow');
//        /*$('.fstStage tr').css('display','none');*/
//    });
//    $('#emailInput').focus(function(){
//        if($(this).parent().find('span').length==1){
//            $(this).parent().find('span').remove();
//        }
//    });
////});
//var pwd=document.getElementById('password'),cnfrm_pwd=document.getElementById('confirm_password');
//
//function validatePasswordRepeat(){
//    alert();
//    if(pwd.value != cnfrm_pwd.value){
//        cnfrm_pwd.setCustomValidity("Password do not match!");
//    }
//    else{
//        cnfrm_pwd.setCustomValidity("");
//    }
//}
//
//pwd.onchange = validatePasswordRepeat;
//cnfrm_pwd.onkeyup = validatePasswordRepeat;
