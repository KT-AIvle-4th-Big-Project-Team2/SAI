// convertCoordinatesToLatLng.js
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
