function createJSON(id) {
    var json = {};
    var titulos = getTitulo();
    var conteudos = getConteudo();
    json['secoes'] = [];
    for (let i = 0; i < titulos.length; i++) {
        json['secoes'].push({'titulo':titulos[i].replace(/"/g, "'"),'conteudo':conteudos[i].map(rep)})
    }
    var output = {'json':json,'_id':id};
    return JSON.stringify(output);
}

function saveJSON(id){
    var dataJSON = createJSON(id);
    $.ajax({
      type: 'POST',
      url: '/construcao/salvar',
      data: dataJSON,
      dataType : 'json',
      contentType: 'application/json; charset=utf-8',
      cache: false,
    });
    alert('O Documento foi Salvo.');
  }

function loadJSON(json){
    var jsonDecoded = JSON.parse(decodeEntity(json).replace(/\n\r?/g, ''));
    var sleep = 1500+jsonDecoded.secoes.length*350;
    /*console.log(jsonDecoded);*/
    setConteudo(jsonDecoded);
}

function decodeEntity(inputStr) {
    var textarea = document.createElement("textarea");
    textarea.innerHTML = inputStr;
    return textarea.value;
}

function rep(string){
    return string.replace(/"/g, "'");
}

function setConteudo(jsonDecoded){
    for (let index = 0; index < jsonDecoded.secoes.length; index++) {
        /*console.log(secao_filhos[j].id);*/
        /*$(jsonDecoded.secoes[index].titulo)[0].children[1].outerHTML*/
        var title = '';
        if($(jsonDecoded.secoes[index].titulo)[0].tagName == 'DIV'){title = $(jsonDecoded.secoes[index].titulo)[0].children[1].outerHTML}        
        loadInstanciaTinyMCE(jsonDecoded.secoes[index].conteudo[0],title);
    }
}

function loadInstanciaTinyMCE(json,title){
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
        setup: function (editor) {
            editor.on('init', function (e) {
              editor.setContent(title);
            });
          },
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
      setup: function (editor) {
        editor.on('init', function (e) {
          editor.setContent(json);
        });
      },
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