function initMap(){
    map = new google.maps.Map(document.getElementById('map'),{
        center: {lat: -33.500022547145974, lng: -70.61664685434545},
        zoom: 18,
        mapId: '1697707868d02e57'
    });
    new google.maps.Marker({
        position : {lat: -33.500022547145974, lng: -70.61664685434545},
        map,
        title: "Hola Mundo"
    })
}

//-33.500022547145974, -70.61664685434545