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
   console.log(texto)
   document.getElementById("txtArea2").value = texto
  }

  function baixarPdf(){
    document.getElementById("Button").addEventListener('click', analyzeText());

  }
