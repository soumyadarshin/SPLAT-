
document.addEventListener("DOMContentLoaded", function() {
            // Get the map element
            var map = document.querySelector('#map .folium-map');

            if (map) {
                var mapObject = L.map(map).setView([20.359142977029173, 85.82264111855899], 13);

                L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
                    maxZoom: 19
                }).addTo(mapObject);

                

                // Function to add a circle to the map
                window.addCircle = function() {
                    var radius = parseFloat(document.getElementById('radius').value);

                    if (isNaN(radius)) {
                        alert('Please enter a valid radius.');
                        return;
                    }

                    L.circle([20.359142977029173, 85.82264111855899], {
                        color: 'blue',
                        fillColor: 'blue',
                        fillOpacity: 0.5,
                        radius: radius
                    }).addTo(mapObject);
                };
            }
        });