function integer_to_roman(num) {
    if (typeof num !== 'number'){ 
      return false; 
    }
    var digits = String(+num).split(""),
    key = ["","C","CC","CCC","CD","D","DC","DCC","DCCC","CM",
    "","X","XX","XXX","XL","L","LX","LXX","LXXX","XC",
    "","I","II","III","IV","V","VI","VII","VIII","IX"],
    roman_num = "",
    i = 3;
    while (i--)
    roman_num = (key[+digits.pop() + (i * 10)] || "") + roman_num;
    return Array(+digits.join("") + 1).join("M") + roman_num;
  }

  function padraoSecao(numeracao, secoes_lista){
    numeracao = integer_to_roman(numeracao)
    secao_titulo = prefixo + " " + numeracao + " - "  + secoes_lista[0];
    return secao_titulo
  }

  function padraoCapitulo(numeracao, secoes_lista){
    numeracao = integer_to_roman(numeracao)
    secao_titulo = prefixo + " " + numeracao + " - "  + secoes_lista[0];
    return secao_titulo
  }

  function padraoNumerico(numeracao, secoes_lista){
    secao_titulo  = numeracao + ". "  + secoes_lista[0];
    return secao_titulo
  }

  function padraoSecaoEditavel(prefixo, count){
    count = integer_to_roman(count)
    numeracao = prefixo + " " + count + " - ";
    return numeracao
  }

  function padraoCapituloEditavel(prefixo, count){
    count = integer_to_roman(count)
    numeracao = prefixo + " " + count + " - ";
    return numeracao
  }

  function padraoNumericoEditavel(count){
    numeracao = count + ". ";
    return numeracao
  }