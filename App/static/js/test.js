function fn11(){
    return 7
}

function fn110(str) {
    splited = str.split(" ")
    console.log(splited[0],' and ',  splited[1])
}
// 15. Написать функцию принимающую список, добавить к этому списку новый элемент который будет равен сумме первого и
// последнего элемента этого списка. Получить последний элемент списка можно так: ls[-1]

function fn115(list){
    sum = list[0] + list[list.length - 1]
    list.push(sum)
    console.log(list)
}

//Написать функцию которая принимает словарь и число, удаляет ключ 'a' и добавляет ключ 'c' который должен содержать значение равное этому числу.

function fn118(dict, x) {
    console.log(dict)
    // var c = {'c': x}
    dict['c'] = x
    delete dict['a']
    console.log(dict)
}
// 1. Написать функцию которая принимает число через input и если оно меньше или равно 34 печатает ваше имя иначе имя вашей мамы.

function fn21() {
    a = Number(prompt('Введи число'))
    if (a <= 34) {
        console.log('Mom')
    }
}

// 2. Написать функцию которая принимает 2 числа  через input , и если их сумма равна 5 делит эту сумму
// на 2 и возвращает результат в противном случае возвращает их сумму.

function fn22() {
    a = Number(prompt('Введи a'))
    b = Number(prompt('Введи b'))
    c = a+b
    if (c === 5) {
        return c/2
    }
    else {
        return c
    }
}

// 3. Написать функцию принимающую строку  через input и если она меньше пяти символов напечатать её
// иначе напечатать сообщение 'строка сильно большая , я устал'.

function fn23() {
    str = prompt('Введи строку')
    if (str.length < 5) {
        console.log(str)
    }
    else {
        console.log('Я устал')
    }
}

// 8. Написать функцию принимающую имя. Если имена 'Вася' или 'Петя' то печатает привет братаны.
// Если она 'Толик' то напечатать 'Поделись на нолик'. Если имя не является 'Вася' или 'Петя' или 'Толик'  то функция печатает - ‘Я тебя не знаю’.

function fn28(name){
    if (( name === 'Вася') || (name === 'Петя')) {
        console.log('Hi, bro')
    }
    else if (name === 'Толик') {
        console.log('Podelis na nolik')
    }
    else {console.log('Bye!')}
}

// 4. Написать функцию, которая принимает список чисел и некоторое число и возвращает True если число есть в списке, иначе возвращает False. Нельзя пользоваться in.
function fn34(list,x){
    for (i in list.length()){
        if (list[i] === x) {
            console.log('True')
        }
        else { console.log('False')}
    }
}



$(document).ready(function () {
    $('.classSuper').click(function (e) {
        alert('Не тыкай!')
    })
})


$( document ).ready(function() {
  $( "#login" ).focus();
});