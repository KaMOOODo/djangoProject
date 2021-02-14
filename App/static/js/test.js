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