var intToRoman = function(num) {
    let tabela = [[1000, 'M'], [900, 'CM'], [500, 'D'], [400, 'CD'], [100, 'C'], [90, 'XC'], [50, 'L'], [40, 'XL'], [10, 'X'], [9, 'IX'], [5, 'V'], [4, 'IV'], [1, 'I']]
    let numero = []
    for (let i = 0; i < tabela.length; i++) {
        quociente = Math.floor(num / tabela[i][0])
        resto = num % tabela[i][0]
        num = resto
        numero.push(tabela[i][1].repeat(quociente))
    }
    return numero.join('')
};

console.log(intToRoman(num = 3))
console.log(intToRoman(num = 58))
console.log(intToRoman(num = 1994))
