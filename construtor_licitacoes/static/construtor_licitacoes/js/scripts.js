tinymce.init({
    selector: '.lic-title',
    height : '10.3rem',
    menubar: false,
    statusbar: false,
    style_formats: [
      // Adds the h1 format defined above to style_formats
      { title: 'Titulo 1', format: 'h1' },
      { title: 'Titulo 2', format: 'h2' },
      { title: 'Titulo 3', format: 'h3' },
      { title: 'Titulo 4', format: 'h4' },
      ],
    language: 'pt_BR',
    language_url: '{%static "js/langs/pt_BR.js" %}',
    branding: false,
    tinycomments_mode: 'embedded',
    tinycomments_author: 'Author name',
  });

  function addSecao(){
    tinymce.init({
      selector: '#sessao',
      height : '10.3rem',
      menubar: false,
      statusbar: false,
      style_formats: [
        // Adds the h1 format defined above to style_formats
        { title: 'Titulo 1', format: 'h1' },
        { title: 'Titulo 2', format: 'h2' },
        { title: 'Titulo 3', format: 'h3' },
        { title: 'Titulo 4', format: 'h4' },
        ],
      language: 'pt_BR',
      language_url: '{%static "js/langs/pt_BR.js" %}',
      branding: false,
      tinycomments_mode: 'embedded',
      tinycomments_author: 'Author name',
    });
  }

  function save(){
   var texto = tinymce.get("txtArea1").getContent()
   document.getElementById("txtArea2").value = texto

   //var texto1 = "";
   //var textareaList = document.querySelectorAll("textarea");
   //for(var i = 0; i < textareaList.length; i++){
   //   texto1 = texto1+' '+textareaList[i];
   //}
  }


  function instanceMCE(){
    tinymce.init({
      selector: '.secoes',
      plugins: 'autoresize',
      autoresize_bottom_margin: 10,
      max_height: 500,
      menubar: false,
      statusbar: false,
      style_formats: [
        // Adds the h1 format defined above to style_formats
        { title: 'Titulo 1', format: 'h1' },
        { title: 'Titulo 2', format: 'h2' },
        { title: 'Titulo 3', format: 'h3' },
        { title: 'Titulo 4', format: 'h4' },
        ],
      language: 'pt_BR',
      language_url: '{%static "js/langs/pt_BR.js" %}',
      branding: false,
      tinycomments_mode: 'embedded',
      tinycomments_author: 'Author name',
    });
  }

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


  var secoes_lista = ["DO OBJETO","DO JULGAMENTO","DAS CONDIÇÕES DE PARTICIPAÇÃO", "DA HABILITAÇÃO", "DO CREDENCIAMENTO"];
  var count = 1;


  function novaInstanciaTinyMCE(){
    var secoes = document.getElementById('div_secoes');
    var numeracao = document.createElement("h5");
    numeracao.setAttribute('id', 'secao_titulo')
    
    var secao_completa = document.createElement('div')
    secao_completa.setAttribute('class','secoesSemNome');
    if (secoes_lista.length == 0){
      if (prefixo == "SEÇÃO"){
        numeracao.innerHTML = padraoSecaoEditavel(prefixo, count)
      }
      else if (prefixo == 'CAPÍTULO'){
        numeracao.innerHTML = padraoCapituloEditavel(prefixo, count)
      }
      else {
        numeracao.innerHTML = padraoNumericoEditavel(count)
      }

      var secao_titulo = document.createElement("textarea");
      secao_titulo.setAttribute('class','titulo_secoes');
      secao_completa.appendChild(numeracao)
      secao_completa.appendChild(secao_titulo)
      secoes.appendChild(secao_completa)

      tinymce.init({
        selector: '.titulo_secoes',
        height : '3.0rem',
        width: '100%',
        toolbar: false,
        menubar: false,
        statusbar: false,
        style_formats: [
          // Adds the h1 format defined above to style_formats
          { title: 'Titulo 1', format: 'h1' },
          { title: 'Titulo 2', format: 'h2' },
          { title: 'Titulo 3', format: 'h3' },
          { title: 'Titulo 4', format: 'h4' },
          ],
        language: 'pt_BR',
        language_url: '{%static "js/langs/pt_BR.js" %}',
        branding: false,
        tinycomments_mode: 'embedded',
        tinycomments_author: 'Author name',
      });
      count ++;
    }else{
      var secao_titulo = document.createElement("h5");
      secao_titulo.setAttribute('id', 'secao_titulo')
      if (prefixo == "SEÇÃO"){
        secao_titulo.innerHTML = padraoSecao(count, secoes_lista)
      }
      else if (prefixo == 'CAPÍTULO'){
        secao_titulo.innerHTML = padraoCapitulo(count, secoes_lista)
      }
      else {
        secao_titulo.innerHTML = padraoNumerico(count, secoes_lista)
      }
      count ++;
      secoes_lista.shift();
      secoes.appendChild(secao_titulo);
    }
    var conteudo = document.createElement("textarea");
    conteudo.setAttribute('class','secoes');
    secoes.appendChild(conteudo);
    instanceMCE();
  }

  
  function myFunction3(){
   var texto = tinymce.get("txtArea1").getContent()
   tinymce.activeEditor.hide();
   document.getElementById("txtArea2").value = tinymce.activeEditor.getContent();
  }

  
  function handler( event ) {
    var target = $( event.target );
  }


  function ImprimeDocumento(){
    tinymce.activeEditor.execCommand('mcePrint');
  }
