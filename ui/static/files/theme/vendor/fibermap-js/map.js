// hack para add a lib do google maps no codepen
document.addEventListener("DOMContentLoaded", function () {
    const externalFile = document.createElement("script");
    externalFile.type = "text/javascript";
    externalFile.src =
      "https://maps.googleapis.com/maps/api/js?key=AIzaSyB9RIjP1NM54CF0_jpt4tGyX0QbGaxxc8A&region=BR&language=pt-br";
    document.getElementsByTagName("head")[0].appendChild(externalFile);
  });
  
  
  
  /**
   * adiciona o mapa no divMap centralizando na cidade de campos
   */
  function getMap() {
    const div = document.querySelector("#divMap");
    const campos = {
      lat: -21.7478578,
      lng: -41.3479713
    };
    const config = {
      zoom: 18,
      center: campos,
      mapTypeControl: false,
      fullscreenControl: false,
      zoomControl: true,
      disableDoubleClickZoom: true,
      streetViewControl: false
    };
    const map = new google.maps.Map(div, config);
    return map;
  }

  function getMapIndex() {
    
    const div = document.querySelector("#divMapIndex");
    const campos = {
      lat: -21.7478578,
      lng: -41.3479713
    };
    const config = {
      zoom: 18,
      center: campos,
      mapTypeControl: false,
      fullscreenControl: false,
      zoomControl: true,
      disableDoubleClickZoom: true,
      streetViewControl: false
    };
    

    const mapindex = new google.maps.Map(div, config);
    
    new google.maps.Marker({
      position: campos,
      mapindex,
      title: "Hello World!",
    });

    return mapindex;
  }
  
  /**
   * Remove algum evento de click esquecido
  */
  function clearClickEventOn(map) {
    google.maps.event.clearListeners(map, "click");
  }
  
  /**
   * Executa a funcao callback quando houver um click no mapa
  */
  function addClickEventTo(map, callback) {
    map.addListener("click", callback);
  }
  
  /**
   * Recebe as coordenadas e envia para uma api qualquer
  */
  async function sendCoordsToMyApi(evt) {
    const coords = {
      lat: evt.latLng.lat(),
      lng: evt.latLng.lng()
    };

    document.getElementById("id_geolocation").value = JSON.stringify(coords);

    /*
      const res = fetch('http://localhost/minha/api', {
        method: 'POST',
        headers: {
          'Accept': 'application/json',
          'Content-Type': 'application/json'
        },
        body: JSON.stringify(coords)
      });
      const content = await res.json();
      console.log(content)
      */
  }

 
  
  /**
   * Funcao executada ao clicar no botao
  */
  function start() {
    // 1. cria uma instancia do mapa adicionando ao divMap
    const map = getMap();
  
    // 2. limpa qualquer funcao atribuida ao click do mouse no mapa
    clearClickEventOn(map);
  
    // 3. adiciona a funcao que recebe um objeto evt como parametro (o google maps envia esse objeto pra funcao)
    // e obtem a latitude e longitude onde houve o click. depois envia como um request POST para /minha/api
    addClickEventTo(map, sendCoordsToMyApi);
  }
  

  function startMapIndex() {
    // 1. cria uma instancia do mapa adicionando ao divMap da tela inicial
    const mapindex = getMapIndex();
  
  }

