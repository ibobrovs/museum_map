fetch('map_data_fixed.csv')
  .then(res => res.text())
  .then(csv => {
    const data = Papa.parse(csv, { header: true }).data;

    data.forEach(row => {
      const lat = parseFloat(row.lat);
      const lng = parseFloat(row.lon);  // убедитесь, что колонка называется "lon"
      const popup = `<div style="min-width: 250px;"><b>${row.parskts || ''}</b><br>${row.overview || ''}</div>`;
      const category = row.type?.toLowerCase();

      if (!isNaN(lat) && !isNaN(lng)) {
        const icon = icons[category] || undefined;
        const marker = L.marker([lat, lng], { icon });
        marker.bindPopup(popup);
        markerCluster.addLayer(marker);
      }
    });
  });
