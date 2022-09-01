function openNavLeft() {
    document.getElementById('menuLateralEsquerdo').style.display = "none";
    document.getElementById("mySidebarLeft").style.width = "18%";
    document.getElementById("main").style.marginLeft = "18%";
  }

  function closeNavLeft() {
    document.getElementById('menuLateralEsquerdo').style.display = "flex";
    document.getElementById("mySidebarLeft").style.width = "0";
    document.getElementById("main").style.marginLeft= "0";
  }

  function openNavRight() {
    document.getElementById('menuLateralDireito').style.display = "none";
    document.getElementById("mySidebarRight").style.width = "40%";
    document.getElementById("main").style.marginRight = "40%";
  }

  function closeNavRight() {
    document.getElementById('menuLateralDireito').style.display = "flex";
    document.getElementById("mySidebarRight").style.width = "0";
    document.getElementById("main").style.marginRight= "0";
  }

  function openNavLeftSecoes() {
    document.getElementById('menuLateralEsquerdo').style.display = "none";
    document.getElementById("mySidebarLeftSecoes").style.width = "18%";
    document.getElementById("main").style.marginLeft = "18%";
    menuSecoesFeitas();
  }

  function closeNavLeftSecoes() {
    document.getElementById('menuLateralEsquerdo').style.display = "flex";
    document.getElementById("mySidebarLeftSecoes").style.width = "0";
    document.getElementById("main").style.marginLeft= "0";
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