// Initialize and add the map
function initMap() {
  // The location of Uluru
  const campos = { lat: -21.747745351847826, lng: -41.34579804582231 };
  // The map, centered at Uluru
  const map = new google.maps.Map(document.getElementById("divMapIndex"), {
    zoom: 18,
    center: campos,
  });
  // The marker, positioned at Uluru
  const marker = new google.maps.Marker({
    position: campos,
    map: map,
  });
}