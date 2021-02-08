$(document).ready(function () {
    $('.classSuper').click(function () {
        alert('Не тыкай!')
    })

    $("#name").blur(function () {
        $.get(
            'validate_login',
            {'login': $(this).val()},
            function (response){
                if (response.message === true) {
                    document.getElementById("msg").innerText='Sorry, user with this login exists'
                    document.getElementById("RegButton").disabled = true
                }
                else {
                    document.getElementById("msg").innerText='Please enter'
                    document.getElementById("RegButton").disabled = false
                }
            }
        )
    })

    $("#email").blur(function () {
        $.get(
            'validate_email',
            {'email':$(this).val()},
            function (response){
                if (response.email === true) {
                    document.getElementById("msg").innerText='Sorry, user with this email exists'
                    document.getElementById("RegButton").disabled = true
                }
                else {
                    document.getElementById("msg").innerText='Please enter'
                    document.getElementById("RegButton").disabled = false
                }
            }
        )
    })

})