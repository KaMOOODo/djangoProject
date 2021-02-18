
(function ($) {
    "use strict";


    /*==================================================================
    [ Validate ]*/
    var input = $('.validate-input .input100');

    $('.validate-form').on('submit',function(){
        var check = true;

        for(var i=0; i<input.length; i++) {
            if(validate(input[i]) == false){
                showValidate(input[i]);
                check=false;
            }
        }

        return check;
    });


    $('.validate-form .input100').each(function(){
        $(this).focus(function(){
           hideValidate(this);
        });
    });

    function validate (input) {
        if($(input).attr('type') == 'email' || $(input).attr('name') == 'email') {
            if($(input).val().trim().match(/^([a-zA-Z0-9_\-\.]+)@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.)|(([a-zA-Z0-9\-]+\.)+))([a-zA-Z]{1,5}|[0-9]{1,3})(\]?)$/) == null) {
                return false;
            }
        }
        else {
            if($(input).val().trim() == ''){
                return false;
            }
        }
    }

    function showValidate(input) {
        var thisAlert = $(input).parent();

        $(thisAlert).addClass('alert-validate');
    }

    function hideValidate(input) {
        var thisAlert = $(input).parent();

        $(thisAlert).removeClass('alert-validate');
    }
    
    

})(jQuery);

$(document).ready(function () {
    $("#name").blur(function () {
        $.get(
            'validate',
            {'login': $(this).val()},
            function (response){
                if (response.message === true) {
                    document.getElementById("msg").innerText='Извините, такой аккаунт существует'
                    document.getElementById("RegButton").disabled = true
                }
                else {
                    document.getElementById("msg").innerText='Заполните форму'
                    document.getElementById("RegButton").disabled = false
                }
            }
        )
    })

    $("#email").blur(function () {
        $.get(
            'validate',
            {'email':$(this).val()},
            function (response){
                if (response.email === true) {
                    document.getElementById("msg").innerText='Извините, аккаунт с таким email существует'
                    document.getElementById("RegButton").disabled = true
                }
                else {
                    document.getElementById("msg").innerText='Заполните форму'
                    document.getElementById("RegButton").disabled = false
                }
            }
        )
    })


})