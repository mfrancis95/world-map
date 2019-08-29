function init() {
    const map = new google.maps.Map(document.getElementById('map'), {
        center: {lat: 39.8097343, lng: -98.556199}, zoom: 4
    });
    $.ajax({url: '/people'}).done(people => {
        for (let person of people) {
            new google.maps.Marker({
                label: person.username[0].toUpperCase(),
                map: map,
                position: person.position,
                title: person.username
            });
        }
    });
}