$(document).ready(function () {
    $('.classSuper').click(function (e) {
        alert('Не тыкай!')
    })

    $("#name").blur(function () {
        $.post(
            'validate_login',
            {'login': $(this).val()},
            function (response){
                if (response.message === true) {
                    document.getElementById("msg").innerText='Sorry, user with this login exists'
                    document.getElementById("RegButton").disabled = true
                }
                else
                {
                    document.getElementById("msg").innerText='Please enter'
                    document.getElementById("RegButton").disabled = false
                }
            }

        )

    })

    $("#email").blur(function () {
        $.post(
            'validate_email',
            {'email':$(this).val()},
            function (response){
                if (response.email === true) {
                    document.getElementById("msg").innerText='Sorry, user with this email exists'
                    document.getElementById("RegButton").disabled = true
                }
                else
                {
                    document.getElementById("msg").innerText='Please enter'
                    document.getElementById("RegButton").disabled = false
                }
            }

        )

    })

    $('#eng').click(function (e) {
        $.post(
            'change_language_eng',
            {'lang': 'en'},
            function (response){}
        )
    })

})





// $(document).ready(function(){
//
// 		var validName = false;
// 		var validEmail = false;
//
// 		$("form").submit(function(event){
// 			event.preventDefault();
//
// 			var name = $("#name").val();
// 			var email = $("#email").val();
//
// 			if(name == "") {
// 				$("#name").parent().removeClass("has-success").addClass("has-error");
// 				$(".nameBlock").append("<span class='glyphicon glyphicon-remove form-control-feedback' aria-hidden='true'></span>");
// 				$(".nameBlock .glyphicon-ok").remove();
// 				validName = false;
// 			} else {
// 				$("#name").parent().removeClass("has-error").addClass("has-success");
// 				$(".nameBlock").append("<span class='glyphicon glyphicon-ok form-control-feedback' aria-hidden='true'></span>");
// 				$(".nameBlock .glyphicon-remove").remove();
// 				validName = true;
// 			}
//
// 			if(email == "") {
// 				$("#email").parent().removeClass("has-success").addClass("has-error");
// 				$(".emailBlock").append("<span class='glyphicon glyphicon-remove form-control-feedback' aria-hidden='true'></span>");
// 				$(".emailBlock .glyphicon-ok").remove();
// 				validEmail = false;
// 			} else {
// 				$("#email").parent().removeClass("has-error").addClass("has-success");
// 				$(".emailBlock").append("<span class='glyphicon glyphicon-ok form-control-feedback' aria-hidden='true'></span>");
// 				$(".emailBlock .glyphicon-remove").remove();
// 				validEmail = true;
// 			}
//
//
// 			if(validName == true && validEmail == true) {
// 				$("form").unbind('submit').submit();
// 			}
//
// 		});
//
// 	});