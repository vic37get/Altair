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
    console.log("okj")
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
   console.log(texto)
   document.getElementById("txtArea2").value = texto
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
  
    tinymce.init({
      selector: '.titulo_secoes',
      height : '3.3rem',
      content_style: "margin: 0px; padding: 0px;",
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
  }
  
  var secoes_lista = ["DO OBJETO","DO JULGAMENTO","DAS CONDIÇÕES DE PARTICIPAÇÃO"];
  
  function myFunction(){
    console.log(tinymce.activeEditor.execCommand('mcePrint'));
  }
  var count = 1;
  function novaInstanciaTinyMCE(){
    var secoes = document.getElementById('div_secoes');
    
    var numeracao = document.createElement("h3");
    numeracao.setAttribute('id', 'numeracao_titulo')
    numeracao.innerHTML = count;
    if (secoes_lista.length == 0){
      var secao_titulo = document.createElement("textarea");
      secao_titulo.setAttribute('class','titulo_secoes');
      secoes.appendChild(numeracao);
      count ++;
    }else{
      var secao_titulo = document.createElement("h3");
      secao_titulo.innerHTML = count + " " +prefixo+" "+secoes_lista[0];
      count ++;
      //console.log(secao_titulo);
      secoes_lista.shift();
    }
    secoes.appendChild(secao_titulo);
    instanceMCE();
    secoes.appendChild(document.createElement("br"));
    var conteudo = document.createElement("textarea");
    conteudo.setAttribute('class','secoes');
    secoes.appendChild(conteudo);
    instanceMCE();
  }
  
  function myFunction3(){
   var texto = tinymce.get("txtArea1").getContent()
   console.log(texto)
   tinymce.activeEditor.hide();
   document.getElementById("txtArea2").value = tinymce.activeEditor.getContent();
  }
  
  function handler( event ) {
    var target = $( event.target );
    console.log(target)
  }