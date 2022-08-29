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
      branding: false,
      tinycomments_mode: 'embedded',
      tinycomments_author: 'Author name',
      
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
        height : '2.5rem',
        width: '100%',
        toolbar: false,
        menubar: false,
        statusbar: false,
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