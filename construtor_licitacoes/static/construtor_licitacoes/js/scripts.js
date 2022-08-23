

  

  function openNavLeft() {
    document.getElementById('menuLateralEsquerdo').style.display = "none";
    document.getElementById("mySidebarLeft").style.width = "20%";
    document.getElementById("main").style.marginLeft = "16%";
  }

  function closeNavLeft() {
    document.getElementById('menuLateralEsquerdo').style.display = "flex";
    document.getElementById("mySidebarLeft").style.width = "0";
    document.getElementById("main").style.marginLeft= "0";
  }

  function openNavRight() {
    document.getElementById('menuLateralDireito').style.display = "none";
    document.getElementById("mySidebarRight").style.width = "40%";
    document.getElementById("main").style.marginRight = "38%";
  }

  function closeNavRight() {
    document.getElementById('menuLateralDireito').style.display = "flex";
    document.getElementById("mySidebarRight").style.width = "0";
    document.getElementById("main").style.marginRight= "0";
  }

  function openNavLeftSecoes() {
    document.getElementById('menuLateralEsquerdo').style.display = "none";
    document.getElementById("mySidebarLeftSecoes").style.width = "20%";
    document.getElementById("main").style.marginLeft = "16%";
    menuSecoesFeitas();
  }

  function closeNavLeftSecoes() {
    document.getElementById('menuLateralEsquerdo').style.display = "flex";
    document.getElementById("mySidebarLeftSecoes").style.width = "0";
    document.getElementById("main").style.marginLeft= "0";
  }

  function getHeader(){
   return tinymce.get("cabecalho").getContent();
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

  function menuSecoesFeitas(){
    var menu = document.getElementById('menuSecoesFeitas');
    menu.innerHTML = ""
    lista = getTitulo()
    lista.forEach(element => {
      elemento = $(element)[0];
      if (elemento.tagName == "DIV"){
        p = $(elemento.getElementsByTagName("p"))[0];
        elemento = $(elemento.getElementsByTagName("H5"))[0];
        try {
          elemento.innerHTML = elemento.innerHTML + p.innerHTML.toUpperCase();
        } catch (error) {
        }
      }
      elemento.setAttribute('class', 'tituloSecaoFeita');
      menu.appendChild(elemento);
    });
  }
  
  var secoes_lista = ["DO OBJETO","DO JULGAMENTO","DAS CONDIÇÕES DE PARTICIPAÇÃO", "DA HABILITAÇÃO", "DO CREDENCIAMENTO"];
  var count = 1;

  function novaInstanciaTinyMCE(){
    var secoes = document.getElementById('div_secoes');
    var numeracao = document.createElement("h5");
    numeracao.setAttribute('class', 'secao_titulo');
    
    var secao_completa = document.createElement('div')
    secao_completa.setAttribute('class','conteudoCaptura secoesSemNome');
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
      var titulo_secaoSemNome = document.createElement("div");
      titulo_secaoSemNome.setAttribute('class','d-flex flex-row w-100 pb-2 tituloCaptura');
      secao_titulo.setAttribute('class','titulo_secoes');
      titulo_secaoSemNome.appendChild(numeracao);
      titulo_secaoSemNome.appendChild(secao_titulo);
      secao_completa.appendChild(titulo_secaoSemNome);
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
      secao_titulo.setAttribute('class', 'secao_titulo tituloCaptura');
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
      secao_completa.appendChild(secao_titulo);
      secoes.appendChild(secao_completa)
    }
    var conteudo = document.createElement("textarea");
    conteudo.setAttribute('class','secoes');
    secao_completa.appendChild(conteudo);
    tinymce.init({
      selector: '.secoes',
      width: '100%',
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

  function filterTinyMce(textarea){
    if(textarea.id.match(/mce_.*/i) != null){
      return textarea
    }
  }

  function mapTinyMce(textarea){
    return textarea.id
  }
  function getAllIds(){
    var lista_textAreas = document.getElementsByTagName('textarea');
    lista_textAreas = Array.prototype.slice.call(lista_textAreas);
    lista_textAreas = lista_textAreas.filter(filterTinyMce);
    lista_textAreas = lista_textAreas.map(mapTinyMce);
    return lista_textAreas
  }

  function getAllContent(){
    var ids = getAllIds();
    var divconteudo = []
    var divs_secoes = document.getElementsByClassName('conteudoCaptura');

    for (let index = 0; index < divs_secoes.length; index++) {
      var div_conteudo = document.createElement('div');
      div_conteudo.setAttribute('class','w-100')
      var filhos = divs_secoes[index].childNodes;
      if(filhos[0].tagName == 'DIV'){
        var titulo = tinymce.get(filhos[0].childNodes[1].id).getContent();
        div_conteudo.innerHTML = titulo;
      }
      for (let j = 1; j < filhos.length; j++) {
        var elemento = filhos[j];
        if(elemento.id.match(/mce_.*/i)!=null){
          var conteudo = tinymce.get(elemento.id).getContent();
          div_conteudo.innerHTML = conteudo;
          divconteudo.push((divs_secoes[index].childNodes[0]).outerHTML)
          divconteudo.push(conteudo)
        }
      }
    }

    var stringpdf = "";
    divconteudo.forEach(element => {
      stringpdf += element
    });
    var textoHeader = tinymce.get("cabecalho").getContent();
    

    stringpdf = textoHeader + stringpdf
    console.log(stringpdf)

    var doc = new jsPDF();
    doc.fromHTML(stringpdf, // page element which you want to print as PDF
    15,
    15, 
    {
      'width': 170
    },
    function(a) 
    {
      var file = document.getElementById("embedpreview")
      file.src = doc.output('datauristring') + "#view=FitH"
    });
  }

  function getTitulo(){
    var titulos = document.getElementsByClassName('tituloCaptura');
    var titulos_prontos = [];
    for (let i = 0; i < titulos.length; i++) {
      var tituloCompleto = '';
      var titulo = titulos[i];
      if(titulo.tagName=='DIV'){
        filhos_divTitulo = titulo.children;
        var prefixo;
        var tituloCaixa;
        for (let j = 0; j < filhos_divTitulo.length; j++) {
          var filho = filhos_divTitulo[j];
          if(filho.tagName == 'H5'){
            prefixo = filho;
          }else{
            if(filho.tagName == 'TEXTAREA'){
              tituloCaixa = $(tinymce.get(filho.id).getContent())[0];
            }
          }
        }
        if (tituloCaixa == undefined){
          tituloCompleto = document.createElement('div');
          tituloCompleto.appendChild(prefixo.cloneNode(true));
        }
        else{
        tituloCompleto = document.createElement('div');
        tituloCompleto.appendChild(prefixo.cloneNode(true));
        tituloCompleto.appendChild(tituloCaixa);
        }
      }
      else{
        tituloCompleto = titulo;
      }
      titulos_prontos.push(tituloCompleto.outerHTML);
    }
    return titulos_prontos;
  }

  function getConteudo(){
    var divs_secoes = document.getElementsByClassName('conteudoCaptura');
    var conteudosAll = [];
    for (let index = 0; index < divs_secoes.length; index++) {
      var conteudos = []
      var secao = divs_secoes[index];
      var secao_filhos = secao.children;
      for (let j = 0; j < secao_filhos.length; j++) {
        if(secao_filhos[j].tagName == 'TEXTAREA'){
          conteudos.push(tinymce.get(secao_filhos[j].id).getContent());
        }
      }
      conteudosAll.push(conteudos);
    }
    return conteudosAll;
  }



  
  function baixarPdf(salvar){
    var ids = getAllIds();
    var divconteudo = []
    var divs_secoes = document.getElementsByClassName('conteudoCaptura');
    var textoInicial = tinymce.get('cabecalho').getContent();
    if(divs_secoes.length>0)
      divs_secoes[0].childNodes[0]

    for (let index = 0; index < divs_secoes.length; index++) {
      var div_conteudo = document.createElement('div');
      div_conteudo.setAttribute('class','w-100')
      var filhos = divs_secoes[index].childNodes;
      if(filhos[0].tagName == 'DIV'){
        var titulo = tinymce.get(filhos[0].childNodes[1].id).getContent();
        div_conteudo.innerHTML = titulo;
        filhos[0].appendChild(div_conteudo)
        filhos[0].removeChild(filhos[0].childNodes[2]);
      }

      for (let j = 1; j < filhos.length; j++) {
        var elemento = filhos[j];
        if(elemento.id.match(/mce_.*/i)!=null){
          var conteudo = tinymce.get(elemento.id).getContent();
          div_conteudo.innerHTML = conteudo;
          divconteudo.push((divs_secoes[index].childNodes[0]).outerHTML)
          divconteudo.push(conteudo)
        }
       
      }
    }
    var stringpdf = "<h4>Preambulo</h4>"+textoInicial;
    divconteudo.forEach(element => {
      stringpdf += element
    });
    //console.log(stringpdf)

    var doc = new jsPDF();
    var data = new Date();
    
    var dataAtual = new Date();
    var dataAtual = dataAtual.getDate()+'-'+(dataAtual.getMonth()+1)+'-'+dataAtual.getFullYear();

    doc.fromHTML(stringpdf, // page element which you want to print as PDF
    15,
    15, 
    {
      'width': 170
    },
    function(a) 
    {
        doc.save("edital "+ dataAtual.toString()+".pdf","../");
    });
  }

