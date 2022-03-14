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