
tinymce.init({
    selector: '.lic-title',
    weight : '80%',
    height : '20 rem',
    plugin: 'pagebreak',
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

  function openNavLeft() {
    document.getElementsByClassName('openbtn')[1].style.display = "none";
    document.getElementById("mySidebarLeft").style.width = "20%";
    document.getElementById("main").style.marginLeft = "20%";
  }

  function closeNavLeft() {
    document.getElementsByClassName('openbtn')[1].style.display = "flex";
    document.getElementById("mySidebarLeft").style.width = "0";
    document.getElementById("main").style.marginLeft= "0";
  }

  function openNavRight() {
    document.getElementsByClassName('openbtn')[0].style.display = "none";
    document.getElementById("mySidebarRight").style.width = "40%";
    document.getElementById("main").style.marginRight = "40%";
  }

  function closeNavRight() {
    document.getElementsByClassName('openbtn')[0].style.display = "flex";
    document.getElementById("mySidebarRight").style.width = "0";
    document.getElementById("main").style.marginRight= "0";
  }

