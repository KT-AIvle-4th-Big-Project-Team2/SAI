import { convertCoordinatesToLatLng } from "./convertCoordinatesToLatLng";

export const drawSelectedPolygon = (map, geoJsonData, displayMessage, selectedSgg, selectedAdm, polygonsArray) => {
    // 기존 폴리곤 제거
    polygonsArray.forEach(polygon => polygon.setMap(null));
    polygonsArray.length = 0; // 배열 초기화

    geoJsonData.features.forEach(feature => {
        const { geometry: { type, coordinates }, properties } = feature;

        if (type === "Polygon" || type === "MultiPolygon") {
            const adm_nm = properties.adm_nm;
            const fullAddress = `서울특별시 ${selectedSgg} ${selectedAdm}`;

            if (adm_nm === fullAddress) {
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

                polygonsArray.push(polygon); // 새로운 폴리곤을 배열에 추가

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
        }
    });
};
