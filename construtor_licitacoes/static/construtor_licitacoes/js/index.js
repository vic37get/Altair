
function statusLicitacao(licitacao,id) {
    if(licitacao==0){
        document.getElementById("status"+id).setAttribute('class','status pendente fa-solid fa-circle');
        document.getElementById("Labelstatus"+id).innerHTML = "Pendente";
    }

    if(licitacao==1){
        document.getElementById("Labelstatus"+id).innerHTML = "Submetido";
        document.getElementById("status"+id).setAttribute('class','status submetido fa-solid fa-circle');


    }

    if(licitacao<1){
        document.getElementById( "modalButton" ).style.display = "none";

    }
  }

  function switchLockEdit(licitacao,id) {
    if(licitacao==0){
        document.getElementById("editar"+id).disabled = false;
        document.getElementById("excluir"+id).disabled = false;
    }
    if(licitacao!=0){
        document.getElementById("editar"+id).disabled = true;
        document.getElementById("excluir"+id).disabled = true;
        
    }
  }