const address = $('#address');
const myLocationModal = $('#my-location-modal');
let map, markers = {};
$('#my-location-form').submit(event => {
    event.preventDefault();
    $.post('/position', address.val()).done(person => {
        myLocationModal.modal('hide');
        markers[person.username].setPosition(person.position);
        map.setCenter(person.position);
    });
});

function init() {
    map = new google.maps.Map(document.getElementById('map'), {
        center: {lat: 39.8097343, lng: -98.556199}, zoom: 4
    });
    $.get('/people').done(people => {
        for (let person of people) {
            markers[person.username] = new google.maps.Marker({
                label: person.username[0].toUpperCase(), map: map,
                position: person.position, title: person.username
            });
        }
    });
}