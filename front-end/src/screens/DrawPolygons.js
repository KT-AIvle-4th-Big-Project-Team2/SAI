// drawPolygons.js
export const convertCoordinatesToLatLng = (coordinates, type) => {
    let paths = [];

    if (type === "Polygon") {
        paths = coordinates[0].map(coord => new window.kakao.maps.LatLng(coord[1], coord[0]));
    } else if (type === "MultiPolygon") {
        coordinates.forEach(polygon => {
            const path = polygon[0].map(coord => new window.kakao.maps.LatLng(coord[1], coord[0]));
            paths.push(path);
        });
    }

    return paths;
};

export const drawPolygons = (map, geoJsonData, displayMessage) => {
    geoJsonData.features.forEach(feature => {
        const { geometry: { type, coordinates }, properties } = feature;
    
        if (type === "Polygon" || type === "MultiPolygon") {
            const paths = convertCoordinatesToLatLng(coordinates, type);
    
            const polygon = new window.kakao.maps.Polygon({
                map: map,
                path: paths,
                strokeWeight: 3,
                strokeColor: '#FFA500',
                strokeOpacity: 0.8,
                fillColor: '#FFA500',
                fillOpacity: 0.3
            });

            window.kakao.maps.event.addListener(polygon, 'mouseover', () => {
                polygon.setOptions({ fillColor: '#0000FF' });
                if (properties && properties.TRDAR_CD_N) {
                    displayMessage(`상권 이름: ${properties.TRDAR_CD_N}`);
                }
            });

            window.kakao.maps.event.addListener(polygon, 'mouseout', () => {
                polygon.setOptions({ fillColor: '#FFA500' });
                displayMessage('');
            });
        }
    });
};
