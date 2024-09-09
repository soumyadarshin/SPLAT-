<script>
      var mapCenter = [{{ map_center.lat }}, {{ map_center.lng }}];
      var map = L.map('map').setView(mapCenter, 13);
      L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
          maxZoom: 19,
      }).addTo(map);
      var kmlLayer = new L.KML('{{ kml_file_url }}', {
          async: true,
      });
      map.addLayer(kmlLayer);
</script>
